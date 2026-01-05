#!/usr/bin/env python3
"""
=============================================================================
CIRCUITOS ELÉCTRICOS - Generador Automático de Figuras
=============================================================================
Busca y ejecuta scripts fig_*.py en carpetas media/ de todo el repositorio.

Uso:
    python generate_figs.py                    # Genera todas las figuras
    python generate_figs.py --module cd-01    # Solo un módulo específico
    python generate_figs.py --dry-run         # Muestra qué se generaría
    python generate_figs.py --verbose         # Salida detallada

Estructura esperada:
    XX-Modulo/
        YY-Subtema/
            media/
                fig_01_nombre.py  → genera fig_01_nombre.svg

=============================================================================
"""

import os
import sys
import glob
import json
import argparse
import importlib.util
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

# Agregar tools al path para imports de estilos
TOOLS_DIR = Path(__file__).parent
sys.path.insert(0, str(TOOLS_DIR))

# =============================================================================
# CONFIGURACIÓN
# =============================================================================

REPO_ROOT = TOOLS_DIR.parent.parent  # Subir dos niveles desde tools/
FIG_PATTERN = '**/media/fig_*.py'
MANIFEST_NAME = 'manifest.json'

# Colores para output en terminal
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'


def colorize(text: str, color: str) -> str:
    """Aplica color al texto si el terminal lo soporta."""
    if sys.stdout.isatty():
        return f"{color}{text}{Colors.END}"
    return text


# =============================================================================
# FUNCIONES PRINCIPALES
# =============================================================================

def find_figure_scripts(root: Path, module_filter: str = None) -> List[Path]:
    """
    Encuentra todos los scripts de figuras en el repositorio.
    
    Args:
        root: Directorio raíz del repositorio
        module_filter: Filtro opcional por módulo (ej: 'cd-01', 'ca-02')
    
    Returns:
        Lista de rutas a scripts fig_*.py
    """
    pattern = str(root / FIG_PATTERN)
    scripts = [Path(p) for p in glob.glob(pattern, recursive=True)]
    
    if module_filter:
        # Filtrar por módulo (case-insensitive)
        filter_lower = module_filter.lower().replace('-', '')
        scripts = [
            s for s in scripts 
            if filter_lower in str(s).lower().replace('-', '')
        ]
    
    return sorted(scripts)


def execute_figure_script(script_path: Path, verbose: bool = False) -> Dict:
    """
    Ejecuta un script de figura y retorna información del resultado.
    
    Args:
        script_path: Ruta al script Python
        verbose: Si mostrar salida detallada
    
    Returns:
        Diccionario con resultado de ejecución
    """
    result = {
        'script': str(script_path),
        'success': False,
        'output_file': None,
        'error': None,
        'execution_time': None,
    }
    
    start_time = datetime.now()
    
    try:
        # Cambiar al directorio del script para que los paths relativos funcionen
        original_cwd = os.getcwd()
        os.chdir(script_path.parent)
        
        # Cargar y ejecutar el módulo
        spec = importlib.util.spec_from_file_location(
            f"fig_{script_path.stem}", 
            script_path
        )
        module = importlib.util.module_from_spec(spec)
        
        # Agregar tools al path del módulo
        sys.path.insert(0, str(TOOLS_DIR))
        
        spec.loader.exec_module(module)
        
        # El archivo de salida debería ser el mismo nombre pero .svg
        expected_output = script_path.with_suffix('.svg')
        if expected_output.exists():
            result['output_file'] = str(expected_output)
            result['success'] = True
        else:
            # Buscar cualquier SVG nuevo en el directorio
            svgs = list(script_path.parent.glob('*.svg'))
            if svgs:
                result['output_file'] = str(svgs[-1])  # El más reciente
                result['success'] = True
            else:
                result['error'] = "No se generó archivo SVG"
        
        os.chdir(original_cwd)
        
    except Exception as e:
        result['error'] = str(e)
        if verbose:
            import traceback
            result['traceback'] = traceback.format_exc()
        
        try:
            os.chdir(original_cwd)
        except:
            pass
    
    result['execution_time'] = (datetime.now() - start_time).total_seconds()
    return result


def update_manifest_media(subtema_path: Path, media_files: List[Dict]):
    """
    Actualiza el manifest.json con información de media generada.
    
    Args:
        subtema_path: Ruta al directorio del subtema
        media_files: Lista de archivos de media generados
    """
    manifest_path = subtema_path / MANIFEST_NAME
    
    if not manifest_path.exists():
        return
    
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
        
        # Agregar o actualizar sección media
        manifest['media'] = media_files
        manifest['media_generated_on'] = datetime.now().isoformat()
        
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
            
    except Exception as e:
        print(colorize(f"  ⚠ Error actualizando manifest: {e}", Colors.YELLOW))


def generate_all_figures(
    root: Path,
    module_filter: str = None,
    dry_run: bool = False,
    verbose: bool = False
) -> Dict:
    """
    Genera todas las figuras del repositorio.
    
    Args:
        root: Directorio raíz
        module_filter: Filtro opcional por módulo
        dry_run: Si solo mostrar qué se generaría
        verbose: Salida detallada
    
    Returns:
        Resumen de resultados
    """
    scripts = find_figure_scripts(root, module_filter)
    
    if not scripts:
        print(colorize("⚠ No se encontraron scripts de figuras.", Colors.YELLOW))
        return {'total': 0, 'success': 0, 'failed': 0}
    
    print(colorize(f"\n🔍 Encontrados {len(scripts)} scripts de figuras.", Colors.CYAN))
    
    if dry_run:
        print(colorize("\n📋 Modo dry-run - Scripts que se ejecutarían:", Colors.BLUE))
        for script in scripts:
            rel_path = script.relative_to(root)
            print(f"  • {rel_path}")
        return {'total': len(scripts), 'success': 0, 'failed': 0, 'dry_run': True}
    
    print(colorize("\n⚙️  Generando figuras...\n", Colors.BLUE))
    
    results = []
    media_by_subtema = {}  # Para actualizar manifests
    
    for script in scripts:
        rel_path = script.relative_to(root)
        print(f"  📊 {rel_path}...", end=' ')
        
        result = execute_figure_script(script, verbose)
        results.append(result)
        
        if result['success']:
            print(colorize("✓", Colors.GREEN))
            
            # Agrupar por subtema para manifest
            subtema_path = script.parent.parent
            if subtema_path not in media_by_subtema:
                media_by_subtema[subtema_path] = []
            
            media_by_subtema[subtema_path].append({
                'file': f"media/{Path(result['output_file']).name}",
                'source': f"media/{script.name}",
                'generated_by': 'schemdraw',
            })
        else:
            print(colorize(f"✗ ({result['error']})", Colors.RED))
            if verbose and 'traceback' in result:
                print(colorize(result['traceback'], Colors.RED))
    
    # Actualizar manifests
    for subtema_path, media_files in media_by_subtema.items():
        update_manifest_media(subtema_path, media_files)
    
    # Resumen
    success_count = sum(1 for r in results if r['success'])
    failed_count = len(results) - success_count
    
    print(colorize(f"\n{'='*50}", Colors.CYAN))
    print(colorize(f"📊 Resumen:", Colors.BOLD))
    print(f"   Total: {len(results)}")
    print(colorize(f"   ✓ Éxito: {success_count}", Colors.GREEN))
    if failed_count > 0:
        print(colorize(f"   ✗ Fallidos: {failed_count}", Colors.RED))
    print(colorize(f"{'='*50}\n", Colors.CYAN))
    
    return {
        'total': len(results),
        'success': success_count,
        'failed': failed_count,
        'results': results,
    }


# =============================================================================
# CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Genera figuras de circuitos eléctricos automáticamente.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python generate_figs.py                    # Genera todas las figuras
  python generate_figs.py --module cd-01    # Solo módulo CD-01
  python generate_figs.py --dry-run         # Preview sin ejecutar
  python generate_figs.py -v                # Salida detallada
        """
    )
    
    parser.add_argument(
        '--module', '-m',
        help='Filtrar por módulo (ej: cd-01, ca-02)'
    )
    parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help='Mostrar qué se generaría sin ejecutar'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Salida detallada'
    )
    parser.add_argument(
        '--root',
        type=Path,
        default=REPO_ROOT,
        help='Directorio raíz del repositorio'
    )
    
    args = parser.parse_args()
    
    print(colorize("\n" + "="*50, Colors.CYAN))
    print(colorize(" CIRCUITOS ELÉCTRICOS - Generador de Figuras", Colors.BOLD))
    print(colorize("="*50, Colors.CYAN))
    
    results = generate_all_figures(
        root=args.root,
        module_filter=args.module,
        dry_run=args.dry_run,
        verbose=args.verbose,
    )
    
    # Exit code basado en resultados
    sys.exit(0 if results.get('failed', 0) == 0 else 1)


if __name__ == '__main__':
    main()
