# TH-01: Características de la Onda Senoidal

## Objetivos
- Describir los parámetros de una onda senoidal
- Calcular período, [frecuencia](../../../glossary.md#frecuencia) y fase
- Relacionar valores instantáneos y máximos

## Contenido

### La Onda Senoidal

La [corriente alterna](../../../glossary.md#corriente) se describe mediante funciones senoidales:

$$v(t) = V_m \sin(\omega t + \phi)$$

o equivalentemente:

$$v(t) = V_m \cos(\omega t + \phi)$$

### Parámetros de la Onda Senoidal

**Amplitud o Valor Máximo (Vm):**
Valor pico de la señal. Unidades: V o A.

**Frecuencia Angular (ω):**
$$\omega = 2\pi f$$
Unidades: rad/s

**Frecuencia (f):**
Número de ciclos por segundo.
Unidades: Hertz (Hz)

**Período (T):**
Tiempo de un ciclo completo.
$$T = \frac{1}{f} = \frac{2\pi}{\omega}$$
Unidades: segundos (s)

**Fase (φ):**
Desplazamiento angular respecto a una referencia.
Unidades: radianes o grados

### Gráfica de la Onda Senoidal

```
v(t)
│    ╭─╮       ╭─╮
Vm├──╱   ╲─────╱   ╲───
│ ╱     ╲   ╱     ╲
0├─────────╳─────────╳── t
│         ╲ ╱       ╲╱
-Vm├────────╲╱─────────
│
└──────────┬──────────┬
           T          2T
```

### Valores Instantáneos

El valor de la señal en cualquier instante t:
$$v(t_1) = V_m \sin(\omega t_1 + \phi)$$

### Relaciones de Fase

**Señales en fase:**
Tienen el mismo ángulo de fase.

**Señal adelantada:**
Si v₁ tiene fase mayor que v₂, v₁ adelanta a v₂.
$$v_1 = V_m \sin(\omega t + \phi_1)$$
$$v_2 = V_m \sin(\omega t + \phi_2)$$
Si φ₁ > φ₂, v₁ adelanta a v₂ por (φ₁ - φ₂).

**Señal atrasada:**
Si φ₁ < φ₂, v₁ atrasa a v₂.

### Frecuencias Estándar

| País/Región | Frecuencia |
|-------------|------------|
| América, Japón (parcial) | 60 Hz |
| Europa, Asia, África | 50 Hz |

### Ejemplo

**Señal:** v(t) = 170 sin(377t + 30°) V

**Parámetros:**
- Vm = 170 V
- ω = 377 rad/s
- f = 377/(2π) = 60 Hz
- T = 1/60 = 16.67 ms
- φ = 30° = π/6 rad

## Conceptos Clave
- ω = 2πf = 2π/T
- La fase determina el desplazamiento temporal
- Adelanto/atraso de fase
