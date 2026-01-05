#!/usr/bin/env python3
"""
fig_01_ley_ohm_basico.py - Circuito básico para ilustrar Ley de Ohm
Genera: fig_01_ley_ohm_basico.svg, fig_01_ley_ohm_basico.png

Circuito: Fuente de voltaje + Resistor simple
Ilustra: V = IR
"""

import os
import sys

# Agregar tools al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '00-META', 'tools'))

import schemdraw
import schemdraw.elements as elm
from styles.style_config import apply_style, COLORS

# Aplicar estilo global
apply_style()

# Nombres de salida basados en el script
BASE_NAME = os.path.join(os.path.dirname(__file__), 
                         os.path.splitext(os.path.basename(__file__))[0])
OUTPUT_SVG = BASE_NAME + '.svg'
OUTPUT_PNG = BASE_NAME + '.png'

with schemdraw.Drawing(show=False) as d:
    d.config(unit=3, fontsize=12)
    
    # Fuente de voltaje
    d += (V := elm.SourceV().up().label('$V_s$').color(COLORS['primary']))
    d += elm.Line().right().length(2)
    
    # Resistor
    d += (R := elm.Resistor().down().label('$R$', loc='bottom').color(COLORS['secondary']))
    
    # Cerrar circuito
    d += elm.Line().left().length(2)
    
    # Tierra
    d += elm.Ground().at(V.start)
    
    # Flecha de corriente
    d += elm.CurrentLabelInline(direction='in').at(V.end).label('$I$').color(COLORS['accent'])
    
    # Marcador de voltaje en resistor
    d += elm.Gap().at(R.start).to(R.end).label(('+', '$V_R$', '−'))
    
    # Guardar en ambos formatos
    d.save(OUTPUT_SVG)
    d.save(OUTPUT_PNG, dpi=150)

print(f"✓ Generado: {OUTPUT_SVG}")
print(f"✓ Generado: {OUTPUT_PNG}")
