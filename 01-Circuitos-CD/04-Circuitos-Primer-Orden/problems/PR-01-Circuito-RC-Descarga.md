# PR-01: Circuito RC - Respuesta Natural (Descarga) ⭐⭐

## Enunciado
Un capacitor de 100μF está inicialmente cargado a 50V. En t = 0, se conecta a una resistencia de 10kΩ. Determine:
a) La constante de tiempo del circuito
b) La expresión del voltaje v(t) para t ≥ 0
c) El voltaje en el capacitor en t = 1s y t = 5τ
d) El tiempo requerido para que el voltaje caiga a 5V
e) La energía inicial almacenada y la disipada en 2τ

## Diagrama del Circuito

```
    t=0 (interruptor cierra)
    ○──/──○
    │     │
  + │     │
   C ═   R = 10kΩ
 100μF    │
  - │     │
    └─────┘
    
V₀ = 50V (voltaje inicial)
```

## Netlist SPICE

```spice
* PR-01: Circuito RC - Descarga del Capacitor
* Respuesta natural (sin fuente)

R1 1 0 10k         ; R = 10kΩ
C1 1 0 100u IC=50  ; C = 100μF con condición inicial 50V

.TRAN 0.1s 5s UIC  ; Análisis transitorio hasta 5s, usar CI
.PRINT TRAN V(1)
.PROBE
.END
```

## Solución

### Datos
- C = 100 μF = 100 × 10⁻⁶ F
- R = 10 kΩ = 10 × 10³ Ω
- V₀ = v(0) = 50 V

### Parte a) Constante de tiempo

$$\tau = RC = (10 \times 10^3)(100 \times 10^{-6}) = 1\text{ s}$$

### Parte b) Expresión del voltaje

Para un circuito RC sin fuente (respuesta natural):

$$v(t) = V_0 e^{-t/\tau}$$

$$\boxed{v(t) = 50 e^{-t}\text{ V}, \quad t \geq 0}$$

### Parte c) Voltaje en tiempos específicos

**En t = 1s = τ:**
$$v(1) = 50 e^{-1/1} = 50 e^{-1} = 50 \times 0.368 = 18.4\text{ V}$$

**En t = 5τ = 5s:**
$$v(5) = 50 e^{-5/1} = 50 e^{-5} = 50 \times 0.00674 = 0.337\text{ V}$$

Prácticamente descargado (< 1% del valor inicial).

### Parte d) Tiempo para v = 5V

$$5 = 50 e^{-t/1}$$
$$\frac{5}{50} = e^{-t}$$
$$0.1 = e^{-t}$$
$$\ln(0.1) = -t$$
$$t = -\ln(0.1) = \ln(10) = 2.303\text{ s}$$

### Parte e) Energía

**Energía inicial almacenada:**
$$W_0 = \frac{1}{2}CV_0^2 = \frac{1}{2}(100 \times 10^{-6})(50)^2 = \frac{1}{2}(100 \times 10^{-6})(2500)$$
$$W_0 = 0.125\text{ J} = 125\text{ mJ}$$

**Voltaje en t = 2τ = 2s:**
$$v(2) = 50 e^{-2} = 50 \times 0.135 = 6.77\text{ V}$$

**Energía en t = 2τ:**
$$W(2\tau) = \frac{1}{2}C[v(2\tau)]^2 = \frac{1}{2}(100 \times 10^{-6})(6.77)^2 = 2.29\text{ mJ}$$

**Energía disipada en R hasta t = 2τ:**
$$W_{disipada} = W_0 - W(2\tau) = 125 - 2.29 = 122.7\text{ mJ}$$

O como porcentaje:
$$\frac{W_{disipada}}{W_0} = 1 - e^{-2(2\tau)/\tau} = 1 - e^{-4} = 98.2\%$$

## Tabla de Valores

| t | t/τ | v(t) | % de V₀ |
|---|-----|------|---------|
| 0 | 0 | 50 V | 100% |
| 1s | 1τ | 18.4 V | 36.8% |
| 2s | 2τ | 6.77 V | 13.5% |
| 3s | 3τ | 2.49 V | 5.0% |
| 4s | 4τ | 0.92 V | 1.8% |
| 5s | 5τ | 0.34 V | 0.7% |

## Gráfica del Voltaje

```
v(V)
50├──╮
   │  ╲
   │   ╲
   │    ╲
18.4├─────●─────
   │       ╲
   │        ╲____
   │             ─────
 0 └────────────────────── t(s)
       1τ    2τ    3τ    4τ    5τ
```

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| a) τ | **1 s** |
| b) v(t) | **50e⁻ᵗ V** |
| c) v(1s) | **18.4 V** |
| c) v(5τ) | **0.34 V** |
| d) t para v=5V | **2.303 s** |
| e) W₀ | **125 mJ** |
| e) W disipada en 2τ | **122.7 mJ** |

## Simulación SPICE - Resultados Esperados
```
t=0:     V(1) = 50.000
t=1s:    V(1) = 18.394
t=2s:    V(1) = 6.767
t=2.3s:  V(1) = 5.000
t=5s:    V(1) = 0.337
```

## Corriente en el circuito

$$i(t) = -C\frac{dv}{dt} = -C \times V_0 \times \left(-\frac{1}{\tau}\right) e^{-t/\tau} = \frac{V_0}{R}e^{-t/\tau}$$

$$i(t) = \frac{50}{10000}e^{-t} = 5\text{ mA} \times e^{-t}$$

## Conceptos Aplicados
- Respuesta natural de circuito RC
- Constante de tiempo τ = RC
- Decaimiento exponencial
- Energía almacenada en capacitor