# PR-01: Circuito RLC Serie - Respuesta Natural Subamortiguada ⭐⭐⭐

## Enunciado
El interruptor del [circuito](../../../glossary.md#circuito) RLC serie ha estado cerrado por largo tiempo. En t = 0 se abre el interruptor. Determine:
a) Las raíces de la ecuación característica
b) El tipo de amortiguamiento
c) La expresión para v(t) para t ≥ 0
d) El tiempo del primer máximo de v(t)

Datos: R = 200Ω, L = 0.5H, C = 10μF, iL(0⁻) = 50mA, vC(0⁻) = 10V

## Diagrama del Circuito

```
        t=0
    ┌────/────┐
    │   (SW)  │
    │         │
   ┌┴┐        │
   │R│ 200Ω   │
   └┬┘        │
    │      ┌──┴──┐
  ┌─┴─┐    │  C  │
  │ L │    │10μF │
  │0.5H    │     │
  └─┬─┘    └──┬──┘
    │         │
    └────┬────┘
         │
        ─┴─
         ▼  GND
         
iL(0⁻) = 50mA, vC(0⁻) = 10V
```

## Netlist SPICE

```spice
* PR-01: Circuito RLC Serie - Subamortiguado
* Respuesta natural

R1 1 2 200          ; R = 200Ω
L1 2 3 0.5 IC=50m   ; L = 0.5H con corriente inicial 50mA
C1 3 0 10u IC=10    ; C = 10μF con voltaje inicial 10V

.TRAN 0.1ms 50ms UIC ; Análisis transitorio
.PRINT TRAN V(3) I(L1)
.PROBE
.END
```

## Solución

### Datos
- R = 200 Ω
- L = 0.5 H
- C = 10 μF = 10×10⁻⁶ F
- iL(0⁻) = iL(0⁺) = 50 mA = 0.05 A
- vC(0⁻) = vC(0⁺) = 10 V

### Parte a) Raíces de la ecuación característica

**Ecuación característica del circuito RLC serie:**
$$s^2 + \frac{R}{L}s + \frac{1}{LC} = 0$$

**Coeficiente de amortiguamiento (α):**
$$\alpha = \frac{R}{2L} = \frac{200}{2(0.5)} = 200\text{ rad/s}$$

**[Frecuencia](../../../glossary.md#frecuencia) de [resonancia](../../../glossary.md#resonancia) (ω₀):**
$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{0.5 \times 10 \times 10^{-6}}} = \frac{1}{\sqrt{5 \times 10^{-6}}}$$
$$\omega_0 = \frac{1}{2.236 \times 10^{-3}} = 447.2\text{ rad/s}$$

**Raíces:**
$$s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$$

$$\alpha^2 = 40000, \quad \omega_0^2 = 200000$$

Como α² < ω₀², tenemos raíces complejas conjugadas:

$$s_{1,2} = -\alpha \pm j\sqrt{\omega_0^2 - \alpha^2}$$

**Frecuencia amortiguada (ωd):**
$$\omega_d = \sqrt{\omega_0^2 - \alpha^2} = \sqrt{200000 - 40000} = \sqrt{160000} = 400\text{ rad/s}$$

$$\boxed{s_{1,2} = -200 \pm j400\text{ rad/s}}$$

### Parte b) Tipo de amortiguamiento

Como α < ω₀ (200 < 447.2), el sistema es:

$$\boxed{\text{SUBAMORTIGUADO}}$$

**Factor de amortiguamiento:**
$$\zeta = \frac{\alpha}{\omega_0} = \frac{200}{447.2} = 0.447$$

### Parte c) Expresión de v(t)

Para un sistema subamortiguado, la respuesta natural es:
$$v(t) = e^{-\alpha t}(A_1\cos\omega_d t + A_2\sin\omega_d t)$$

**Condiciones iniciales:**

1) En t = 0⁺:
$$v(0^+) = v_C(0^+) = 10\text{ V}$$
$$10 = e^0(A_1\cos 0 + A_2\sin 0) = A_1$$
$$A_1 = 10\text{ V}$$

2) Derivada en t = 0⁺:
$$\frac{dv(0^+)}{dt} = \frac{i_C(0^+)}{C}$$

En t = 0⁺, por [LVK](../../../glossary.md#lvk): $v_R + v_L + v_C = 0$

La [corriente](../../../glossary.md#corriente) del [inductor](../../../glossary.md#inductancia) fluye por todo el circuito serie:
$$i_C(0^+) = i_L(0^+) = 50\text{ mA}$$

$$\frac{dv(0^+)}{dt} = \frac{0.05}{10 \times 10^{-6}} = 5000\text{ V/s}$$

**Derivada de v(t):**
$$\frac{dv}{dt} = e^{-\alpha t}[-\alpha(A_1\cos\omega_d t + A_2\sin\omega_d t) + (-A_1\omega_d\sin\omega_d t + A_2\omega_d\cos\omega_d t)]$$

En t = 0:
$$\frac{dv(0)}{dt} = -\alpha A_1 + \omega_d A_2 = 5000$$
$$-200(10) + 400(A_2) = 5000$$
$$400A_2 = 7000$$
$$A_2 = 17.5\text{ V}$$

**Respuesta:**
$$\boxed{v(t) = e^{-200t}(10\cos 400t + 17.5\sin 400t)\text{ V}}$$

**Forma alternativa (magnitud y fase):**
$$B = \sqrt{A_1^2 + A_2^2} = \sqrt{100 + 306.25} = \sqrt{406.25} = 20.16\text{ V}$$
$$\phi = \arctan\left(\frac{A_1}{A_2}\right) = \arctan\left(\frac{10}{17.5}\right) = 29.74° = 0.519\text{ rad}$$

$$v(t) = 20.16e^{-200t}\sin(400t + 29.74°)\text{ V}$$

### Parte d) Tiempo del primer máximo

Para el máximo, dv/dt = 0:
$$\frac{dv}{dt} = e^{-\alpha t}[(-\alpha A_1 + \omega_d A_2)\cos\omega_d t + (-\alpha A_2 - \omega_d A_1)\sin\omega_d t] = 0$$

Sustituyendo valores:
$$[(-200)(10) + (400)(17.5)]\cos 400t + [(-200)(17.5) - (400)(10)]\sin 400t = 0$$
$$5000\cos 400t - 7500\sin 400t = 0$$
$$\tan 400t = \frac{5000}{7500} = 0.667$$
$$400t = \arctan(0.667) = 33.69° = 0.588\text{ rad}$$
$$t = \frac{0.588}{400} = 1.47\text{ ms}$$

$$\boxed{t_{max} = 1.47\text{ ms}}$$

**Valor máximo:**
$$v_{max} = e^{-200(0.00147)}(10\cos(0.588) + 17.5\sin(0.588))$$
$$v_{max} = e^{-0.294}(10(0.832) + 17.5(0.555))$$
$$v_{max} = 0.745(8.32 + 9.71) = 13.44\text{ V}$$

## Tabla de Valores

| t (ms) | v(t) (V) | i(t) (mA) | Observación |
|--------|----------|-----------|-------------|
| 0 | 10.0 | 50.0 | Inicio |
| 1.47 | 13.44 | 33.7 | Primer máximo |
| 5 | 3.82 | -2.8 | Cruzando |
| 7.85 | -2.08 | -24.6 | Primer mínimo |
| 10 | 1.36 | -16.8 | |
| 15 | 0.68 | -4.5 | |
| 25 | -0.01 | 0.3 | Amortiguándose |

## Gráfica de la Respuesta

```
v(V)
  │
13.4├────●──────── Primer máximo (t=1.47ms)
    │   /\
 10 ├──●  \
    │ /    \
    │/      \     /\
  0 ├────────\───/──\─────── t(ms)
    │         \ /    \___
 -2 │          ●      mínimo
    │
    └──┴──┴──┴──┴──┴──┴──┴──►
       0  2  5  8  10 15 20
```

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| α | **200 rad/s** |
| ω₀ | **447.2 rad/s** |
| ωd | **400 rad/s** |
| a) Raíces | **s₁,₂ = -200 ± j400 rad/s** |
| b) Tipo | **Subamortiguado (ζ = 0.447)** |
| c) v(t) | **e⁻²⁰⁰ᵗ(10cos400t + 17.5sin400t) V** |
| d) t primer máximo | **1.47 ms** |
| v máximo | **13.44 V** |

## Simulación SPICE - Resultados Esperados
```
t=0:       V(3) = 10.00,  I(L1) = 50mA
t=1.47ms:  V(3) = 13.44,  I(L1) = 33.7mA  (máximo)
t=5ms:     V(3) = 3.82,   I(L1) = -2.8mA
t=7.85ms:  V(3) = -2.08,  I(L1) = -24.6mA (mínimo)
t=20ms:    V(3) ≈ 0.5,    I(L1) ≈ 1mA
```

## Conceptos Aplicados
- Ecuación característica de segundo orden
- Respuesta subamortiguada con oscilaciones
- Coeficiente de amortiguamiento α
- Frecuencia natural ω₀ y amortiguada ωd
- Factor de amortiguamiento ζ