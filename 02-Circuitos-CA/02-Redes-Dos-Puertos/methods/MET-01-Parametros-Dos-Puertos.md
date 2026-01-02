# MET-01: Método de Parámetros de Redes de Dos Puertos

## Descripción del Método

Una **red de dos puertos** es un [circuito](../../../glossary.md#circuito) con dos pares de terminales: un puerto de entrada y uno de salida. Los parámetros de dos puertos relacionan los voltajes y corrientes de ambos puertos mediante matrices.

---

## Variables de la Red

```
     I₁ →              ← I₂
    ●────────┬────────┬────────●
    +        │        │        +
   V₁      ┌─┴────────┴─┐     V₂
    -      │  Red de 2  │      -
    ●──────┤   Puertos  ├──────●
           └────────────┘
```

Convención:
- $I_1$ entra al puerto 1
- $I_2$ sale del puerto 2 (a veces se define entrando)

---

## Tipos de Parámetros

### Parámetros Z (Impedancia)
$$\begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} Z_{11} & Z_{12} \\ Z_{21} & Z_{22} \end{bmatrix} \begin{bmatrix} I_1 \\ I_2 \end{bmatrix}$$

### Parámetros Y (Admitancia)
$$\begin{bmatrix} I_1 \\ I_2 \end{bmatrix} = \begin{bmatrix} Y_{11} & Y_{12} \\ Y_{21} & Y_{22} \end{bmatrix} \begin{bmatrix} V_1 \\ V_2 \end{bmatrix}$$

### Parámetros ABCD (Transmisión)
$$\begin{bmatrix} V_1 \\ I_1 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} V_2 \\ -I_2 \end{bmatrix}$$

### Parámetros h (Híbridos)
$$\begin{bmatrix} V_1 \\ I_2 \end{bmatrix} = \begin{bmatrix} h_{11} & h_{12} \\ h_{21} & h_{22} \end{bmatrix} \begin{bmatrix} I_1 \\ V_2 \end{bmatrix}$$

---

## Métodos para Encontrar Parámetros Z

### Definiciones
$$Z_{11} = \frac{V_1}{I_1}\bigg|_{I_2=0} \quad \text{(puerto 2 abierto)}$$
$$Z_{12} = \frac{V_1}{I_2}\bigg|_{I_1=0} \quad \text{(puerto 1 abierto)}$$
$$Z_{21} = \frac{V_2}{I_1}\bigg|_{I_2=0} \quad \text{(puerto 2 abierto)}$$
$$Z_{22} = \frac{V_2}{I_2}\bigg|_{I_1=0} \quad \text{(puerto 1 abierto)}$$

### Procedimiento
1. Abrir puerto 2 (I₂ = 0), aplicar fuente en puerto 1
2. Medir/calcular V₁ y V₂ → Z₁₁ = V₁/I₁, Z₂₁ = V₂/I₁
3. Abrir puerto 1 (I₁ = 0), aplicar fuente en puerto 2
4. Medir/calcular V₁ y V₂ → Z₁₂ = V₁/I₂, Z₂₂ = V₂/I₂

---

## Métodos para Encontrar Parámetros Y

### Definiciones
$$Y_{11} = \frac{I_1}{V_1}\bigg|_{V_2=0} \quad \text{(puerto 2 en corto)}$$
$$Y_{12} = \frac{I_1}{V_2}\bigg|_{V_1=0} \quad \text{(puerto 1 en corto)}$$
$$Y_{21} = \frac{I_2}{V_1}\bigg|_{V_2=0} \quad \text{(puerto 2 en corto)}$$
$$Y_{22} = \frac{I_2}{V_2}\bigg|_{V_1=0} \quad \text{(puerto 1 en corto)}$$

### Procedimiento
1. Cortocircuitar puerto 2 (V₂ = 0), aplicar fuente en puerto 1
2. Medir/calcular I₁ e I₂ → Y₁₁ = I₁/V₁, Y₂₁ = I₂/V₁
3. Cortocircuitar puerto 1 (V₁ = 0), aplicar fuente en puerto 2
4. Medir/calcular I₁ e I₂ → Y₁₂ = I₁/V₂, Y₂₂ = I₂/V₂

---

## Ejemplo Clásico 1: Parámetros Z de Red en T

### Enunciado
Encuentre los parámetros Z de la red en T mostrada.

### Diagrama
```
     I₁ →      Z₁        Z₂      ← I₂
    ●────────/\/\/──┬──/\/\/────────●
    +               │               +
   V₁             ┌─┴─┐            V₂
    -             │Z₃ │             -
    ●─────────────┴───┴─────────────●
```

Con: Z₁ = 10 Ω, Z₂ = 20 Ω, Z₃ = 30 Ω

### Solución

#### **Método 1: Por definición**

**Con I₂ = 0 (puerto 2 abierto):**
```
     I₁ →      10Ω       20Ω      
    ●────────/\/\/──┬──/\/\/────○ (abierto)
    +               │               
   V₁             ┌─┴─┐            V₂
    -             │30Ω│             
    ●─────────────┴───┴─────────────●
```

$$V_1 = I_1(Z_1 + Z_3) = I_1(10 + 30) = 40I_1$$
$$Z_{11} = \frac{V_1}{I_1} = 40\text{ Ω}$$

$$V_2 = I_1 \cdot Z_3 = 30I_1$$
$$Z_{21} = \frac{V_2}{I_1} = 30\text{ Ω}$$

**Con I₁ = 0 (puerto 1 abierto):**
$$V_2 = I_2(Z_2 + Z_3) = I_2(20 + 30) = 50I_2$$
$$Z_{22} = \frac{V_2}{I_2} = 50\text{ Ω}$$

$$V_1 = I_2 \cdot Z_3 = 30I_2$$
$$Z_{12} = \frac{V_1}{I_2} = 30\text{ Ω}$$

#### **Método 2: Fórmula directa para red T**
Para redes en T:
$$Z_{11} = Z_1 + Z_3$$
$$Z_{12} = Z_{21} = Z_3$$
$$Z_{22} = Z_2 + Z_3$$

### Respuesta
$$\boxed{[Z] = \begin{bmatrix} 40 & 30 \\ 30 & 50 \end{bmatrix}\text{ Ω}}$$

### Explicación
La red es recíproca (Z₁₂ = Z₂₁) porque no contiene fuentes dependientes ni elementos no lineales. Z₃ aparece como el término de acoplamiento porque es el elemento común a ambos puertos.

---

## Ejemplo Clásico 2: Parámetros Y de Red en π

### Enunciado
Encuentre los parámetros Y de la red en π mostrada.

### Diagrama
```
     I₁ →           Yb           ← I₂
    ●────────┬────/\/\/\/────┬────────●
    +        │               │        +
   V₁      ┌─┴─┐           ┌─┴─┐     V₂
    -      │Ya │           │Yc │      -
    ●──────┴───┴───────────┴───┴──────●
```

Con: Ya = 0.1 S, Yb = 0.05 S, Yc = 0.2 S

### Solución

#### **Con V₂ = 0 (puerto 2 en corto):**
Por [LCK](../../../glossary.md#lck) en [nodo](../../../glossary.md#nodo) izquierdo:
$$I_1 = V_1(Y_a + Y_b) = V_1(0.1 + 0.05) = 0.15V_1$$
$$Y_{11} = \frac{I_1}{V_1} = 0.15\text{ S}$$

Por LCK en nodo derecho (V₂ = 0):
$$I_2 = -V_1 \cdot Y_b = -0.05V_1$$
$$Y_{21} = \frac{I_2}{V_1} = -0.05\text{ S}$$

#### **Con V₁ = 0 (puerto 1 en corto):**
$$I_2 = V_2(Y_b + Y_c) = V_2(0.05 + 0.2) = 0.25V_2$$
$$Y_{22} = \frac{I_2}{V_2} = 0.25\text{ S}$$

$$I_1 = -V_2 \cdot Y_b = -0.05V_2$$
$$Y_{12} = \frac{I_1}{V_2} = -0.05\text{ S}$$

#### **Fórmula directa para red π**
$$Y_{11} = Y_a + Y_b$$
$$Y_{12} = Y_{21} = -Y_b$$
$$Y_{22} = Y_b + Y_c$$

### Respuesta
$$\boxed{[Y] = \begin{bmatrix} 0.15 & -0.05 \\ -0.05 & 0.25 \end{bmatrix}\text{ S}}$$

### Explicación
Los signos negativos en Y₁₂ e Y₂₁ indican que la [corriente](../../../glossary.md#corriente) en un puerto fluye en dirección opuesta cuando se excita el otro puerto.

---

## Ejemplo Clásico 3: Parámetros ABCD en Cascada

### Enunciado
Dos redes de dos puertos están conectadas en cascada. Encuentre los parámetros ABCD totales.

Red 1: $[ABCD]_1 = \begin{bmatrix} 1 & 10 \\ 0 & 1 \end{bmatrix}$ ([Impedancia](../../../glossary.md#impedancia) serie)

Red 2: $[ABCD]_2 = \begin{bmatrix} 1 & 0 \\ 0.1 & 1 \end{bmatrix}$ ([Admitancia](../../../glossary.md#admitancia) paralelo)

### Diagrama
```
●────[ Red 1 ]────[ Red 2 ]────●
│                              │
●──────────────────────────────●
```

### Solución

#### **Propiedad de cascada**
Para redes en cascada:
$$[ABCD]_{total} = [ABCD]_1 \times [ABCD]_2$$

#### **Multiplicación de matrices**
$$[ABCD]_{total} = \begin{bmatrix} 1 & 10 \\ 0 & 1 \end{bmatrix} \times \begin{bmatrix} 1 & 0 \\ 0.1 & 1 \end{bmatrix}$$

$$= \begin{bmatrix} 1(1) + 10(0.1) & 1(0) + 10(1) \\ 0(1) + 1(0.1) & 0(0) + 1(1) \end{bmatrix}$$

$$= \begin{bmatrix} 1 + 1 & 0 + 10 \\ 0 + 0.1 & 0 + 1 \end{bmatrix}$$

$$= \begin{bmatrix} 2 & 10 \\ 0.1 & 1 \end{bmatrix}$$

### Verificación
Para una red válida: $AD - BC = 1$
$$2(1) - 10(0.1) = 2 - 1 = 1$$ ✓

### Respuesta
$$\boxed{[ABCD]_{total} = \begin{bmatrix} 2 & 10 \\ 0.1 & 1 \end{bmatrix}}$$

### Explicación
Los parámetros ABCD son especialmente útiles para redes en cascada porque la matriz total es simplemente el producto de las matrices individuales. Esto simplifica enormemente el análisis de líneas de transmisión y filtros.

---

## Conversión entre Parámetros

### Z a Y
$$[Y] = [Z]^{-1}$$

### Z a ABCD
$$A = \frac{Z_{11}}{Z_{21}}, \quad B = \frac{\Delta_Z}{Z_{21}}, \quad C = \frac{1}{Z_{21}}, \quad D = \frac{Z_{22}}{Z_{21}}$$

donde $\Delta_Z = Z_{11}Z_{22} - Z_{12}Z_{21}$

### Y a Z
$$[Z] = [Y]^{-1}$$

### ABCD a Z
$$Z_{11} = \frac{A}{C}, \quad Z_{12} = \frac{\Delta_{ABCD}}{C}, \quad Z_{21} = \frac{1}{C}, \quad Z_{22} = \frac{D}{C}$$

donde $\Delta_{ABCD} = AD - BC$

---

## Redes Especiales

### Red Simétrica
$$Z_{11} = Z_{22}$$ o $$A = D$$

### Red Recíproca
$$Z_{12} = Z_{21}$$ o $$AD - BC = 1$$

### Red Sin Pérdidas (Reactiva)
Todos los elementos Z o Y son imaginarios puros.

---

## Resumen de Fórmulas para Redes Básicas

| Red | Parámetros ABCD |
|-----|-----------------|
| Impedancia serie Z | $\begin{bmatrix} 1 & Z \\ 0 & 1 \end{bmatrix}$ |
| Admitancia paralelo Y | $\begin{bmatrix} 1 & 0 \\ Y & 1 \end{bmatrix}$ |
| Transformador ideal n:1 | $\begin{bmatrix} n & 0 \\ 0 & 1/n \end{bmatrix}$ |
| Línea de transmisión | $\begin{bmatrix} \cosh\gamma l & Z_0\sinh\gamma l \\ \sinh\gamma l/Z_0 & \cosh\gamma l \end{bmatrix}$ |

## Errores Comunes
1. Confundir la convención de dirección de I₂
2. Olvidar que Y = Z⁻¹ requiere invertir la matriz, no los elementos individuales
3. No verificar la condición AD - BC = 1 para redes recíprocas
4. Multiplicar matrices ABCD en orden incorrecto para cascada
