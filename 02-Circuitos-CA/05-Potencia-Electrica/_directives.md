<!--
::METADATA::
type: directive
topic_id: ca-05-potencia-electrica
file_id: _directives
status: active
audience: ai_context
last_updated: 2026-01-05
-->

# Directivas IA — Potencia Eléctrica

## Hereda de

- [Contrato IA Global](../../00-META/ia-contract.md)
- [Nomenclatura Estándar](../../00-META/nomenclatura-estandar.md)
- [Notación y Símbolos](../../00-META/notation-cheatsheet.md)

---

## Contexto del Subtema

| Campo | Valor |
|-------|-------|
| **ID** | `ca-05-potencia-electrica` |
| **Módulo** | 02-Circuitos-CA |
| **Prerequisitos** | `ca-01-analisis-ca-estado-estacionario`, `ca-04-circuitos-trifasicos` |
| **Nivel base** | ⭐⭐ Intermedio |

---

## Directivas Específicas

### 1. Conceptos Clave a Dominar

- Potencia instantánea
- Potencia real (activa) P
- Potencia reactiva Q
- Potencia aparente S
- Potencia compleja
- Factor de potencia y su corrección
- Triángulo de potencias
- Método de los dos wattímetros

### 2. Convenciones de Notación

| Símbolo | Significado | Unidad |
|---------|-------------|--------|
| $P$ | Potencia real (activa) | W |
| $Q$ | Potencia reactiva | VAR |
| $S$ | Potencia aparente | VA |
| $\mathbf{S}$ | Potencia compleja | VA |
| $pf$ o $fp$ | Factor de potencia | - |
| $\theta$ | Ángulo de factor de potencia | ° o rad |

### 3. Fórmulas Clave

**Potencia compleja:**
$$\mathbf{S} = P + jQ = V_{rms} I_{rms}^* = \frac{1}{2}\mathbf{V}\mathbf{I}^*$$

**Relaciones:**
$$S = \sqrt{P^2 + Q^2}, \quad pf = \cos\theta = \frac{P}{S}$$

**Factor de potencia:**
- Adelantado (leading): carga capacitiva, $Q < 0$
- Atrasado (lagging): carga inductiva, $Q > 0$

### 4. Verificación de Respuestas

- [ ] Verificar triángulo de potencias: $S^2 = P^2 + Q^2$
- [ ] Factor de potencia: $0 \leq pf \leq 1$
- [ ] Potencia reactiva: signo correcto según carga
- [ ] Conservación de potencia en todo el circuito

### 5. Errores Comunes a Detectar

- Confundir valores pico con RMS
- Signo incorrecto en Q (capacitivo vs inductivo)
- Usar $I$ en lugar de $I^*$ para potencia compleja
- Olvidar especificar adelantado/atrasado en fp

---

## Referencias Bibliográficas

Ver [`manifest.json`](manifest.json) para mapeo completo de capítulos.

**Fuentes principales:**
- Sadiku (2013): Capítulo 11
- Nilsson (2015): Capítulo 10

---

## Mapa de Recursos

```
theory/      → Fundamentos teóricos (TH-01 a TH-03)
methods/     → Procedimientos paso a paso (MET-01)
problems/    → Enunciados de ejercicios (PR-01 a PR-02)
solutions/   → Respuestas y soluciones desarrolladas
simulation/  → Archivos Proteus 8.15
```
