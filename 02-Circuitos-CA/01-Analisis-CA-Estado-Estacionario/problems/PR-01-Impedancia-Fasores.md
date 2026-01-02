# PR-01: Análisis con Fasores - Impedancia y Admitancia ⭐⭐

## Enunciado
Para el circuito mostrado con una fuente de voltaje v(t) = 170cos(377t)V, determine:
a) La impedancia total vista desde la fuente
b) La corriente total i(t) del circuito
c) Los voltajes vR(t), vL(t) y vC(t)
d) Verifique que se cumple la LVK

Datos: R = 50Ω, L = 0.2H, C = 50μF, ω = 377 rad/s (60 Hz)

## Diagrama del Circuito

```
    ┌────────┬────/\/\/────┬────────┐
    │        │    R=50Ω    │        │
  + │        │           + │        │
v(t)│      ┌─┴─┐       vR │        │
    │      │ L │         - │        │
  - │      │0.2H           │        │
    │      └─┬─┘           │        │
    │      + │           ┌─┴─┐      │
    │     vL │           │ C │      │
    │      - │           │50μF     │
    │        │           └─┬─┘      │
    └────────┴─────────────┴────────┘

v(t) = 170cos(377t) V
```

## Netlist SPICE

```spice
* PR-01: Análisis con Fasores - Circuito RLC Serie
* Análisis CA estado estacionario

V1 1 0 AC 170 0     ; Fuente senoidal 170V, fase 0°
R1 1 2 50           ; R = 50Ω
L1 2 3 0.2          ; L = 0.2H
C1 3 0 50u          ; C = 50μF

.AC LIN 1 60 60     ; Análisis CA a 60 Hz
.PRINT AC VM(1) VP(1) IM(R1) IP(R1) VM(2) VP(2) VM(3) VP(3)
.END

* Alternativa: Análisis transitorio
.TRAN 0.1ms 100ms
.PRINT TRAN V(1) V(2) V(3) I(R1)
```

## Solución

### Datos
- Vm = 170 V (amplitud)
- ω = 377 rad/s
- f = 60 Hz
- R = 50 Ω
- L = 0.2 H
- C = 50 μF

### Cálculo de impedancias individuales

**Resistencia:**
$$Z_R = R = 50\angle 0° \text{ Ω}$$

**Reactancia inductiva:**
$$X_L = \omega L = 377 \times 0.2 = 75.4\text{ Ω}$$
$$Z_L = jX_L = j75.4 = 75.4\angle 90° \text{ Ω}$$

**Reactancia capacitiva:**
$$X_C = \frac{1}{\omega C} = \frac{1}{377 \times 50 \times 10^{-6}} = 53.1\text{ Ω}$$
$$Z_C = -jX_C = -j53.1 = 53.1\angle -90° \text{ Ω}$$

### Parte a) Impedancia total

Circuito RLC serie:
$$Z_T = Z_R + Z_L + Z_C = 50 + j75.4 - j53.1$$
$$Z_T = 50 + j22.3\text{ Ω}$$

**Forma polar:**
$$|Z_T| = \sqrt{50^2 + 22.3^2} = \sqrt{2500 + 497} = \sqrt{2997} = 54.75\text{ Ω}$$
$$\theta_Z = \arctan\left(\frac{22.3}{50}\right) = 24.03°$$

$$\boxed{Z_T = 54.75\angle 24.03° \text{ Ω}}$$

**Naturaleza del circuito:** X_L > X_C → Circuito **inductivo** (corriente atrasada respecto al voltaje)

### Parte b) Corriente total i(t)

**Fasor de voltaje:**
$$\mathbf{V} = 170\angle 0° \text{ V}$$

**Fasor de corriente:**
$$\mathbf{I} = \frac{\mathbf{V}}{Z_T} = \frac{170\angle 0°}{54.75\angle 24.03°}$$

$$\mathbf{I} = \frac{170}{54.75}\angle (0° - 24.03°) = 3.105\angle -24.03° \text{ A}$$

**En dominio del tiempo:**
$$\boxed{i(t) = 3.105\cos(377t - 24.03°)\text{ A}}$$

La corriente **atrasa** 24.03° respecto al voltaje (circuito inductivo).

### Parte c) Voltajes en cada elemento

**Voltaje en la resistencia:**
$$\mathbf{V}_R = \mathbf{I} \times Z_R = 3.105\angle -24.03° \times 50\angle 0°$$
$$\mathbf{V}_R = 155.25\angle -24.03° \text{ V}$$

$$\boxed{v_R(t) = 155.25\cos(377t - 24.03°)\text{ V}}$$

**Voltaje en el inductor:**
$$\mathbf{V}_L = \mathbf{I} \times Z_L = 3.105\angle -24.03° \times 75.4\angle 90°$$
$$\mathbf{V}_L = 234.12\angle 65.97° \text{ V}$$

$$\boxed{v_L(t) = 234.12\cos(377t + 65.97°)\text{ V}}$$

**Voltaje en el capacitor:**
$$\mathbf{V}_C = \mathbf{I} \times Z_C = 3.105\angle -24.03° \times 53.1\angle -90°$$
$$\mathbf{V}_C = 164.88\angle -114.03° \text{ V}$$

$$\boxed{v_C(t) = 164.88\cos(377t - 114.03°)\text{ V}}$$

### Parte d) Verificación LVK

$$\mathbf{V} = \mathbf{V}_R + \mathbf{V}_L + \mathbf{V}_C$$

Convertimos a forma rectangular:
- $\mathbf{V}_R = 155.25\angle -24.03° = 141.7 - j63.2$ V
- $\mathbf{V}_L = 234.12\angle 65.97° = 95.2 + j213.9$ V
- $\mathbf{V}_C = 164.88\angle -114.03° = -67.0 - j150.6$ V

**Suma:**
$$\mathbf{V}_R + \mathbf{V}_L + \mathbf{V}_C = (141.7 + 95.2 - 67.0) + j(-63.2 + 213.9 - 150.6)$$
$$= 169.9 + j0.1 \approx 170\angle 0° \text{ V}$$

$$\boxed{\text{LVK verificada: } \sum V = 170\angle 0° \text{ V ✓}}$$

## Diagrama Fasorial

```
              Im
              │     VL
              │    ╱
              │   ╱ 234V
              │  ╱ θ=66°
              │ ╱
    ──────────┼────────────── Re
     VC ╲     │╱╲   VR
    -114°╲    │  ╲ -24°
          ╲   │   I
         165V │
              │V=170V (referencia)
```

## Tabla de Valores (forma rectangular y polar)

| Cantidad | Rectangular | Polar |
|----------|-------------|-------|
| ZT | 50 + j22.3 Ω | 54.75∠24.03° Ω |
| I | 2.84 - j1.27 A | 3.105∠-24.03° A |
| VR | 141.7 - j63.2 V | 155.25∠-24.03° V |
| VL | 95.2 + j213.9 V | 234.12∠65.97° V |
| VC | -67.0 - j150.6 V | 164.88∠-114.03° V |

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| XL | **75.4 Ω** |
| XC | **53.1 Ω** |
| a) ZT | **54.75∠24.03° Ω** |
| b) i(t) | **3.105cos(377t - 24.03°) A** |
| c) vR(t) | **155.25cos(377t - 24.03°) V** |
| c) vL(t) | **234.12cos(377t + 65.97°) V** |
| c) vC(t) | **164.88cos(377t - 114.03°) V** |
| d) LVK | **Verificada ✓** |

## Simulación SPICE - Resultados Esperados
```
Análisis AC (60 Hz):
VM(1) = 170V,     VP(1) = 0°
IM(R1) = 3.105A,  IP(R1) = -24.03°
VM(2) = 234.1V,   VP(2) = 65.97°   (VL)
VM(3) = 164.9V,   VP(3) = -114.03° (VC)
```

## Conceptos Aplicados
- Transformación al dominio de la frecuencia
- Impedancia compleja: Z = R + jX
- Reactancias: XL = ωL, XC = 1/ωC
- Ley de Ohm en fasores: V = IZ
- Circuito inductivo vs capacitivo
- Diagrama fasorial