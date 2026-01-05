#!/usr/bin/env python3
"""
fig_04_divisor_tension.py - Circuito divisor de tensión
Genera: fig_04_divisor_tension.svg

Ilustra: v1 = Vs * R1/(R1+R2)
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
    
    # Fuente de voltaje
    d += (V := elm.SourceV().up().label('$V_s$', loc='left').color(COLORS['primary']))
    d += elm.Line().right().length(1)
    
    # Resistor R1
    d += (R1 := elm.Resistor().right().label('$R_1$', loc='top').color(COLORS['secondary']))
    
    # Punto de división (salida)
    d += (mid := elm.Dot())
    d += elm.Line().right().length(1)
    d += elm.Dot(open=True).label('$V_{out}$', loc='right')
    
    # Resistor R2
    d.push()
    d += (R2 := elm.Resistor().at(mid.center).down().label('$R_2$', loc='right').color(COLORS['secondary']))
    d += elm.Line().left().to(V.start)
    d.pop()
    
    # Tierra
    d += elm.Ground().at(V.start)
    
    # Fórmula
    d += elm.Label().at((4, -1.5)).label(r'$V_{out} = V_s \cdot \frac{R_2}{R_1 + R_2}$', fontsize=11)

    d.save(OUTPUT_SVG)
    d.save(OUTPUT_PNG, dpi=150)

print(f"✓ Generado: {OUTPUT_SVG}")
print(f"✓ Generado: {OUTPUT_PNG}")
