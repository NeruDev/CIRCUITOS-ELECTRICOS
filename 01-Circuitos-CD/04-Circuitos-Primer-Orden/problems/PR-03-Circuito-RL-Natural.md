```markdown
# PR-03: Circuito RL - Respuesta Natural ⭐⭐

## Enunciado
Un inductor de 0.5H tiene una corriente inicial de 4A. En t = 0, se desconecta de su fuente y se conecta a una resistencia de 20Ω. Determine:
a) La constante de tiempo
b) La expresión de i(t) para t ≥ 0
c) El tiempo para que la corriente caiga a 1A
d) La energía inicial almacenada en el inductor
e) La potencia disipada en R en t = τ/2

## Diagrama del Circuito

```
    t=0 (interruptor cambia)
    
Antes (t<0):          Después (t≥0):
    ┌────────┐            ┌────────┐
    │        │            │        │
  + │      ┌─┴─┐          │      ┌─┴─┐
(Vs)│      │ L │          │      │ L │
    │      │0.5H│          │      │0.5H│
  - │      └─┬─┘          │      └─┬─┘
    │        │            │        │
    └────────┘            └──/\/\/─┘
                            R=20Ω
                            
iL(0⁻) = 4A
```

## Netlist SPICE

```spice
* PR-03: Circuito RL - Respuesta Natural
* Descarga del inductor

R1 1 0 20          ; R = 20Ω
L1 1 0 0.5 IC=4    ; L = 0.5H con condición inicial 4A

.TRAN 0.001s 0.15s UIC  ; Análisis transitorio
.PRINT TRAN I(L1) V(1)
.PROBE
.END
```

## Solución

### Datos
- L = 0.5 H
- R = 20 Ω
- i(0⁻) = i(0⁺) = 4 A (corriente inicial)

### Parte a) Constante de tiempo

$$\tau = \frac{L}{R} = \frac{0.5}{20} = 0.025\text{ s} = 25\text{ ms}$$

### Parte b) Expresión de i(t)

Para un circuito RL sin fuente (respuesta natural):

$$i(t) = I_0 e^{-t/\tau}$$

$$\boxed{i(t) = 4e^{-40t}\text{ A}, \quad t \geq 0}$$

Donde el exponente es: $-t/\tau = -t/0.025 = -40t$

### Parte c) Tiempo para i = 1A

$$1 = 4e^{-40t}$$
$$\frac{1}{4} = e^{-40t}$$
$$\ln(0.25) = -40t$$
$$t = -\frac{\ln(0.25)}{40} = \frac{1.386}{40} = 0.0347\text{ s} = 34.7\text{ ms}$$

Expresado en constantes de tiempo: t = 1.386τ

### Parte d) Energía inicial almacenada

$$W_0 = \frac{1}{2}LI_0^2 = \frac{1}{2}(0.5)(4)^2 = \frac{1}{2}(0.5)(16) = 4\text{ J}$$

### Parte e) Potencia disipada en t = τ/2

**Corriente en t = τ/2 = 12.5ms:**
$$i(\tau/2) = 4e^{-40(0.0125)} = 4e^{-0.5} = 4 \times 0.606 = 2.426\text{ A}$$

**Potencia disipada en R:**
$$P_R = i^2 R = (2.426)^2 (20) = 5.89 \times 20 = 117.7\text{ W}$$

**Verificación con voltaje:**
$$v_L(t) = L\frac{di}{dt} = L \times I_0 \times (-40) e^{-40t} = -0.5 \times 4 \times 40 \times e^{-40t}$$
$$v_L(t) = -80e^{-40t}\text{ V}$$

En t = 0: vL(0) = -80V (el voltaje aparece negativo porque se opone al decaimiento de corriente)

El voltaje en R: vR = -vL = 80e^(-40t) V (por LVK)

$$P_R(\tau/2) = \frac{v_R^2}{R} = \frac{(80 \times 0.606)^2}{20} = \frac{(48.5)^2}{20} = 117.7\text{ W} \checkmark$$

## Tabla de Valores

| t (ms) | t/τ | i(t) (A) | v_R(t) (V) | P_R (W) |
|--------|-----|----------|------------|---------|
| 0 | 0 | 4.00 | 80.0 | 320.0 |
| 12.5 | 0.5τ | 2.43 | 48.5 | 117.7 |
| 25 | 1τ | 1.47 | 29.4 | 43.3 |
| 50 | 2τ | 0.54 | 10.8 | 5.85 |
| 75 | 3τ | 0.20 | 3.97 | 0.79 |
| 100 | 4τ | 0.073 | 1.46 | 0.11 |
| 125 | 5τ | 0.027 | 0.54 | 0.015 |

## Gráfica de la Corriente

```
i(A)
4 ├──╮
   │  ╲
   │   ╲
   │    ╲
1.47├─────●─────
   │       ╲
   │        ╲____
   │             ─────
 0 └────────────────────── t(ms)
       25    50    75   100   125
        1τ    2τ    3τ   4τ    5τ
```

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| a) τ | **25 ms** |
| b) i(t) | **4e⁻⁴⁰ᵗ A** |
| c) t para i=1A | **34.7 ms** |
| d) W₀ | **4 J** |
| e) P_R en τ/2 | **117.7 W** |

## Simulación SPICE - Resultados Esperados
```
t=0:       I(L1) = 4.000,  V(1) = 80.00
t=0.0125s: I(L1) = 2.426,  V(1) = 48.52
t=0.025s:  I(L1) = 1.472,  V(1) = 29.44
t=0.035s:  I(L1) = 0.988,  V(1) = 19.76
```

## Balance de Energía

Toda la energía almacenada inicialmente en L se disipa en R:

$$W_{disipada} = \int_0^{\infty} P_R \, dt = \int_0^{\infty} i^2 R \, dt = \int_0^{\infty} (I_0 e^{-t/\tau})^2 R \, dt$$

$$W_{disipada} = I_0^2 R \int_0^{\infty} e^{-2t/\tau} dt = I_0^2 R \left[-\frac{\tau}{2}e^{-2t/\tau}\right]_0^{\infty}$$

$$W_{disipada} = I_0^2 R \times \frac{\tau}{2} = (16)(20)(0.0125) = 4\text{ J} = W_0 \checkmark$$

## Conceptos Aplicados
- Respuesta natural de circuito RL
- Constante de tiempo τ = L/R
- Continuidad de corriente en inductor
- Conservación de energía
```
