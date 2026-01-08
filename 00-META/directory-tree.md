<!--
::METADATA::
type: reference
topic_id: meta-audit
file_id: directory-tree
status: active
audience: both
last_updated: 2026-01-08
-->

# 🌳 Árbol de Directorios — Estructura Ideal

> Estructura de directorios objetivo para el repositorio de Circuitos Eléctricos.

---

## Estructura Completa

```
CIRCUITOS-ELECTRICOS/
│
├── 📄 NAVEGACIÓN PRINCIPAL
│   ├── README.md                    # Portada del proyecto
│   ├── WIKI_INDEX.md                # Tabla de contenidos maestra
│   ├── glossary.md                  # Diccionario de términos
│   ├── constants.md                 # Constantes físicas
│   └── AUDITORIA_ESTADO_REPO.md     # Reporte de salud
│
├── 🎛️ 00-META/                      # Centro de control
│   ├── ia-contract.md               # LEY SUPREMA para IA
│   ├── ai-directives.md             # Directivas técnicas
│   ├── nomenclatura-estandar.md     # Convenciones de nombrado
│   ├── notation-cheatsheet.md       # Símbolos y notación
│   ├── bibliografia-general.md     # Fuentes académicas
│   ├── study-guide.md               # Guía para estudiantes
│   ├── prompts-for-students.md      # Prompts prediseñados
│   ├── plantilla-respuestas.md      # Modelo para soluciones
│   ├── audit-file-list.md           # Lista de archivos obligatorios
│   ├── audit-table-issues.md        # Registro de problemas
│   ├── directory-tree.md            # Este documento
│   ├── repo-tests.md                # Pruebas de integridad
│   │
│   ├── 🔧 tools/                    # Scripts de automatización
│   │   ├── validate_repo.py         # Auditor de estructura
│   │   ├── link_knowledge_base.py   # Auto-vinculador
│   │   ├── autolink_glossary.py     # Enlaces al glosario
│   │   ├── check_tables.py          # Validador de tablas
│   │   ├── generate_figs.py         # Generador de figuras
│   │   ├── convert_svg_to_png.py    # Conversión de imágenes
│   │   ├── requirements.txt         # Dependencias Python
│   │   ├── README.md                # Documentación
│   │   └── styles/                  # Estilos para figuras
│   │
│   └── 📦 spice-models/             # Modelos SPICE
│       ├── README.md
│       ├── diodes/
│       ├── opamps/
│       ├── passive/
│       └── transistors/
│
├── 🔋 01-Circuitos-CD/              # Módulo: Corriente Directa
│   ├── 00-Index.md                  # Índice del módulo
│   │
│   ├── 01-Conceptos-Leyes-Fundamentales/
│   │   ├── manifest.json
│   │   ├── _directives.md
│   │   ├── 00-Intro.md
│   │   ├── Resumen-Formulas.md
│   │   ├── theory/
│   │   ├── methods/
│   │   ├── problems/
│   │   ├── solutions/
│   │   ├── simulation/
│   │   ├── media/
│   │   └── Notas/
│   │       └── README.md
│   │
│   ├── 02-Tecnicas-Analisis-Circuitos/
│   │   └── [misma estructura]
│   │
│   ├── 03-Teoremas-Circuitos/
│   │   └── [misma estructura]
│   │
│   ├── 04-Circuitos-Primer-Orden/
│   │   └── [misma estructura]
│   │
│   └── 05-Circuitos-Segundo-Orden/
│       └── [misma estructura]
│
└── ⚡ 02-Circuitos-CA/              # Módulo: Corriente Alterna
    ├── 00-Index.md                  # Índice del módulo
    │
    ├── 01-Analisis-CA-Estado-Estacionario/
    │   └── [estructura estándar de subtema]
    │
    ├── 02-Redes-Dos-Puertos/
    │   └── [estructura estándar de subtema]
    │
    ├── 03-Circuitos-Acoplados-Magneticamente/
    │   └── [estructura estándar de subtema]
    │
    ├── 04-Circuitos-Trifasicos/
    │   └── [estructura estándar de subtema]
    │
    ├── 05-Potencia-Electrica/
    │   └── [estructura estándar de subtema]
    │
    └── 06-Analisis-Dominio-Frecuencia/
        └── [estructura estándar de subtema]
```

---

## Estructura Estándar de Subtema

```
XX-Nombre-Subtema/
│
├── 📋 CONFIGURACIÓN
│   ├── manifest.json            # Metadatos para IA
│   └── _directives.md           # Instrucciones específicas
│
├── 📚 CONTENIDO PRINCIPAL
│   ├── 00-Intro.md              # Punto de entrada
│   └── Resumen-Formulas.md      # Cheatsheet
│
├── 📖 CARPETAS SEMÁNTICAS
│   ├── theory/                  # EL "QUÉ" — Definiciones, teoremas
│   │   └── TH-XX-*.md
│   ├── methods/                 # EL "CÓMO" — Procedimientos
│   │   └── MET-XX-*.md
│   ├── problems/                # PRÁCTICA — Ejercicios
│   │   ├── PR-XX-*.md           # Problemas resueltos
│   │   └── EJ-XX-*.md           # Ejercicios propuestos
│   └── solutions/               # VALIDACIÓN — Respuestas
│       └── [Respuestas y desarrollos]
│
├── 📁 RECURSOS
│   ├── simulation/              # Archivos Proteus .pdsprj
│   │   └── SIM-XX-*.pdsprj
│   └── media/                   # Recursos visuales
│       ├── *.svg
│       ├── *.png
│       └── generated/           # Auto-generados
│
└── 🔓 SANDBOX
    └── Notas/                   # Zona libre (exenta de validación)
        └── README.md            # Directiva de excepción
```

---

## Prefijos por Módulo

| Módulo | Prefijo | Ejemplo |
|--------|---------|---------|
| 01-Circuitos-CD | `CD` | `CD-01-Teoria.md` |
| 02-Circuitos-CA | `CA` | `CA-01-Fasores.md` |

---

## Convenciones de Nombrado

| Patrón | Uso |
|--------|-----|
| `TH-XX-Nombre.md` | Archivos de teoría |
| `MET-XX-Nombre.md` | Archivos de métodos |
| `PR-XX-Nombre.md` | Problemas resueltos |
| `EJ-XX-Nombre.md` | Ejercicios propuestos |
| `SIM-XX-Nombre.pdsprj` | Simulaciones Proteus |
| `fig_XX_descripcion.svg` | Figuras generadas |
