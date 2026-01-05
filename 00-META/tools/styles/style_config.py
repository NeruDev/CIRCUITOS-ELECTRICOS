"""
=============================================================================
CIRCUITOS ELÉCTRICOS - Configuración de Estilos para Schemdraw
=============================================================================
Define estilos globales consistentes para todos los diagramas del repositorio.

Uso:
    from styles.style_config import apply_style, COLORS, FONTS
    apply_style()
=============================================================================
"""

# Configurar matplotlib backend ANTES de importar schemdraw
import matplotlib
matplotlib.use('Agg')  # Backend sin GUI para renderizado headless

import schemdraw
from schemdraw import elements as elm

# =============================================================================
# PALETA DE COLORES
# =============================================================================
COLORS = {
    'primary': '#2563eb',      # Azul - elementos activos (fuentes)
    'secondary': '#059669',    # Verde - elementos pasivos (resistencias)
    'accent': '#dc2626',       # Rojo - puntos de medición, corrientes
    'neutral': '#1f2937',      # Gris oscuro - líneas, conexiones
    'ground': '#6b7280',       # Gris - tierra
    'highlight': '#f59e0b',    # Amarillo/naranja - destacados
    'capacitor': '#7c3aed',    # Violeta - capacitores
    'inductor': '#0891b2',     # Cyan - inductores
    'annotation': '#374151',   # Gris para anotaciones
}

# =============================================================================
# CONFIGURACIÓN DE FUENTES
# =============================================================================
FONTS = {
    'family': 'sans-serif',
    'size': 12,
    'label_size': 11,
    'annotation_size': 10,
}

# =============================================================================
# CONFIGURACIÓN DE LÍNEAS
# =============================================================================
LINE_CONFIG = {
    'lw': 2,           # Grosor de línea estándar
    'lw_thin': 1.5,    # Grosor para líneas secundarias
    'lw_thick': 2.5,   # Grosor para destacados
}

# =============================================================================
# CONFIGURACIÓN GLOBAL DE SCHEMDRAW
# =============================================================================
DEFAULT_CONFIG = {
    'unit': 3,              # Unidad base de espaciado
    'inches_per_unit': 0.5,
    'lw': LINE_CONFIG['lw'],
    'fontsize': FONTS['size'],
    'font': FONTS['family'],
    'color': COLORS['neutral'],
}


def apply_style():
    """
    Aplica la configuración de estilo global a schemdraw.
    Llamar al inicio de cada script de figura.
    """
    # Aplicar tema por defecto y luego personalizar
    schemdraw.theme('default')
    
    # Configuración adicional se aplica en cada Drawing
    return DEFAULT_CONFIG


def get_drawing_config():
    """
    Retorna la configuración para pasar a schemdraw.Drawing().
    
    Uso:
        with schemdraw.Drawing(**get_drawing_config()) as d:
            ...
    """
    return DEFAULT_CONFIG.copy()


# =============================================================================
# ELEMENTOS PERSONALIZADOS Y HELPERS
# =============================================================================

def labeled_resistor(value: str, name: str = None, **kwargs):
    """
    Crea un resistor con etiqueta de valor formateada.
    
    Args:
        value: Valor de resistencia (ej: '1kΩ', '470Ω')
        name: Nombre opcional del componente (ej: 'R1')
    """
    label = f'{name}={value}' if name else value
    return elm.Resistor(**kwargs).label(label)


def labeled_capacitor(value: str, name: str = None, **kwargs):
    """
    Crea un capacitor con etiqueta de valor formateada.
    """
    label = f'{name}={value}' if name else value
    return elm.Capacitor(**kwargs).label(label).color(COLORS['capacitor'])


def labeled_inductor(value: str, name: str = None, **kwargs):
    """
    Crea un inductor con etiqueta de valor formateada.
    """
    label = f'{name}={value}' if name else value
    return elm.Inductor2(loops=3, **kwargs).label(label).color(COLORS['inductor'])


def voltage_source(value: str, name: str = None, **kwargs):
    """
    Crea una fuente de voltaje con etiqueta.
    """
    label = f'{name}={value}' if name else value
    return elm.SourceV(**kwargs).label(label).color(COLORS['primary'])


def current_source(value: str, name: str = None, **kwargs):
    """
    Crea una fuente de corriente con etiqueta.
    """
    label = f'{name}={value}' if name else value
    return elm.SourceI(**kwargs).label(label).color(COLORS['primary'])


def ac_source(value: str, name: str = None, freq: str = None, **kwargs):
    """
    Crea una fuente de CA con etiqueta.
    """
    if freq:
        label = f'{value}, {freq}'
    else:
        label = value
    if name:
        label = f'{name}={label}'
    return elm.SourceSin(**kwargs).label(label).color(COLORS['primary'])


# =============================================================================
# ANOTACIONES Y MARCADORES
# =============================================================================

def current_arrow(label: str = 'I', **kwargs):
    """
    Crea una flecha de corriente con etiqueta.
    """
    return elm.CurrentLabel(**kwargs).label(label).color(COLORS['accent'])


def voltage_arrow(label: str = 'V', **kwargs):
    """
    Crea marcador de voltaje.
    """
    return elm.Gap(**kwargs).label(('+', f'{label}', '−'))


# =============================================================================
# METADATOS PARA SVG
# =============================================================================

def get_svg_metadata(script_name: str, description: str = ''):
    """
    Genera metadatos para incrustar en el SVG generado.
    
    Nota: Schemdraw no soporta metadatos directos en SVG,
    pero esto puede usarse para documentación.
    """
    from datetime import datetime
    return {
        'generated_by': 'schemdraw',
        'source_script': script_name,
        'description': description,
        'generated_on': datetime.now().isoformat(),
        'repository': 'CIRCUITOS-ELECTRICOS'
    }
