# TH-02: Método de Nodos

## Objetivos
- Formular las ecuaciones del método de nodos
- Resolver circuitos usando análisis nodal
- Manejar casos especiales (supernodos)

## Contenido

### Fundamento
El método de nodos aplica la [Ley de Corrientes](../../../glossary.md#lck) de [Kirchhoff](../../../glossary.md#lvk) (LCK) en cada [nodo](../../../glossary.md#nodo), expresando las corrientes en términos de los voltajes de nodo.

### Procedimiento General

1. **Seleccionar un nodo de referencia** (tierra, 0V)
2. **Asignar voltajes** a los demás nodos (v₁, v₂, ...)
3. **Aplicar LCK** en cada nodo no referencia
4. **Expresar corrientes** usando [ley de](../../../glossary.md#ley-ohm) [Ohm](../../../glossary.md#ohm-unidad): i = (vₐ - v_b)/R
5. **Resolver** el sistema de ecuaciones

### Formulación

Para un nodo k con [voltaje](../../../glossary.md#voltaje) vₖ:
$$\sum \frac{v_k - v_j}{R_{kj}} = \sum I_{fuentes}$$

### Forma Matricial

$$\mathbf{G} \cdot \mathbf{v} = \mathbf{i}$$

Donde:
- **G** = matriz de conductancias
- **v** = vector de voltajes de nodo
- **i** = vector de corrientes de fuente

### Construcción de la Matriz G

- **Diagonal (Gₖₖ):** Suma de conductancias conectadas al nodo k
- **Fuera de diagonal (Gₖⱼ):** Negativo de la conductancia entre nodos k y j

### Caso Especial: Supernodo

Cuando una fuente de voltaje conecta dos nodos no referencia:

1. **Formar un supernodo** que englobe ambos nodos
2. **Aplicar LCK** al supernodo completo
3. **Añadir la ecuación** de restricción: vₐ - v_b = V_fuente

### Ejemplo

```
    10Ω
 ○──/\/\/──○ v₁
 │         │
12V       5Ω    ← 2A
 │         │
 ○─────────○ (ref)
```

**Ecuación en v₁:**
$$\frac{v_1 - 12}{10} + \frac{v_1 - 0}{5} = -2$$

**Simplificando:**
$$v_1(0.1 + 0.2) - 1.2 = -2$$
$$0.3v_1 = -0.8$$
$$v_1 = -2.67V$$

## Ventajas del Método de Nodos
- Menos ecuaciones cuando hay pocos nodos
- Fácil de programar
- Natural para circuitos en paralelo

## Conceptos Clave
- Selección estratégica del nodo de referencia
- Manejo de fuentes de voltaje (supernodos)
- Verificación con LCK
