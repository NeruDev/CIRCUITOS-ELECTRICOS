# Nomenclatura Estándar del Repositorio

## Estructura de Carpetas

```
XX-Nombre-Modulo/
├── 00-Intro.md
├── theory/
│   └── TH-XX-Nombre-Tema.md
├── methods/
│   └── MET-XX-Nombre-Metodo.md
├── problems/
│   ├── PR-XX-Problema-Resuelto.md
│   └── EJ-XX-Ejercicio-Propuesto.md
├── simulation/
│   └── SIM-XX-Nombre-Simulacion.pdsprj
├── Resumen-Formulas.md
└── manifest.json
```

## Prefijos de Archivos

| Prefijo | Tipo | Descripción | Ubicación |
|---------|------|-------------|-----------|
| TH-XX | Teoría | Contenido teórico del tema | `theory/` |
| MET-XX | Método | Procedimientos paso a paso | `methods/` |
| PR-XX | Problema | Problemas completamente resueltos | `problems/` |
| EJ-XX | Ejercicio | Ejercicios para práctica | `problems/` |
| SIM-XX | Simulación | Archivos Proteus 8.15 | `simulation/` |

## Niveles de Dificultad

| Nivel | Símbolo | Descripción |
|-------|---------|-------------|
| Conceptual | ⭐ | Aplicación directa de fórmulas |
| Intermedio | ⭐⭐ | Requiere sistemas de ecuaciones |
| Avanzado | ⭐⭐⭐ | Circuitos complejos, fuentes dependientes |

## Convenciones de Nombres

1. **Carpetas**: `XX-Nombre-Con-Guiones`
   - XX = número de dos dígitos
   - Usar guiones entre palabras
   - Primera letra mayúscula en cada palabra

2. **Archivos**: `PREFIJO-XX-Nombre-Descriptivo.md`
   - Prefijo según tipo de contenido
   - XX = número de dos dígitos
   - Extensión `.md` para Markdown
   - Extensión `.pdsprj` para Proteus

## Estructura de manifest.json

```json
{
  "id": "modulo-xx",
  "name": "Nombre del Módulo",
  "description": "Descripción breve",
  "topics": ["tema1", "tema2"],
  "prerequisites": ["modulo-anterior"],
  "status": "en_desarrollo|completo",
  "software_requirements": ["Proteus 8.15"],
  "difficulty_levels": {
    "conceptual": "⭐",
    "intermedio": "⭐⭐",
    "avanzado": "⭐⭐⭐"
  },
  "resource_map": {
    "theory": "theory/",
    "methods": "methods/",
    "problems": "problems/",
    "simulation": "simulation/"
  },
  "theoryFiles": 0,
  "methodFiles": 0,
  "problemFiles": 0,
  "simulationFiles": 0
}
```

## Estados de Módulos

| Estado | Símbolo | Descripción |
|--------|---------|-------------|
| En desarrollo | 🔄 | Contenido en progreso |
| Completo | ✅ | Todo el contenido disponible |
| En revisión | 📝 | Pendiente de revisión |
