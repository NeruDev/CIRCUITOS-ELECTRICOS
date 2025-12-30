# TH-01: Topología de Redes

## Objetivos
- Definir los términos topológicos básicos
- Identificar ramas, nodos, lazos y mallas
- Determinar el número de ecuaciones independientes

## Contenido

### Conceptos Topológicos

**Rama:** Camino único entre dos nodos que contiene un elemento de circuito.

**Nodo:** Punto de conexión de dos o más ramas.

**Nodo de referencia:** Nodo al que se asigna potencial cero (tierra).

**Lazo:** Cualquier trayectoria cerrada en un circuito.

**Malla:** Lazo que no contiene ningún otro lazo en su interior.

### Relaciones Topológicas

Para un circuito con:
- b = número de ramas
- n = número de nodos

**Número de ecuaciones LCK independientes:**
$$n - 1$$

**Número de ecuaciones LVK independientes (eslabones):**
$$b - (n - 1) = b - n + 1$$

**Verificación:**
$$\text{Ecuaciones totales} = (n-1) + (b-n+1) = b$$

### Árbol y Eslabones

**Árbol:** Subgrafo conectado que contiene todos los nodos pero ningún lazo.
- Un árbol tiene exactamente (n-1) ramas

**Ramas del árbol (twigs):** Las ramas que forman el árbol.

**Eslabones (links):** Las ramas que no pertenecen al árbol.
- Número de eslabones = b - (n-1)

### Ejemplo

```
     R1
  ○──/\/\/──○
  │    1    │
  R2       R3
  │         │
  ○────○────○
  2    3    
```

- Nodos (n) = 3
- Ramas (b) = 3
- Ecuaciones LCK = 3 - 1 = 2
- Ecuaciones LVK = 3 - 3 + 1 = 1

### Grafo del Circuito

El grafo representa la estructura del circuito:
- Los nodos se representan como puntos
- Las ramas se representan como líneas

## Conceptos Clave
- Nodos esenciales vs nodos no esenciales
- Selección del árbol óptimo
- Relación entre topología y ecuaciones
