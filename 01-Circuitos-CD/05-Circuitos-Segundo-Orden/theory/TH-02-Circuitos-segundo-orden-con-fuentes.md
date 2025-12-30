# TH-02: Análisis de Circuitos de Segundo Orden con Fuentes

## Objetivos
- Resolver circuitos de segundo orden con fuentes constantes
- Determinar la respuesta completa (natural + forzada)
- Aplicar el método de solución general

## Contenido

### Ecuación Diferencial con Fuente

**Forma general:**
$$\frac{d^2x}{dt^2} + 2\alpha\frac{dx}{dt} + \omega_0^2 x = f(t)$$

Para fuente constante f(t) = F:
$$\frac{d^2x}{dt^2} + 2\alpha\frac{dx}{dt} + \omega_0^2 x = F$$

### Respuesta Completa

$$x(t) = x_n(t) + x_f(t)$$

Donde:
- x_n(t) = respuesta natural (solución homogénea)
- x_f(t) = respuesta forzada (solución particular)

### Respuesta Forzada para Fuente DC

Para una fuente constante, la solución particular es constante:
$$x_f = x_{ss} = \frac{F}{\omega_0^2}$$

Este es el valor de estado estable.

### Respuesta Natural

Depende del tipo de amortiguamiento (ver TH-01):

**Sobreamortiguada (α > ω₀):**
$$x_n(t) = A_1 e^{s_1 t} + A_2 e^{s_2 t}$$

**Críticamente amortiguada (α = ω₀):**
$$x_n(t) = (A_1 + A_2 t)e^{-\alpha t}$$

**Subamortiguada (α < ω₀):**
$$x_n(t) = e^{-\alpha t}(A_1 \cos\omega_d t + A_2 \sin\omega_d t)$$

### Respuesta Completa

$$x(t) = x_{ss} + x_n(t)$$

### Procedimiento de Solución

1. **Identificar** el tipo de circuito y obtener α, ω₀

2. **Determinar** el tipo de respuesta (comparar α con ω₀)

3. **Calcular** x(∞) = valor de estado estable
   - Para DC: C = abierto, L = corto

4. **Escribir** la forma general de x(t)

5. **Encontrar** condiciones iniciales:
   - x(0⁺) (continuidad de variables de estado)
   - dx/dt|₀₊

6. **Calcular** las constantes A₁, A₂

### Condiciones Iniciales

**Para circuito serie (variable i):**
- i(0⁺) = i(0⁻) (continuidad en L)
- di/dt|₀₊ = v_L(0⁺)/L

**Para circuito paralelo (variable v):**
- v(0⁺) = v(0⁻) (continuidad en C)
- dv/dt|₀₊ = i_C(0⁺)/C

### Ejemplo: RLC Serie con Fuente DC

```
    t=0    R      L
Vs──/──/\/\/──⌇⌇⌇──┬──○
                   │
                   C
                   │
───────────────────┴──○
```

**Datos:** Vs = 12V, R = 4Ω, L = 1H, C = 0.25F
v_C(0⁻) = 0, i(0⁻) = 0

**Solución:**
1. α = R/(2L) = 4/(2×1) = 2
2. ω₀ = 1/√(LC) = 1/√(0.25) = 2
3. α = ω₀ → Críticamente amortiguada

**v_C(∞):** Divisor de voltaje con L=corto, C=abierto
v_C(∞) = Vs = 12V

**Forma de respuesta:**
$$v_C(t) = 12 + (A_1 + A_2 t)e^{-2t}$$

**Condiciones iniciales:**
- v_C(0⁺) = 0 → 12 + A₁ = 0 → A₁ = -12
- i(0⁺) = 0 → dv_C/dt|₀₊ = 0
- dv_C/dt = A₂e^{-2t} - 2(A₁ + A₂t)e^{-2t}
- En t=0: A₂ - 2A₁ = 0 → A₂ = -24

**Respuesta:**
$$v_C(t) = 12 + (-12 - 24t)e^{-2t} = 12(1 - (1 + 2t)e^{-2t}) \text{ V}$$

## Conceptos Clave
- Respuesta completa = natural + forzada
- Estado estable determinado por análisis DC
- Dos condiciones iniciales necesarias
