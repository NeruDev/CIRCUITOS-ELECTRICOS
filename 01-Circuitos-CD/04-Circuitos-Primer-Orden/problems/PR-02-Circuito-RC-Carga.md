# PR-02: Circuito RC - Respuesta Completa (Carga) ⭐⭐

## Enunciado
En t = 0, se cierra el interruptor conectando una fuente de 12V a un circuito RC. El capacitor tiene una carga inicial de 2V. Determine:
a) La constante de tiempo
b) La expresión de v(t) para t ≥ 0
c) El tiempo para que v alcance el 95% del valor final
d) La corriente i(t) y su valor inicial

Datos: R = 5kΩ, C = 20μF, v(0⁻) = 2V, Vs = 12V

## Diagrama del Circuito

```
        t=0
    ┌────/────┬────/\/\/────┐
    │         │    R=5kΩ    │
  + │         │             │
(Vs)│       + │           + │
 12V│       vc(t)         vR │
  - │       - C             │
    │        20μF           │
    └─────────┴─────────────┘
    
vc(0⁻) = 2V
```

## Netlist SPICE

```spice
* PR-02: Circuito RC - Carga del Capacitor
* Respuesta completa con fuente DC

V1 1 0 DC 12V      ; Fuente de voltaje 12V
R1 1 2 5k          ; R = 5kΩ
C1 2 0 20u IC=2    ; C = 20μF con condición inicial 2V

.TRAN 0.01s 0.5s UIC  ; Análisis transitorio hasta 0.5s
.PRINT TRAN V(2) I(R1)
.PROBE
.END
```

## Solución

### Datos
- Vs = 12 V
- R = 5 kΩ = 5000 Ω
- C = 20 μF = 20 × 10⁻⁶ F
- v(0⁻) = v(0⁺) = 2 V (voltaje inicial)

### Parte a) Constante de tiempo

$$\tau = RC = (5 \times 10^3)(20 \times 10^{-6}) = 0.1\text{ s} = 100\text{ ms}$$

### Parte b) Expresión de v(t)

Usando la fórmula general:
$$v(t) = v(\infty) + [v(0^+) - v(\infty)]e^{-t/\tau}$$

**Valor inicial:** v(0⁺) = 2 V (continuidad del voltaje en C)

**Valor final:** En estado estable, el capacitor se comporta como circuito abierto:
$$v(\infty) = V_s = 12\text{ V}$$

**Expresión completa:**
$$v(t) = 12 + (2 - 12)e^{-t/0.1}$$

$$\boxed{v(t) = 12 - 10e^{-10t}\text{ V}, \quad t \geq 0}$$

**Verificación:**
- En t = 0: v(0) = 12 - 10(1) = 2 V ✓
- En t → ∞: v(∞) = 12 - 10(0) = 12 V ✓

### Parte c) Tiempo para alcanzar 95% del valor final

El 95% del valor final:
$$v = 0.95 \times 12 = 11.4\text{ V}$$

$$11.4 = 12 - 10e^{-10t}$$
$$10e^{-10t} = 0.6$$
$$e^{-10t} = 0.06$$
$$-10t = \ln(0.06)$$
$$t = -\frac{\ln(0.06)}{10} = \frac{2.813}{10} = 0.281\text{ s}$$

Alternativamente, usando la regla práctica:
Para alcanzar ~95% del valor final: t ≈ 3τ = 3(0.1) = 0.3 s

### Parte d) Corriente i(t)

$$i(t) = C\frac{dv}{dt} = C \times 10 \times 10 \times e^{-10t} = 100Ce^{-10t}$$

$$i(t) = (20 \times 10^{-6})(100)e^{-10t} = 2 \times 10^{-3} e^{-10t}$$

$$\boxed{i(t) = 2e^{-10t}\text{ mA}, \quad t \geq 0}$$

**Corriente inicial (t = 0⁺):**
$$i(0^+) = 2e^0 = 2\text{ mA}$$

**Verificación con Ley de Ohm:**
$$i(0^+) = \frac{V_s - v(0^+)}{R} = \frac{12 - 2}{5000} = \frac{10}{5000} = 2\text{ mA} \checkmark$$

## Tabla de Valores

| t (ms) | t/τ | v(t) (V) | i(t) (mA) |
|--------|-----|----------|-----------|
| 0 | 0 | 2.00 | 2.00 |
| 50 | 0.5τ | 5.93 | 1.21 |
| 100 | 1τ | 8.32 | 0.74 |
| 200 | 2τ | 10.64 | 0.27 |
| 300 | 3τ | 11.50 | 0.10 |
| 400 | 4τ | 11.82 | 0.04 |
| 500 | 5τ | 11.93 | 0.01 |

## Gráfica del Voltaje

```
v(V)
12├────────────────────────●
   │                   ╱───
   │              ╱───
   │         ╱───
   │    ╱───
 2 ├──●
   │
 0 └─────────────────────────── t(ms)
       100   200   300   400   500
        1τ    2τ    3τ    4τ    5τ
```

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| a) τ | **100 ms** |
| b) v(t) | **12 - 10e⁻¹⁰ᵗ V** |
| c) t para 95% | **281 ms ≈ 3τ** |
| d) i(t) | **2e⁻¹⁰ᵗ mA** |
| d) i(0⁺) | **2 mA** |

## Simulación SPICE - Resultados Esperados
```
t=0:      V(2) = 2.000,  I(R1) = 2.000mA
t=0.1s:   V(2) = 8.321,  I(R1) = 0.736mA
t=0.281s: V(2) = 11.40,  I(R1) = 0.12mA
t=0.5s:   V(2) = 11.93,  I(R1) = 0.014mA
```

## Descomposición de la Respuesta

La respuesta completa se puede expresar como:

$$v(t) = \underbrace{12}_{\text{Respuesta forzada}} + \underbrace{(-10)e^{-10t}}_{\text{Respuesta natural}}$$

O equivalentemente:
$$v(t) = \underbrace{12(1-e^{-10t})}_{\text{Respuesta a escalón}} + \underbrace{2e^{-10t}}_{\text{Respuesta a CI}}$$

## Conceptos Aplicados
- Respuesta completa de circuito RC
- Fórmula general: v(t) = v(∞) + [v(0⁺) - v(∞)]e^(-t/τ)
- Continuidad del voltaje en capacitor
- Relación i-v en capacitor