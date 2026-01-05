<!--
::METADATA::
type: directive
topic_id: ca-06-analisis-dominio-frecuencia
file_id: _directives
status: active
audience: ai_context
last_updated: 2026-01-05
-->

# Directivas IA — Análisis en el Dominio de la Frecuencia

## Hereda de

- [Contrato IA Global](../../00-META/ia-contract.md)
- [Nomenclatura Estándar](../../00-META/nomenclatura-estandar.md)
- [Notación y Símbolos](../../00-META/notation-cheatsheet.md)

---

## Contexto del Subtema

| Campo | Valor |
|-------|-------|
| **ID** | `ca-06-analisis-dominio-frecuencia` |
| **Módulo** | 02-Circuitos-CA |
| **Prerequisitos** | `ca-01-analisis-ca-estado-estacionario`, `cd-05-circuitos-segundo-orden` |
| **Nivel base** | ⭐⭐⭐ Avanzado |

---

## Directivas Específicas

### 1. Conceptos Clave a Dominar

- Función de transferencia $H(j\omega)$ o $H(s)$
- Respuesta en frecuencia
- Diagramas de Bode (magnitud y fase)
- Resonancia serie y paralelo
- Factor de calidad Q
- Ancho de banda
- Polos y ceros
- Filtros (pasa-bajos, pasa-altos, pasa-banda, rechaza-banda)

### 2. Convenciones de Notación

| Símbolo | Significado |
|---------|-------------|
| $H(j\omega)$ | Función de transferencia |
| $\omega_0$ | Frecuencia de resonancia |
| $Q$ | Factor de calidad |
| $BW$ | Ancho de banda |
| $\omega_c$ | Frecuencia de corte |
| $|H|_{dB}$ | Magnitud en decibeles |

### 3. Fórmulas Clave

**Resonancia RLC serie:**
$$\omega_0 = \frac{1}{\sqrt{LC}}, \quad Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 RC}$$

**Ancho de banda:**
$$BW = \frac{\omega_0}{Q} = \omega_2 - \omega_1$$

**Decibeles:**
$$|H|_{dB} = 20\log_{10}|H|$$

### 4. Verificación de Respuestas

- [ ] En resonancia: impedancia mínima (serie) o máxima (paralelo)
- [ ] Frecuencias de corte: $|H| = \frac{1}{\sqrt{2}}|H|_{max}$ (-3 dB)
- [ ] Verificar unidades de $Q$ (adimensional)
- [ ] Polos en semiplano izquierdo = sistema estable

### 5. Errores Comunes a Detectar

- Confundir $\omega$ (rad/s) con $f$ (Hz)
- Error en pendiente de Bode (20 dB/década por polo/cero)
- Confundir resonancia serie vs paralelo
- Olvidar contribución de fase de cada polo/cero

---

## Referencias Bibliográficas

Ver [`manifest.json`](manifest.json) para mapeo completo de capítulos.

**Fuentes principales:**
- Sadiku (2013): Capítulo 14
- Boylestad (2011): Capítulo 20

---

## Mapa de Recursos

```
theory/      → Fundamentos teóricos (TH-01 a TH-05)
methods/     → Procedimientos paso a paso (MET-01)
problems/    → Enunciados de ejercicios (PR-01 a PR-04)
solutions/   → Respuestas y soluciones desarrolladas
simulation/  → Archivos Proteus 8.15
```
