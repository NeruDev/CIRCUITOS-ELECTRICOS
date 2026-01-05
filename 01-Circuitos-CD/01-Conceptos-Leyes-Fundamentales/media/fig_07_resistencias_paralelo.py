#!/usr/bin/env python3
"""
fig_07_resistencias_paralelo.py - Resistencias en paralelo
Genera: fig_07_resistencias_paralelo.svg

Ilustra: 1/Req = 1/R1 + 1/R2 + 1/R3
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
    
    # Entrada
    d += elm.Dot(open=True).at((0, 0)).label('A', loc='left')
    d += elm.Line().right().length(1)
    d += (top := elm.Dot())
    
    # Rama 1 (arriba)
    d.push()
    d += elm.Line().up().length(1)
    d += (R1 := elm.Resistor().right().label('$R_1$', loc='top').color(COLORS['secondary']))
    d += elm.Line().down().length(1)
    d += (right := elm.Dot())
    d.pop()
    
    # Rama 2 (medio)
    d.push()
    d += (R2 := elm.Resistor().right().label('$R_2$', loc='top').color(COLORS['secondary']))
    d.pop()
    
    # Rama 3 (abajo)
    d += elm.Line().down().length(1)
    d += (R3 := elm.Resistor().right().label('$R_3$', loc='bottom').color(COLORS['secondary']))
    d += elm.Line().up().length(1)
    
    # Salida
    d += elm.Line().right().length(1)
    d += elm.Dot(open=True).label('B', loc='right')
    
    # Fórmulas
    d += elm.Label().at((5.5, 0)).label(r'$\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}$', fontsize=10)
    d += elm.Label().at((5.5, -1.2)).label(r'Para 2 resistencias: $R_{eq} = \frac{R_1 R_2}{R_1 + R_2}$', fontsize=9)

    d.save(OUTPUT_SVG)
    d.save(OUTPUT_PNG, dpi=150)

print(f"✓ Generado: {OUTPUT_SVG}")
print(f"✓ Generado: {OUTPUT_PNG}")
