#!/usr/bin/env python3
"""
fig_02_circuito_rl.py - Circuito RL de primer orden
Genera: fig_02_circuito_rl.svg

Muestra: Circuito RL con constante de tiempo τ = L/R
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
    
    # Switch
    d += (sw := elm.Switch().right().label('$t=0$', loc='top'))
    d += elm.Line().right().length(0.5)
    
    # Resistor
    d += (R := elm.Resistor().right().label('$R$', loc='top').color(COLORS['secondary']))
    
    # Inductor
    d += (L := elm.Inductor2(loops=3).right().label('$L$', loc='top').color(COLORS['inductor']))
    
    # Cerrar circuito
    d += elm.Line().down().length(3)
    
    # Fuente
    d += elm.Line().at(sw.start).left().length(0.5)
    d += (V := elm.SourceV().down().label('$V_s$', loc='left').color(COLORS['primary']))
    d += elm.Line().right().to(L.end).toy(V.end)
    
    # Tierra
    d += elm.Ground().at(V.end)
    
    # Corriente
    d += elm.CurrentLabelInline(direction='in').at(R.center).label('$i(t)$').color(COLORS['accent'])
    
    # Fórmulas
    d += elm.Label().at((5.5, 0)).label(r'Carga: $i(t) = \frac{V_s}{R}(1 - e^{-t/\tau})$', fontsize=10)
    d += elm.Label().at((5.5, -0.8)).label(r'Descarga: $i(t) = I_0 e^{-t/\tau}$', fontsize=10)
    d += elm.Label().at((5.5, -1.8)).label(r'$\tau = \frac{L}{R}$ (constante de tiempo)', fontsize=10)

    d.save(OUTPUT_SVG)
    d.save(OUTPUT_PNG, dpi=150)

print(f"✓ Generado: {OUTPUT_SVG}")
print(f"✓ Generado: {OUTPUT_PNG}")
