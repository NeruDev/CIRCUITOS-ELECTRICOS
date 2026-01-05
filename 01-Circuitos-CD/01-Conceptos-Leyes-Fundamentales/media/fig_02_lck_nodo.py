#!/usr/bin/env python3
"""
fig_02_lck_nodo.py - Ilustración de Ley de Corrientes de Kirchhoff (LCK)
Genera: fig_02_lck_nodo.svg

Muestra: Σi_entrada = Σi_salida en un nodo
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '00-META', 'tools'))

import schemdraw
import schemdraw.elements as elm
from styles.style_config import apply_style, COLORS

apply_style()

BASE_NAME = os.path.join(os.path.dirname(__file__), 
                         os.path.splitext(os.path.basename(__file__))[0])
OUTPUT_SVG = BASE_NAME + '.svg'
OUTPUT_PNG = BASE_NAME + '.png'

with schemdraw.Drawing(show=False) as d:
    d.config(unit=2.5, fontsize=11)
    
    # Nodo central
    d += (dot := elm.Dot().at((0, 0)))
    
    # Corriente I1 entrando desde la izquierda
    d += elm.Line().at((-3, 0)).to(dot.center).color(COLORS['neutral'])
    d += elm.CurrentLabelInline(direction='in').at((-2, 0)).label('$I_1$').color(COLORS['accent'])
    
    # Corriente I2 entrando desde arriba
    d += elm.Line().at((0, 2.5)).to(dot.center).color(COLORS['neutral'])
    d += elm.CurrentLabelInline(direction='in').at((0, 1.5)).label('$I_2$').color(COLORS['primary'])
    
    # Corriente I3 saliendo hacia la derecha
    d += elm.Line().at(dot.center).to((3, 0)).color(COLORS['neutral'])
    d += elm.CurrentLabelInline(direction='out').at((2, 0)).label('$I_3$').color(COLORS['secondary'])
    
    # Corriente I4 saliendo hacia abajo
    d += elm.Line().at(dot.center).to((0, -2.5)).color(COLORS['neutral'])
    d += elm.CurrentLabelInline(direction='out').at((0, -1.5)).label('$I_4$').color(COLORS['highlight'])
    
    # Etiqueta del nodo
    d += elm.Label().at((0.5, 0.5)).label('Nodo', fontsize=10)
    
    # Ecuación LCK
    d += elm.Label().at((0, -3.5)).label('$I_1 + I_2 = I_3 + I_4$', fontsize=12)

    d.save(OUTPUT_SVG)
    d.save(OUTPUT_PNG, dpi=150)

print(f"✓ Generado: {OUTPUT_SVG}")
print(f"✓ Generado: {OUTPUT_PNG}")
