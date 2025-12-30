# TH-03: Método de Mallas, Eslabones y Análisis de Lazos

## Objetivos
- Formular las ecuaciones del método de mallas
- Resolver circuitos usando análisis por mallas
- Entender el análisis de lazos con eslabones
- Manejar casos especiales (supermallas)

## Contenido

### Fundamento
El método de mallas aplica la Ley de Voltajes de Kirchhoff (LVK) alrededor de cada malla, expresando los voltajes en términos de las corrientes de malla.

### Definiciones

**Corriente de malla:** Corriente ficticia que circula alrededor de una malla.

**Malla:** Lazo que no contiene otros lazos en su interior.

### Procedimiento General

1. **Identificar las mallas** del circuito
2. **Asignar corrientes de malla** (i₁, i₂, ...)
3. **Aplicar LVK** en cada malla
4. **Expresar voltajes** usando ley de Ohm
5. **Resolver** el sistema de ecuaciones

### Formulación

Para una malla k con corriente iₖ:
$$\sum R_{malla} \cdot i_k - \sum R_{compartida} \cdot i_{adyacente} = \sum V_{fuentes}$$

### Forma Matricial

$$\mathbf{R} \cdot \mathbf{i} = \mathbf{v}$$

Donde:
- **R** = matriz de resistencias
- **i** = vector de corrientes de malla
- **v** = vector de voltajes de fuente

### Construcción de la Matriz R

- **Diagonal (Rₖₖ):** Suma de resistencias en la malla k
- **Fuera de diagonal (Rₖⱼ):** Negativo de la resistencia compartida entre mallas k y j

### Caso Especial: Supermalla

Cuando una fuente de corriente está en una rama compartida:

1. **Formar una supermalla** que evite la fuente de corriente
2. **Aplicar LVK** a la supermalla
3. **Añadir la ecuación** de restricción: iₐ - i_b = I_fuente

### Análisis de Lazos con Eslabones

**Procedimiento:**
1. Seleccionar un árbol del circuito
2. Identificar los eslabones (b - n + 1)
3. Cada eslabón define un lazo fundamental
4. Asignar corrientes de lazo
5. Aplicar LVK a cada lazo

### Ejemplo

```
    R₁=2Ω      R₂=4Ω
 ○──/\/\/──○──/\/\/──○
 │         │         │
12V  i₁   R₃=6Ω  i₂  6V
 │         │         │
 ○─────────○─────────○
```

**Malla 1:** 
$$12 - 2i_1 - 6(i_1 - i_2) = 0$$
$$12 - 8i_1 + 6i_2 = 0$$

**Malla 2:**
$$-6(i_2 - i_1) - 4i_2 - 6 = 0$$
$$6i_1 - 10i_2 = 6$$

### Comparación: Nodos vs Mallas

| Aspecto | Método de Nodos | Método de Mallas |
|---------|-----------------|------------------|
| Variables | Voltajes | Corrientes |
| Ecuaciones | n - 1 | b - n + 1 |
| Mejor para | Muchas mallas | Muchos nodos |
| Caso especial | Supernodo | Supermalla |

## Conceptos Clave
- Corrientes de malla vs corrientes de rama
- Formación de supermallas
- Relación entre eslabones y lazos independientes
