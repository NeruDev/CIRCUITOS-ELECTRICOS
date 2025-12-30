# Nomenclatura Estándar del Repositorio

## Estructura de Carpetas

```
XX-Nombre-Modulo/
├── 00-Intro.md
├── theory/
│   └── TH-XX-Nombre-Tema.md
├── methods/
│   └── MT-XX-Nombre-Metodo.md
├── problems/
│   ├── PR-XX-Problema-Resuelto.md
│   └── EJ-XX-Ejercicio-Propuesto.md
├── Resumen-Formulas.md
└── manifest.json
```

## Prefijos de Archivos

| Prefijo | Tipo | Descripción |
|---------|------|-------------|
| TH-XX | Teoría | Contenido teórico del tema |
| MT-XX | Método | Procedimientos paso a paso |
| PR-XX | Problema | Problemas completamente resueltos |
| EJ-XX | Ejercicio | Ejercicios para práctica |

## Convenciones de Nombres

1. **Carpetas**: `XX-Nombre-Con-Guiones`
   - XX = número de dos dígitos
   - Usar guiones entre palabras
   - Primera letra mayúscula en cada palabra

2. **Archivos**: `PREFIJO-XX-Nombre-Descriptivo.md`
   - Prefijo según tipo de contenido
   - XX = número de dos dígitos
   - Extensión `.md` para Markdown

## Estructura de manifest.json

```json
{
  "id": "modulo-xx",
  "name": "Nombre del Módulo",
  "description": "Descripción breve",
  "topics": ["tema1", "tema2"],
  "prerequisites": ["modulo-anterior"],
  "status": "en_desarrollo|completo"
}
```

## Estados de Módulos

| Estado | Símbolo | Descripción |
|--------|---------|-------------|
| En desarrollo | 🔄 | Contenido en progreso |
| Completo | ✅ | Todo el contenido disponible |
| En revisión | 📝 | Pendiente de revisión |
