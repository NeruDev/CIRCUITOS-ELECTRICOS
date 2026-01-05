<!--
::METADATA::
type: directive
topic_id: cd-03-teoremas-circuitos
file_id: _directives
status: active
audience: ai_context
last_updated: 2026-01-05
-->

# Directivas IA — Teoremas de Circuitos

## Hereda de

- [Contrato IA Global](../../00-META/ia-contract.md)
- [Nomenclatura Estándar](../../00-META/nomenclatura-estandar.md)
- [Notación y Símbolos](../../00-META/notation-cheatsheet.md)

---

## Contexto del Subtema

| Campo | Valor |
|-------|-------|
| **ID** | `cd-03-teoremas-circuitos` |
| **Módulo** | 01-Circuitos-CD |
| **Prerequisitos** | `cd-01-conceptos-leyes-fundamentales`, `cd-02-tecnicas-analisis-circuitos` |
| **Nivel base** | ⭐⭐ Intermedio |

---

## Directivas Específicas

### 1. Conceptos Clave a Dominar

- Linealidad y proporcionalidad
- Teorema de superposición
- Teorema de Thévenin
- Teorema de Norton
- Máxima transferencia de potencia
- Teorema de reciprocidad

### 2. Convenciones de Notación

| Símbolo | Significado |
|---------|-------------|
| $V_{Th}$ | Voltaje de Thévenin |
| $R_{Th}$ | Resistencia de Thévenin |
| $I_N$ | Corriente de Norton |
| $R_N$ | Resistencia de Norton ($R_N = R_{Th}$) |
| $R_L$ | Resistencia de carga |

### 3. Verificación de Respuestas

Al resolver problemas de este tema:

- [ ] Para Thévenin: $V_{Th}$ = voltaje en circuito abierto
- [ ] Para Norton: $I_N$ = corriente en cortocircuito
- [ ] Verificar: $V_{Th} = I_N \cdot R_{Th}$
- [ ] MTP: $R_L = R_{Th}$ para máxima potencia
- [ ] $P_{max} = \frac{V_{Th}^2}{4R_{Th}}$

### 4. Errores Comunes a Detectar

- Olvidar desactivar fuentes independientes (no dependientes)
- Confundir fuente de voltaje en cortocircuito vs fuente de corriente en abierto
- Calcular $R_{Th}$ con fuentes activas
- Aplicar superposición con fuentes dependientes incorrectamente

---

## Referencias Bibliográficas

Ver [`manifest.json`](manifest.json) para mapeo completo de capítulos.

**Fuentes principales:**
- Sadiku (2013): Capítulo 4
- Boylestad (2011): Capítulo 9

---

## Mapa de Recursos

```
theory/      → Fundamentos teóricos (TH-01 a TH-04)
methods/     → Procedimientos paso a paso (MET-01 a MET-03)
problems/    → Enunciados de ejercicios (PR-01 a PR-04)
solutions/   → Respuestas y soluciones desarrolladas
simulation/  → Archivos Proteus 8.15
```
