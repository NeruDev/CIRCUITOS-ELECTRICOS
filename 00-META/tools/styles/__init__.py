# __init__.py para el paquete styles
"""
Estilos y configuración para generación de diagramas de circuitos.
"""
from .style_config import (
    apply_style,
    get_drawing_config,
    COLORS,
    FONTS,
    LINE_CONFIG,
    labeled_resistor,
    labeled_capacitor,
    labeled_inductor,
    voltage_source,
    current_source,
    ac_source,
    current_arrow,
    voltage_arrow,
    get_svg_metadata,
)

__all__ = [
    'apply_style',
    'get_drawing_config',
    'COLORS',
    'FONTS',
    'LINE_CONFIG',
    'labeled_resistor',
    'labeled_capacitor',
    'labeled_inductor',
    'voltage_source',
    'current_source',
    'ac_source',
    'current_arrow',
    'voltage_arrow',
    'get_svg_metadata',
]
