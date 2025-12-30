# Resumen de Fórmulas - Circuitos Acoplados Magnéticamente

## Inductancia Mutua

$$M = k\sqrt{L_1 L_2}$$

**Coeficiente de acoplamiento:**
$$0 \leq k \leq 1$$

## Ecuaciones de Voltaje

$$v_1 = L_1\frac{di_1}{dt} \pm M\frac{di_2}{dt}$$
$$v_2 = L_2\frac{di_2}{dt} \pm M\frac{di_1}{dt}$$

**Forma fasorial:**
$$\mathbf{V}_1 = j\omega L_1 \mathbf{I}_1 \pm j\omega M \mathbf{I}_2$$
$$\mathbf{V}_2 = j\omega L_2 \mathbf{I}_2 \pm j\omega M \mathbf{I}_1$$

## Convención del Punto

- (+) cuando ambas corrientes entran (o salen) por los puntos
- (-) cuando una entra y otra sale

## Circuito Equivalente T

```
   L₁-M      L₂-M
──⌇⌇⌇──┬──⌇⌇⌇──
       │
       M
```

- La = L₁ - M
- Lb = L₂ - M
- Lc = M

## Energía Almacenada

$$W = \frac{1}{2}L_1 i_1^2 + \frac{1}{2}L_2 i_2^2 \pm M i_1 i_2$$

## Transformador Ideal

**Relación de vueltas:**
$$n = \frac{N_2}{N_1}$$

**Relaciones de voltaje y corriente:**
$$\frac{V_2}{V_1} = n$$
$$\frac{I_1}{I_2} = n$$

**Impedancia reflejada:**
$$Z_{reflejada} = \frac{Z_L}{n^2}$$

**Potencia:**
$$P_1 = P_2$$

## Adaptación de Impedancias

$$n_{óptimo} = \sqrt{\frac{Z_L}{Z_s}}$$

## Tipos de Transformador

| Tipo | n | Voltaje | Corriente |
|------|---|---------|-----------|
| Elevador | n > 1 | Aumenta | Disminuye |
| Reductor | n < 1 | Disminuye | Aumenta |
