# PR-02: Filtro Pasa-Bajos RC ⭐⭐

## Enunciado
Un filtro pasa-bajos RC de primer orden tiene R = 10kΩ y C = 10nF. Determine:
a) La [frecuencia](../../../glossary.md#frecuencia) de corte fc
b) La función de transferencia H(jω)
c) La ganancia en dB y fase a las frecuencias: 0.1fc, fc, 10fc
d) Dibuje el diagrama de Bode (magnitud y fase)

## Diagrama del Circuito

```
         R = 10kΩ
    ●────/\/\/────┬─────●
    │             │     │
  + │           ┌─┴─┐ + │
Vin │           │ C │ Vout
    │           │10nF   │
  - │           └─┬─┘ - │
    ●─────────────┴─────●
    
    H(jω) = Vout/Vin = 1/(1 + jωRC)
```

## Netlist SPICE

```spice
* PR-02: Filtro Pasa-Bajos RC
* Análisis de frecuencia

V1 1 0 AC 1 0         ; Entrada unitaria para H(f)
R1 1 2 10k            ; R = 10kΩ
C1 2 0 10n            ; C = 10nF

* Barrido de frecuencia logarítmico
.AC DEC 20 10 100k    ; 20 puntos por década, 10Hz a 100kHz
.PRINT AC VDB(2) VP(2); Magnitud en dB y fase
.PROBE
.END
```

## Solución

### Datos
- R = 10 kΩ = 10000 Ω
- C = 10 nF = 10×10⁻⁹ F

### Parte a) Frecuencia de corte

$$f_c = \frac{1}{2\pi RC}$$

$$f_c = \frac{1}{2\pi \times 10000 \times 10 \times 10^{-9}}$$

$$f_c = \frac{1}{2\pi \times 10^{-4}} = \frac{1}{6.283 \times 10^{-4}}$$

$$\boxed{f_c = 1591.5\text{ Hz} \approx 1.59\text{ kHz}}$$

**Frecuencia angular de corte:**
$$\omega_c = 2\pi f_c = \frac{1}{RC} = \frac{1}{10^{-4}} = 10000\text{ rad/s}$$

### Parte b) Función de transferencia

**En el dominio de la frecuencia:**
$$H(j\omega) = \frac{V_{out}}{V_{in}} = \frac{Z_C}{R + Z_C} = \frac{\frac{1}{j\omega C}}{R + \frac{1}{j\omega C}}$$

Multiplicando numerador y denominador por jωC:
$$H(j\omega) = \frac{1}{1 + j\omega RC}$$

Sustituyendo ωc = 1/RC:
$$\boxed{H(j\omega) = \frac{1}{1 + j\frac{\omega}{\omega_c}} = \frac{1}{1 + j\frac{f}{f_c}}}$$

**En forma normalizada:**
Sea u = ω/ωc = f/fc (frecuencia normalizada):
$$H(ju) = \frac{1}{1 + ju}$$

**Magnitud y fase:**
$$|H(j\omega)| = \frac{1}{\sqrt{1 + \left(\frac{\omega}{\omega_c}\right)^2}}$$

$$\phi(\omega) = -\arctan\left(\frac{\omega}{\omega_c}\right)$$

### Parte c) Ganancia y fase a frecuencias específicas

**A f = 0.1fc (159 Hz):**
$$|H| = \frac{1}{\sqrt{1 + 0.1^2}} = \frac{1}{\sqrt{1.01}} = 0.995$$
$$|H|_{dB} = 20\log_{10}(0.995) = -0.043\text{ dB}$$
$$\phi = -\arctan(0.1) = -5.71°$$

**A f = fc (1591 Hz):**
$$|H| = \frac{1}{\sqrt{1 + 1^2}} = \frac{1}{\sqrt{2}} = 0.707$$
$$|H|_{dB} = 20\log_{10}(0.707) = -3.01\text{ dB}$$
$$\phi = -\arctan(1) = -45°$$

**A f = 10fc (15.9 kHz):**
$$|H| = \frac{1}{\sqrt{1 + 10^2}} = \frac{1}{\sqrt{101}} = 0.0995$$
$$|H|_{dB} = 20\log_{10}(0.0995) = -20.04\text{ dB}$$
$$\phi = -\arctan(10) = -84.3°$$

### Parte d) Diagrama de Bode

**Asíntotas de magnitud:**
- Para f << fc: |H|dB ≈ 0 dB (constante)
- Para f >> fc: |H|dB ≈ -20log(f/fc) dB (pendiente -20 dB/década)
- En f = fc: -3 dB

**Asíntotas de fase:**
- Para f << 0.1fc: φ ≈ 0°
- Para f >> 10fc: φ ≈ -90°
- En f = fc: φ = -45°

```
|H| (dB)
    │
  0 ├════════════●═══════════ Asíntota baja frecuencia
    │             ╲
 -3 ├──────────────●──────── Punto de corte (fc)
    │               ╲
-10 │                ╲
    │                 ╲ -20 dB/década
-20 ├──────────────────●────
    │                   ╲
-30 │                    ╲
    │                     ╲
-40 │                      ●
    └──┴────┴────┴────┴────┴──► f (Hz)
      100  159  1.59k  15.9k
          0.1fc  fc   10fc

φ (grados)
    │
  0°├════════●════════════════
    │         ╲
-45°├──────────●─────────────── En fc
    │           ╲
-90°├════════════●════════════ Asíntota alta frecuencia
    └──┴────┴────┴────┴────┴──► f (Hz)
      100  159  1.59k  15.9k
          0.1fc  fc   10fc
```

## Tabla de Respuesta en Frecuencia

| f/fc | f (Hz) | |H| | |H| (dB) | φ (°) |
|------|--------|------|---------|-------|
| 0.01 | 15.9 | 0.99995 | -0.0004 | -0.57 |
| 0.1 | 159 | 0.995 | -0.043 | -5.71 |
| 0.5 | 796 | 0.894 | -0.97 | -26.6 |
| 1.0 | 1591 | 0.707 | -3.01 | -45.0 |
| 2.0 | 3183 | 0.447 | -6.99 | -63.4 |
| 10 | 15915 | 0.0995 | -20.04 | -84.3 |
| 100 | 159155 | 0.01 | -40.0 | -89.4 |

## Características del Filtro

| Parámetro | Valor |
|-----------|-------|
| Tipo | Pasa-bajos de primer orden |
| fc | 1591.5 Hz |
| Pendiente | -20 dB/década = -6 dB/octava |
| Fase en fc | -45° |
| Retardo de grupo | τg = RC = 100 μs |

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| a) fc | **1591.5 Hz** |
| a) ωc | **10000 rad/s** |
| b) H(jω) | **1/(1 + jω/ωc)** |
| c) |H| en 0.1fc | **0.995 (-0.043 dB), φ = -5.7°** |
| c) |H| en fc | **0.707 (-3.01 dB), φ = -45°** |
| c) |H| en 10fc | **0.0995 (-20 dB), φ = -84.3°** |

## Simulación SPICE - Resultados Esperados
```
f = 159.15 Hz:  VDB(2) = -0.04 dB, VP(2) = -5.7°
f = 1591.5 Hz:  VDB(2) = -3.0 dB,  VP(2) = -45°
f = 15915 Hz:   VDB(2) = -20.0 dB, VP(2) = -84.3°
```

## Aplicaciones

1. **Filtro anti-aliasing:** Antes de conversión A/D
2. **Suavizado de señales:** Eliminar ruido de alta frecuencia
3. **Demodulación AM:** Extraer envolvente
4. **Integrador aproximado:** A altas frecuencias

## Conceptos Aplicados
- Función de transferencia de filtros
- Frecuencia de corte a -3dB
- Diagrama de Bode
- Pendiente en dB/década
- Relación fase-frecuencia