# Resumen de Fórmulas - Técnicas de Análisis de Circuitos

## Topología de Redes

| Concepto | Fórmula |
|----------|---------|
| Ecuaciones LCK independientes | n - 1 |
| Ecuaciones LVK independientes | b - n + 1 |
| Ramas del árbol | n - 1 |
| Eslabones | b - (n - 1) |

Donde: b = ramas, n = nodos

## Método de Nodos

### Formulación General
$$\mathbf{G} \cdot \mathbf{v} = \mathbf{i}$$

### Matriz de Conductancias
- **Diagonal:** $G_{kk} = \sum G$ conectadas al nodo k
- **Fuera de diagonal:** $G_{kj} = -G$ entre nodos k y j

### Corriente en rama (de nodo a a b)
$$i_{ab} = \frac{v_a - v_b}{R_{ab}} = G_{ab}(v_a - v_b)$$

### Supernodo
Si fuente Vs conecta nodos a y b:
- LCK: suma de corrientes al supernodo = 0
- Restricción: $v_a - v_b = V_s$

## Método de Mallas

### Formulación General
$$\mathbf{R} \cdot \mathbf{i} = \mathbf{v}$$

### Matriz de Resistencias
- **Diagonal:** $R_{kk} = \sum R$ en la malla k
- **Fuera de diagonal:** $R_{kj} = -R$ compartida entre mallas k y j

### Corriente en rama compartida
$$i_{rama} = i_k - i_j$$

### Supermalla
Si fuente Is está en rama compartida:
- LVK: alrededor de la supermalla
- Restricción: $i_a - i_b = I_s$

## Número de Ecuaciones

| Método | Número de ecuaciones |
|--------|---------------------|
| Nodos | n - 1 |
| Mallas | b - n + 1 |

## Verificación
- Suma de potencias = 0
- LCK en cada nodo
- LVK en cada malla
