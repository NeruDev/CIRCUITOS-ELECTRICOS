# PR-04: Circuito RL - Respuesta Completa ⭐⭐

## Enunciado
En t = 0 se cierra el interruptor en el circuito mostrado. Si la corriente inicial en el inductor es i(0⁻) = 1A, determine:
a) La corriente i(t) para t ≥ 0
b) El voltaje vL(t) en el inductor
c) El tiempo para que i alcance el 90% del valor final
d) La energía suministrada por la fuente en el intervalo 0 < t < 2τ

Datos: Vs = 24V, R = 8Ω, L = 2H

## Diagrama del Circuito

```
        t=0
    ┌────/────┬────/\/\/────┐
    │         │    R=8Ω     │
  + │         │           + │
(Vs)│       ┌─┴─┐        vR │
 24V│       │ L │         - │
  - │       │ 2H│           │
    │       └─┬─┘           │
    └─────────┴─────────────┘
    
iL(0⁻) = 1A
```

## Netlist SPICE

```spice
* PR-04: Circuito RL - Respuesta Completa
* Con fuente DC

V1 1 0 DC 24V      ; Fuente de voltaje 24V
R1 1 2 8           ; R = 8Ω
L1 2 0 2 IC=1      ; L = 2H con condición inicial 1A

.TRAN 0.01s 2s UIC ; Análisis transitorio hasta 2s
.PRINT TRAN I(L1) V(2) V(1,2)
.PROBE
.END
```

## Solución

### Datos
- Vs = 24 V
- R = 8 Ω
- L = 2 H
- i(0⁻) = i(0⁺) = 1 A (corriente inicial)

### Paso previo: Análisis de valores límite

**Constante de tiempo:**
$$\tau = \frac{L}{R} = \frac{2}{8} = 0.25\text{ s} = 250\text{ ms}$$

**Valor inicial:** i(0⁺) = 1 A (continuidad de corriente en L)

**Valor final:** En estado estable, L actúa como cortocircuito:
$$i(\infty) = \frac{V_s}{R} = \frac{24}{8} = 3\text{ A}$$

### Parte a) Expresión de i(t)

Usando la fórmula general:
$$i(t) = i(\infty) + [i(0^+) - i(\infty)]e^{-t/\tau}$$

$$i(t) = 3 + (1 - 3)e^{-t/0.25}$$

$$\boxed{i(t) = 3 - 2e^{-4t}\text{ A}, \quad t \geq 0}$$

**Verificación:**
- En t = 0: i(0) = 3 - 2(1) = 1 A ✓
- En t → ∞: i(∞) = 3 - 2(0) = 3 A ✓

### Parte b) Voltaje vL(t)

$$v_L(t) = L\frac{di}{dt} = 2 \times \frac{d}{dt}(3 - 2e^{-4t})$$

$$v_L(t) = 2 \times (-2)(-4)e^{-4t} = 16e^{-4t}\text{ V}$$

$$\boxed{v_L(t) = 16e^{-4t}\text{ V}, \quad t \geq 0}$$

**Verificación con LVK:**
$$v_R(t) = i(t) \times R = 8(3 - 2e^{-4t}) = 24 - 16e^{-4t}\text{ V}$$

$$V_s = v_R + v_L$$
$$24 = (24 - 16e^{-4t}) + 16e^{-4t} = 24 \checkmark$$

**Valor inicial del voltaje:**
$$v_L(0^+) = 16\text{ V}$$

Verificación: $v_L(0^+) = V_s - i(0^+)R = 24 - (1)(8) = 16$ V ✓

### Parte c) Tiempo para 90% del valor final

El 90% del valor final:
$$i = 0.9 \times 3 = 2.7\text{ A}$$

$$2.7 = 3 - 2e^{-4t}$$
$$2e^{-4t} = 0.3$$
$$e^{-4t} = 0.15$$
$$-4t = \ln(0.15) = -1.897$$
$$t = \frac{1.897}{4} = 0.474\text{ s} = 474\text{ ms}$$

Expresado en τ: t ≈ 1.9τ

### Parte d) Energía suministrada por la fuente (0 < t < 2τ)

**Potencia de la fuente:**
$$p_s(t) = V_s \times i(t) = 24(3 - 2e^{-4t}) = 72 - 48e^{-4t}\text{ W}$$

**Energía en el intervalo 0 < t < 2τ = 0.5s:**
$$W_s = \int_0^{0.5} p_s(t) \, dt = \int_0^{0.5} (72 - 48e^{-4t}) dt$$

$$W_s = \left[72t + \frac{48}{4}e^{-4t}\right]_0^{0.5}$$

$$W_s = \left[72t + 12e^{-4t}\right]_0^{0.5}$$

$$W_s = \left(72(0.5) + 12e^{-2}\right) - \left(0 + 12e^0\right)$$

$$W_s = (36 + 12 \times 0.135) - 12 = 36 + 1.62 - 12 = 25.62\text{ J}$$

## Tabla de Valores

| t (ms) | t/τ | i(t) (A) | vL(t) (V) | vR(t) (V) |
|--------|-----|----------|-----------|-----------|
| 0 | 0 | 1.00 | 16.0 | 8.0 |
| 125 | 0.5τ | 1.79 | 9.7 | 14.3 |
| 250 | 1τ | 2.26 | 5.9 | 18.1 |
| 500 | 2τ | 2.73 | 2.2 | 21.8 |
| 750 | 3τ | 2.90 | 0.8 | 23.2 |
| 1000 | 4τ | 2.96 | 0.3 | 23.7 |

## Gráfica de Corriente y Voltaje

```
i(A), vL(V)
     │
  3A ├────────────────────────● i(t)
     │                   ╱───
     │              ╱───
     │         ╱───
  1A ├──●────
     │
 16V ├──●
     │   ╲
     │    ╲____
     │         ─────● vL(t)
   0 └─────────────────────────── t(ms)
         250   500   750   1000
          1τ    2τ    3τ    4τ
```

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| τ | **250 ms** |
| a) i(t) | **3 - 2e⁻⁴ᵗ A** |
| b) vL(t) | **16e⁻⁴ᵗ V** |
| c) t para 90% | **474 ms** |
| d) Ws (0 a 2τ) | **25.62 J** |

## Simulación SPICE - Resultados Esperados
```
t=0:     I(L1) = 1.000,  V(2) = 16.00
t=0.25s: I(L1) = 2.264,  V(2) = 5.89
t=0.47s: I(L1) = 2.697,  V(2) = 2.42
t=0.5s:  I(L1) = 2.729,  V(2) = 2.17
t=1s:    I(L1) = 2.963,  V(2) = 0.29
```

## Conceptos Aplicados
- Respuesta completa de circuito RL
- Fórmula general: i(t) = i(∞) + [i(0⁺) - i(∞)]e^(-t/τ)
- Continuidad de corriente en inductor
- L actúa como cortocircuito en DC estable