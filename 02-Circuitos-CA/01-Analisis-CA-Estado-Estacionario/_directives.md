<!--
::METADATA::
type: directive
topic_id: ca-01-analisis-ca-estado-estacionario
file_id: _directives
status: active
audience: ai_context
last_updated: 2026-01-05
-->

# Directivas IA — Análisis CA Estado Estacionario

## Hereda de

- [Contrato IA Global](../../00-META/ia-contract.md)
- [Nomenclatura Estándar](../../00-META/nomenclatura-estandar.md)
- [Notación y Símbolos](../../00-META/notation-cheatsheet.md)

---

## Contexto del Subtema

| Campo | Valor |
|-------|-------|
| **ID** | `ca-01-analisis-ca-estado-estacionario` |
| **Módulo** | 02-Circuitos-CA |
| **Prerequisitos** | `cd-01`, `cd-02`, `cd-03` |
| **Nivel base** | ⭐⭐ Intermedio |

---

## Directivas Específicas

### 1. Conceptos Clave a Dominar

- Onda senoidal: amplitud, frecuencia, fase
- Valor eficaz (RMS) y valor medio
- Números complejos y operaciones
- Fasores y transformación al dominio de la frecuencia
- Impedancia y admitancia compleja
- Análisis nodal y de mallas en CA
- Teoremas de Thévenin/Norton en CA

### 2. Convenciones de Notación

| Símbolo | Significado |
|---------|-------------|
| $\mathbf{V}$, $\tilde{V}$ | Fasor de voltaje |
| $\mathbf{I}$, $\tilde{I}$ | Fasor de corriente |
| $\mathbf{Z}$ | Impedancia compleja |
| $\mathbf{Y}$ | Admitancia compleja |
| $\omega$ | Frecuencia angular (rad/s) |
| $f$ | Frecuencia (Hz) |
| $\angle\theta$ | Ángulo de fase |

### 3. Fórmulas Clave

**Impedancias:**
- Resistor: $\mathbf{Z}_R = R$
- Inductor: $\mathbf{Z}_L = j\omega L$
- Capacitor: $\mathbf{Z}_C = \frac{1}{j\omega C} = -\frac{j}{\omega C}$

**Valor eficaz:**
$$V_{rms} = \frac{V_m}{\sqrt{2}}$$

### 4. Verificación de Respuestas

- [ ] Todas las fuentes deben tener la misma frecuencia $\omega$
- [ ] Verificar conversión rectangular ↔ polar
- [ ] Comprobar unidades de impedancia (Ω)
- [ ] Verificar ángulos en grados o radianes consistentemente

### 5. Errores Comunes a Detectar

- Mezclar valores pico con valores RMS
- Olvidar que $j^2 = -1$
- Confundir $\omega$ (rad/s) con $f$ (Hz)
- Error en signo de impedancia capacitiva
- No convertir ángulos consistentemente

---

## Referencias Bibliográficas

Ver [`manifest.json`](manifest.json) para mapeo completo de capítulos.

**Fuentes principales:**
- Sadiku (2013): Capítulos 9-10
- Hayt (2012): Capítulos 9-10

---

## Mapa de Recursos

```
theory/      → Fundamentos teóricos (TH-01 a TH-08)
methods/     → Procedimientos paso a paso (MET-01 a MET-02)
problems/    → Enunciados de ejercicios (PR-01 a PR-04)
solutions/   → Respuestas y soluciones desarrolladas
simulation/  → Archivos Proteus 8.15
```
