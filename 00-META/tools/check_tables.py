#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_tables.py - Validador de Tablas Markdown

Detecta y reporta problemas en tablas Markdown:
- Columnas desalineadas
- Caracteres '|' en celdas (ej. valor absoluto)
- Filas con numero incorrecto de columnas
- Headers mal formados

Uso:
    python check_tables.py [ruta]

Si no se especifica ruta, escanea todo el repositorio.
"""

import os
import re
import sys
import io
from pathlib import Path

# Configurar stdout para UTF-8 en Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from typing import List, Tuple, Dict

# Configuración
EXCLUDE_DIRS = {'.git', '.venv', 'node_modules', '__pycache__', 'Notas'}
CONTENT_EXTENSIONS = {'.md'}


def find_markdown_files(root_path: Path) -> List[Path]:
    """Encuentra todos los archivos Markdown en el directorio."""
    md_files = []
    for path in root_path.rglob('*.md'):
        # Excluir directorios específicos
        if any(excluded in path.parts for excluded in EXCLUDE_DIRS):
            continue
        md_files.append(path)
    return md_files


def extract_tables(content: str) -> List[Tuple[int, List[str]]]:
    """
    Extrae todas las tablas del contenido Markdown.
    Retorna lista de (línea_inicio, filas_de_tabla).
    """
    lines = content.split('\n')
    tables = []
    current_table = []
    table_start = -1
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Detectar línea de tabla (contiene | y no es código)
        if '|' in stripped and not stripped.startswith('```'):
            if not current_table:
                table_start = i + 1  # 1-indexed
            current_table.append(line)
        else:
            # Fin de tabla
            if current_table:
                # Verificar que es una tabla válida (tiene separador)
                has_separator = any(re.match(r'^\s*\|?\s*[-:]+\s*\|', row) for row in current_table)
                if has_separator and len(current_table) >= 2:
                    tables.append((table_start, current_table))
                current_table = []
    
    # Capturar última tabla si existe
    if current_table:
        has_separator = any(re.match(r'^\s*\|?\s*[-:]+\s*\|', row) for row in current_table)
        if has_separator and len(current_table) >= 2:
            tables.append((table_start, current_table))
    
    return tables


def count_columns(row: str) -> int:
    """
    Cuenta el numero de columnas en una fila de tabla.
    Maneja casos de | escapados (\\|) o en contenido.
    """
    # Reemplazar pipes escapados temporalmente
    temp_row = row.replace('\\|', '\x00')
    
    # Eliminar | inicial y final si existen
    stripped = temp_row.strip()
    if stripped.startswith('|'):
        stripped = stripped[1:]
    if stripped.endswith('|'):
        stripped = stripped[:-1]
    
    # Contar separadores reales (no escapados)
    return stripped.count('|') + 1


def analyze_table(table_start: int, table_rows: List[str]) -> List[Dict]:
    """
    Analiza una tabla y detecta problemas.
    """
    issues = []
    
    if len(table_rows) < 2:
        return issues
    
    # Obtener número de columnas del header
    header_cols = count_columns(table_rows[0])
    
    for i, row in enumerate(table_rows):
        line_num = table_start + i
        row_cols = count_columns(row)
        
        # Verificar alineación de columnas
        if row_cols != header_cols:
            # Ignorar fila separadora
            if not re.match(r'^\s*\|?\s*[-:|\s]+\s*\|?\s*$', row):
                issues.append({
                    'line': line_num,
                    'type': 'column_mismatch',
                    'message': f'Columnas esperadas: {header_cols}, encontradas: {row_cols}',
                    'row': row.strip()[:60] + ('...' if len(row.strip()) > 60 else '')
                })
        
        # Detectar posibles problemas con | en contenido matemático
        # (ej. |x| para valor absoluto)
        if re.search(r'\|[^|]+\|', row) and '$$' not in row and '$' in row:
            issues.append({
                'line': line_num,
                'type': 'possible_math_pipe',
                'message': 'Posible conflicto: | en expresión matemática',
                'row': row.strip()[:60] + ('...' if len(row.strip()) > 60 else '')
            })
    
    return issues


def validate_file(file_path: Path) -> List[Dict]:
    """Valida un archivo Markdown y retorna problemas encontrados."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        return [{'file': str(file_path), 'error': str(e)}]
    
    tables = extract_tables(content)
    all_issues = []
    
    for table_start, table_rows in tables:
        issues = analyze_table(table_start, table_rows)
        for issue in issues:
            issue['file'] = str(file_path)
        all_issues.extend(issues)
    
    return all_issues


def main():
    """Punto de entrada principal."""
    # Determinar ruta raíz
    if len(sys.argv) > 1:
        root = Path(sys.argv[1])
    else:
        # Subir dos niveles desde tools/
        root = Path(__file__).parent.parent.parent
    
    if not root.exists():
        print(f"[ERROR] Ruta no encontrada: {root}")
        sys.exit(1)
    
    print(f"[SCAN] Escaneando tablas en: {root}")
    print("=" * 60)
    
    # Encontrar archivos
    md_files = find_markdown_files(root)
    print(f"[INFO] Archivos Markdown encontrados: {len(md_files)}")
    
    # Validar archivos
    all_issues = []
    files_with_issues = set()
    
    for file_path in md_files:
        issues = validate_file(file_path)
        if issues:
            files_with_issues.add(str(file_path))
            all_issues.extend(issues)
    
    # Reportar resultados
    print()
    if not all_issues:
        print("[OK] No se encontraron problemas en las tablas")
    else:
        print(f"[WARN] Problemas encontrados: {len(all_issues)}")
        print(f"[INFO] Archivos afectados: {len(files_with_issues)}")
        print()
        
        # Agrupar por archivo
        current_file = None
        for issue in sorted(all_issues, key=lambda x: (x.get('file', ''), x.get('line', 0))):
            if 'error' in issue:
                print(f"[ERROR] Error leyendo {issue['file']}: {issue['error']}")
                continue
            
            if issue['file'] != current_file:
                current_file = issue['file']
                rel_path = Path(current_file).relative_to(root) if root in Path(current_file).parents else current_file
                print(f"\n[FILE] {rel_path}")
            
            icon = '[WARN]' if issue['type'] == 'possible_math_pipe' else '[ERROR]'
            print(f"  {icon} Linea {issue['line']}: {issue['message']}")
            print(f"     -> {issue['row']}")
    
    print()
    print("=" * 60)
    print(f"Resumen: {len(md_files)} archivos, {len(all_issues)} problemas")
    
    # Código de salida
    sys.exit(0 if not all_issues else 1)


if __name__ == '__main__':
    main()
