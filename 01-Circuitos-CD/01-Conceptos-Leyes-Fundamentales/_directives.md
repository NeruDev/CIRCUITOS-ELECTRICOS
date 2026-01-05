<!--
::METADATA::
type: directive
topic_id: cd-01-conceptos-leyes-fundamentales
file_id: _directives
status: active
audience: ai_context
last_updated: 2026-01-05
-->

# Directivas IA — Conceptos y Leyes Fundamentales

## Hereda de

- [Contrato IA Global](../../00-META/ia-contract.md)
- [Nomenclatura Estándar](../../00-META/nomenclatura-estandar.md)
- [Notación y Símbolos](../../00-META/notation-cheatsheet.md)

---

## Contexto del Subtema

| Campo | Valor |
|-------|-------|
| **ID** | `cd-01-conceptos-leyes-fundamentales` |
| **Módulo** | 01-Circuitos-CD |
| **Prerequisitos** | Ninguno (tema inicial) |
| **Nivel base** | ⭐ Conceptual |

---

## Directivas Específicas

### 1. Conceptos Clave a Dominar

- Carga eléctrica, corriente, tensión y potencia
- Ley de Ohm: $V = IR$
- Leyes de Kirchhoff (LKV y LKC)
- Resistencias en serie y paralelo
- Divisores de tensión y corriente
- Transformación de fuentes

### 2. Convenciones de Notación

| Símbolo | Significado | Unidad |
|---------|-------------|--------|
| $V$, $v$ | Tensión/Voltaje | V (Volts) |
| $I$, $i$ | Corriente | A (Amperes) |
| $R$ | Resistencia | Ω (Ohms) |
| $P$ | Potencia | W (Watts) |

### 3. Verificación de Respuestas

Al resolver problemas de este tema:

- [ ] Verificar unidades dimensionales
- [ ] Comprobar que $\sum V_{lazo} = 0$ (LKV)
- [ ] Comprobar que $\sum I_{nodo} = 0$ (LKC)
- [ ] Validar con simulación Proteus cuando sea posible

### 4. Errores Comunes a Detectar

- Confundir polaridad de voltajes
- Olvidar la convención de signos en LKV
- Aplicar fórmula de paralelo incorrectamente
- No considerar la dirección de la corriente

---

## Referencias Bibliográficas

Ver [`manifest.json`](manifest.json) para mapeo completo de capítulos.

**Fuentes principales:**
- Sadiku (2013): Capítulos 1-2
- Nilsson (2015): Capítulos 1-3

---

## Mapa de Recursos

```
theory/      → Fundamentos teóricos (TH-01 a TH-09)
methods/     → Procedimientos paso a paso (MET-01 a MET-04)
problems/    → Enunciados de ejercicios (PR-01 a PR-08)
solutions/   → Respuestas y soluciones desarrolladas
simulation/  → Archivos Proteus 8.15
```
