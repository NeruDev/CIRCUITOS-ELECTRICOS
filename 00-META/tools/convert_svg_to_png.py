#!/usr/bin/env python3
"""
convert_svg_to_png.py - Convierte SVG a PNG usando svglib/reportlab
Uso: python convert_svg_to_png.py [--dpi DPI]
"""

import sys
from pathlib import Path

# Configurar matplotlib backend antes de cualquier import
import matplotlib
matplotlib.use('Agg')

def convert_svg_to_png(svg_path: Path, dpi: int = 150, scale: float = 2.0):
    """Convierte un archivo SVG a PNG usando svglib y reportlab."""
    try:
        from svglib.svglib import svg2rlg
        from reportlab.graphics import renderPM
        
        drawing = svg2rlg(str(svg_path))
        if drawing is None:
            print(f"Error: No se pudo cargar {svg_path}")
            return None
        
        png_path = svg_path.with_suffix('.png')
        
        # Escalar para mejor calidad
        drawing.width *= scale
        drawing.height *= scale
        drawing.scale(scale, scale)
        
        renderPM.drawToFile(drawing, str(png_path), fmt='PNG', dpi=dpi)
        return png_path
        
    except ImportError as e:
        print(f"Error: Dependencia faltante - {e}")
        print("Instale: pip install svglib reportlab")
        return None
    except Exception as e:
        print(f"Error convirtiendo {svg_path}: {e}")
        return None


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Convierte SVG a PNG')
    parser.add_argument('--dpi', type=int, default=150, help='DPI para PNG (default: 150)')
    parser.add_argument('--input', type=str, help='Archivo SVG específico a convertir')
    args = parser.parse_args()
    
    ROOT = Path(__file__).parents[2]
    
    if args.input:
        svg_files = [Path(args.input)]
    else:
        # Buscar todos los SVG en carpetas media/
        svg_files = list(ROOT.glob('**/media/fig_*.svg'))
    
    print(f"\n{'='*50}")
    print(" Convertidor SVG → PNG")
    print(f"{'='*50}\n")
    print(f"🔍 Encontrados {len(svg_files)} archivos SVG.\n")
    
    success = 0
    failed = 0
    
    for svg in svg_files:
        rel_path = svg.relative_to(ROOT)
        print(f"  📷 {rel_path}... ", end="", flush=True)
        
        png = convert_svg_to_png(svg, args.dpi)
        if png and png.exists():
            print("✓")
            success += 1
        else:
            print("✗")
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"📊 Resumen:")
    print(f"   Total: {len(svg_files)}")
    print(f"   ✓ Éxito: {success}")
    if failed > 0:
        print(f"   ✗ Fallidos: {failed}")
    print(f"{'='*50}\n")


if __name__ == '__main__':
    main()
