<!--
::METADATA::
type: directive
topic_id: cd-02-tecnicas-analisis-circuitos
file_id: _directives
status: active
audience: ai_context
last_updated: 2026-01-05
-->

# Directivas IA — Técnicas para el Análisis de Circuitos

## Hereda de

- [Contrato IA Global](../../00-META/ia-contract.md)
- [Nomenclatura Estándar](../../00-META/nomenclatura-estandar.md)
- [Notación y Símbolos](../../00-META/notation-cheatsheet.md)

---

## Contexto del Subtema

| Campo | Valor |
|-------|-------|
| **ID** | `cd-02-tecnicas-analisis-circuitos` |
| **Módulo** | 01-Circuitos-CD |
| **Prerequisitos** | `cd-01-conceptos-leyes-fundamentales` |
| **Nivel base** | ⭐⭐ Intermedio |

---

## Directivas Específicas

### 1. Conceptos Clave a Dominar

- Topología de redes: nodos, ramas, lazos, mallas
- Método de análisis nodal (nodos esenciales)
- Método de análisis de mallas
- Supernodo y supermalla
- Eslabones y análisis de lazos

### 2. Convenciones de Notación

| Símbolo | Significado |
|---------|-------------|
| $V_n$ | Voltaje en nodo $n$ respecto a referencia |
| $I_m$ | Corriente de malla $m$ |
| $G$ | Conductancia ($G = 1/R$) |
| Nodo de referencia | Siempre el de mayor conectividad |

### 3. Verificación de Respuestas

Al resolver problemas de este tema:

- [ ] Verificar número de ecuaciones = variables incógnitas
- [ ] Para nodos: $n-1$ ecuaciones (n = nodos esenciales)
- [ ] Para mallas: $m$ ecuaciones (m = mallas independientes)
- [ ] Validar solución sustituyendo en ecuaciones originales

### 4. Errores Comunes a Detectar

- Elegir mal el nodo de referencia
- Confundir corriente de malla con corriente de rama
- Olvidar ecuación auxiliar en supernodo/supermalla
- Signos incorrectos en fuentes dependientes

---

## Referencias Bibliográficas

Ver [`manifest.json`](manifest.json) para mapeo completo de capítulos.

**Fuentes principales:**
- Sadiku (2013): Capítulo 3
- Hayt (2012): Capítulo 3

---

## Mapa de Recursos

```
theory/      → Fundamentos teóricos (TH-01 a TH-03)
methods/     → Procedimientos paso a paso (MET-01 a MET-03)
problems/    → Enunciados de ejercicios (PR-01 a PR-04)
solutions/   → Respuestas y soluciones desarrolladas
simulation/  → Archivos Proteus 8.15
```
