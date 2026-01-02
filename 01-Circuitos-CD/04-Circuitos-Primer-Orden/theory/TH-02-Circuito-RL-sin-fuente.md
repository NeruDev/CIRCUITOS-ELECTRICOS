# TH-02: Circuito RL sin Fuente

## Objetivos
- Analizar la respuesta natural del [circuito](../../../glossary.md#circuito) RL
- Calcular la constante de tiempo
- Determinar la [corriente](../../../glossary.md#corriente) y [voltaje](../../../glossary.md#voltaje) en función del tiempo

## Contenido

### Circuito RL sin Fuente

```
    t=0
  ○──/──○
  │     │
  L     R
  │     │
  ○─────○
```

En t < 0, el [inductor](../../../glossary.md#inductancia) tiene una corriente inicial I₀.
En t = 0, se cierra el interruptor.

### Ecuación Diferencial

Aplicando [LVK](../../../glossary.md#lvk):
$$L\frac{di}{dt} + Ri = 0$$

Ecuación diferencial de primer orden homogénea.

### Solución

$$i(t) = I_0 e^{-t/\tau}$$

Donde:
- I₀ = corriente inicial en el inductor
- τ = L/R = constante de tiempo

### Constante de Tiempo

$$\tau = \frac{L}{R}$$

**Significado:**
- Tiempo para que la corriente decaiga a 36.8% de I₀
- En 5τ, la corriente ha decaído prácticamente a cero (< 1%)

### Voltaje en el Resistor

$$v_R(t) = Ri(t) = RI_0 e^{-t/\tau}$$

### Voltaje en el Inductor

$$v_L(t) = L\frac{di}{dt} = -RI_0 e^{-t/\tau}$$

### Energía Disipada

La energía inicial almacenada en el inductor:
$$w_L(0) = \frac{1}{2}LI_0^2$$

Esta energía se disipa completamente en el [resistor](../../../glossary.md#resistencia):
$$w_R = \int_0^{\infty} i^2R \, dt = \frac{1}{2}LI_0^2$$

### Comportamiento Temporal

| Tiempo | i(t)/I₀ | % restante |
|--------|---------|------------|
| τ | 0.368 | 36.8% |
| 2τ | 0.135 | 13.5% |
| 3τ | 0.050 | 5.0% |
| 4τ | 0.018 | 1.8% |
| 5τ | 0.007 | 0.7% |

### Gráfica de la Respuesta

```
i(t)
│
I₀├──╮
│ │   ╲
│ │     ╲
│ │       ╲____
│ │            ─────
0 └────────────────── t
      τ    2τ   3τ
```

## Conceptos Clave
- Respuesta natural: decaimiento exponencial
- τ = L/R determina la velocidad de decaimiento
- La corriente en L es continua
