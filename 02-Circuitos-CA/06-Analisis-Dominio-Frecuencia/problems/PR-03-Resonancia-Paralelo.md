```markdown
# PR-03: Resonancia Paralelo RLC ⭐⭐⭐

## Enunciado
Un circuito RLC en paralelo tiene R = 100 kΩ, L = 10 mH y C = 10 nF. Una fuente de corriente alterna I = 10 mA conectada en paralelo. Determine:
a) La frecuencia de resonancia f₀
b) El factor de calidad Q
c) El ancho de banda BW y las frecuencias de corte f₁, f₂
d) La impedancia y voltaje en resonancia
e) La corriente en cada elemento a la frecuencia de resonancia

## Diagrama del Circuito

```
       ┌─────┬─────┬─────┐
       │     │     │     │
       │   ┌─┴─┐ ┌─┴─┐ ┌─┴─┐
 Is ○──┤   │ R │ │ L │ │ C │
10mA∠0°│   │100k│ │10m│ │10n│
       │   └─┬─┘ └─┬─┘ └─┬─┘
       │     │     │     │
       └─────┴─────┴─────┘
             │
            ═╧═ GND

Admitancia: Y = G + j(ωC - 1/ωL)
En resonancia: ωC = 1/ωL → Y = G (mínima, real)
```

## Netlist SPICE

```spice
* PR-03: Resonancia Paralelo RLC
* Análisis de frecuencia

I1 0 1 AC 10m 0       ; Fuente de corriente 10mA
R1 1 0 100k           ; R = 100kΩ en paralelo
L1 1 0 10m            ; L = 10mH en paralelo
C1 1 0 10n            ; C = 10nF en paralelo

* Barrido de frecuencia
.AC DEC 50 1k 100k    ; 50 pts/década, 1kHz a 100kHz
.PRINT AC VM(1) VP(1) ; Magnitud y fase del voltaje
.PROBE
.END
```

## Solución

### Datos
- R = 100 kΩ = 100000 Ω
- L = 10 mH = 0.01 H
- C = 10 nF = 10×10⁻⁹ F
- Is = 10 mA ∠0°

### Parte a) Frecuencia de resonancia

En el circuito paralelo, la resonancia ocurre cuando la parte imaginaria de la admitancia es cero:

$$\omega_0 C = \frac{1}{\omega_0 L}$$

$$\omega_0 = \frac{1}{\sqrt{LC}}$$

$$\omega_0 = \frac{1}{\sqrt{0.01 \times 10 \times 10^{-9}}} = \frac{1}{\sqrt{10^{-10}}}$$

$$\omega_0 = \frac{1}{10^{-5}} = 100000\text{ rad/s}$$

$$f_0 = \frac{\omega_0}{2\pi} = \frac{100000}{2\pi}$$

$$\boxed{f_0 = 15915.5\text{ Hz} \approx 15.92\text{ kHz}}$$

### Parte b) Factor de calidad Q

Para el circuito paralelo, Q se define de manera diferente al serie:

$$Q = R\sqrt{\frac{C}{L}} = \frac{R}{X_{L0}} = \omega_0 RC$$

Calculando:
$$Q = 100000 \times \sqrt{\frac{10 \times 10^{-9}}{0.01}}$$

$$Q = 100000 \times \sqrt{10^{-6}} = 100000 \times 10^{-3}$$

$$\boxed{Q = 100}$$

**Verificación alternativa:**
$$Q = \omega_0 RC = 100000 \times 100000 \times 10 \times 10^{-9} = 100$$ ✓

$$Q = \frac{R}{X_{L0}} = \frac{100000}{\omega_0 L} = \frac{100000}{100000 \times 0.01} = \frac{100000}{1000} = 100$$ ✓

### Parte c) Ancho de banda y frecuencias de corte

**Ancho de banda:**
$$BW = \frac{f_0}{Q} = \frac{15915.5}{100}$$

$$\boxed{BW = 159.15\text{ Hz}}$$

**Frecuencias de media potencia:**
$$f_1 = f_0\sqrt{1 + \frac{1}{4Q^2}} - \frac{BW}{2}$$

$$f_2 = f_0\sqrt{1 + \frac{1}{4Q^2}} + \frac{BW}{2}$$

Para Q alto (Q >> 1), aproximación:
$$f_1 \approx f_0 - \frac{BW}{2} = 15915.5 - 79.6 = 15836\text{ Hz}$$
$$f_2 \approx f_0 + \frac{BW}{2} = 15915.5 + 79.6 = 15995\text{ Hz}$$

**Valores exactos:**
$$f_1 = -\frac{1}{4\pi RC} + \sqrt{\left(\frac{1}{4\pi RC}\right)^2 + f_0^2} = 15836.0\text{ Hz}$$
$$f_2 = +\frac{1}{4\pi RC} + \sqrt{\left(\frac{1}{4\pi RC}\right)^2 + f_0^2} = 15995.1\text{ Hz}$$

$$\boxed{f_1 = 15836\text{ Hz}, \quad f_2 = 15995\text{ Hz}}$$

### Parte d) Impedancia y voltaje en resonancia

**Impedancia en resonancia:**

En resonancia, las admitancias del inductor y capacitor se cancelan:
$$Y_{L0} = \frac{1}{j\omega_0 L} = \frac{1}{j \times 1000} = -j0.001\text{ S}$$
$$Y_{C0} = j\omega_0 C = j \times 100000 \times 10^{-8} = j0.001\text{ S}$$

$$Y_{total} = G + j(Y_C - |Y_L|) = \frac{1}{R} + j(0.001 - 0.001) = \frac{1}{100000}$$

$$Z_0 = \frac{1}{Y_{total}} = R = 100\text{ k}\Omega$$

$$\boxed{Z_0 = 100\text{ k}\Omega \text{ (puramente resistiva)}}$$

**Voltaje en resonancia:**
$$V_0 = I_s \times Z_0 = 10 \times 10^{-3} \times 100000$$

$$\boxed{V_0 = 1000\text{ V} = 1\text{ kV}}$$

### Parte e) Corrientes en cada elemento a f₀

**Corriente en R:**
$$I_R = \frac{V_0}{R} = \frac{1000}{100000} = 10\text{ mA} \angle 0°$$

**Corriente en L:**
$$X_{L0} = \omega_0 L = 100000 \times 0.01 = 1000\text{ Ω}$$
$$I_L = \frac{V_0}{jX_{L0}} = \frac{1000}{j1000} = -j1\text{ A} = 1\text{ A} \angle -90°$$

**Corriente en C:**
$$X_{C0} = \frac{1}{\omega_0 C} = \frac{1}{100000 \times 10^{-8}} = 1000\text{ Ω}$$
$$I_C = \frac{V_0}{-jX_{C0}} = \frac{1000}{-j1000} = j1\text{ A} = 1\text{ A} \angle +90°$$

**Verificación (LKC):**
$$I_s = I_R + I_L + I_C = 10\text{mA} + (-j1\text{A}) + (j1\text{A}) = 10\text{ mA}$$ ✓

**Amplificación de corriente Q:**
$$\frac{I_L}{I_s} = \frac{I_C}{I_s} = \frac{1\text{ A}}{10\text{ mA}} = 100 = Q$$ ✓

$$\boxed{I_R = 10\text{ mA}\angle 0°, \quad I_L = 1\text{ A}\angle -90°, \quad I_C = 1\text{ A}\angle +90°}$$

## Comparación: Resonancia Serie vs Paralelo

| Característica | Serie | Paralelo |
|---------------|-------|----------|
| En resonancia | Z = R (mínima) | Z = R (máxima) |
| Q | Q = XL/R = 1/ωRC | Q = R/XL = ωRC |
| Amplificación | VL = VC = Q×Vs | IL = IC = Q×Is |
| Uso típico | Filtro pasa-banda | Rechazo de banda |

## Tabla de Resultados

| Parámetro | Valor |
|-----------|-------|
| f₀ | **15915.5 Hz** |
| ω₀ | **100000 rad/s** |
| Q | **100** |
| BW | **159.15 Hz** |
| f₁ | **15836 Hz** |
| f₂ | **15995 Hz** |
| Z₀ | **100 kΩ ∠0°** |
| V₀ | **1000 V ∠0°** |
| IR | **10 mA ∠0°** |
| IL | **1 A ∠-90°** |
| IC | **1 A ∠+90°** |

## Simulación SPICE - Resultados Esperados
```
f = 15915.5 Hz (resonancia):
  VM(1) = 1000 V
  VP(1) = 0°
  Z = 100 kΩ (máxima)

f = 15836 Hz (f1) y f = 15995 Hz (f2):
  VM(1) = 707 V (-3dB)
```

## Respuesta en Frecuencia

```
|Z| (kΩ)
    │        ╱╲
100 ├───────●──────── Z máxima en f₀
    │      ╱  ╲
 71 ├─────●────●───── -3dB (Z = R/√2)
    │    ╱      ╲
    │   ╱        ╲
    │  ╱          ╲
    └─┴────┴──────┴─► f (kHz)
       f₁  f₀   f₂
     15.84 15.92 16.0
```

## Conceptos Aplicados
- Resonancia en circuito paralelo
- Admitancia compleja Y = G + jB
- Factor de calidad en circuito paralelo
- Amplificación de corriente Q:1
- Impedancia máxima en resonancia
- Ancho de banda y selectividad
```
