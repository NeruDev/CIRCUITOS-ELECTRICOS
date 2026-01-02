# TH-03: Circuitos Trifásicos con Cargas Desbalanceadas en Estrella y Delta

## Objetivos
- Analizar sistemas con cargas desbalanceadas
- Calcular corrientes y voltajes en sistemas no simétricos
- Aplicar métodos de análisis general

## Contenido

### Sistema Desbalanceado

Un sistema es **desbalanceado** cuando las impedancias de [carga](../../../glossary.md#carga) no son iguales:
$$Z_a \neq Z_b \neq Z_c$$

### Carga Y Desbalanceada con Neutro

```
        a──Za──┐
        b──Zb──┼──n
        c──Zc──┘
           │
         neutro
```

Con conexión de neutro, cada fase es independiente:

$$\mathbf{I}_a = \frac{\mathbf{V}_{an}}{Z_a}$$
$$\mathbf{I}_b = \frac{\mathbf{V}_{bn}}{Z_b}$$
$$\mathbf{I}_c = \frac{\mathbf{V}_{cn}}{Z_c}$$

**[Corriente](../../../glossary.md#corriente) de neutro:**
$$\mathbf{I}_n = \mathbf{I}_a + \mathbf{I}_b + \mathbf{I}_c$$

En sistemas desbalanceados, In ≠ 0.

### Carga Y Desbalanceada sin Neutro

```
        a──Za──┐
        b──Zb──┼──n' (flotante)
        c──Zc──┘
```

Sin neutro, el punto común "n'" flota y su potencial es diferente de cero.

**Análisis por nodos:**
El voltaje del punto flotante n' respecto al neutro de la fuente:

$$\mathbf{V}_{n'n} = \frac{\mathbf{V}_{an}Y_a + \mathbf{V}_{bn}Y_b + \mathbf{V}_{cn}Y_c}{Y_a + Y_b + Y_c}$$

Donde Y = 1/Z.

**Voltajes en las cargas:**
$$\mathbf{V}_{an'} = \mathbf{V}_{an} - \mathbf{V}_{n'n}$$

### Carga Δ Desbalanceada

```
    a ────Zab──── b
     \          /
      \        /
      Zca    Zbc
        \    /
         \  /
          c
```

Las corrientes de fase se calculan directamente:
$$\mathbf{I}_{ab} = \frac{\mathbf{V}_{ab}}{Z_{ab}}$$
$$\mathbf{I}_{bc} = \frac{\mathbf{V}_{bc}}{Z_{bc}}$$
$$\mathbf{I}_{ca} = \frac{\mathbf{V}_{ca}}{Z_{ca}}$$

**Corrientes de línea (por [LCK](../../../glossary.md#lck)):**
$$\mathbf{I}_a = \mathbf{I}_{ab} - \mathbf{I}_{ca}$$
$$\mathbf{I}_b = \mathbf{I}_{bc} - \mathbf{I}_{ab}$$
$$\mathbf{I}_c = \mathbf{I}_{ca} - \mathbf{I}_{bc}$$

### Método de Análisis General

Para cualquier sistema desbalanceado:
1. Convertir todas las cargas a Y si es conveniente
2. Aplicar método de nodos o mallas
3. Resolver el sistema de ecuaciones complejas

### Ejemplo: Carga Y sin Neutro

**Datos:** 
- VL = 200V (línea), secuencia abc
- Za = 10Ω, Zb = j10Ω, Zc = -j10Ω

**Voltajes de fase de la fuente:**
- Van = 200/√3∠0° = 115.5∠0° V
- Vbn = 115.5∠-120° V
- Vcn = 115.5∠120° V

**Admitancias:**
- Ya = 0.1 S
- Yb = -j0.1 S
- Yc = j0.1 S

**Voltaje del punto flotante:**
$$V_{n'n} = \frac{(115.5\angle 0°)(0.1) + (115.5\angle -120°)(-j0.1) + (115.5\angle 120°)(j0.1)}{0.1 - j0.1 + j0.1}$$

$$V_{n'n} = \frac{11.55 + j11.55 \cdot 0.866 - j0.5 \cdot 11.55 + ...}{0.1}$$

(El cálculo completo requiere operaciones con números complejos)

### Potencia en Sistemas Desbalanceados

La potencia total es la suma de las potencias de cada fase:
$$P_{total} = P_a + P_b + P_c$$
$$Q_{total} = Q_a + Q_b + Q_c$$

No se puede usar la fórmula simplificada de sistemas balanceados.

## Conceptos Clave
- Con neutro: cada fase es independiente
- Sin neutro: el punto común flota
- Potencia total = suma de potencias por fase
