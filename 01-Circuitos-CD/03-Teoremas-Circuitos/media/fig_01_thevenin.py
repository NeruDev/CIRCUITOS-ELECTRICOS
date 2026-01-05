#!/usr/bin/env python3
"""
fig_01_thevenin.py - Equivalente de Thévenin
Genera: fig_01_thevenin.svg

Muestra: Circuito original → Equivalente Thévenin (Vth + Rth)
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
    
    # === EQUIVALENTE THÉVENIN (derecha) ===
    d += elm.Label().at((7, 2.5)).label('Equivalente Thévenin', fontsize=11)
    
    # Fuente Vth
    d += (Vth := elm.SourceV().at((5, -1)).up().label('$V_{Th}$', loc='left').color(COLORS['primary']))
    
    # Rth en serie
    d += elm.Line().right().length(0.5)
    d += (Rth := elm.Resistor().right().label('$R_{Th}$', loc='top').color(COLORS['secondary']))
    
    # Terminal a
    d += elm.Line().right().length(0.5)
    d += elm.Dot(open=True).label('a', loc='right')
    
    # Terminal b
    d += elm.Line().at(Vth.start).right().length(3.5)
    d += elm.Dot(open=True).label('b', loc='right')
    
    # Fórmulas
    d += elm.Label().at((3.5, -3)).label(r'$V_{Th}$ = Voltaje de circuito abierto entre a-b', fontsize=9)
    d += elm.Label().at((3.5, -3.7)).label(r'$R_{Th}$ = Resistencia equivalente vista desde a-b', fontsize=9)

    d.save(OUTPUT_SVG)
    d.save(OUTPUT_PNG, dpi=150)

print(f"✓ Generado: {OUTPUT_SVG}")
print(f"✓ Generado: {OUTPUT_PNG}")
