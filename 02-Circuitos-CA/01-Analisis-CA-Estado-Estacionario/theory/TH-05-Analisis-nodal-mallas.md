# TH-05: Análisis Nodal y por Mallas de Redes Eléctricas CA

## Objetivos
- Aplicar el método de nodos a circuitos CA
- Aplicar el método de mallas a circuitos CA
- Resolver sistemas de ecuaciones con números complejos

## Contenido

### Aplicación de Técnicas de Análisis en CA

Los métodos de análisis de CD se aplican directamente en CA usando:
- Fasores en lugar de valores instantáneos
- Impedancias en lugar de resistencias
- Admitancias en lugar de conductancias

### Método de Nodos en CA

**Procedimiento:**
1. Convertir todas las fuentes y elementos al dominio fasorial
2. Seleccionar nodo de referencia
3. Aplicar LCK en cada nodo usando fasores
4. Resolver el sistema de ecuaciones complejas

**Formulación:**
$$\sum \frac{\mathbf{V}_k - \mathbf{V}_j}{\mathbf{Z}_{kj}} = \sum \mathbf{I}_{fuentes}$$

En forma matricial:
$$\mathbf{Y} \cdot \mathbf{V} = \mathbf{I}$$

Donde **Y** es la matriz de admitancias (números complejos).

### Método de Mallas en CA

**Procedimiento:**
1. Convertir al dominio fasorial
2. Asignar corrientes de malla fasoriales
3. Aplicar LVK en cada malla
4. Resolver el sistema de ecuaciones complejas

**Formulación:**
$$\sum \mathbf{Z}_{malla} \cdot \mathbf{I}_k - \sum \mathbf{Z}_{compartida} \cdot \mathbf{I}_{adyacente} = \sum \mathbf{V}_{fuentes}$$

En forma matricial:
$$\mathbf{Z} \cdot \mathbf{I} = \mathbf{V}$$

### Ejemplo: Análisis Nodal

```
         Z₁=10Ω      Z₂=j10Ω
    ○──────/\/\/──┬───⌇⌇⌇───○
    │             │         │
   Vs=20∠0°     Z₃=-j5Ω    V₂
    │             │         │
    ○─────────────┴─────────○
       (ref)
```

**Ecuación en V₂:**
$$\frac{\mathbf{V}_2 - 20\angle 0°}{10} + \frac{\mathbf{V}_2}{-j5} + \frac{\mathbf{V}_2}{j10} = 0$$

$$\mathbf{V}_2\left(\frac{1}{10} + j0.2 - j0.1\right) = 2$$

$$\mathbf{V}_2(0.1 + j0.1) = 2$$

$$\mathbf{V}_2 = \frac{2}{0.1 + j0.1} = \frac{2}{0.1414\angle 45°} = 14.14\angle -45° \text{ V}$$

### Ejemplo: Análisis por Mallas

```
    Z₁=4Ω      Z₂=j3Ω
 ○──/\/\/──○───⌇⌇⌇───○
 │         │         │
Vs=10∠0°  Z₃=2Ω     │
 │   I₁    │   I₂   -j4Ω
 │         │         │
 ○─────────┴─────────○
```

**Malla 1:**
$$10\angle 0° = (4 + 2)\mathbf{I}_1 - 2\mathbf{I}_2$$

**Malla 2:**
$$0 = -2\mathbf{I}_1 + (2 + j3 - j4)\mathbf{I}_2$$
$$0 = -2\mathbf{I}_1 + (2 - j)\mathbf{I}_2$$

### Solución de Sistemas Complejos

**Método de Cramer:**
$$\mathbf{I}_k = \frac{\Delta_k}{\Delta}$$

Donde Δ y Δk son determinantes de matrices complejas.

**Usando calculadora o software:**
- MATLAB: I = Z\V
- Python con numpy: I = np.linalg.solve(Z, V)

### Consideraciones Prácticas

1. Mantener consistencia en unidades (ω fija)
2. Todas las fuentes deben tener la misma frecuencia
3. Los resultados son fasores; convertir a tiempo si se requiere

## Conceptos Clave
- Mismos métodos de CD, con cantidades complejas
- Las matrices Y y Z contienen números complejos
- Los resultados son fasores (magnitud y fase)
