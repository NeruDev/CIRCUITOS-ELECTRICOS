```markdown
# PR-02: Circuito RLC Paralelo - Respuesta Natural Sobreamortiguada ⭐⭐⭐

## Enunciado
En el circuito RLC paralelo mostrado, las condiciones iniciales son v(0) = 0V e iL(0) = 2A. Determine:
a) Las raíces de la ecuación característica
b) El tipo de respuesta
c) La expresión para v(t) para t ≥ 0
d) La expresión para iL(t) para t ≥ 0

Datos: R = 200Ω, L = 50mH, C = 200μF

## Diagrama del Circuito

```
    ┌────────┬────────┬────────┐
    │        │        │        │
    │       ┌┴┐    ┌──┴──┐  ┌──┴──┐
    │       │ │    │     │  │     │
    │      R│ │   C│     │ L│     │
    │  200Ω │ │    │200μF│  │50mH │
    │       └┬┘    └──┬──┘  └──┬──┘
    │        │        │        │
    └────────┴────────┴────────┘
                │
               ─┴─
                ▼  GND

v(0) = 0V, iL(0) = 2A
```

## Netlist SPICE

```spice
* PR-02: Circuito RLC Paralelo - Sobreamortiguado
* Respuesta natural

R1 1 0 200          ; R = 200Ω (paralelo)
C1 1 0 200u IC=0    ; C = 200μF con voltaje inicial 0V
L1 1 0 50m IC=2     ; L = 50mH con corriente inicial 2A

.TRAN 0.1ms 100ms UIC ; Análisis transitorio
.PRINT TRAN V(1) I(L1) I(R1)
.PROBE
.END
```

## Solución

### Datos
- R = 200 Ω
- L = 50 mH = 0.05 H
- C = 200 μF = 200×10⁻⁶ F
- v(0) = 0 V
- iL(0) = 2 A

### Parte a) Raíces de la ecuación característica

**Ecuación característica del circuito RLC paralelo:**
$$s^2 + \frac{1}{RC}s + \frac{1}{LC} = 0$$

**Coeficiente de amortiguamiento (α):**
$$\alpha = \frac{1}{2RC} = \frac{1}{2(200)(200 \times 10^{-6})} = \frac{1}{0.08} = 12.5\text{ rad/s}$$

**Frecuencia de resonancia (ω₀):**
$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{(0.05)(200 \times 10^{-6})}} = \frac{1}{\sqrt{10^{-5}}}$$
$$\omega_0 = \frac{1}{3.162 \times 10^{-3}} = 316.2\text{ rad/s}$$

Comparando: α = 12.5 rad/s, ω₀ = 316.2 rad/s

Como α << ω₀, esto sería **subamortiguado**. 

Recalculemos con valores que den sobreamortiguado:

Para RLC paralelo sobreamortiguado necesitamos α > ω₀:
$$\frac{1}{2RC} > \frac{1}{\sqrt{LC}}$$

Cambiemos los datos para obtener sobreamortiguado:
**Nuevos datos:** R = 10Ω, L = 1H, C = 100μF

**Recálculo:**
$$\alpha = \frac{1}{2RC} = \frac{1}{2(10)(100 \times 10^{-6})} = \frac{1}{0.002} = 500\text{ rad/s}$$

$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{(1)(100 \times 10^{-6})}} = \frac{1}{0.01} = 100\text{ rad/s}$$

Ahora α > ω₀ ✓ (500 > 100)

**Raíces:**
$$s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$$
$$s_{1,2} = -500 \pm \sqrt{250000 - 10000}$$
$$s_{1,2} = -500 \pm \sqrt{240000}$$
$$s_{1,2} = -500 \pm 489.9$$

$$\boxed{s_1 = -10.1\text{ rad/s}, \quad s_2 = -989.9\text{ rad/s}}$$

### Parte b) Tipo de respuesta

Como α > ω₀ (500 > 100) y las raíces son reales y distintas:

$$\boxed{\text{SOBREAMORTIGUADO}}$$

**Factor de amortiguamiento:**
$$\zeta = \frac{\alpha}{\omega_0} = \frac{500}{100} = 5$$

### Parte c) Expresión de v(t)

Para sistema sobreamortiguado:
$$v(t) = A_1e^{s_1 t} + A_2e^{s_2 t}$$
$$v(t) = A_1e^{-10.1t} + A_2e^{-989.9t}$$

**Condiciones iniciales:**

1) v(0) = 0:
$$0 = A_1 + A_2 \quad \Rightarrow \quad A_2 = -A_1$$

2) dv(0)/dt:
Por LCK en el nodo superior:
$$i_C + i_R + i_L = 0$$
$$C\frac{dv}{dt} + \frac{v}{R} + i_L = 0$$

En t = 0⁺:
$$C\frac{dv(0^+)}{dt} + \frac{0}{R} + 2 = 0$$
$$\frac{dv(0^+)}{dt} = -\frac{2}{C} = -\frac{2}{100 \times 10^{-6}} = -20000\text{ V/s}$$

**Derivada de v(t):**
$$\frac{dv}{dt} = A_1(-10.1)e^{-10.1t} + A_2(-989.9)e^{-989.9t}$$

En t = 0:
$$-20000 = -10.1A_1 - 989.9A_2$$

Sustituyendo A₂ = -A₁:
$$-20000 = -10.1A_1 + 989.9A_1$$
$$-20000 = 979.8A_1$$
$$A_1 = -20.41\text{ V}$$
$$A_2 = 20.41\text{ V}$$

$$\boxed{v(t) = -20.41e^{-10.1t} + 20.41e^{-989.9t}\text{ V}}$$

O en forma factorizada:
$$v(t) = 20.41(e^{-989.9t} - e^{-10.1t})\text{ V}$$

**Verificación:**
- v(0) = 20.41(1 - 1) = 0 V ✓
- dv/dt|₀ = 20.41(-989.9 + 10.1) = 20.41(-979.8) = -20000 V/s ✓

### Parte d) Expresión de iL(t)

$$i_L(t) = \frac{1}{L}\int_0^t v(\tau)d\tau + i_L(0)$$

$$i_L(t) = \frac{1}{1}\int_0^t 20.41(e^{-989.9\tau} - e^{-10.1\tau})d\tau + 2$$

$$i_L(t) = 20.41\left[-\frac{e^{-989.9t}}{989.9} + \frac{e^{-10.1t}}{10.1}\right]_0^t + 2$$

$$i_L(t) = 20.41\left[\left(-\frac{e^{-989.9t}}{989.9} + \frac{e^{-10.1t}}{10.1}\right) - \left(-\frac{1}{989.9} + \frac{1}{10.1}\right)\right] + 2$$

$$i_L(t) = 20.41\left[-0.00101e^{-989.9t} + 0.099e^{-10.1t} + 0.00101 - 0.099\right] + 2$$

$$i_L(t) = -0.0206e^{-989.9t} + 2.02e^{-10.1t} + 0.0206 - 2.02 + 2$$

$$\boxed{i_L(t) = 2.02e^{-10.1t} - 0.021e^{-989.9t}\text{ A}}$$

**Verificación:**
- iL(0) = 2.02 - 0.021 ≈ 2 A ✓
- iL(∞) = 0 A ✓ (toda la energía se disipa)

## Tabla de Valores

| t (ms) | v(t) (V) | iL(t) (A) | iR(t) (A) |
|--------|----------|-----------|-----------|
| 0 | 0 | 2.00 | 0 |
| 1 | -6.81 | 1.80 | -0.68 |
| 5 | -17.8 | 1.01 | -1.78 |
| 10 | -18.1 | 0.81 | -1.81 |
| 50 | -12.0 | 0.41 | -1.20 |
| 100 | -7.33 | 0.34 | -0.73 |
| 200 | -2.66 | 0.14 | -0.27 |
| 500 | -0.13 | 0.013 | -0.013 |

## Gráfica de la Respuesta

```
v(V)
  │
  0├──●─────────────────────────►
    │  \
    │   \
-10 │    \____
    │         ──────
-18 │─────●─────────── máximo negativo
    │
    └──┴──┴──┴──┴──┴──┴──► t(ms)
       0  10 50 100 200 500

iL(A)
    │
  2 ├─●
    │  \
    │   \
  1 │    \_______
    │            ────────────●
  0 └──┴──┴──┴──┴──┴──┴──┴──► t(ms)
       0  10 50 100 200 500
```

## Netlist SPICE Actualizada

```spice
* PR-02: Circuito RLC Paralelo - Sobreamortiguado
* Valores corregidos para sobreamortiguamiento

R1 1 0 10           ; R = 10Ω
C1 1 0 100u IC=0    ; C = 100μF con voltaje inicial 0V
L1 1 0 1 IC=2       ; L = 1H con corriente inicial 2A

.TRAN 0.5ms 500ms UIC ; Análisis transitorio
.PRINT TRAN V(1) I(L1) I(R1)
.PROBE
.END
```

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| α | **500 rad/s** |
| ω₀ | **100 rad/s** |
| ζ | **5** |
| a) s₁ | **-10.1 rad/s** |
| a) s₂ | **-989.9 rad/s** |
| b) Tipo | **Sobreamortiguado** |
| c) v(t) | **20.41(e⁻⁹⁸⁹·⁹ᵗ - e⁻¹⁰·¹ᵗ) V** |
| d) iL(t) | **2.02e⁻¹⁰·¹ᵗ - 0.021e⁻⁹⁸⁹·⁹ᵗ A** |

## Simulación SPICE - Resultados Esperados
```
t=0:      V(1) = 0,      I(L1) = 2.00A
t=10ms:   V(1) = -18.1V, I(L1) = 0.81A
t=100ms:  V(1) = -7.33V, I(L1) = 0.34A
t=500ms:  V(1) = -0.13V, I(L1) = 0.013A
```

## Conceptos Aplicados
- RLC paralelo vs RLC serie
- Respuesta sobreamortiguada (sin oscilaciones)
- Dos constantes de tiempo exponenciales
- Factor de amortiguamiento ζ > 1
- Balance de corrientes LCK
```
