#!/usr/bin/env python3
"""
fig_01_fasor_impedancia.py - Representación fasorial e impedancia
Genera: fig_01_fasor_impedancia.svg

Muestra: Circuito RLC serie con impedancia compleja
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
    
    # Fuente AC
    d += (Vs := elm.SourceSin().up().label(r'$V_s = V_m\angle\theta$', loc='left').color(COLORS['primary']))
    d += elm.Line().right().length(0.5)
    
    # Resistor
    d += (R := elm.Resistor().right().label('$R$', loc='top').color(COLORS['secondary']))
    d += elm.Label().at(R.center).label('$Z_R = R$', loc='bottom', ofst=0.4, fontsize=9)
    
    # Inductor
    d += (L := elm.Inductor2(loops=3).right().label('$L$', loc='top').color(COLORS['inductor']))
    d += elm.Label().at(L.center).label(r'$Z_L = j\omega L$', loc='bottom', ofst=0.4, fontsize=9)
    
    # Capacitor
    d += (C := elm.Capacitor().right().label('$C$', loc='top').color(COLORS['capacitor']))
    d += elm.Label().at(C.center).label(r'$Z_C = \frac{1}{j\omega C}$', loc='bottom', ofst=0.4, fontsize=9)
    
    # Cerrar circuito
    d += elm.Line().down().length(3)
    d += elm.Line().left().to(Vs.start)
    
    # Corriente
    d += elm.CurrentLabelInline(direction='in').at(R.start).label(r'$\mathbf{I}$').color(COLORS['accent'])
    
    # Fórmulas
    d += elm.Label().at((5, -2)).label(r'$\mathbf{Z}_{total} = R + j\omega L + \frac{1}{j\omega C}$', fontsize=10)
    d += elm.Label().at((5, -2.8)).label(r'$\mathbf{Z} = R + j(X_L - X_C)$', fontsize=10)
    d += elm.Label().at((5, -3.6)).label(r'$|\mathbf{Z}| = \sqrt{R^2 + (X_L - X_C)^2}$', fontsize=10)

    d.save(OUTPUT_SVG)
    d.save(OUTPUT_PNG, dpi=150)

print(f"✓ Generado: {OUTPUT_SVG}")
print(f"✓ Generado: {OUTPUT_PNG}")
