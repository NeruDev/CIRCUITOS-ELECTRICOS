#!/usr/bin/env python3
"""
link_knowledge_base.py - Sistema de Jardín Digital tipo Wikipedia/Zettelkasten

Este script convierte un repositorio educativo en un "Jardín Digital" interconectado
realizando dos tareas principales:

  TAREA 1: Auto-hipervinculación (Glosario Activo)
  TAREA 2: Generación del Index Wiki (Directorio Principal)

Uso:
    python link_knowledge_base.py                  # Vista previa (DRY_RUN)
    python link_knowledge_base.py --apply          # Aplicar cambios
    python link_knowledge_base.py --index-only     # Solo generar WIKI_INDEX.md
    python link_knowledge_base.py --links-only     # Solo hipervinculación
    python link_knowledge_base.py --check          # Verificar enlaces rotos
    python link_knowledge_base.py --report         # Generar reporte

Autor: Repositorio Circuitos Eléctricos
Versión: 2.0.0
"""

import os
import re
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Set, Optional
from dataclasses import dataclass, field
from datetime import datetime


# ============================================================================
# CONFIGURACIÓN GLOBAL
# ============================================================================

DRY_RUN = True  # Por defecto NO modifica archivos (modo seguro)

# Carpetas a escanear para contenido
CONTENT_FOLDERS = ['theory', 'problems', 'methods', 'simulation']

# Patrones de archivos a procesar
FILE_PATTERNS = {
    'theory': 'TH-*.md',
    'problems': 'PR-*.md', 
    'methods': 'MET-*.md',
    'simulation': 'SIM-*.md'
}

# Emojis por tipo de contenido
CONTENT_EMOJIS = {
    'theory': '📘',
    'problems': '📝',
    'methods': '🧪',
    'simulation': '💻',
    'index': '📑',
    'module': '📁',
    'submodule': '📂'
}


# ============================================================================
# ESTRUCTURAS DE DATOS
# ============================================================================

@dataclass
class GlossaryTerm:
    """Representa un término del glosario."""
    term: str
    anchor: str
    aliases: List[str] = field(default_factory=list)


@dataclass 
class ContentFile:
    """Representa un archivo de contenido."""
    path: Path
    title: str
    file_type: str  # theory, problems, methods, simulation
    rel_path: str


@dataclass
class Module:
    """Representa un módulo del repositorio."""
    path: Path
    name: str
    order: int
    submodules: List['Submodule'] = field(default_factory=list)


@dataclass
class Submodule:
    """Representa un submódulo (tema dentro de un módulo)."""
    path: Path
    name: str
    order: int
    files: Dict[str, List[ContentFile]] = field(default_factory=dict)


# ============================================================================
# CLASE PRINCIPAL
# ============================================================================

class KnowledgeBaseLinker:
    """Motor principal del Jardín Digital."""
    
    def __init__(self, repo_root: Path, dry_run: bool = True):
        self.repo_root = repo_root
        self.dry_run = dry_run
        self.glossary_path = repo_root / "glossary.md"
        self.readme_path = repo_root / "README.md"
        self.wiki_index_path = repo_root / "WIKI_INDEX.md"
        
        self.terms: Dict[str, GlossaryTerm] = {}
        self.modules: List[Module] = []
        
        self.stats = {
            "files_scanned": 0,
            "links_added": 0,
            "terms_found": 0,
            "files_modified": 0,
            "index_entries": 0
        }
    
    # ========================================================================
    # TAREA 1: AUTO-HIPERVINCULACIÓN
    # ========================================================================
    
    def parse_glossary(self) -> Dict[str, GlossaryTerm]:
        """
        Analiza glossary.md y extrae términos con sus anclas.
        Soporta:
          - Anclas HTML: <a id="termino"></a>
          - Encabezados h2/h3: ## Término o ### Término
        """
        if not self.glossary_path.exists():
            raise FileNotFoundError(f"No se encontró glossary.md en {self.glossary_path}")
        
        content = self.glossary_path.read_text(encoding='utf-8')
        terms = {}
        
        # Método 1: Anclas HTML seguidas de texto en negrita
        # <a id="capacitancia"></a>\n**Capacitancia (C)**:
        pattern_html = r'(<a id="([^"]+)"></a>\s*)+\*\*([^*:]+)'
        
        for match in re.finditer(pattern_html, content):
            anchors = re.findall(r'<a id="([^"]+)">', match.group(0))
            term_raw = match.group(3).strip()
            term_clean = re.sub(r'\s*\([^)]*\)', '', term_raw).strip()
            
            if anchors and term_clean:
                self._add_term(terms, term_clean, anchors[0], anchors)
        
        # Método 2: Encabezados h2/h3 (fallback si no hay anclas)
        # ## Impedancia  → ancla automática: #impedancia
        pattern_headers = r'^#{2,3}\s+(.+)$'
        
        for match in re.finditer(pattern_headers, content, re.MULTILINE):
            term = match.group(1).strip()
            # Ignorar si ya existe el término
            if term.lower() not in terms:
                anchor = self._generate_anchor(term)
                self._add_term(terms, term, anchor, [anchor])
        
        self.terms = terms
        self.stats["terms_found"] = len(terms)
        return terms
    
    def _generate_anchor(self, text: str) -> str:
        """Genera un ancla tipo GitHub a partir de texto."""
        anchor = text.lower()
        anchor = re.sub(r'[^\w\s-]', '', anchor)  # Quitar caracteres especiales
        anchor = re.sub(r'\s+', '-', anchor)      # Espacios → guiones
        return anchor
    
    def _add_term(self, terms: dict, term: str, primary_anchor: str, 
                  anchors: List[str]) -> None:
        """Agrega un término al diccionario con sus aliases."""
        aliases = [term, term.lower()]
        
        # Variantes comunes
        if "Ley de" in term:
            aliases.append(term.replace("Ley de ", ""))
        if ", " in term:
            aliases.extend([p.strip() for p in term.split(", ")])
        
        # Aliases de anclas adicionales
        for anchor in anchors:
            alias = anchor.replace("-", " ").title()
            if alias not in aliases:
                aliases.append(alias)
        
        terms[term.lower()] = GlossaryTerm(
            term=term,
            anchor=primary_anchor,
            aliases=list(set(aliases))
        )
    
    def get_relative_path(self, from_file: Path, to_file: Path) -> str:
        """Calcula la ruta relativa desde un archivo hacia otro."""
        try:
            rel = os.path.relpath(to_file, from_file.parent)
            return rel.replace("\\", "/")
        except ValueError:
            return str(to_file).replace("\\", "/")
    
    def should_skip_line(self, line: str) -> bool:
        """Determina si una línea debe ignorarse para hipervinculación."""
        skip_patterns = [
            r'^\s*#',           # Encabezados
            r'^\s*\|',          # Tablas
            r'^\s*```',         # Bloques de código
            r'^\s*\$\$',        # Ecuaciones de bloque
            r'^\s*>',           # Blockquotes
            r'^\s*-\s*\[',      # Items con enlaces
            r'\[.*\]\(.*\)',    # Ya tiene enlaces
        ]
        return any(re.match(p, line) for p in skip_patterns)
    
    def process_file_links(self, file_path: Path) -> Tuple[str, List[str]]:
        """
        Procesa un archivo e inyecta enlaces al glosario.
        Solo enlaza la PRIMERA mención de cada término.
        """
        content = file_path.read_text(encoding='utf-8')
        original_content = content
        changes = []
        linked_terms: Set[str] = set()
        
        glossary_rel = self.get_relative_path(file_path, self.glossary_path)
        
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
                if term_key in linked_terms:
                    continue
                
                for alias in term_data.aliases:
                    # Palabra completa, no dentro de enlace existente
                    pattern = rf'(?<!\[)\b({re.escape(alias)})\b(?!\]|\()'
                    match = re.search(pattern, new_line, re.IGNORECASE)
                    
                    if match:
                        original_term = match.group(1)
                        link = f'[{original_term}]({glossary_rel}#{term_data.anchor})'
                        new_line = new_line[:match.start()] + link + new_line[match.end():]
                        
                        linked_terms.add(term_key)
                        changes.append(f"  ✓ '{original_term}' → #{term_data.anchor}")
                        self.stats["links_added"] += 1
                        break
            
            new_lines.append(new_line)
        
        new_content = '\n'.join(new_lines)
        
        if not self.dry_run and new_content != original_content:
            file_path.write_text(new_content, encoding='utf-8')
            self.stats["files_modified"] += 1
        
        return new_content, changes
    
    def find_content_files(self) -> List[Path]:
        """Encuentra todos los archivos de contenido en el repositorio."""
        files = []
        for folder in CONTENT_FOLDERS:
            for pattern in FILE_PATTERNS.values():
                files.extend(self.repo_root.glob(f'**/{folder}/{pattern}'))
        return sorted(files)
    
    def run_autolinking(self, verbose: bool = True) -> None:
        """Ejecuta TAREA 1: Auto-hipervinculación."""
        print("\n" + "=" * 60)
        print("🔗 TAREA 1: AUTO-HIPERVINCULACIÓN (Glosario Activo)")
        print("=" * 60)
        
        self.parse_glossary()
        print(f"📖 Términos en glosario: {len(self.terms)}")
        
        if verbose:
            print("\n📚 Términos disponibles:")
            for term_data in sorted(self.terms.values(), key=lambda x: x.term):
                print(f"   • {term_data.term} (#{term_data.anchor})")
        
        files = self.find_content_files()
        print(f"\n📁 Archivos a procesar: {len(files)}")
        print("-" * 60)
        
        for file_path in files:
            self.stats["files_scanned"] += 1
            rel_path = file_path.relative_to(self.repo_root)
            
            _, changes = self.process_file_links(file_path)
            
            if changes:
                print(f"\n📄 {rel_path}")
                for change in changes:
                    print(change)
    
    # ========================================================================
    # TAREA 2: GENERACIÓN DEL INDEX WIKI
    # ========================================================================
    
    def extract_title(self, file_path: Path) -> str:
        """
        Extrae el título H1 de un archivo Markdown.
        Si no existe H1, usa el nombre del archivo como fallback.
        """
        try:
            content = file_path.read_text(encoding='utf-8')
            match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if match:
                return match.group(1).strip()
        except Exception:
            pass
        
        # Fallback: usar nombre del archivo
        name = file_path.stem
        # Limpiar prefijo numérico y guiones
        name = re.sub(r'^[0-9]+-', '', name)
        name = name.replace('-', ' ').replace('_', ' ')
        return name.title()
    
    def scan_repository_structure(self) -> List[Module]:
        """Escanea la estructura del repositorio y construye el árbol."""
        modules = []
        
        # Encontrar módulos principales (01-Nombre, 02-Nombre, etc.)
        for item in sorted(self.repo_root.iterdir()):
            if item.is_dir() and re.match(r'^\d{2}-', item.name):
                module = self._parse_module(item)
                if module:
                    modules.append(module)
        
        self.modules = modules
        return modules
    
    def _parse_module(self, module_path: Path) -> Optional[Module]:
        """Parsea un módulo y sus submódulos."""
        match = re.match(r'^(\d{2})-(.+)$', module_path.name)
        if not match:
            return None
        
        order = int(match.group(1))
        name = match.group(2).replace('-', ' ')
        
        module = Module(
            path=module_path,
            name=name,
            order=order,
            submodules=[]
        )
        
        # Buscar submódulos (01-Subtema/, 02-Subtema/, etc.)
        for item in sorted(module_path.iterdir()):
            if item.is_dir() and re.match(r'^\d{2}-', item.name):
                submodule = self._parse_submodule(item)
                if submodule:
                    module.submodules.append(submodule)
        
        return module
    
    def _parse_submodule(self, submodule_path: Path) -> Optional[Submodule]:
        """Parsea un submódulo y sus archivos."""
        match = re.match(r'^(\d{2})-(.+)$', submodule_path.name)
        if not match:
            return None
        
        order = int(match.group(1))
        name = match.group(2).replace('-', ' ')
        
        submodule = Submodule(
            path=submodule_path,
            name=name,
            order=order,
            files={}
        )
        
        # Buscar archivos por tipo
        for folder_type in CONTENT_FOLDERS:
            folder_path = submodule_path / folder_type
            if folder_path.exists():
                submodule.files[folder_type] = []
                
                pattern = FILE_PATTERNS.get(folder_type, '*.md')
                for file_path in sorted(folder_path.glob(pattern)):
                    title = self.extract_title(file_path)
                    rel_path = str(file_path.relative_to(self.repo_root)).replace("\\", "/")
                    
                    content_file = ContentFile(
                        path=file_path,
                        title=title,
                        file_type=folder_type,
                        rel_path=rel_path
                    )
                    submodule.files[folder_type].append(content_file)
                    self.stats["index_entries"] += 1
        
        return submodule
    
    def generate_wiki_index(self) -> str:
        """Genera el contenido de WIKI_INDEX.md."""
        self.scan_repository_structure()
        
        lines = []
        
        # Cabecera
        lines.append("# 📚 WIKI INDEX - Directorio Principal")
        lines.append("")
        lines.append("> **Navegación centralizada** — Mapa completo del repositorio generado automáticamente.")
        lines.append(">")
        lines.append(f"> _Última actualización: {datetime.now().strftime('%Y-%m-%d %H:%M')}_")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # Enlaces de navegación principal
        lines.append("## 🔗 Navegación Principal")
        lines.append("")
        lines.append(f"| Recurso | Descripción |")
        lines.append("|---------|-------------|")
        lines.append(f"| 📋 [README Principal](README.md) | Información del repositorio |")
        lines.append(f"| 📖 [Glosario Completo](glossary.md) | Definiciones de términos |")
        
        if (self.repo_root / "constants.md").exists():
            lines.append(f"| ⚡ [Constantes Físicas](constants.md) | Valores de referencia |")
        
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # Árbol de contenido
        lines.append("## 📁 Árbol de Contenido")
        lines.append("")
        
        for module in self.modules:
            # Encabezado del módulo
            emoji = CONTENT_EMOJIS['module']
            lines.append(f"### {emoji} {module.order:02d} — {module.name}")
            lines.append("")
            
            for submodule in module.submodules:
                # Encabezado del submódulo
                sub_emoji = CONTENT_EMOJIS['submodule']
                lines.append(f"#### {sub_emoji} {submodule.order:02d} — {submodule.name}")
                lines.append("")
                
                # Archivos por tipo
                for folder_type, files in submodule.files.items():
                    if files:
                        type_emoji = CONTENT_EMOJIS.get(folder_type, '📄')
                        type_label = folder_type.title()
                        
                        lines.append(f"**{type_emoji} {type_label}:**")
                        for cf in files:
                            lines.append(f"- [{cf.title}]({cf.rel_path})")
                        lines.append("")
                
                lines.append("---")
                lines.append("")
        
        # Estadísticas
        lines.append("## 📊 Estadísticas")
        lines.append("")
        lines.append(f"- **Módulos:** {len(self.modules)}")
        total_submodules = sum(len(m.submodules) for m in self.modules)
        lines.append(f"- **Submódulos:** {total_submodules}")
        lines.append(f"- **Archivos indexados:** {self.stats['index_entries']}")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("_Generado automáticamente por `link_knowledge_base.py`_")
        
        return '\n'.join(lines)
    
    def run_index_generation(self) -> None:
        """Ejecuta TAREA 2: Generación del Index Wiki."""
        print("\n" + "=" * 60)
        print("📑 TAREA 2: GENERACIÓN DEL INDEX WIKI")
        print("=" * 60)
        
        content = self.generate_wiki_index()
        
        if self.dry_run:
            print(f"\n📄 Vista previa de WIKI_INDEX.md:\n")
            print("-" * 60)
            # Mostrar primeras 50 líneas
            preview_lines = content.split('\n')[:50]
            print('\n'.join(preview_lines))
            if len(content.split('\n')) > 50:
                print(f"\n... ({len(content.split(chr(10))) - 50} líneas más)")
            print("-" * 60)
        else:
            self.wiki_index_path.write_text(content, encoding='utf-8')
            print(f"\n✅ Archivo generado: {self.wiki_index_path}")
        
        print(f"\n📊 Estadísticas del índice:")
        print(f"   Módulos: {len(self.modules)}")
        print(f"   Submódulos: {sum(len(m.submodules) for m in self.modules)}")
        print(f"   Archivos indexados: {self.stats['index_entries']}")
    
    # ========================================================================
    # UTILIDADES
    # ========================================================================
    
    def check_broken_links(self) -> List[Tuple[Path, str, str]]:
        """Verifica enlaces rotos al glosario."""
        broken = []
        files = self.find_content_files()
        
        # Incluir también índices
        files.extend(self.repo_root.glob('**/*Index*.md'))
        files.extend(self.repo_root.glob('**/*Intro*.md'))
        
        glossary_anchors = set()
        glossary_content = self.glossary_path.read_text(encoding='utf-8')
        for match in re.finditer(r'<a id="([^"]+)">', glossary_content):
            glossary_anchors.add(match.group(1))
        
        for file_path in files:
            try:
                content = file_path.read_text(encoding='utf-8')
                for match in re.finditer(r'\[([^\]]+)\]\([^)]*glossary\.md#([^)]+)\)', content):
                    anchor = match.group(2)
                    if anchor not in glossary_anchors:
                        broken.append((file_path, match.group(1), anchor))
            except Exception:
                continue
        
        return broken
    
    def generate_report(self) -> str:
        """Genera un reporte del estado de hipervinculación."""
        self.parse_glossary()
        files = self.find_content_files()
        
        lines = []
        lines.append("# 📊 Reporte del Jardín Digital")
        lines.append("")
        lines.append(f"**Fecha:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        lines.append(f"**Términos en glosario:** {len(self.terms)}")
        lines.append(f"**Archivos de contenido:** {len(files)}")
        lines.append("")
        
        # Uso de términos
        term_usage = {term: 0 for term in self.terms}
        for file_path in files:
            try:
                content = file_path.read_text(encoding='utf-8')
                for term_key, term_data in self.terms.items():
                    if f'#{term_data.anchor})' in content:
                        term_usage[term_key] += 1
            except Exception:
                continue
        
        lines.append("## Uso de Términos del Glosario")
        lines.append("")
        lines.append("| Término | Enlaces | Estado |")
        lines.append("|---------|---------|--------|")
        
        for term_key, count in sorted(term_usage.items(), key=lambda x: (-x[1], x[0])):
            term_data = self.terms[term_key]
            status = "✅ Activo" if count > 0 else "⚠️ Sin usar"
            lines.append(f"| {term_data.term} | {count} | {status} |")
        
        return '\n'.join(lines)
    
    # ========================================================================
    # EJECUCIÓN PRINCIPAL
    # ========================================================================
    
    def run(self, links_only: bool = False, index_only: bool = False,
            verbose: bool = True) -> Dict:
        """Ejecuta el proceso completo."""
        print("=" * 60)
        print("🌳 LINK KNOWLEDGE BASE - Jardín Digital")
        print("=" * 60)
        
        if self.dry_run:
            print("📋 Modo: VISTA PREVIA (DRY_RUN = True)")
            print("   Los archivos NO serán modificados.")
        else:
            print("⚡ Modo: APLICAR CAMBIOS")
        
        if not index_only:
            self.run_autolinking(verbose)
        
        if not links_only:
            self.run_index_generation()
        
        # Resumen final
        print("\n" + "=" * 60)
        print("📊 RESUMEN FINAL")
        print("=" * 60)
        print(f"   Archivos escaneados: {self.stats['files_scanned']}")
        print(f"   Términos en glosario: {self.stats['terms_found']}")
        print(f"   Enlaces {'a agregar' if self.dry_run else 'agregados'}: {self.stats['links_added']}")
        print(f"   Archivos {'a modificar' if self.dry_run else 'modificados'}: {self.stats['files_modified']}")
        print(f"   Entradas en WIKI_INDEX: {self.stats['index_entries']}")
        
        if self.dry_run and (self.stats['links_added'] > 0 or self.stats['index_entries'] > 0):
            print("\n💡 Ejecuta con --apply para aplicar los cambios")
        
        return self.stats


# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Convierte un repositorio en un Jardín Digital interconectado',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python link_knowledge_base.py                  # Vista previa completa
  python link_knowledge_base.py --apply          # Aplicar todo
  python link_knowledge_base.py --index-only     # Solo generar WIKI_INDEX.md
  python link_knowledge_base.py --links-only     # Solo hipervinculación
  python link_knowledge_base.py --check          # Verificar enlaces rotos
  python link_knowledge_base.py --report         # Generar reporte
        """
    )
    
    parser.add_argument('--apply', action='store_true',
                        help='Aplicar cambios (sin esto, DRY_RUN = True)')
    parser.add_argument('--index-only', action='store_true',
                        help='Solo generar WIKI_INDEX.md')
    parser.add_argument('--links-only', action='store_true',
                        help='Solo ejecutar auto-hipervinculación')
    parser.add_argument('--check', action='store_true',
                        help='Verificar enlaces rotos al glosario')
    parser.add_argument('--report', action='store_true',
                        help='Generar reporte de uso del glosario')
    parser.add_argument('--quiet', '-q', action='store_true',
                        help='Modo silencioso')
    
    args = parser.parse_args()
    
    # Encontrar raíz del repositorio
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent  # Subir desde 00-META/tools/
    
    dry_run = not args.apply
    linker = KnowledgeBaseLinker(repo_root, dry_run=dry_run)
    
    if args.check:
        print("🔍 Verificando enlaces rotos al glosario...")
        broken = linker.check_broken_links()
        if broken:
            print(f"\n❌ Se encontraron {len(broken)} enlaces rotos:\n")
            for file_path, text, anchor in broken:
                rel_path = file_path.relative_to(repo_root)
                print(f"  • {rel_path}: [{text}] → #{anchor}")
        else:
            print("\n✅ No se encontraron enlaces rotos")
        return
    
    if args.report:
        report = linker.generate_report()
        report_path = repo_root / "00-META" / "knowledge-report.md"
        report_path.write_text(report, encoding='utf-8')
        print(f"📄 Reporte generado: {report_path}")
        print(report)
        return
    
    # Ejecutar proceso
    linker.run(
        links_only=args.links_only,
        index_only=args.index_only,
        verbose=not args.quiet
    )


if __name__ == "__main__":
    main()
