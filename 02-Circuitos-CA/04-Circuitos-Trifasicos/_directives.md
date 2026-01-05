<!--
::METADATA::
type: directive
topic_id: ca-04-circuitos-trifasicos
file_id: _directives
status: active
audience: ai_context
last_updated: 2026-01-05
-->

# Directivas IA — Circuitos Trifásicos

## Hereda de

- [Contrato IA Global](../../00-META/ia-contract.md)
- [Nomenclatura Estándar](../../00-META/nomenclatura-estandar.md)
- [Notación y Símbolos](../../00-META/notation-cheatsheet.md)

---

## Contexto del Subtema

| Campo | Valor |
|-------|-------|
| **ID** | `ca-04-circuitos-trifasicos` |
| **Módulo** | 02-Circuitos-CA |
| **Prerequisitos** | `ca-01-analisis-ca-estado-estacionario` |
| **Nivel base** | ⭐⭐ Intermedio |

---

## Directivas Específicas

### 1. Conceptos Clave a Dominar

- Generación de voltajes trifásicos
- Secuencia de fases (positiva/negativa)
- Conexión estrella (Y) y delta (Δ)
- Voltajes de línea y de fase
- Corrientes de línea y de fase
- Cargas balanceadas y desbalanceadas

### 2. Convenciones de Notación

| Símbolo | Significado |
|---------|-------------|
| $V_{ab}, V_{bc}, V_{ca}$ | Voltajes de línea |
| $V_{an}, V_{bn}, V_{cn}$ | Voltajes de fase (Y) |
| $I_a, I_b, I_c$ | Corrientes de línea |
| $I_{AB}, I_{BC}, I_{CA}$ | Corrientes de fase (Δ) |
| $V_L$ | Magnitud de voltaje de línea |
| $V_p$ | Magnitud de voltaje de fase |

### 3. Fórmulas Clave

**Conexión Y balanceada:**
$$V_L = \sqrt{3} V_p, \quad I_L = I_p$$

**Conexión Δ balanceada:**
$$V_L = V_p, \quad I_L = \sqrt{3} I_p$$

**Potencia trifásica balanceada:**
$$P_{3\phi} = \sqrt{3} V_L I_L \cos\theta = 3 V_p I_p \cos\theta$$

### 4. Verificación de Respuestas

- [ ] Verificar secuencia de fases (120° de desfase)
- [ ] Comprobar relación $\sqrt{3}$ entre línea y fase
- [ ] En sistema balanceado: $I_n = 0$ (corriente de neutro)
- [ ] Verificar ángulos de fase consistentes

### 5. Errores Comunes a Detectar

- Confundir voltaje de línea con voltaje de fase
- Aplicar $\sqrt{3}$ en la conexión incorrecta
- Olvidar desfase de 30° entre $V_L$ y $V_p$ en Y
- Error en secuencia de fases

---

## Referencias Bibliográficas

Ver [`manifest.json`](manifest.json) para mapeo completo de capítulos.

**Fuentes principales:**
- Sadiku (2013): Capítulo 12
- Nilsson (2015): Capítulo 11

---

## Mapa de Recursos

```
theory/      → Fundamentos teóricos (TH-01 a TH-03)
methods/     → Procedimientos paso a paso (MET-01)
problems/    → Enunciados de ejercicios (PR-01 a PR-02)
solutions/   → Respuestas y soluciones desarrolladas
simulation/  → Archivos Proteus 8.15
```
