# Resumen de Fórmulas - Conceptos y Leyes Fundamentales

## Variables Básicas

| Magnitud | Símbolo | Unidad | Fórmula |
|----------|---------|--------|---------|
| Carga | Q, q | Coulomb (C) | q = ∫i dt |
| Corriente | I, i | Ampere (A) | i = dq/dt |
| Voltaje | V, v | Volt (V) | v = dw/dq |
| Potencia | P, p | Watt (W) | p = vi |
| Energía | W, w | Joule (J) | w = ∫p dt |

## Ley de Ohm

$$v = iR$$
$$i = \frac{v}{R}$$
$$R = \frac{v}{i}$$

**Potencia en resistor:**
$$p = vi = i^2R = \frac{v^2}{R}$$

## Leyes de Kirchhoff

**Ley de Corrientes (LCK):**
$$\sum_{k=1}^{n} i_k = 0$$

**Ley de Voltajes (LVK):**
$$\sum_{k=1}^{n} v_k = 0$$

## Resistencias

**Serie:**
$$R_{eq} = R_1 + R_2 + ... + R_n$$

**Paralelo:**
$$\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + ... + \frac{1}{R_n}$$

**Dos resistencias en paralelo:**
$$R_{eq} = \frac{R_1 \cdot R_2}{R_1 + R_2}$$

## Transformación Delta-Estrella

**De Δ a Y:**
$$R_1 = \frac{R_a R_b}{R_a + R_b + R_c}$$
$$R_2 = \frac{R_b R_c}{R_a + R_b + R_c}$$
$$R_3 = \frac{R_a R_c}{R_a + R_b + R_c}$$

**De Y a Δ:**
$$R_a = \frac{R_1 R_2 + R_2 R_3 + R_1 R_3}{R_3}$$

## Divisores

**Divisor de tensión:**
$$v_k = V_s \cdot \frac{R_k}{R_{total}}$$

**Divisor de corriente (dos resistencias):**
$$i_1 = I_s \cdot \frac{R_2}{R_1 + R_2}$$
$$i_2 = I_s \cdot \frac{R_1}{R_1 + R_2}$$

## Transformación de Fuentes

$$I_s = \frac{V_s}{R_s}$$
$$V_s = I_s \cdot R_s$$
