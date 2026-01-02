# TH-02: Parámetros z, y, h, T

## Objetivos
- Definir y calcular cada tipo de parámetro
- Interpretar físicamente cada parámetro
- Convertir entre diferentes tipos de parámetros

## Contenido

### Parámetros de Impedancia (z)

$$\begin{bmatrix} \mathbf{V}_1 \\ \mathbf{V}_2 \end{bmatrix} = \begin{bmatrix} z_{11} & z_{12} \\ z_{21} & z_{22} \end{bmatrix} \begin{bmatrix} \mathbf{I}_1 \\ \mathbf{I}_2 \end{bmatrix}$$

**Definiciones:**
- $z_{11} = \frac{V_1}{I_1}\bigg|_{I_2=0}$ (impedancia de entrada con salida abierta)
- $z_{12} = \frac{V_1}{I_2}\bigg|_{I_1=0}$ (impedancia de transferencia inversa)
- $z_{21} = \frac{V_2}{I_1}\bigg|_{I_2=0}$ (impedancia de transferencia directa)
- $z_{22} = \frac{V_2}{I_2}\bigg|_{I_1=0}$ (impedancia de salida con entrada abierta)

### Parámetros de Admitancia (y)

$$\begin{bmatrix} \mathbf{I}_1 \\ \mathbf{I}_2 \end{bmatrix} = \begin{bmatrix} y_{11} & y_{12} \\ y_{21} & y_{22} \end{bmatrix} \begin{bmatrix} \mathbf{V}_1 \\ \mathbf{V}_2 \end{bmatrix}$$

**Definiciones:**
- $y_{11} = \frac{I_1}{V_1}\bigg|_{V_2=0}$ ([admitancia](../../../glossary.md#admitancia) de entrada con salida en corto)
- $y_{12} = \frac{I_1}{V_2}\bigg|_{V_1=0}$ (admitancia de transferencia inversa)
- $y_{21} = \frac{I_2}{V_1}\bigg|_{V_2=0}$ (admitancia de transferencia directa)
- $y_{22} = \frac{I_2}{V_2}\bigg|_{V_1=0}$ (admitancia de salida con entrada en corto)

### Parámetros Híbridos (h)

$$\begin{bmatrix} \mathbf{V}_1 \\ \mathbf{I}_2 \end{bmatrix} = \begin{bmatrix} h_{11} & h_{12} \\ h_{21} & h_{22} \end{bmatrix} \begin{bmatrix} \mathbf{I}_1 \\ \mathbf{V}_2 \end{bmatrix}$$

**Definiciones:**
- $h_{11} = \frac{V_1}{I_1}\bigg|_{V_2=0}$ (impedancia de entrada con salida en corto)
- $h_{12} = \frac{V_1}{V_2}\bigg|_{I_1=0}$ (ganancia de voltaje inversa)
- $h_{21} = \frac{I_2}{I_1}\bigg|_{V_2=0}$ (ganancia de corriente directa)
- $h_{22} = \frac{I_2}{V_2}\bigg|_{I_1=0}$ (admitancia de salida)

**Aplicación:** Muy usados en análisis de transistores BJT.

### Parámetros de Transmisión (ABCD o T)

$$\begin{bmatrix} \mathbf{V}_1 \\ \mathbf{I}_1 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} \mathbf{V}_2 \\ -\mathbf{I}_2 \end{bmatrix}$$

**Definiciones:**
- $A = \frac{V_1}{V_2}\bigg|_{I_2=0}$ (ganancia de [voltaje](../../../glossary.md#voltaje) inversa, salida abierta)
- $B = -\frac{V_1}{I_2}\bigg|_{V_2=0}$ ([impedancia](../../../glossary.md#impedancia) de transferencia)
- $C = \frac{I_1}{V_2}\bigg|_{I_2=0}$ (admitancia de transferencia)
- $D = -\frac{I_1}{I_2}\bigg|_{V_2=0}$ (ganancia de [corriente](../../../glossary.md#corriente) inversa)

**Aplicación:** Análisis de redes en cascada.

### Conversión entre Parámetros

**De z a y:**
$$[\mathbf{y}] = [\mathbf{z}]^{-1}$$

$$\begin{bmatrix} y_{11} & y_{12} \\ y_{21} & y_{22} \end{bmatrix} = \frac{1}{\Delta_z}\begin{bmatrix} z_{22} & -z_{12} \\ -z_{21} & z_{11} \end{bmatrix}$$

donde $\Delta_z = z_{11}z_{22} - z_{12}z_{21}$

### Tabla de Conversión Resumida

| De \ A | z | y | ABCD |
|--------|---|---|------|
| z | - | z⁻¹ | ... |
| y | y⁻¹ | - | ... |
| ABCD | ... | ... | - |

### Ejemplo: Red T

```
    Z₁       Z₂
○──⬚───┬───⬚───○
       │
      Z₃
       │
○──────┴───────○
```

**Parámetros z:**
- z₁₁ = Z₁ + Z₃
- z₁₂ = z₂₁ = Z₃
- z₂₂ = Z₂ + Z₃

## Conceptos Clave
- z: condiciones de [circuito](../../../glossary.md#circuito) abierto
- y: condiciones de cortocircuito
- h: mezclado, útil para transistores
- T: útil para cascada
