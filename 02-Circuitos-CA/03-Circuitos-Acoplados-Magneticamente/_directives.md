<!--
::METADATA::
type: directive
topic_id: ca-03-circuitos-acoplados-magneticamente
file_id: _directives
status: active
audience: ai_context
last_updated: 2026-01-05
-->

# Directivas IA — Circuitos Acoplados Magnéticamente

## Hereda de

- [Contrato IA Global](../../00-META/ia-contract.md)
- [Nomenclatura Estándar](../../00-META/nomenclatura-estandar.md)
- [Notación y Símbolos](../../00-META/notation-cheatsheet.md)

---

## Contexto del Subtema

| Campo | Valor |
|-------|-------|
| **ID** | `ca-03-circuitos-acoplados-magneticamente` |
| **Módulo** | 02-Circuitos-CA |
| **Prerequisitos** | `ca-01-analisis-ca-estado-estacionario` |
| **Nivel base** | ⭐⭐⭐ Avanzado |

---

## Directivas Específicas

### 1. Conceptos Clave a Dominar

- Fenómeno de inducción electromagnética
- Autoinductancia e inductancia mutua
- Coeficiente de acoplamiento $k$
- Convención del punto (marcas de polaridad)
- Transformador ideal
- Impedancia reflejada
- Circuitos equivalentes T y π

### 2. Convenciones de Notación

| Símbolo | Significado | Unidad |
|---------|-------------|--------|
| $M$ | Inductancia mutua | H |
| $k$ | Coeficiente de acoplamiento | - |
| $L_1, L_2$ | Inductancias propias | H |
| $n$ | Relación de transformación | - |
| $\bullet$ | Marca de polaridad (punto) | - |

### 3. Fórmulas Clave

**Coeficiente de acoplamiento:**
$$k = \frac{M}{\sqrt{L_1 L_2}}, \quad 0 \leq k \leq 1$$

**Transformador ideal:**
$$\frac{V_1}{V_2} = \frac{N_1}{N_2} = n, \quad \frac{I_1}{I_2} = \frac{1}{n}$$

**Impedancia reflejada:**
$$Z_{ref} = n^2 Z_L$$

### 4. Verificación de Respuestas

- [ ] Verificar convención del punto para signo de $M$
- [ ] Comprobar $0 \leq k \leq 1$
- [ ] Verificar conservación de potencia en transformador ideal
- [ ] Validar polaridad de voltajes inducidos

### 5. Errores Comunes a Detectar

- Ignorar convención del punto
- Confundir signo de voltaje mutuamente inducido
- Aplicar $k > 1$ (físicamente imposible)
- Error en dirección de corriente respecto al punto

---

## Referencias Bibliográficas

Ver [`manifest.json`](manifest.json) para mapeo completo de capítulos.

**Fuentes principales:**
- Sadiku (2013): Capítulo 13
- Hayt (2012): Capítulo 13

---

## Mapa de Recursos

```
theory/      → Fundamentos teóricos (TH-01 a TH-05)
methods/     → Procedimientos paso a paso (MET-01)
problems/    → Enunciados de ejercicios (PR-01 a PR-02)
solutions/   → Respuestas y soluciones desarrolladas
simulation/  → Archivos Proteus 8.15
```
