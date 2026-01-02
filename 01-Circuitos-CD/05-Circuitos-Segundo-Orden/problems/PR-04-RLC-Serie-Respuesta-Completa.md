# PR-04: Circuito RLC Serie - Respuesta Completa con Fuente DC ⭐⭐⭐

## Enunciado
En el [circuito](../../../glossary.md#circuito) mostrado, el interruptor se cierra en t = 0. Las condiciones iniciales son vC(0) = 0V e iL(0) = 0A. Determine:
a) El tipo de amortiguamiento
b) La expresión para iL(t) para t ≥ 0
c) La expresión para vC(t) para t ≥ 0
d) El tiempo para que vC alcance el 95% del valor final

Datos: Vs = 50V, R = 100Ω, L = 0.2H, C = 50μF

## Diagrama del Circuito

```
        t=0
    ┌────/────┬────────────────┐
    │         │                │
  + │        ┌┴┐            ┌──┴──┐
(Vs)│        │R│ 100Ω       │  C  │
 50V│        └┬┘            │ 50μF│
  - │         │             └──┬──┘
    │      ┌──┴──┐             │
    │      │  L  │             │
    │      │0.2H │             │
    │      └──┬──┘             │
    │         │                │
    └─────────┴────────────────┘
    
vC(0) = 0V, iL(0) = 0A
```

## Netlist SPICE

```spice
* PR-04: Circuito RLC Serie con Fuente DC
* Respuesta completa

V1 1 0 DC 50V       ; Fuente de voltaje 50V
R1 1 2 100          ; R = 100Ω
L1 2 3 0.2 IC=0     ; L = 0.2H con corriente inicial 0A
C1 3 0 50u IC=0     ; C = 50μF con voltaje inicial 0V

.TRAN 0.5ms 50ms UIC ; Análisis transitorio
.PRINT TRAN V(3) I(L1) V(2,3)
.PROBE
.END
```

## Solución

### Datos
- Vs = 50 V
- R = 100 Ω
- L = 0.2 H
- C = 50 μF = 50×10⁻⁶ F
- vC(0) = 0 V
- iL(0) = 0 A

### Parte a) Tipo de amortiguamiento

**Coeficiente de amortiguamiento:**
$$\alpha = \frac{R}{2L} = \frac{100}{2(0.2)} = 250\text{ rad/s}$$

**Frecuencia de resonancia:**
$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{(0.2)(50 \times 10^{-6})}} = \frac{1}{\sqrt{10^{-5}}}$$
$$\omega_0 = \frac{1}{3.162 \times 10^{-3}} = 316.2\text{ rad/s}$$

**Comparación:** α = 250 rad/s, ω₀ = 316.2 rad/s

Como α < ω₀:
$$\boxed{\text{SUBAMORTIGUADO}}$$

**Factor de amortiguamiento:**
$$\zeta = \frac{\alpha}{\omega_0} = \frac{250}{316.2} = 0.791$$

**Frecuencia amortiguada:**
$$\omega_d = \sqrt{\omega_0^2 - \alpha^2} = \sqrt{100000 - 62500} = \sqrt{37500} = 193.6\text{ rad/s}$$

**Raíces:**
$$s_{1,2} = -250 \pm j193.6\text{ rad/s}$$

### Parte b) Expresión de iL(t)

**Respuesta completa = Respuesta natural + Respuesta forzada**

**Respuesta forzada (estado estable):**
En DC estable, L → cortocircuito, C → circuito abierto
$$i_L(\infty) = 0\text{ A}$$ (corriente en estado estable es cero porque C es abierto)

La respuesta natural subamortiguada:
$$i_L(t) = e^{-\alpha t}(A_1\cos\omega_d t + A_2\sin\omega_d t)$$

**Condiciones iniciales:**

1) iL(0) = 0:
$$0 = e^0(A_1 \cdot 1 + A_2 \cdot 0) = A_1$$
$$A_1 = 0$$

2) diL(0)/dt:
Por LVK: $V_s = v_R + v_L + v_C$

En t = 0⁺:
$$50 = R \cdot i_L(0^+) + L\frac{di_L(0^+)}{dt} + v_C(0^+)$$
$$50 = 100(0) + 0.2\frac{di_L(0^+)}{dt} + 0$$
$$\frac{di_L(0^+)}{dt} = \frac{50}{0.2} = 250\text{ A/s}$$

**Derivada de iL(t):**
$$\frac{di_L}{dt} = e^{-\alpha t}(-\omega_d A_1 \sin\omega_d t + \omega_d A_2 \cos\omega_d t - \alpha A_2 \sin\omega_d t)$$

En t = 0 (con A₁ = 0):
$$250 = \omega_d A_2 = 193.6 A_2$$
$$A_2 = \frac{250}{193.6} = 1.29\text{ A}$$

$$\boxed{i_L(t) = 1.29e^{-250t}\sin(193.6t)\text{ A}}$$

**Verificación:**
- iL(0) = 1.29(1)(0) = 0 A ✓
- diL/dt|₀ = 1.29(193.6) = 249.7 ≈ 250 A/s ✓

### Parte c) Expresión de vC(t)

**Respuesta forzada:**
$$v_C(\infty) = V_s = 50\text{ V}$$

**Respuesta completa:**
$$v_C(t) = v_C(\infty) + e^{-\alpha t}(B_1\cos\omega_d t + B_2\sin\omega_d t)$$
$$v_C(t) = 50 + e^{-250t}(B_1\cos 193.6t + B_2\sin 193.6t)$$

**Condiciones iniciales:**

1) vC(0) = 0:
$$0 = 50 + B_1$$
$$B_1 = -50\text{ V}$$

2) dvC(0)/dt = iC(0)/C = iL(0)/C = 0:
$$\frac{dv_C}{dt} = e^{-\alpha t}[-\omega_d B_1 \sin\omega_d t + \omega_d B_2 \cos\omega_d t] + (-\alpha)e^{-\alpha t}[B_1\cos\omega_d t + B_2\sin\omega_d t]$$

En t = 0:
$$0 = \omega_d B_2 - \alpha B_1 = 193.6 B_2 - 250(-50)$$
$$193.6 B_2 = -12500$$
$$B_2 = -64.6\text{ V}$$

$$\boxed{v_C(t) = 50 - e^{-250t}(50\cos 193.6t + 64.6\sin 193.6t)\text{ V}}$$

**Forma alternativa:**
$$B = \sqrt{B_1^2 + B_2^2} = \sqrt{2500 + 4173} = 81.7\text{ V}$$
$$\phi = \arctan\left(\frac{B_1}{B_2}\right) = \arctan\left(\frac{-50}{-64.6}\right) = 37.7° = 0.658\text{ rad}$$

Como ambos coeficientes son negativos, la fase está en el tercer cuadrante:
$$v_C(t) = 50 - 81.7e^{-250t}\sin(193.6t + 37.7°)\text{ V}$$

### Parte d) Tiempo para vC = 95% del valor final

El 95% de 50V = 47.5V

Necesitamos resolver:
$$47.5 = 50 - e^{-250t}(50\cos 193.6t + 64.6\sin 193.6t)$$
$$2.5 = e^{-250t}(50\cos 193.6t + 64.6\sin 193.6t)$$

Esta ecuación es trascendente. Por método numérico o de la envolvente exponencial:

La envolvente es $81.7e^{-250t}$. Aproximadamente cuando:
$$81.7e^{-250t} \approx 2.5$$
$$e^{-250t} = 0.0306$$
$$t = \frac{\ln(0.0306)}{-250} = \frac{3.49}{250} = 13.96\text{ ms}$$

Por inspección numérica más precisa (considerando oscilaciones):
$$\boxed{t_{95\%} \approx 16\text{ ms}}$$

En términos de τ = 1/α = 4 ms, esto es aproximadamente 4τ.

## Tabla de Valores

| t (ms) | iL(t) (mA) | vC(t) (V) | vL(t) (V) |
|--------|------------|-----------|-----------|
| 0 | 0 | 0 | 50.0 |
| 2 | 303 | 5.0 | 35.0 |
| 5 | 341 | 19.5 | 14.3 |
| 8 | 218 | 34.2 | -0.5 |
| 10 | 107 | 41.3 | -5.6 |
| 16 | -42 | 49.3 | -2.3 |
| 20 | -50 | 49.0 | 0.2 |
| 30 | 4 | 50.0 | 0.2 |

## Gráfica de las Respuestas

```
vC(V), iL×100(mA)
     │
 50  ├────────────●────────────── vC(∞)
     │         ●__/\____
 40  │        /      ──────●
     │       /
 30  │      / 
     │     /   ●────── iL(t)
 20  │    /   / \
     │   /   /   \_______
 10  │  /   /
     │ / ●/
  0  ├─●────────────────────────► t(ms)
     │ 0   5   10   16   20   30
```

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| α | **250 rad/s** |
| ω₀ | **316.2 rad/s** |
| ωd | **193.6 rad/s** |
| ζ | **0.791** |
| a) Tipo | **Subamortiguado** |
| b) iL(t) | **1.29e⁻²⁵⁰ᵗsin(193.6t) A** |
| c) vC(t) | **50 - e⁻²⁵⁰ᵗ(50cos193.6t + 64.6sin193.6t) V** |
| d) t₉₅% | **≈ 16 ms** |

## Simulación SPICE - Resultados Esperados
```
t=0:     V(3) = 0,     I(L1) = 0
t=5ms:   V(3) = 19.5V, I(L1) = 341mA (cerca del máximo)
t=10ms:  V(3) = 41.3V, I(L1) = 107mA
t=16ms:  V(3) = 49.3V, I(L1) = -42mA
t=30ms:  V(3) ≈ 50V,   I(L1) ≈ 0mA
```

## Conceptos Aplicados
- Respuesta completa = natural + forzada
- Circuito RLC serie con fuente DC
- Comportamiento oscilatorio amortiguado
- Estado estable: L→cortocircuito, C→abierto