<!--
::METADATA::
type: directive
topic_id: cd-05-circuitos-segundo-orden
file_id: _directives
status: active
audience: ai_context
last_updated: 2026-01-05
-->

# Directivas IA — Circuitos de Segundo Orden

## Hereda de

- [Contrato IA Global](../../00-META/ia-contract.md)
- [Nomenclatura Estándar](../../00-META/nomenclatura-estandar.md)
- [Notación y Símbolos](../../00-META/notation-cheatsheet.md)

---

## Contexto del Subtema

| Campo | Valor |
|-------|-------|
| **ID** | `cd-05-circuitos-segundo-orden` |
| **Módulo** | 01-Circuitos-CD |
| **Prerequisitos** | `cd-04-circuitos-primer-orden` |
| **Nivel base** | ⭐⭐⭐ Avanzado |

---

## Directivas Específicas

### 1. Conceptos Clave a Dominar

- Circuitos RLC serie y paralelo
- Ecuación característica de segundo orden
- Frecuencia natural no amortiguada $\omega_0$
- Factor de amortiguamiento $\alpha$
- Tipos de respuesta: subamortiguada, críticamente amortiguada, sobreamortiguada

### 2. Convenciones de Notación

| Símbolo | Significado |
|---------|-------------|
| $\omega_0$ | Frecuencia natural no amortiguada |
| $\alpha$ | Factor de amortiguamiento (Neper frequency) |
| $\omega_d$ | Frecuencia amortiguada |
| $\zeta$ | Razón de amortiguamiento |
| $s_1, s_2$ | Raíces de ecuación característica |

### 3. Fórmulas Clave

**RLC Serie:**
- $\alpha = \frac{R}{2L}$
- $\omega_0 = \frac{1}{\sqrt{LC}}$

**RLC Paralelo:**
- $\alpha = \frac{1}{2RC}$
- $\omega_0 = \frac{1}{\sqrt{LC}}$

**Tipos de respuesta:**
| Condición | Tipo | Raíces |
|-----------|------|--------|
| $\alpha > \omega_0$ | Sobreamortiguada | Reales distintas |
| $\alpha = \omega_0$ | Críticamente amortiguada | Reales iguales |
| $\alpha < \omega_0$ | Subamortiguada | Complejas conjugadas |

### 4. Verificación de Respuestas

- [ ] Verificar 2 condiciones iniciales: $x(0^+)$ y $\frac{dx}{dt}(0^+)$
- [ ] Calcular $\alpha$ y $\omega_0$ correctamente
- [ ] Identificar tipo de amortiguamiento
- [ ] Verificar estado estable ($t \to \infty$)

### 5. Errores Comunes a Detectar

- Confundir fórmulas de RLC serie vs paralelo
- Olvidar calcular $\frac{dx}{dt}(0^+)$
- Usar forma incorrecta de solución según amortiguamiento
- Error de signo en raíces complejas

---

## Referencias Bibliográficas

Ver [`manifest.json`](manifest.json) para mapeo completo de capítulos.

**Fuentes principales:**
- Sadiku (2013): Capítulo 8
- Nilsson (2015): Capítulo 8

---

## Mapa de Recursos

```
theory/      → Fundamentos teóricos (TH-01 a TH-02)
methods/     → Procedimientos paso a paso (MET-01 a MET-02)
problems/    → Enunciados de ejercicios (PR-01 a PR-04)
solutions/   → Respuestas y soluciones desarrolladas
simulation/  → Archivos Proteus 8.15
```
