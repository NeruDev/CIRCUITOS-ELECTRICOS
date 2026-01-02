# PR-03: Circuito RLC Serie - Críticamente Amortiguado ⭐⭐⭐

## Enunciado
Un [circuito](../../../glossary.md#circuito) RLC serie tiene L = 1H y C = 1mF. Determine:
a) El valor de R para amortiguamiento crítico
b) La expresión para i(t) si v(0) = 10V e iL(0) = 0A
c) El tiempo en que i(t) alcanza su máximo
d) El valor máximo de la [corriente](../../../glossary.md#corriente)

## Diagrama del Circuito

```
    ┌────────┬────────────┬────────┐
    │        │            │        │
    │      + │           ┌┴┐       │
    │     ┌──┴──┐        │R│       │
    │     │  C  │       │ │Rcrit  │
    │     │ 1mF │        └┬┘       │
    │     └──┬──┘         │        │
    │  +     │         ┌──┴──┐     │
    │  v(0)=10V        │  L  │     │
    │  -     │         │ 1H  │     │
    │        │         └──┬──┘     │
    └────────┴────────────┴────────┘

v(0) = 10V, iL(0) = 0A
```

## Netlist SPICE

```spice
* PR-03: Circuito RLC Serie - Críticamente Amortiguado

* Valores para amortiguamiento crítico
R1 1 2 63.25        ; R crítico = 63.25Ω
L1 2 3 1            ; L = 1H con corriente inicial 0A
C1 3 0 1m IC=10     ; C = 1mF con voltaje inicial 10V

.TRAN 0.5ms 100ms UIC ; Análisis transitorio
.PRINT TRAN V(3) I(L1)
.PROBE
.END
```

## Solución

### Datos
- L = 1 H
- C = 1 mF = 10⁻³ F
- v(0) = vC(0) = 10 V
- iL(0) = 0 A

### Parte a) Valor de R para amortiguamiento crítico

**Condición de amortiguamiento crítico:**
$$\alpha = \omega_0$$

Para RLC serie:
$$\alpha = \frac{R}{2L}, \quad \omega_0 = \frac{1}{\sqrt{LC}}$$

$$\frac{R}{2L} = \frac{1}{\sqrt{LC}}$$

$$R = \frac{2L}{\sqrt{LC}} = 2\sqrt{\frac{L}{C}}$$

$$R_{crit} = 2\sqrt{\frac{1}{10^{-3}}} = 2\sqrt{1000} = 2 \times 31.62$$

$$\boxed{R_{crit} = 63.25\text{ Ω}}$$

**[Frecuencia](../../../glossary.md#frecuencia) crítica:**
$$\omega_0 = \alpha = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{(1)(10^{-3})}} = \frac{1}{0.03162} = 31.62\text{ rad/s}$$

### Parte b) Expresión de i(t)

Para amortiguamiento crítico (raíces repetidas), la forma general es:
$$i(t) = (A_1 + A_2 t)e^{-\alpha t}$$
$$i(t) = (A_1 + A_2 t)e^{-31.62t}$$

**Condiciones iniciales:**

1) i(0) = 0:
$$0 = (A_1 + A_2(0))e^0 = A_1$$
$$A_1 = 0$$

2) di(0)/dt:
En el inductor: $v_L = L\frac{di}{dt}$

Por LVK en t = 0⁺:
$$v_R(0^+) + v_L(0^+) + v_C(0^+) = 0$$

Con i(0⁺) = 0: $v_R(0^+) = R \cdot i(0^+) = 0$

$$0 + v_L(0^+) + 10 = 0$$
$$v_L(0^+) = -10\text{ V}$$

$$\frac{di(0^+)}{dt} = \frac{v_L(0^+)}{L} = \frac{-10}{1} = -10\text{ A/s}$$

**Derivada de i(t):**
$$\frac{di}{dt} = A_2 e^{-\alpha t} + (A_1 + A_2 t)(-\alpha)e^{-\alpha t}$$
$$\frac{di}{dt} = [A_2 - \alpha(A_1 + A_2 t)]e^{-\alpha t}$$

En t = 0:
$$-10 = A_2 - \alpha A_1 = A_2 - 31.62(0) = A_2$$
$$A_2 = -10\text{ A/s}$$

$$\boxed{i(t) = -10t \cdot e^{-31.62t}\text{ A}}$$

**Verificación:**
- i(0) = -10(0)e⁰ = 0 A ✓
- El signo negativo indica que la corriente fluye en dirección opuesta a la referencia (el [capacitor](../../../glossary.md#capacitancia) se descarga)

**Forma con signo correcto (corriente de descarga):**
Si definimos la corriente positiva en la dirección de descarga del capacitor:
$$\boxed{i(t) = 10t \cdot e^{-31.62t}\text{ A}}$$

### Parte c) Tiempo del máximo de i(t)

Para el máximo: $\frac{di}{dt} = 0$

$$\frac{di}{dt} = 10e^{-31.62t} + 10t(-31.62)e^{-31.62t} = 0$$
$$10e^{-31.62t}(1 - 31.62t) = 0$$

Como $e^{-31.62t} \neq 0$:
$$1 - 31.62t = 0$$
$$t = \frac{1}{31.62} = \frac{1}{\alpha}$$

$$\boxed{t_{max} = 31.62\text{ ms}}$$

Este resultado es general: en amortiguamiento crítico con i(0)=0, el máximo ocurre en t = 1/α.

### Parte d) Valor máximo de la corriente

$$i_{max} = i(t_{max}) = 10(0.03162)e^{-31.62(0.03162)}$$
$$i_{max} = 0.3162 \times e^{-1}$$
$$i_{max} = 0.3162 \times 0.3679$$

$$\boxed{i_{max} = 116.3\text{ mA}}$$

**Resultado general:** Para este tipo de circuito:
$$i_{max} = \frac{v_C(0)}{L\alpha}e^{-1} = \frac{v_C(0)}{L\alpha \cdot e}$$

$$i_{max} = \frac{10}{1 \times 31.62 \times 2.718} = \frac{10}{85.95} = 116.3\text{ mA ✓}$$

## Tabla de Valores

| t (ms) | t/τ | i(t) (mA) | vC(t) (V) | vL(t) (V) |
|--------|-----|-----------|-----------|-----------|
| 0 | 0 | 0 | 10.0 | -10.0 |
| 10 | 0.32 | 72.7 | 8.95 | -8.50 |
| 20 | 0.63 | 106.3 | 7.41 | -6.16 |
| 31.62 | 1.0 | 116.3 | 5.62 | -3.67 |
| 50 | 1.58 | 103.2 | 3.73 | -1.62 |
| 100 | 3.16 | 42.5 | 1.11 | -0.22 |
| 150 | 4.75 | 12.3 | 0.38 | -0.03 |
| 200 | 6.32 | 2.9 | 0.15 | -0.004 |

## Gráfica de la Respuesta

```
i(mA)
     │
116.3├────────●─────── máximo (t=31.62ms)
     │       / \
100  │      /   \
     │     /     \____
 50  │    /           ────____
     │   /                    ───────
  0  ├──●─────────────────────────────► t(ms)
     │  0   31.62  100  150  200
            1/α     3τ   5τ   6τ

vC(V)
     │
 10  ├─●
     │  \
     │   \
  5  │    \____
     │         ────____
  0  ├─────────────────────────► t(ms)
```

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| α = ω₀ | **31.62 rad/s** |
| τ = 1/α | **31.62 ms** |
| a) R crítico | **63.25 Ω** |
| b) i(t) | **10t·e⁻³¹·⁶²ᵗ A** |
| c) t máximo | **31.62 ms = 1/α** |
| d) i máximo | **116.3 mA** |

## Simulación SPICE - Resultados Esperados
```
t=0:       I(L1) = 0,       V(3) = 10V
t=31.62ms: I(L1) = 116.3mA, V(3) = 5.62V (máximo)
t=100ms:   I(L1) = 42.5mA,  V(3) = 1.11V
t=200ms:   I(L1) = 2.9mA,   V(3) = 0.15V
```

## Conceptos Aplicados
- Amortiguamiento crítico: α = ω₀
- Raíces repetidas: s₁ = s₂ = -α
- Forma de solución: (A₁ + A₂t)e⁻αᵗ
- [Resistencia](../../../glossary.md#resistencia) crítica: R = 2√(L/C)
- Respuesta más rápida sin oscilaciones