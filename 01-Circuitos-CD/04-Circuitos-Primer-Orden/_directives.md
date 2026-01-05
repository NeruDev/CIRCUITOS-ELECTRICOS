<!--
::METADATA::
type: directive
topic_id: cd-04-circuitos-primer-orden
file_id: _directives
status: active
audience: ai_context
last_updated: 2026-01-05
-->

# Directivas IA — Circuitos de Primer Orden

## Hereda de

- [Contrato IA Global](../../00-META/ia-contract.md)
- [Nomenclatura Estándar](../../00-META/nomenclatura-estandar.md)
- [Notación y Símbolos](../../00-META/notation-cheatsheet.md)

---

## Contexto del Subtema

| Campo | Valor |
|-------|-------|
| **ID** | `cd-04-circuitos-primer-orden` |
| **Módulo** | 01-Circuitos-CD |
| **Prerequisitos** | `cd-01`, `cd-02`, `cd-03` |
| **Nivel base** | ⭐⭐ Intermedio |

---

## Directivas Específicas

### 1. Conceptos Clave a Dominar

- Inductancia y capacitancia
- Constante de tiempo $\tau$
- Circuitos RC y RL
- Respuesta natural (sin fuente)
- Respuesta forzada (con fuente)
- Respuesta completa
- Funciones singulares (escalón, impulso)

### 2. Convenciones de Notación

| Símbolo | Significado | Unidad |
|---------|-------------|--------|
| $L$ | Inductancia | H (Henrios) |
| $C$ | Capacitancia | F (Faradios) |
| $\tau$ | Constante de tiempo | s (segundos) |
| $v(0^-)$, $v(0^+)$ | Condiciones iniciales | V |
| $i(0^-)$, $i(0^+)$ | Condiciones iniciales | A |

### 3. Fórmulas Clave

**Constantes de tiempo:**
- RC: $\tau = RC$
- RL: $\tau = L/R$

**Respuesta general primer orden:**
$$x(t) = x(\infty) + [x(0^+) - x(\infty)]e^{-t/\tau}$$

### 4. Verificación de Respuestas

- [ ] Verificar condiciones iniciales ($t = 0^+$)
- [ ] Verificar estado estable ($t \to \infty$)
- [ ] Calcular $\tau$ correctamente
- [ ] En $t = 5\tau$, respuesta ≈ 99% del valor final

### 5. Errores Comunes a Detectar

- Confundir $v(0^-)$ con $v(0^+)$ en capacitores
- Olvidar que $i_L$ no puede cambiar instantáneamente
- Olvidar que $v_C$ no puede cambiar instantáneamente
- Calcular $\tau$ con $R$ incorrecta (usar Thévenin)

---

## Referencias Bibliográficas

Ver [`manifest.json`](manifest.json) para mapeo completo de capítulos.

**Fuentes principales:**
- Sadiku (2013): Capítulos 6-7
- Nilsson (2015): Capítulos 6-7

---

## Mapa de Recursos

```
theory/      → Fundamentos teóricos (TH-01 a TH-07)
methods/     → Procedimientos paso a paso (MET-01 a MET-02)
problems/    → Enunciados de ejercicios (PR-01 a PR-05)
solutions/   → Respuestas y soluciones desarrolladas
simulation/  → Archivos Proteus 8.15
```
