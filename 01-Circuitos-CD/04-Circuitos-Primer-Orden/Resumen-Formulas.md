# Resumen de Fórmulas - Circuitos de Primer Orden

## Capacitor

| Propiedad | Fórmula |
|-----------|---------|
| Relación i-v | i = C(dv/dt) |
| Voltaje | v = (1/C)∫i dt + v(t₀) |
| Energía | w = ½Cv² |
| Serie | 1/C_eq = Σ(1/Cₖ) |
| Paralelo | C_eq = ΣCₖ |

## Inductor

| Propiedad | Fórmula |
|-----------|---------|
| Relación v-i | v = L(di/dt) |
| Corriente | i = (1/L)∫v dt + i(t₀) |
| Energía | w = ½Li² |
| Serie | L_eq = ΣLₖ |
| Paralelo | 1/L_eq = Σ(1/Lₖ) |

## Constantes de Tiempo

| Circuito | τ |
|----------|---|
| RC | τ = RC |
| RL | τ = L/R |

## Respuesta de Circuitos de Primer Orden

### Fórmula General
$$x(t) = x(\infty) + [x(0^+) - x(\infty)]e^{-t/\tau}$$

### Sin Fuente (Respuesta Natural)
$$x(t) = x(0)e^{-t/\tau}$$

### Con Fuente DC (Desde cero)
$$x(t) = x(\infty)(1 - e^{-t/\tau})$$

## Funciones Singulares

| Función | Definición |
|---------|------------|
| Escalón | u(t) = 0 para t<0, 1 para t≥0 |
| Impulso | δ(t) = du(t)/dt |
| Rampa | r(t) = tu(t) |

## Relaciones

$$\delta(t) = \frac{d}{dt}u(t)$$
$$u(t) = \frac{d}{dt}r(t)$$

## Comportamiento Temporal

| Tiempo | e^(-t/τ) | 1-e^(-t/τ) |
|--------|----------|------------|
| τ | 0.368 | 0.632 |
| 2τ | 0.135 | 0.865 |
| 3τ | 0.050 | 0.950 |
| 5τ | 0.007 | 0.993 |

## Continuidad

- v_C(0⁺) = v_C(0⁻)
- i_L(0⁺) = i_L(0⁻)

## En Estado Estable (DC)

- Capacitor → Circuito abierto
- Inductor → Cortocircuito
