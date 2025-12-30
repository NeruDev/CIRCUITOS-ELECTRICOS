# TH-06: La Respuesta Natural y la Respuesta Forzada

## Objetivos
- Distinguir entre respuesta natural y forzada
- Comprender la respuesta transitoria y de estado estable
- Analizar la respuesta completa de circuitos de primer orden

## Contenido

### Descomposición de la Respuesta

La respuesta completa de un circuito se puede expresar como:

$$x(t) = x_n(t) + x_f(t)$$

Donde:
- x_n(t) = respuesta natural
- x_f(t) = respuesta forzada

### Respuesta Natural

La **respuesta natural** es la respuesta del circuito debido a las condiciones iniciales, sin fuentes externas.

**Características:**
- Depende de las condiciones iniciales (energía almacenada)
- Tiene la forma de la solución homogénea
- Decae exponencialmente a cero (sistemas estables)

**Para circuito de primer orden:**
$$x_n(t) = Ae^{-t/\tau}$$

### Respuesta Forzada

La **respuesta forzada** es la respuesta debida a las fuentes externas, independiente de las condiciones iniciales.

**Características:**
- Depende de la forma de la excitación
- Tiene la misma forma que la entrada (para sistemas lineales)
- También llamada solución particular

**Para fuente DC:**
$$x_f(t) = x_{ss}$$ (valor constante)

### Respuesta Transitoria vs Estado Estable

Otra forma de descomponer:

$$x(t) = x_{tr}(t) + x_{ss}(t)$$

- **x_tr(t)**: Respuesta transitoria (decae con el tiempo)
- **x_ss(t)**: Respuesta de estado estable (permanece)

### Relación entre Descomposiciones

| Natural/Forzada | Transitoria/Estado Estable |
|-----------------|---------------------------|
| x_n(t) | Parte de x_tr(t) |
| x_f(t) | Contribuye a x_tr(t) y x_ss(t) |

### Respuesta Completa

**Forma general:**
$$x(t) = x(\infty) + [x(0^+) - x(\infty)]e^{-t/\tau}$$

Donde:
- x(∞) = valor de estado estable (respuesta forzada para DC)
- x(0⁺) = condición inicial
- [x(0⁺) - x(∞)]e^(-t/τ) = componente transitoria

### Ejemplo: Circuito RC con fuente

```
Vs──/──R──┬──○
          │
          C
          │
──────────┴──○
```

**Respuesta del voltaje en C:**

- Respuesta natural: v_n(t) = V₀e^(-t/RC)
- Respuesta forzada: v_f(t) = Vs
- Respuesta completa: v(t) = Vs + (V₀ - Vs)e^(-t/RC)

### Interpretación Física

1. **Transitorio**: Período de ajuste mientras la energía se redistribuye
2. **Estado estable**: Equilibrio alcanzado después del transitorio
3. **τ**: Mide qué tan rápido el sistema alcanza el estado estable

## Conceptos Clave
- Natural: debido a energía almacenada
- Forzada: debido a fuentes externas
- Completa = Natural + Forzada
