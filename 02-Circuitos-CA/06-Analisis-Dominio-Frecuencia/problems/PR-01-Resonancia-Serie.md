```markdown
# PR-01: Resonancia en Circuito RLC Serie ⭐⭐⭐

## Enunciado
Un circuito RLC serie tiene R = 10Ω, L = 10mH y C = 10μF. Determine:
a) La frecuencia de resonancia f₀
b) El factor de calidad Q
c) El ancho de banda BW
d) Las frecuencias de corte (mitad de potencia)
e) La impedancia y corriente a la frecuencia de resonancia si Vs = 10V

## Diagrama del Circuito

```
    ┌────/\/\/────┬────◯────┬────||────┐
    │    R=10Ω   │    L    │    C     │
  + │            │  10mH   │  10μF    │
Vs (─)           │         │          │
    │            │         │          │
  - │            │         │          │
    └────────────┴─────────┴──────────┘

    |Z|                    Resonancia
     │                        ↓
     │    ╲                  ╱
     │     ╲   Z = R       ╱
   R ├──────●─────────────●────────
     │       ╲           ╱
     │        ╲_________╱
     └─────────┴────┴────┴──────► f
              f₁   f₀   f₂
              BW = f₂ - f₁
```

## Netlist SPICE

```spice
* PR-01: Resonancia RLC Serie
* Barrido en frecuencia

V1 1 0 AC 10 0        ; Fuente 10V
R1 1 2 10             ; R = 10Ω
L1 2 3 10m            ; L = 10mH
C1 3 0 10u            ; C = 10μF

* Barrido de frecuencia de 100Hz a 1kHz
.AC DEC 100 100 10k
.PRINT AC VM(3) IM(R1) VP(R1)
.PROBE
.END
```

## Solución

### Datos
- R = 10 Ω
- L = 10 mH = 0.01 H
- C = 10 μF = 10×10⁻⁶ F
- Vs = 10 V

### Parte a) Frecuencia de resonancia

$$f_0 = \frac{1}{2\pi\sqrt{LC}}$$

$$f_0 = \frac{1}{2\pi\sqrt{(0.01)(10 \times 10^{-6})}}$$

$$f_0 = \frac{1}{2\pi\sqrt{10^{-7}}} = \frac{1}{2\pi \times 3.162 \times 10^{-4}}$$

$$f_0 = \frac{1}{1.987 \times 10^{-3}} = 503.3\text{ Hz}$$

$$\boxed{f_0 = 503.3\text{ Hz}}$$

**Frecuencia angular de resonancia:**
$$\omega_0 = 2\pi f_0 = 3162\text{ rad/s}$$

**Verificación:** 
$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{10^{-7}}} = 3162\text{ rad/s ✓}$$

### Parte b) Factor de calidad Q

Para circuito RLC serie:
$$Q = \frac{\omega_0 L}{R} = \frac{X_{L0}}{R}$$

$$Q = \frac{3162 \times 0.01}{10} = \frac{31.62}{10}$$

$$\boxed{Q = 3.162}$$

**Fórmula alternativa:**
$$Q = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{1}{10}\sqrt{\frac{0.01}{10^{-5}}} = \frac{1}{10}\sqrt{1000} = \frac{31.62}{10} = 3.162\text{ ✓}$$

**Interpretación:** Q = 3.162 indica una selectividad moderada. El voltaje en L y C será 3.162 veces mayor que el voltaje de entrada en resonancia.

### Parte c) Ancho de banda

$$BW = \frac{f_0}{Q} = \frac{503.3}{3.162}$$

$$\boxed{BW = 159.2\text{ Hz}}$$

**Fórmula alternativa:**
$$BW = \frac{R}{2\pi L} = \frac{10}{2\pi \times 0.01} = \frac{10}{0.0628} = 159.2\text{ Hz ✓}$$

### Parte d) Frecuencias de corte

Las frecuencias de mitad de potencia (donde |Z| = √2 × R):

$$f_1 = f_0\sqrt{1 + \frac{1}{4Q^2}} - \frac{f_0}{2Q}$$
$$f_2 = f_0\sqrt{1 + \frac{1}{4Q^2}} + \frac{f_0}{2Q}$$

O usando la aproximación para Q > 1:
$$f_1 \approx f_0 - \frac{BW}{2} = 503.3 - \frac{159.2}{2} = 503.3 - 79.6 = 423.7\text{ Hz}$$

$$f_2 \approx f_0 + \frac{BW}{2} = 503.3 + 79.6 = 582.9\text{ Hz}$$

**Cálculo exacto:**
$$f_1 = -\frac{R}{4\pi L} + \sqrt{\left(\frac{R}{4\pi L}\right)^2 + f_0^2}$$
$$f_1 = -79.6 + \sqrt{79.6^2 + 503.3^2} = -79.6 + 509.6 = 430\text{ Hz}$$

$$f_2 = \frac{R}{4\pi L} + \sqrt{\left(\frac{R}{4\pi L}\right)^2 + f_0^2}$$
$$f_2 = 79.6 + 509.6 = 589.2\text{ Hz}$$

$$\boxed{f_1 = 430\text{ Hz}, \quad f_2 = 589\text{ Hz}}$$

**Verificación:** BW = f₂ - f₁ = 589 - 430 = 159 Hz ✓

### Parte e) Impedancia y corriente en resonancia

**En resonancia (f = f₀):**
$$X_L = X_C \quad \Rightarrow \quad Z = R + j(X_L - X_C) = R + j0 = R$$

$$\boxed{Z_{f_0} = R = 10\text{ Ω}}$$

La impedancia es puramente resistiva (mínima).

**Corriente en resonancia:**
$$I_0 = \frac{V_s}{Z} = \frac{V_s}{R} = \frac{10}{10} = 1\text{ A}$$

$$\boxed{I_0 = 1\angle 0°\text{ A}}$$

Esta es la corriente **máxima** posible en el circuito.

### Voltajes en los elementos en resonancia

$$V_R = I_0 \times R = 1 \times 10 = 10\text{ V}$$

$$V_L = I_0 \times X_L = 1 \times 31.62 = 31.62\text{ V}$$

$$V_C = I_0 \times X_C = 1 \times 31.62 = 31.62\text{ V}$$

**Verificación LVK:**
$$V_s = V_R + V_L + V_C = 10 + j31.62 - j31.62 = 10\text{ V ✓}$$

Los voltajes en L y C son iguales en magnitud pero opuestos en fase, se cancelan.

**Amplificación de voltaje:**
$$\frac{V_L}{V_s} = \frac{V_C}{V_s} = Q = 3.162$$

## Curva de Respuesta en Frecuencia

```
|I| (A)
    │
  1 ├──────────●──────────── I₀ = Vs/R (máximo)
    │         ╱│╲
0.707├───────╱─┼─╲───────── I₁,₂ = I₀/√2
    │       ╱  │  ╲
    │      ╱   │   ╲
    │     ╱    │    ╲
    │    ╱     │     ╲____
    │___╱      │
    └───┴──────┴──────┴───► f (Hz)
       100   503.3   1000
             f₀
         ├───BW = 159 Hz───┤
         f₁=430       f₂=589
```

## Tabla de Resultados vs Frecuencia

| f (Hz) | XL (Ω) | XC (Ω) | |Z| (Ω) | I (A) | θ |
|--------|--------|--------|-------|------|-----|
| 200 | 12.6 | 79.6 | 68.3 | 0.146 | -80.6° |
| 430 | 27.0 | 37.0 | 14.1 | 0.707 | -45° |
| 503.3 | 31.6 | 31.6 | 10.0 | 1.0 | 0° |
| 589 | 37.0 | 27.0 | 14.1 | 0.707 | +45° |
| 1000 | 62.8 | 15.9 | 48.4 | 0.207 | +78° |

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| a) f₀ | **503.3 Hz** |
| a) ω₀ | **3162 rad/s** |
| b) Q | **3.162** |
| c) BW | **159.2 Hz** |
| d) f₁ | **430 Hz** |
| d) f₂ | **589 Hz** |
| e) Z(f₀) | **10 Ω** |
| e) I(f₀) | **1 A** |
| VL = VC | **31.62 V** |

## Simulación SPICE - Resultados Esperados
```
f = 430 Hz:  I = 0.707A, θ = -45°
f = 503 Hz:  I = 1.0A,   θ = 0° (resonancia)
f = 589 Hz:  I = 0.707A, θ = +45°
```

## Conceptos Aplicados
- Resonancia serie: XL = XC, Z = R (mínimo)
- Factor de calidad Q = ω₀L/R = 1/(ω₀CR)
- Ancho de banda BW = f₀/Q = R/(2πL)
- Frecuencias de corte a -3dB
- Amplificación de voltaje Q en L y C
```
