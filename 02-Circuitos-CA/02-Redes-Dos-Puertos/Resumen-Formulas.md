# Resumen de Fórmulas - Redes de Dos Puertos

## Parámetros de Impedancia (z)

$$\begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} z_{11} & z_{12} \\ z_{21} & z_{22} \end{bmatrix} \begin{bmatrix} I_1 \\ I_2 \end{bmatrix}$$

- $z_{11} = V_1/I_1|_{I_2=0}$
- $z_{22} = V_2/I_2|_{I_1=0}$
- $z_{12} = V_1/I_2|_{I_1=0}$
- $z_{21} = V_2/I_1|_{I_2=0}$

## Parámetros de Admitancia (y)

$$\begin{bmatrix} I_1 \\ I_2 \end{bmatrix} = \begin{bmatrix} y_{11} & y_{12} \\ y_{21} & y_{22} \end{bmatrix} \begin{bmatrix} V_1 \\ V_2 \end{bmatrix}$$

- $y_{11} = I_1/V_1|_{V_2=0}$
- $y_{22} = I_2/V_2|_{V_1=0}$

## Parámetros Híbridos (h)

$$\begin{bmatrix} V_1 \\ I_2 \end{bmatrix} = \begin{bmatrix} h_{11} & h_{12} \\ h_{21} & h_{22} \end{bmatrix} \begin{bmatrix} I_1 \\ V_2 \end{bmatrix}$$

## Parámetros de Transmisión (ABCD)

$$\begin{bmatrix} V_1 \\ I_1 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} V_2 \\ -I_2 \end{bmatrix}$$

## Conversiones

**z ↔ y:**
$$[y] = [z]^{-1}$$

**Determinante:**
$$\Delta_z = z_{11}z_{22} - z_{12}z_{21}$$

## Redes Recíprocas

- $z_{12} = z_{21}$
- $y_{12} = y_{21}$
- $h_{12} = -h_{21}$
- $AD - BC = 1$

## Redes Simétricas

- $z_{11} = z_{22}$
- $y_{11} = y_{22}$
- $A = D$

## Interconexiones

| Tipo | Parámetros | Operación |
|------|------------|-----------|
| Serie | z | $[z] = [z_a] + [z_b]$ |
| Paralelo | y | $[y] = [y_a] + [y_b]$ |
| Cascada | ABCD | $[T] = [T_a][T_b]$ |

## Red T (Parámetros z)

```
    Z₁       Z₂
○──⬚───┬───⬚───○
       │
      Z₃
```

- $z_{11} = Z_1 + Z_3$
- $z_{22} = Z_2 + Z_3$
- $z_{12} = z_{21} = Z_3$

## Red π (Parámetros y)

```
○──┬───⬚───┬──○
   │   Z₃   │
  Z₁       Z₂
   │        │
○──┴────────┴──○
```

- $y_{11} = 1/Z_1 + 1/Z_3$
- $y_{22} = 1/Z_2 + 1/Z_3$
- $y_{12} = y_{21} = -1/Z_3$
