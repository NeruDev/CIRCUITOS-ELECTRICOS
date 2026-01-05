#!/usr/bin/env python3
"""
fig_02_norton.py - Equivalente de Norton
Genera: fig_02_norton.svg

Muestra: Circuito original → Equivalente Norton (In || Rn)
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
    d.config(unit=2.5, fontsize=10)
    
    # === CIRCUITO ORIGINAL (izquierda) ===
    d += elm.Label().at((-1, 2.5)).label('Circuito Original', fontsize=11)
    
    # Caja que representa red lineal
    d += elm.RBox(w=3, h=2.5).at((0, 0)).label('Red\nLineal').color(COLORS['neutral'])
    
    # Terminales a, b
    d += elm.Line().at((1.5, 0.5)).right().length(1)
    d += elm.Dot(open=True).label('a', loc='right')
    d += elm.Line().at((1.5, -0.5)).right().length(1)
    d += elm.Dot(open=True).label('b', loc='right')
    
    # === FLECHA DE EQUIVALENCIA ===
    d += elm.Label().at((4, 0)).label('≡', fontsize=20)
    
    # === EQUIVALENTE NORTON (derecha) ===
    d += elm.Label().at((7, 2.5)).label('Equivalente Norton', fontsize=11)
    
    # Fuente de corriente In
    d += (In := elm.SourceI().at((5, -1)).up().label('$I_N$', loc='left').color(COLORS['primary']))
    
    # Línea superior
    d += elm.Line().right().length(1)
    d += (top := elm.Dot())
    
    # Rn en paralelo
    d.push()
    d += (Rn := elm.Resistor().down().label('$R_N$', loc='right').color(COLORS['secondary']))
    d += (bot := elm.Dot())
    d.pop()
    
    # Terminales
    d += elm.Line().right().length(1.5)
    d += elm.Dot(open=True).label('a', loc='right')
    
    d += elm.Line().at(bot.center).right().length(1.5)
    d += elm.Dot(open=True).label('b', loc='right')
    
    d += elm.Line().at(In.start).right().to(bot.center)
    
    # Fórmulas
    d += elm.Label().at((3.5, -3)).label(r'$I_N$ = Corriente de cortocircuito entre a-b', fontsize=9)
    d += elm.Label().at((3.5, -3.7)).label(r'$R_N = R_{Th}$ (misma resistencia equivalente)', fontsize=9)

    d.save(OUTPUT_SVG)
    d.save(OUTPUT_PNG, dpi=150)

print(f"✓ Generado: {OUTPUT_SVG}")
print(f"✓ Generado: {OUTPUT_PNG}")
