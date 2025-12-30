# Resumen de Fórmulas - Teoremas de Circuitos

## Principio de Superposición

La respuesta total es la suma de las respuestas individuales:
$$v_{total} = v_1 + v_2 + ... + v_n$$
$$i_{total} = i_1 + i_2 + ... + i_n$$

**Desactivar fuentes:**
- Fuente de voltaje → Cortocircuito
- Fuente de corriente → Circuito abierto

**Nota:** No aplica para potencia.

## Teorema de Thévenin

**Voltaje de Thévenin:**
$$V_{th} = V_{circuito\ abierto}$$

**Resistencia de Thévenin:**
$$R_{th} = R_{equivalente\ con\ fuentes\ apagadas}$$

o

$$R_{th} = \frac{V_{th}}{I_{sc}}$$

## Teorema de Norton

**Corriente de Norton:**
$$I_N = I_{cortocircuito}$$

**Resistencia de Norton:**
$$R_N = R_{th}$$

## Relación Thévenin-Norton

$$V_{th} = I_N \cdot R_{th}$$
$$I_N = \frac{V_{th}}{R_{th}}$$

## Máxima Transferencia de Potencia

**Condición:**
$$R_L = R_{th}$$

**Potencia máxima:**
$$P_{max} = \frac{V_{th}^2}{4R_{th}} = \frac{I_N^2 \cdot R_{th}}{4}$$

**Eficiencia en máxima transferencia:**
$$\eta = 50\%$$

**Corriente en máxima transferencia:**
$$i = \frac{V_{th}}{2R_{th}}$$

## Teorema de Reciprocidad

Para circuitos lineales, bilaterales, sin fuentes dependientes:

Si V en posición 1 produce i en posición 2, entonces V en posición 2 produce la misma i en posición 1.

**Implicaciones en parámetros:**
- z₁₂ = z₂₁
- y₁₂ = y₂₁
