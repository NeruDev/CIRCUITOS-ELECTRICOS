# TH-02: Respuesta en Frecuencia de Circuitos RL, RC y RLC

## Objetivos
- Analizar la respuesta en [frecuencia](../../../glossary.md#frecuencia) de circuitos básicos
- Identificar comportamiento pasa-bajas y pasa-altas
- Comprender el efecto de los parámetros del [circuito](../../../glossary.md#circuito)

## Contenido

### Circuito RC Pasa-Bajas

```
    R
○──/\/\/──┬──○
          │
    Vin   C   Vout
          │
○─────────┴──○
```

**Función de transferencia:**
$$H(j\omega) = \frac{1}{1 + j\omega/\omega_c}$$

donde ωc = 1/RC

**Magnitud y fase:**
$$|H| = \frac{1}{\sqrt{1 + (\omega/\omega_c)^2}}$$
$$\phi = -\arctan(\omega/\omega_c)$$

**Comportamiento:**
- ω << ωc: |H| ≈ 1, φ ≈ 0°
- ω = ωc: |H| = 0.707, φ = -45°
- ω >> ωc: |H| → 0, φ → -90°

### Circuito RC Pasa-Altas

```
    C
○──||──┬──○
       │
   Vin R  Vout
       │
○──────┴──○
```

**Función de transferencia:**
$$H(j\omega) = \frac{j\omega/\omega_c}{1 + j\omega/\omega_c}$$

**Magnitud:**
$$|H| = \frac{\omega/\omega_c}{\sqrt{1 + (\omega/\omega_c)^2}}$$

**Comportamiento:**
- ω << ωc: |H| → 0
- ω = ωc: |H| = 0.707
- ω >> ωc: |H| → 1

### Circuito RL Pasa-Bajas

```
    L
○──⌇⌇⌇──┬──○
        │
   Vin  R  Vout
        │
○───────┴──○
```

**Función de transferencia:**
$$H(j\omega) = \frac{1}{1 + j\omega L/R}$$

Frecuencia de corte: ωc = R/L

### Circuito RLC Serie (Función de Transferencia en R)

```
    L       R
○──⌇⌇⌇──/\/\/──┬──○
               │
    Vin        C   Vout
               │
○──────────────┴──○
```

**Función de transferencia:**
$$H(j\omega) = \frac{j\omega RC}{1 - \omega^2 LC + j\omega RC}$$

$$H(j\omega) = \frac{j\omega/\omega_0 Q}{1 - (\omega/\omega_0)^2 + j\omega/(\omega_0 Q)}$$

donde:
- ω₀ = 1/√(LC) (frecuencia de [resonancia](../../../glossary.md#resonancia))
- Q = ω₀L/R = 1/(ω₀RC) (factor de calidad)

### Comparación de Filtros Básicos

| Circuito | Tipo | H(0) | H(∞) | ωc |
|----------|------|------|------|-----|
| RC (V en C) | Pasa-bajas | 1 | 0 | 1/RC |
| RC (V en R) | Pasa-altas | 0 | 1 | 1/RC |
| RL (V en R) | Pasa-bajas | 1 | 0 | R/L |
| RL (V en L) | Pasa-altas | 0 | 1 | R/L |

### Diagrama de Bode Asintótico

**Pasa-bajas de primer orden:**
- ω < ωc: 0 dB (constante)
- ω > ωc: -20 dB/década

**Pasa-altas de primer orden:**
- ω < ωc: +20 dB/década
- ω > ωc: 0 dB (constante)

### Ancho de Banda

El **ancho de banda** BW es el rango de frecuencias donde |H| > 0.707 (-3 dB):

Para filtro pasa-bajas: BW = ωc = 1/RC

Para filtro pasa-banda: BW = ω₂ - ω₁

## Conceptos Clave
- Primer orden: pendiente ±20 dB/década
- Segundo orden: pendiente ±40 dB/década en extremos
- ωc determina la transición entre bandas
