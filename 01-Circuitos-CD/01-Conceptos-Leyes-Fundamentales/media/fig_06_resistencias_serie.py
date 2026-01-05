#!/usr/bin/env python3
"""
fig_06_resistencias_serie.py - Resistencias en serie
Genera: fig_06_resistencias_serie.svg

Ilustra: Req = R1 + R2 + R3
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
    d.config(unit=3, fontsize=11)
    
    # Punto de entrada
    d += elm.Dot(open=True).label('A', loc='left')
    
    # Resistencias en serie
    d += (R1 := elm.Resistor().right().label('$R_1$', loc='top').color(COLORS['secondary']))
    d += (R2 := elm.Resistor().right().label('$R_2$', loc='top').color(COLORS['secondary']))
    d += (R3 := elm.Resistor().right().label('$R_3$', loc='top').color(COLORS['secondary']))
    
    # Punto de salida
    d += elm.Dot(open=True).label('B', loc='right')
    
    # Flecha de corriente
    d += elm.CurrentLabelInline(direction='in').at(R1.start).label('$I$').color(COLORS['accent'])
    
    # Equivalente (debajo)
    d += elm.Label().at((4.5, -1.5)).label('Equivalente:', fontsize=10)
    
    d += elm.Dot(open=True).at((1.5, -2.5)).label('A', loc='left')
    d += elm.Resistor().right().at((1.5, -2.5)).label('$R_{eq}$', loc='top').color(COLORS['highlight'])
    d += elm.Dot(open=True).label('B', loc='right')
    
    # Fórmula
    d += elm.Label().at((4.5, -2.5)).label(r'$R_{eq} = R_1 + R_2 + R_3$', fontsize=11)

    d.save(OUTPUT_SVG)
    d.save(OUTPUT_PNG, dpi=150)

print(f"✓ Generado: {OUTPUT_SVG}")
print(f"✓ Generado: {OUTPUT_PNG}")
