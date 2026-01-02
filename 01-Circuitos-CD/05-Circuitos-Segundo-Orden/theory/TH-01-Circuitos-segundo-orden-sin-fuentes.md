# TH-01: Análisis de Circuitos de Segundo Orden sin Fuentes

## Objetivos
- Formular la ecuación diferencial de segundo orden
- Identificar los tres tipos de respuesta natural
- Resolver circuitos RLC serie y paralelo sin fuentes

## Contenido

### Circuito RLC Serie sin Fuente

```
   ┌──R──L──C──┐
   │           │
   └───────────┘
```

**Ecuación diferencial:**
$$\frac{d^2i}{dt^2} + \frac{R}{L}\frac{di}{dt} + \frac{1}{LC}i = 0$$

### Circuito RLC Paralelo sin Fuente

```
   ┌──┬──┬──┐
   R  L  C  │
   └──┴──┴──┘
```

**Ecuación diferencial:**
$$\frac{d^2v}{dt^2} + \frac{1}{RC}\frac{dv}{dt} + \frac{1}{LC}v = 0$$

### Forma General

$$\frac{d^2x}{dt^2} + 2\alpha\frac{dx}{dt} + \omega_0^2 x = 0$$

### Parámetros Característicos

**Para RLC serie:**
- Factor de amortiguamiento: $\alpha = \frac{R}{2L}$
- Frecuencia de resonancia: $\omega_0 = \frac{1}{\sqrt{LC}}$

**Para RLC paralelo:**
- Factor de amortiguamiento: $\alpha = \frac{1}{2RC}$
- Frecuencia de resonancia: $\omega_0 = \frac{1}{\sqrt{LC}}$

### Ecuación Característica

$$s^2 + 2\alpha s + \omega_0^2 = 0$$

**Raíces:**
$$s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$$

### Tipos de Respuesta

#### 1. Sobreamortiguada (α > ω₀)

Raíces reales y distintas: s₁ ≠ s₂

$$x(t) = A_1 e^{s_1 t} + A_2 e^{s_2 t}$$

donde $s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$

#### 2. Críticamente Amortiguada (α = ω₀)

Raíces reales e iguales: s₁ = s₂ = -α

$$x(t) = (A_1 + A_2 t)e^{-\alpha t}$$

#### 3. Subamortiguada (α < ω₀)

Raíces complejas conjugadas:

$$s_{1,2} = -\alpha \pm j\omega_d$$

donde $\omega_d = \sqrt{\omega_0^2 - \alpha^2}$ ([frecuencia](../../../glossary.md#frecuencia) amortiguada)

$$x(t) = e^{-\alpha t}(A_1 \cos\omega_d t + A_2 \sin\omega_d t)$$

o equivalentemente:

$$x(t) = B e^{-\alpha t} \cos(\omega_d t + \phi)$$

### Determinación de Constantes

Las constantes A₁, A₂ (o B, φ) se determinan con:
1. Condición inicial: x(0)
2. Derivada inicial: dx/dt|ₜ₌₀

### Gráficas de Respuesta

```
x(t)
│
│  Subamortiguada (oscila)
│    ╭─╮
│   ╱   ╲ ╱╲
│──╱─────X───╲────── Críticamente amortiguada
│           ╲╱ ╲
│              ────── Sobreamortiguada
└──────────────────── t
```

## Conceptos Clave
- Tres tipos de respuesta según α vs ω₀
- Condiciones iniciales: x(0) y dx/dt(0)
- La respuesta depende de R, L, C
