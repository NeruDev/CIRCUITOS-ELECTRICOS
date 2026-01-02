# PR-05: Circuito RC con Entrada Escalón y Condición Inicial ⭐⭐⭐

## Enunciado
El interruptor del [circuito](../../../glossary.md#circuito) ha estado en la posición A por largo tiempo. En t = 0 se cambia a la posición B. Determine:
a) La expresión para v(t) para t ≥ 0
b) El tiempo requerido para que v(t) alcance cero
c) La [corriente](../../../glossary.md#corriente) i(t) para t ≥ 0
d) La energía disipada en la [resistencia](../../../glossary.md#resistencia) en el intervalo 0 < t < ∞

Datos: V1 = 12V, V2 = 6V, R = 5kΩ, C = 4μF

## Diagrama del Circuito

```
                    t=0
       A ●────o────/────● B
         │        │      │
       + │        │    + │
   12V (─)        │   (─) 6V
       - │    ┌───┴──┐ - │
         │    │  C   │   │
         │    │ 4μF  │   │
         │    └──┬───┘   │
         │       │       │
         └──/\/\/┴───────┘
           R=5kΩ

En posición A: El capacitor se carga a 12V
En posición B: Nuevo circuito con fuente de 6V
```

## Netlist SPICE

```spice
* PR-05: Circuito RC con Entrada Escalón
* Simulación desde posición B

V1 1 0 DC 6V         ; Nueva fuente de 6V
R1 1 2 5k            ; R = 5kΩ
C1 2 0 4u IC=12      ; C = 4μF con condición inicial 12V

.TRAN 0.1ms 100ms UIC ; Análisis transitorio con IC
.PRINT TRAN V(2) I(R1) I(C1)
.PROBE
.END
```

## Solución

### Datos
- V1 = 12 V (fuente inicial)
- V2 = 6 V (nueva fuente)
- R = 5 kΩ = 5000 Ω
- C = 4 μF = 4×10⁻⁶ F

### Análisis inicial y final

**Constante de tiempo:**
$$\tau = RC = (5000)(4 \times 10^{-6}) = 0.02\text{ s} = 20\text{ ms}$$

**Valor inicial:** Tras largo tiempo en posición A:
$$v(0^-) = v(0^+) = 12\text{ V}$$

**Valor final:** En posición B, cuando el [capacitor](../../../glossary.md#capacitancia) actúa como circuito abierto:
$$v(\infty) = V_2 = 6\text{ V}$$

### Parte a) Expresión de v(t)

Usando la fórmula general:
$$v(t) = v(\infty) + [v(0^+) - v(\infty)]e^{-t/\tau}$$

$$v(t) = 6 + (12 - 6)e^{-t/0.02}$$

$$\boxed{v(t) = 6 + 6e^{-50t}\text{ V}, \quad t \geq 0}$$

**Verificación:**
- En t = 0: v(0) = 6 + 6(1) = 12 V ✓
- En t → ∞: v(∞) = 6 + 6(0) = 6 V ✓

### Parte b) Tiempo para v(t) = 0

$$0 = 6 + 6e^{-50t}$$
$$6e^{-50t} = -6$$
$$e^{-50t} = -1$$

**No existe solución real.** La función exponencial siempre es positiva, por lo que v(t) nunca puede ser cero o negativo. El mínimo valor que alcanza v(t) es 6V cuando t→∞.

$$\boxed{\text{El voltaje nunca alcanza cero}}$$

### Parte c) Corriente i(t)

La corriente en el circuito:
$$i(t) = C\frac{dv}{dt} = (4 \times 10^{-6})\frac{d}{dt}(6 + 6e^{-50t})$$

$$i(t) = (4 \times 10^{-6})(6)(-50)e^{-50t}$$

$$i(t) = -1.2 \times 10^{-3}e^{-50t}\text{ A}$$

$$\boxed{i(t) = -1.2e^{-50t}\text{ mA}, \quad t \geq 0}$$

El signo negativo indica que la corriente fluye en sentido opuesto al de [carga](../../../glossary.md#carga) (el capacitor se descarga parcialmente de 12V a 6V).

**Verificación con [LVK](../../../glossary.md#lvk) en t = 0⁺:**
$$V_2 = v_R(0^+) + v(0^+)$$
$$v_R(0^+) = V_2 - v(0^+) = 6 - 12 = -6\text{ V}$$
$$i(0^+) = \frac{v_R}{R} = \frac{-6}{5000} = -1.2\text{ mA ✓}$$

### Parte d) Energía disipada en R (0 < t < ∞)

**Potencia disipada:**
$$p_R(t) = i^2(t) \cdot R = (1.2 \times 10^{-3})^2 e^{-100t} \cdot 5000$$

$$p_R(t) = 7.2 \times 10^{-3} e^{-100t}\text{ W}$$

**Energía total disipada:**
$$W_R = \int_0^{\infty} p_R(t) \, dt = \int_0^{\infty} 7.2 \times 10^{-3} e^{-100t} dt$$

$$W_R = 7.2 \times 10^{-3} \left[-\frac{1}{100}e^{-100t}\right]_0^{\infty}$$

$$W_R = 7.2 \times 10^{-3} \times \frac{1}{100} \times (0 - (-1))$$

$$W_R = 7.2 \times 10^{-5} = 72\text{ μJ}$$

**Verificación por balance de energía:**
$$W_R = \frac{1}{2}C[v^2(0) - v^2(\infty)] = \frac{1}{2}(4 \times 10^{-6})(12^2 - 6^2)$$
$$W_R = 2 \times 10^{-6}(144 - 36) = 2 \times 10^{-6}(108) = 216\text{ μJ}$$

Hmm, hay una diferencia porque parte de la energía va a la fuente. Recalculemos:

**Energía entregada por la fuente:**
$$W_s = V_2 \int_0^{\infty} i(t) dt = 6 \int_0^{\infty} (-1.2 \times 10^{-3})e^{-50t} dt$$

$$W_s = -7.2 \times 10^{-3} \left[-\frac{1}{50}e^{-50t}\right]_0^{\infty} = -7.2 \times 10^{-3} \times \frac{1}{50}$$

$$W_s = -144 \times 10^{-6}\text{ J} = -144\text{ μJ}$$

El signo negativo indica que la fuente **absorbe** energía.

**Balance de energía:**
- Energía inicial en C: $\frac{1}{2}C v^2(0) = \frac{1}{2}(4\mu)(144) = 288$ μJ
- Energía final en C: $\frac{1}{2}C v^2(\infty) = \frac{1}{2}(4\mu)(36) = 72$ μJ
- Energía perdida por C: 288 - 72 = 216 μJ
- Energía absorbida por fuente: 144 μJ
- Energía disipada en R: 216 - 144 = **72 μJ** ✓

$$\boxed{W_R = 72\text{ μJ}}$$

## Tabla de Valores

| t (ms) | t/τ | v(t) (V) | i(t) (mA) | pR(t) (mW) |
|--------|-----|----------|-----------|------------|
| 0 | 0 | 12.0 | -1.20 | 7.2 |
| 10 | 0.5τ | 9.64 | -0.73 | 2.65 |
| 20 | 1τ | 8.21 | -0.44 | 0.97 |
| 40 | 2τ | 6.81 | -0.16 | 0.13 |
| 60 | 3τ | 6.30 | -0.06 | 0.02 |
| 100 | 5τ | 6.04 | -0.008 | 0.0003 |

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| τ | **20 ms** |
| a) v(t) | **6 + 6e⁻⁵⁰ᵗ V** |
| b) Tiempo v=0 | **Nunca (mínimo 6V)** |
| c) i(t) | **-1.2e⁻⁵⁰ᵗ mA** |
| d) WR | **72 μJ** |

## Simulación SPICE - Resultados Esperados
```
t=0:     V(2) = 12.00,  I(C1) = -1.2mA
t=20ms:  V(2) = 8.21,   I(C1) = -0.44mA
t=40ms:  V(2) = 6.81,   I(C1) = -0.16mA
t=100ms: V(2) = 6.04,   I(C1) = -0.008mA
```

## Conceptos Aplicados
- Respuesta completa de circuito RC
- Cambio de fuentes (conmutación)
- Balance de energía con fuente y resistencia
- Fuente como elemento absorbente de energía