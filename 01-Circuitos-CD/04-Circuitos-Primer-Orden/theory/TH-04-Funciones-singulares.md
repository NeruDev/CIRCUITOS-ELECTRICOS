# TH-04: Funciones Singulares

## Objetivos
- Definir y graficar funciones singulares
- Aplicar funciones singulares en análisis de circuitos
- Modelar señales de entrada con funciones singulares

## Contenido

### Función Escalón Unitario u(t)

La función escalón unitario (función de Heaviside) se define como:

$$u(t) = \begin{cases} 0 & t < 0 \\ 1 & t > 0 \end{cases}$$

**Gráfica:**
```
u(t)
│
1├────────────
│
0└────────────── t
        0
```

**Escalón desplazado:**
$$u(t-t_0) = \begin{cases} 0 & t < t_0 \\ 1 & t > t_0 \end{cases}$$

### Función Impulso Unitario δ(t)

La función impulso ([delta](../../../glossary.md#delta) de Dirac) se define como:

$$\delta(t) = \frac{du(t)}{dt}$$

**Propiedades:**
$$\delta(t) = 0, \quad t \neq 0$$
$$\int_{-\infty}^{\infty} \delta(t) \, dt = 1$$

**Propiedad de muestreo:**
$$\int_{-\infty}^{\infty} f(t)\delta(t-t_0) \, dt = f(t_0)$$

*Nota: Esta propiedad requiere que f(t) sea continua en t = t₀.*

**Gráfica:**
```
δ(t)
│
│  ↑(1)
│  │
0──┴──────────── t
   0
```

### Función Rampa Unitaria r(t)

La función rampa se define como:

$$r(t) = \int_{-\infty}^{t} u(\tau) \, d\tau = tu(t)$$

$$r(t) = \begin{cases} 0 & t < 0 \\ t & t \geq 0 \end{cases}$$

**Gráfica:**
```
r(t)
│     ╱
│   ╱
│ ╱
└────────────── t
0
```

### Relaciones entre Funciones Singulares

$$\delta(t) = \frac{du(t)}{dt}$$
$$u(t) = \frac{dr(t)}{dt}$$
$$u(t) = \int_{-\infty}^{t} \delta(\tau) \, d\tau$$
$$r(t) = \int_{-\infty}^{t} u(\tau) \, d\tau$$

### Representación de Señales

**Pulso rectangular:**
$$p(t) = u(t) - u(t-T)$$

**Señal encendida en t₀:**
$$v(t) = V_0 u(t-t_0)$$

**Señal apagada en t₀:**
$$v(t) = V_0 [1 - u(t-t_0)]$$

### Aplicación en Circuitos

Las funciones singulares modelan:
- Encendido/apagado de fuentes
- Cambios abruptos de parámetros
- Respuesta a entrada impulsiva (respuesta al impulso)

### Ejemplo

Una fuente de 10V se conecta en t = 2s:
$$v(t) = 10 \cdot u(t-2) \text{ V}$$

## Conceptos Clave
- El escalón modela conexión de fuentes
- El impulso es la derivada del escalón
- La rampa es la integral del escalón
