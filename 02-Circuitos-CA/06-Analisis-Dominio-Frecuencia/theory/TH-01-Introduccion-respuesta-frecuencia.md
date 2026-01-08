# TH-01: Introducción al Problema de Respuesta en Frecuencia

## Objetivos
- Comprender el concepto de respuesta en [frecuencia](../../../glossary.md#frecuencia)
- Definir la función de transferencia
- Introducir magnitud y fase en función de la frecuencia

## Contenido

### ¿Qué es la Respuesta en Frecuencia?

La **respuesta en frecuencia** describe cómo un [circuito](../../../glossary.md#circuito) responde a señales de entrada senoidales de diferentes frecuencias.

### Función de Transferencia

La **función de transferencia** H(jω) es la relación entre la salida y la entrada en el dominio de la frecuencia:

$$H(j\omega) = \frac{\mathbf{V}_{salida}}{\mathbf{V}_{entrada}} = \frac{Y(j\omega)}{X(j\omega)}$$

### Forma General

$$H(j\omega) = |H(j\omega)| \angle\phi(\omega)$$

Donde:
- |H(jω)| = magnitud (ganancia)
- φ(ω) = fase

### Variable s y jω

En análisis de circuitos:
- s = σ + jω (variable compleja general)
- Para estado estable senoidal: s = jω (σ = 0)

La función de transferencia H(s) evaluada en s = jω da H(jω).

### Respuesta de un Sistema Lineal

Para una entrada senoidal:
$$x(t) = X_m \cos(\omega t + \phi_x)$$

La salida en estado estable es:
$$y(t) = |H(j\omega)| X_m \cos(\omega t + \phi_x + \angle H(j\omega))$$

**Observaciones:**
- La frecuencia no cambia
- La amplitud se escala por |H(jω)|
- La fase se desplaza por ∠H(jω)

### Representaciones de H(jω)

**1. Tabla de valores:**
| ω | |H| | φ |
|---|-----|---|
| ω₁ | |H₁| | φ₁ |
| ω₂ | |H₂| | φ₂ |

**2. Gráfica de magnitud y fase vs frecuencia**

**3. Diagrama de Bode** (escala logarítmica)

**4. Diagrama polar** (Nyquist)

### Decibeles

La magnitud se expresa frecuentemente en decibeles (dB):

$$|H|_{dB} = 20\log_{10}|H|$$

| \|H\| | dB |
|-------|-----|
| 1 | 0 |
| 0.707 | -3 |
| 0.5 | -6 |
| 0.1 | -20 |
| 10 | 20 |
| 100 | 40 |

### Ejemplo: Filtro RC Pasa-Bajas

```
    R
○──/\/\/──┬──○
          │
    Vin   C   Vout
          │
○─────────┴──○
```

$$H(j\omega) = \frac{V_{out}}{V_{in}} = \frac{1/j\omega C}{R + 1/j\omega C} = \frac{1}{1 + j\omega RC}$$

**Magnitud:**
$$|H| = \frac{1}{\sqrt{1 + (\omega RC)^2}}$$

**Fase:**
$$\phi = -\arctan(\omega RC)$$

### Frecuencia de Corte

La **frecuencia de corte** ωc es donde |H| = 1/√2 ≈ 0.707 (-3 dB):

Para el filtro RC:
$$\omega_c = \frac{1}{RC}$$
$$f_c = \frac{1}{2\pi RC}$$

## Conceptos Clave
- H(jω) = magnitud × fase
- Magnitud en dB = 20 log₁₀|H|
- Frecuencia de corte: -3 dB
