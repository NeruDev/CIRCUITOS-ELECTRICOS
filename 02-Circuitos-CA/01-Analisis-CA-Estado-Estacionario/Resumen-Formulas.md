# Resumen de Fórmulas - Análisis CA en Estado Estacionario

## Onda Senoidal

$$v(t) = V_m \sin(\omega t + \phi)$$

| Parámetro | Fórmula |
|-----------|---------|
| Frecuencia angular | ω = 2πf |
| Período | T = 1/f = 2π/ω |
| Frecuencia | f = 1/T = ω/(2π) |

## Valores Eficaces (RMS)

$$V_{rms} = \frac{V_m}{\sqrt{2}}$$
$$I_{rms} = \frac{I_m}{\sqrt{2}}$$

## Números Complejos

**Rectangular a Polar:**
$$r = \sqrt{a^2 + b^2}$$
$$\theta = \arctan(b/a)$$

**Polar a Rectangular:**
$$a = r\cos\theta$$
$$b = r\sin\theta$$

**Operaciones:**
- Suma: $(a_1 + jb_1) + (a_2 + jb_2) = (a_1+a_2) + j(b_1+b_2)$
- Multiplicación: $r_1\angle\theta_1 \cdot r_2\angle\theta_2 = r_1r_2\angle(\theta_1+\theta_2)$
- División: $\frac{r_1\angle\theta_1}{r_2\angle\theta_2} = \frac{r_1}{r_2}\angle(\theta_1-\theta_2)$

## Impedancias

| Elemento | Z | Magnitud | θ |
|----------|---|----------|---|
| Resistor | R | R | 0° |
| Inductor | jωL | ωL | 90° |
| Capacitor | 1/(jωC) = -j/(ωC) | 1/(ωC) | -90° |

**Impedancia general:**
$$\mathbf{Z} = R + jX = |Z|\angle\theta$$

## Admitancias

$$\mathbf{Y} = \frac{1}{\mathbf{Z}} = G + jB$$

| Elemento | Y |
|----------|---|
| Resistor | 1/R = G |
| Inductor | 1/(jωL) = -j/(ωL) |
| Capacitor | jωC |

## Ley de Ohm Fasorial

$$\mathbf{V} = \mathbf{Z} \cdot \mathbf{I}$$

## Potencia

$$P = V_{rms} I_{rms} \cos\theta$$
$$pf = \cos\theta$$

## Thévenin y Norton

$$\mathbf{V}_{th} = \mathbf{V}_{circuito\ abierto}$$
$$\mathbf{Z}_{th} = \mathbf{Z}_{vista\ con\ fuentes\ apagadas}$$
$$\mathbf{I}_N = \frac{\mathbf{V}_{th}}{\mathbf{Z}_{th}}$$

## Máxima Transferencia de Potencia

$$\mathbf{Z}_L = \mathbf{Z}_{th}^*$$
$$P_{max} = \frac{|\mathbf{V}_{th}|^2}{8R_{th}}$$
