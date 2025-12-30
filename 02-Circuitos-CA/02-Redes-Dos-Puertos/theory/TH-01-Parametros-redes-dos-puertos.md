# TH-01: Parámetros de Redes de Dos Puertos

## Objetivos
- Definir qué es una red de dos puertos
- Establecer las relaciones entre variables de puerto
- Introducir los diferentes tipos de parámetros

## Contenido

### Red de Dos Puertos

Una **red de dos puertos** es un circuito eléctrico con dos pares de terminales (puertos) para conexión externa.

```
        ┌─────────────────┐
   I₁ →─┤                 ├─→ I₂
        │                 │
   V₁   │   Red de dos    │   V₂
        │    puertos      │
   ← ───┤                 ├──── ←
        └─────────────────┘
    Puerto 1           Puerto 2
```

### Convención de Variables

- **Puerto 1 (entrada):** V₁, I₁
- **Puerto 2 (salida):** V₂, I₂
- La corriente que entra por cada terminal superior es positiva

### Conjuntos de Parámetros

Hay cuatro variables: V₁, V₂, I₁, I₂

Se pueden elegir dos como **variables independientes** y dos como **dependientes**, dando lugar a diferentes conjuntos de parámetros:

| Parámetros | Variables independientes | Variables dependientes |
|------------|--------------------------|------------------------|
| z (impedancia) | I₁, I₂ | V₁, V₂ |
| y (admitancia) | V₁, V₂ | I₁, I₂ |
| h (híbridos) | I₁, V₂ | V₁, I₂ |
| g (híbridos inversos) | V₁, I₂ | I₁, V₂ |
| T (transmisión) | V₂, I₂ | V₁, I₁ |
| T' (transmisión inversos) | V₁, I₁ | V₂, I₂ |

### Representación Matricial General

$$\begin{bmatrix} \text{dep}_1 \\ \text{dep}_2 \end{bmatrix} = \begin{bmatrix} p_{11} & p_{12} \\ p_{21} & p_{22} \end{bmatrix} \begin{bmatrix} \text{indep}_1 \\ \text{indep}_2 \end{bmatrix}$$

### Condiciones para Existencia

No todos los parámetros existen para todas las redes:
- **Parámetros z:** Existen si la red es de lazo abierto válida
- **Parámetros y:** Existen si la red es de cortocircuito válida
- **Parámetros T:** Siempre existen (excepto algunos casos especiales)

### Redes Recíprocas

Una red es **recíproca** si:
- Solo contiene elementos pasivos lineales (R, L, C, transformadores sin pérdidas)
- No tiene fuentes dependientes

Para redes recíprocas:
- z₁₂ = z₂₁
- y₁₂ = y₂₁
- h₁₂ = -h₂₁
- AD - BC = 1 (para parámetros T)

### Redes Simétricas

Una red es **simétrica** si se ve igual desde ambos puertos.

Para redes simétricas:
- z₁₁ = z₂₂
- y₁₁ = y₂₂
- A = D (para parámetros T)

### Aplicaciones

- Análisis de líneas de transmisión
- Diseño de filtros
- Caracterización de transistores
- Modelado de transformadores
- Análisis de amplificadores

## Conceptos Clave
- Cuatro variables, se eligen dos independientes
- Diferentes parámetros para diferentes aplicaciones
- Reciprocidad y simetría simplifican análisis
