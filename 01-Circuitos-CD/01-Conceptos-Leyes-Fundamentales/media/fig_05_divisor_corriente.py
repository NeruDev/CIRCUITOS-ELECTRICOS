#!/usr/bin/env python3
"""
fig_05_divisor_corriente.py - Circuito divisor de corriente
Genera: fig_05_divisor_corriente.svg

Ilustra: i1 = Is * R2/(R1+R2) (la corriente se divide inversamente)
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
    
    # Fuente de corriente
    d += (I := elm.SourceI().up().label('$I_s$', loc='left').color(COLORS['primary']))
    d += elm.CurrentLabelInline(direction='in').at(I.center).label('').color(COLORS['accent'])
    
    # Línea superior
    d += elm.Line().right().length(1)
    d += (top := elm.Dot())
    
    # Rama R1
    d.push()
    d += (R1 := elm.Resistor().down().label('$R_1$', loc='left').color(COLORS['secondary']))
    d += elm.CurrentLabelInline(direction='in').at(R1.center).label('$I_1$').color(COLORS['accent'])
    d += (bot1 := elm.Dot())
    d.pop()
    
    # Conexión a rama R2
    d += elm.Line().right().length(2)
    
    # Rama R2
    d += (R2 := elm.Resistor().down().label('$R_2$', loc='right').color(COLORS['secondary']))
    d += elm.CurrentLabelInline(direction='in').at(R2.center).label('$I_2$').color(COLORS['highlight'])
    
    # Línea inferior de retorno
    d += elm.Line().left().to(bot1.center)
    d += elm.Line().left().to(I.start)
    
    # Tierra
    d += elm.Ground().at(I.start)
    
    # Fórmulas
    d += elm.Label().at((4.5, 0)).label(r'$I_1 = I_s \cdot \frac{R_2}{R_1 + R_2}$', fontsize=10)
    d += elm.Label().at((4.5, -1)).label(r'$I_2 = I_s \cdot \frac{R_1}{R_1 + R_2}$', fontsize=10)

    d.save(OUTPUT_SVG)
    d.save(OUTPUT_PNG, dpi=150)

print(f"✓ Generado: {OUTPUT_SVG}")
print(f"✓ Generado: {OUTPUT_PNG}")
