#!/usr/bin/env python3
"""
fig_03_lvk_malla.py - Ilustración de Ley de Voltajes de Kirchhoff (LVK)
Genera: fig_03_lvk_malla.svg

Muestra: Σv = 0 alrededor de una malla cerrada
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
    d += (V := elm.SourceV().up().label('$V_s = 12V$', loc='left').color(COLORS['primary']))
    
    # Resistor R1 en la parte superior
    d += elm.Line().right().length(1)
    d += (R1 := elm.Resistor().right().label('$R_1 = 2Ω$', loc='top').color(COLORS['secondary']))
    d += elm.Line().right().length(1)
    
    # Resistor R2 bajando
    d += (R2 := elm.Resistor().down().label('$R_2 = 4Ω$', loc='right').color(COLORS['secondary']))
    
    # Línea de retorno
    d += elm.Line().left().length(1)
    
    # Resistor R3 en la parte inferior
    d += (R3 := elm.Resistor().left().label('$R_3 = 6Ω$', loc='bottom').color(COLORS['secondary']))
    d += elm.Line().left().length(1)
    
    # Corriente de malla
    d += elm.LoopCurrent([V, R1, R2, R3], direction='cw').label('$I$').color(COLORS['accent'])
    
    # Ecuación LVK - usar fontsize en label()
    d += elm.Label().at((2.5, -2.5)).label('$V_s - V_{R1} - V_{R2} - V_{R3} = 0$', fontsize=10)

    d.save(OUTPUT_SVG)
    d.save(OUTPUT_PNG, dpi=150)

print(f"✓ Generado: {OUTPUT_SVG}")
print(f"✓ Generado: {OUTPUT_PNG}")
