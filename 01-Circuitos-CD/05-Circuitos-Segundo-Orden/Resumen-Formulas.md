# Resumen de Fórmulas - Circuitos de Segundo Orden

## Parámetros Característicos

### RLC Serie
$$\alpha = \frac{R}{2L}$$
$$\omega_0 = \frac{1}{\sqrt{LC}}$$

### RLC Paralelo
$$\alpha = \frac{1}{2RC}$$
$$\omega_0 = \frac{1}{\sqrt{LC}}$$

## Ecuación Característica

$$s^2 + 2\alpha s + \omega_0^2 = 0$$

$$s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$$

## Tipos de Respuesta

| Condición | Tipo | Raíces |
|-----------|------|--------|
| α > ω₀ | Sobreamortiguada | Reales distintas |
| α = ω₀ | Críticamente amortiguada | Reales iguales |
| α < ω₀ | Subamortiguada | Complejas conjugadas |

## Formas de Respuesta Natural

### Sobreamortiguada (α > ω₀)
$$x(t) = A_1 e^{s_1 t} + A_2 e^{s_2 t}$$

### Críticamente Amortiguada (α = ω₀)
$$x(t) = (A_1 + A_2 t)e^{-\alpha t}$$

### Subamortiguada (α < ω₀)
$$x(t) = e^{-\alpha t}(A_1 \cos\omega_d t + A_2 \sin\omega_d t)$$

donde $\omega_d = \sqrt{\omega_0^2 - \alpha^2}$

## Respuesta Completa con Fuente DC

$$x(t) = x_{ss} + x_n(t)$$

## Factor de Calidad

$$Q = \frac{\omega_0}{2\alpha}$$

- Q > 0.5: Subamortiguado
- Q = 0.5: Críticamente amortiguado
- Q < 0.5: Sobreamortiguado

## Condiciones Iniciales

Para circuito serie:
- i(0⁺) = i(0⁻)
- di/dt|₀₊ = v_L(0⁺)/L

Para circuito paralelo:
- v(0⁺) = v(0⁻)
- dv/dt|₀₊ = i_C(0⁺)/C

## Relaciones Útiles

$$\omega_d = \omega_0\sqrt{1 - \zeta^2}$$

donde $\zeta = \alpha/\omega_0$ es el factor de amortiguamiento relativo.
