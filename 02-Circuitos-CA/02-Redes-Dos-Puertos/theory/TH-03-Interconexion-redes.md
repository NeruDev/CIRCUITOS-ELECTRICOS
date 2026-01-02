# TH-03: Interconexión de Redes de Dos Puertos

## Objetivos
- Analizar conexiones serie, paralelo y cascada
- Calcular parámetros equivalentes de redes interconectadas
- Identificar el tipo de conexión apropiado

## Contenido

### Tipos de Interconexión

Las redes de dos puertos se pueden conectar de diferentes formas, y cada tipo de conexión tiene parámetros asociados óptimos.

### Conexión en Serie

Los puertos de entrada están en serie y los de salida también.

```
   ┌──────┐
──┤  Na   ├──
  └──────┘
   ┌──────┐
──┤  Nb   ├──
  └──────┘
```

**Parámetros resultantes (z):**
$$[\mathbf{z}] = [\mathbf{z}_a] + [\mathbf{z}_b]$$

$$z_{ij} = z_{aij} + z_{bij}$$

### Conexión en Paralelo

Los puertos de entrada están en paralelo y los de salida también.

```
   ┌──────┐
├──┤  Na   ├──┤
│  └──────┘  │
│  ┌──────┐  │
├──┤  Nb   ├──┤
   └──────┘
```

**Parámetros resultantes (y):**
$$[\mathbf{y}] = [\mathbf{y}_a] + [\mathbf{y}_b]$$

$$y_{ij} = y_{aij} + y_{bij}$$

### Conexión Serie-Paralelo

Entrada en serie, salida en paralelo.

**Parámetros resultantes (h):**
$$[\mathbf{h}] = [\mathbf{h}_a] + [\mathbf{h}_b]$$

### Conexión Paralelo-Serie

Entrada en paralelo, salida en serie.

**Parámetros resultantes (g):**
$$[\mathbf{g}] = [\mathbf{g}_a] + [\mathbf{g}_b]$$

### Conexión en Cascada

La salida de una red se conecta a la entrada de la siguiente.

```
   ┌──────┐   ┌──────┐
──┤  Na   ├───┤  Nb   ├──
  └──────┘   └──────┘
```

**Parámetros resultantes (ABCD):**
$$[\mathbf{T}] = [\mathbf{T}_a] \cdot [\mathbf{T}_b]$$

$$\begin{bmatrix} A & B \\ C & D \end{bmatrix} = \begin{bmatrix} A_a & B_a \\ C_a & D_a \end{bmatrix} \begin{bmatrix} A_b & B_b \\ C_b & D_b \end{bmatrix}$$

**Nota:** El orden de multiplicación importa (matrices no conmutan).

### Resumen de Interconexiones

| Conexión | Parámetros | Operación |
|----------|------------|-----------|
| Serie-Serie | z | Suma |
| Paralelo-Paralelo | y | Suma |
| Serie-Paralelo | h | Suma |
| Paralelo-Serie | g | Suma |
| Cascada | T (ABCD) | Multiplicación |

### Validez de las Conexiones

⚠️ **Importante:** No todas las conexiones son válidas para cualquier red.

**Condición de validez:** Los puertos deben mantener la condición de puerto (la [corriente](../../../glossary.md#corriente) que entra por un terminal debe ser igual a la que sale por el otro terminal del mismo puerto).

Algunas interconexiones pueden violar esta condición y requerir transformadores de aislamiento.

### Ejemplo: Cascada de Dos Redes T

**Red T con Z₁ = Z₂ = 10Ω, Z₃ = 20Ω**

Parámetros ABCD de una red T:
- A = 1 + Z₁/Z₃ = 1 + 10/20 = 1.5
- B = Z₁ + Z₂ + Z₁Z₂/Z₃ = 10 + 10 + 100/20 = 25Ω
- C = 1/Z₃ = 1/20 = 0.05 S
- D = 1 + Z₂/Z₃ = 1.5

**Cascada de dos redes iguales:**
$$[\mathbf{T}_{total}] = [\mathbf{T}]^2$$

$$\begin{bmatrix} A_{eq} & B_{eq} \\ C_{eq} & D_{eq} \end{bmatrix} = \begin{bmatrix} 1.5 & 25 \\ 0.05 & 1.5 \end{bmatrix}^2$$

$$= \begin{bmatrix} 3.5 & 75 \\ 0.15 & 3.5 \end{bmatrix}$$

### Aplicaciones

1. **Líneas de transmisión:** Modeladas como cascada de secciones
2. **Filtros:** Diseño por secciones en cascada
3. **Amplificadores:** Etapas en cascada
4. **Redes de adaptación:** Múltiples secciones

## Conceptos Clave
- Serie: sumar z
- Paralelo: sumar y
- Cascada: multiplicar ABCD
- Verificar validez de la conexión
