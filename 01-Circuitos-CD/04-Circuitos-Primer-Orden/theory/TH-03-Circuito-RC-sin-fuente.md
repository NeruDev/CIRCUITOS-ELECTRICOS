# TH-03: Circuito RC sin Fuente

## Objetivos
- Analizar la respuesta natural del [circuito](../../../glossary.md#circuito) RC
- Calcular la constante de tiempo
- Determinar el [voltaje](../../../glossary.md#voltaje) y [corriente](../../../glossary.md#corriente) en función del tiempo

## Contenido

### Circuito RC sin Fuente

![Circuito RC de Primer Orden](../media/fig_01_circuito_rc.svg)
*Figura 1: Circuito RC de primer orden con switch - Respuesta de carga y descarga*

En t < 0, el [capacitor](../../../glossary.md#capacitancia) tiene un voltaje inicial V₀.
En t = 0, se cierra el interruptor.

### Ecuación Diferencial

Aplicando [LCK](../../../glossary.md#lck):
$$C\frac{dv}{dt} + \frac{v}{R} = 0$$

Ecuación diferencial de primer orden homogénea.

### Solución

$$v(t) = V_0 e^{-t/\tau}$$

Donde:
- V₀ = voltaje inicial en el capacitor
- τ = RC = constante de tiempo

### Constante de Tiempo

$$\tau = RC$$

**Significado:**
- Tiempo para que el voltaje decaiga a 36.8% de V₀
- En 5τ, el voltaje ha decaído prácticamente a cero

### Corriente en el Circuito

$$i(t) = -C\frac{dv}{dt} = \frac{V_0}{R} e^{-t/\tau}$$

### Corriente en el Resistor

$$i_R(t) = \frac{v(t)}{R} = \frac{V_0}{R} e^{-t/\tau}$$

### Energía Disipada

La energía inicial almacenada en el capacitor:
$$w_C(0) = \frac{1}{2}CV_0^2$$

Esta energía se disipa completamente en el [resistor](../../../glossary.md#resistencia):
$$w_R = \int_0^{\infty} \frac{v^2}{R} \, dt = \frac{1}{2}CV_0^2$$

### Comportamiento Temporal

| Tiempo | v(t)/V₀ | % restante |
|--------|---------|------------|
| τ | 0.368 | 36.8% |
| 2τ | 0.135 | 13.5% |
| 3τ | 0.050 | 5.0% |
| 4τ | 0.018 | 1.8% |
| 5τ | 0.007 | 0.7% |

### Gráfica de la Respuesta

```
v(t)
│
V₀├──╮
│ │   ╲
│ │     ╲
│ │       ╲____
│ │            ─────
0 └────────────────── t
      τ    2τ   3τ
```

### Dualidad RL-RC

| Circuito RL | Circuito RC |
|-------------|-------------|
| i(t) = I₀e^(-t/τ) | v(t) = V₀e^(-t/τ) |
| τ = L/R | τ = RC |
| Corriente continua | Voltaje continuo |
| Energía: ½LI₀² | Energía: ½CV₀² |

## Conceptos Clave
- Respuesta natural: decaimiento exponencial
- τ = RC determina la velocidad de decaimiento
- El voltaje en C es continuo
