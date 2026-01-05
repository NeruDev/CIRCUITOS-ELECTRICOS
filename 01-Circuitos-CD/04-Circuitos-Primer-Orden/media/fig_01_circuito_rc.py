#!/usr/bin/env python3
"""
fig_01_circuito_rc.py - Circuito RC de primer orden
Genera: fig_01_circuito_rc.svg

Muestra: Circuito RC con constante de tiempo τ = RC
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
    
    # Fuente de voltaje con switch
    d += (sw := elm.Switch().right().label('$t=0$', loc='top'))
    d += elm.Line().right().length(0.5)
    
    # Resistor
    d += (R := elm.Resistor().right().label('$R$', loc='top').color(COLORS['secondary']))
    
    # Punto de conexión
    d += (mid := elm.Dot())
    d += elm.Line().right().length(0.5)
    d += elm.Dot(open=True).label('$v_C(t)$', loc='right')
    
    # Capacitor
    d.push()
    d += (C := elm.Capacitor().at(mid.center).down().label('$C$', loc='right').color(COLORS['capacitor']))
    d += (bot := elm.Dot())
    d.pop()
    
    # Fuente de voltaje
    d += elm.Line().at(sw.start).left().length(0.5)
    d += (V := elm.SourceV().down().label('$V_s$', loc='left').color(COLORS['primary']))
    
    # Cerrar circuito
    d += elm.Line().right().to(bot.center)
    d += elm.Line().right().length(0.5)
    d += elm.Dot(open=True)
    
    # Tierra
    d += elm.Ground().at(V.end)
    
    # Fórmulas
    d += elm.Label().at((5.5, 0)).label(r'Carga: $v_C(t) = V_s(1 - e^{-t/\tau})$', fontsize=10)
    d += elm.Label().at((5.5, -0.8)).label(r'Descarga: $v_C(t) = V_0 e^{-t/\tau}$', fontsize=10)
    d += elm.Label().at((5.5, -1.8)).label(r'$\tau = RC$ (constante de tiempo)', fontsize=10)

    d.save(OUTPUT_SVG)
    d.save(OUTPUT_PNG, dpi=150)

print(f"✓ Generado: {OUTPUT_SVG}")
print(f"✓ Generado: {OUTPUT_PNG}")
