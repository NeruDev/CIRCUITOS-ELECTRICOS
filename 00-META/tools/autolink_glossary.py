#!/usr/bin/env python3
"""
Autolink Glossary - Sistema de Hipervinculación Densa tipo Wikipedia/Zettelkasten

Este script escanea archivos de teoría (TH-*.md) y problemas (PR-*.md) y
automáticamente enlaza la primera mención de términos del glosario.

Uso:
    python autolink_glossary.py                    # Vista previa (dry-run)
    python autolink_glossary.py --apply            # Aplicar cambios
    python autolink_glossary.py --report           # Generar reporte de enlaces
    python autolink_glossary.py --check            # Verificar enlaces rotos

Autor: Repositorio Circuitos Eléctricos
Versión: 1.0.0
"""

import os
import re
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass


@dataclass
class GlossaryTerm:
    """Representa un término del glosario."""
    term: str
    anchor: str
    aliases: List[str]
    

class AutolinkGlossary:
    """Motor de hipervinculación automática al glosario."""
    
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.glossary_path = repo_root / "glossary.md"
        self.terms: Dict[str, GlossaryTerm] = {}
        self.stats = {
            "files_scanned": 0,
            "links_added": 0,
            "terms_found": 0,
            "files_modified": 0
        }
        
    def parse_glossary(self) -> Dict[str, GlossaryTerm]:
        """
        Parsea el glosario y extrae términos con sus anclas.
        Soporta múltiples anclas (aliases) por término.
        """
        if not self.glossary_path.exists():
            raise FileNotFoundError(f"No se encontró el glosario en {self.glossary_path}")
        
        content = self.glossary_path.read_text(encoding='utf-8')
        terms = {}
        
        # Patrón para encontrar anclas HTML seguidas de definiciones
        # Ejemplo: <a id="capacitancia"></a>\n**Capacitancia (C)**:
        pattern = r'(<a id="([^"]+)"></a>\s*)+\*\*([^*]+)\*\*'
        
        for match in re.finditer(pattern, content):
            full_match = match.group(0)
            
            # Extraer todas las anclas (puede haber múltiples)
            anchors = re.findall(r'<a id="([^"]+)">', full_match)
            
            # Extraer el término principal (sin paréntesis)
            term_raw = match.group(3)
            term_clean = re.sub(r'\s*\([^)]*\)', '', term_raw).strip()
            
            if anchors and term_clean:
                primary_anchor = anchors[0]
                
                # Crear variantes del término para búsqueda
                aliases = [term_clean, term_clean.lower()]
                
                # Agregar variantes comunes
                if "Ley de" in term_clean:
                    aliases.append(term_clean.replace("Ley de ", ""))
                if ", " in term_clean:
                    parts = term_clean.split(", ")
                    aliases.extend([p.strip() for p in parts])
                
                # Agregar aliases de las anclas adicionales
                for anchor in anchors:
                    alias = anchor.replace("-", " ").title()
                    if alias not in aliases:
                        aliases.append(alias)
                
                terms[term_clean.lower()] = GlossaryTerm(
                    term=term_clean,
                    anchor=primary_anchor,
                    aliases=list(set(aliases))
                )
        
        self.terms = terms
        self.stats["terms_found"] = len(terms)
        return terms
    
    def get_relative_path(self, from_file: Path, to_file: Path) -> str:
        """Calcula la ruta relativa desde un archivo hacia otro."""
        try:
            return os.path.relpath(to_file, from_file.parent).replace("\\", "/")
        except ValueError:
            # En Windows, si están en diferentes unidades
            return str(to_file).replace("\\", "/")
    
    def should_skip_line(self, line: str) -> bool:
        """Determina si una línea debe ser ignorada para el enlazado."""
        skip_patterns = [
            r'^\s*#',           # Encabezados
            r'^\s*\|',          # Tablas
            r'^\s*```',         # Bloques de código
            r'^\s*\$\$',        # Ecuaciones de bloque
            r'^\s*>',           # Blockquotes (como la sección Teoría Relacionada)
            r'^\s*-\s*\[',      # Items de lista con enlaces
            r'\[.*\]\(.*\)',    # Ya tiene enlaces
        ]
        return any(re.match(p, line) for p in skip_patterns)
    
    def process_file(self, file_path: Path, dry_run: bool = True) -> Tuple[str, List[str]]:
        """
        Procesa un archivo y agrega enlaces al glosario.
        
        Args:
            file_path: Ruta al archivo a procesar
            dry_run: Si es True, solo reporta sin modificar
            
        Returns:
            Tuple con (contenido modificado, lista de cambios realizados)
        """
        content = file_path.read_text(encoding='utf-8')
        original_content = content
        changes = []
        linked_terms: Set[str] = set()
        
        # Calcular ruta relativa al glosario
        glossary_rel_path = self.get_relative_path(file_path, self.glossary_path)
        
        # Detectar si estamos dentro de un bloque de código
        in_code_block = False
        in_math_block = False
        lines = content.split('\n')
        new_lines = []
        
        for line in lines:
            # Toggle bloques de código
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                new_lines.append(line)
                continue
            
            # Toggle bloques matemáticos
            if line.strip().startswith('$$'):
                in_math_block = not in_math_block
                new_lines.append(line)
                continue
            
            # Saltar líneas en bloques especiales
            if in_code_block or in_math_block or self.should_skip_line(line):
                new_lines.append(line)
                continue
            
            # Procesar términos del glosario
            new_line = line
            for term_key, term_data in self.terms.items():
                # Saltar si ya enlazamos este término en el archivo
                if term_key in linked_terms:
                    continue
                
                # Buscar el término (case-insensitive, palabra completa)
                for alias in term_data.aliases:
                    # Patrón: palabra completa, no dentro de un enlace existente
                    pattern = rf'(?<!\[)\b({re.escape(alias)})\b(?!\]|\()'
                    
                    match = re.search(pattern, new_line, re.IGNORECASE)
                    if match:
                        original_term = match.group(1)
                        link = f'[{original_term}]({glossary_rel_path}#{term_data.anchor})'
                        
                        # Reemplazar solo la primera ocurrencia
                        new_line = new_line[:match.start()] + link + new_line[match.end():]
                        
                        linked_terms.add(term_key)
                        changes.append(f"  ✓ '{original_term}' → #{term_data.anchor}")
                        self.stats["links_added"] += 1
                        break
            
            new_lines.append(new_line)
        
        new_content = '\n'.join(new_lines)
        
        if not dry_run and new_content != original_content:
            file_path.write_text(new_content, encoding='utf-8')
            self.stats["files_modified"] += 1
        
        return new_content, changes
    
    def find_target_files(self) -> List[Path]:
        """Encuentra todos los archivos TH-*.md y PR-*.md en el repositorio."""
        patterns = ['**/theory/TH-*.md', '**/problems/PR-*.md', '**/methods/MET-*.md']
        files = []
        
        for pattern in patterns:
            files.extend(self.repo_root.glob(pattern))
        
        return sorted(files)
    
    def run(self, dry_run: bool = True, verbose: bool = True) -> Dict:
        """
        Ejecuta el proceso de autoenlazado.
        
        Args:
            dry_run: Si True, solo muestra preview sin modificar archivos
            verbose: Si True, muestra detalles de cada archivo
        """
        print("=" * 60)
        print("🔗 Autolink Glossary - Sistema de Hipervinculación Densa")
        print("=" * 60)
        
        if dry_run:
            print("📋 Modo: VISTA PREVIA (dry-run)")
        else:
            print("⚡ Modo: APLICAR CAMBIOS")
        print()
        
        # Parsear glosario
        print(f"📖 Parseando glosario: {self.glossary_path}")
        self.parse_glossary()
        print(f"   Términos encontrados: {len(self.terms)}")
        print()
        
        # Listar términos
        if verbose:
            print("📚 Términos disponibles:")
            for term_key, term_data in sorted(self.terms.items()):
                print(f"   • {term_data.term} (#{term_data.anchor})")
            print()
        
        # Procesar archivos
        files = self.find_target_files()
        print(f"📁 Archivos a procesar: {len(files)}")
        print("-" * 60)
        
        for file_path in files:
            self.stats["files_scanned"] += 1
            rel_path = file_path.relative_to(self.repo_root)
            
            _, changes = self.process_file(file_path, dry_run)
            
            if changes:
                print(f"\n📄 {rel_path}")
                for change in changes:
                    print(change)
        
        # Resumen
        print()
        print("=" * 60)
        print("📊 RESUMEN")
        print("=" * 60)
        print(f"   Archivos escaneados: {self.stats['files_scanned']}")
        print(f"   Términos en glosario: {self.stats['terms_found']}")
        print(f"   Enlaces {'a agregar' if dry_run else 'agregados'}: {self.stats['links_added']}")
        print(f"   Archivos {'a modificar' if dry_run else 'modificados'}: {self.stats['files_modified']}")
        
        if dry_run and self.stats['links_added'] > 0:
            print()
            print("💡 Ejecuta con --apply para aplicar los cambios")
        
        return self.stats
    
    def check_broken_links(self) -> List[Tuple[Path, str, str]]:
        """Verifica enlaces rotos al glosario en todos los archivos."""
        broken = []
        files = self.find_target_files()
        
        # También revisar archivos de índice
        files.extend(self.repo_root.glob('**/*Index*.md'))
        files.extend(self.repo_root.glob('**/*Intro*.md'))
        
        glossary_anchors = set()
        glossary_content = self.glossary_path.read_text(encoding='utf-8')
        for match in re.finditer(r'<a id="([^"]+)">', glossary_content):
            glossary_anchors.add(match.group(1))
        
        for file_path in files:
            content = file_path.read_text(encoding='utf-8')
            
            # Buscar enlaces al glosario
            for match in re.finditer(r'\[([^\]]+)\]\([^)]*glossary\.md#([^)]+)\)', content):
                link_text = match.group(1)
                anchor = match.group(2)
                
                if anchor not in glossary_anchors:
                    broken.append((file_path, link_text, anchor))
        
        return broken
    
    def generate_report(self) -> str:
        """Genera un reporte detallado del estado de hipervinculación."""
        self.parse_glossary()
        files = self.find_target_files()
        
        report = []
        report.append("# 📊 Reporte de Hipervinculación del Glosario")
        report.append("")
        report.append(f"**Fecha:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}")
        report.append(f"**Términos en glosario:** {len(self.terms)}")
        report.append(f"**Archivos analizados:** {len(files)}")
        report.append("")
        
        # Estadísticas por término
        term_usage = {term: 0 for term in self.terms}
        
        for file_path in files:
            content = file_path.read_text(encoding='utf-8')
            for term_key, term_data in self.terms.items():
                if f'#{term_data.anchor})' in content:
                    term_usage[term_key] += 1
        
        report.append("## Uso de Términos")
        report.append("")
        report.append("| Término | Enlaces | Estado |")
        report.append("|---------|---------|--------|")
        
        for term_key, count in sorted(term_usage.items(), key=lambda x: x[1], reverse=True):
            term_data = self.terms[term_key]
            status = "✅ Activo" if count > 0 else "⚠️ Sin usar"
            report.append(f"| {term_data.term} | {count} | {status} |")
        
        return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(
        description='Sistema de hipervinculación automática al glosario',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python autolink_glossary.py              # Vista previa de cambios
  python autolink_glossary.py --apply      # Aplicar cambios
  python autolink_glossary.py --check      # Verificar enlaces rotos
  python autolink_glossary.py --report     # Generar reporte
        """
    )
    
    parser.add_argument('--apply', action='store_true',
                        help='Aplicar cambios (sin esto, solo muestra preview)')
    parser.add_argument('--check', action='store_true',
                        help='Verificar enlaces rotos al glosario')
    parser.add_argument('--report', action='store_true',
                        help='Generar reporte de uso del glosario')
    parser.add_argument('--quiet', '-q', action='store_true',
                        help='Modo silencioso (menos output)')
    
    args = parser.parse_args()
    
    # Encontrar la raíz del repositorio
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent  # Subir desde 00-META/tools/
    
    autolinker = AutolinkGlossary(repo_root)
    
    if args.check:
        print("🔍 Verificando enlaces rotos al glosario...")
        broken = autolinker.check_broken_links()
        if broken:
            print(f"\n❌ Se encontraron {len(broken)} enlaces rotos:\n")
            for file_path, text, anchor in broken:
                rel_path = file_path.relative_to(repo_root)
                print(f"  • {rel_path}: [{text}] → #{anchor}")
        else:
            print("\n✅ No se encontraron enlaces rotos")
        return
    
    if args.report:
        report = autolinker.generate_report()
        report_path = repo_root / "00-META" / "glossary-report.md"
        report_path.write_text(report, encoding='utf-8')
        print(f"📄 Reporte generado: {report_path}")
        print(report)
        return
    
    # Ejecutar autoenlazado
    autolinker.run(dry_run=not args.apply, verbose=not args.quiet)


if __name__ == "__main__":
    main()
