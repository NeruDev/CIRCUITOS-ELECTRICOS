# TH-02: Autoinducción, Inducción Mutua y Acoplamiento Magnético

## Objetivos
- Definir [inductancia](../../../glossary.md#inductancia) propia y mutua
- Calcular el coeficiente de acoplamiento
- Aplicar la convención del punto

## Contenido

### Autoinducción (Inductancia Propia)

La **inductancia propia** L de una bobina relaciona el flujo propio con la [corriente](../../../glossary.md#corriente):

$$L = \frac{N\Phi}{i}$$

El voltaje autoinducido es:
$$v = L\frac{di}{dt}$$

### Inductancia Mutua

Cuando dos bobinas están acopladas, la **inductancia mutua** M relaciona el flujo que enlaza una bobina debido a la corriente en la otra:

$$M = \frac{N_2\Phi_{12}}{i_1} = \frac{N_1\Phi_{21}}{i_2}$$

Donde:
- Φ₁₂ = flujo producido por bobina 1 que enlaza bobina 2
- M = inductancia mutua (en Henrios)

### Coeficiente de Acoplamiento

El **coeficiente de acoplamiento** k indica qué tan bien están acopladas las bobinas:

$$k = \frac{M}{\sqrt{L_1 L_2}}$$

**Rangos:**
- 0 ≤ k ≤ 1
- k = 0: Sin acoplamiento
- k = 1: Acoplamiento perfecto (todo el flujo enlaza ambas bobinas)
- k típico: 0.95-0.99 para transformadores de potencia

### Convención del Punto

Los **puntos** indican la polaridad relativa de los devanados.

```
   •           •
   ╭───╮      ╭───╮
───┤   ├──────┤   ├───
   │L₁ │  M   │L₂ │
   ╰───╯      ╰───╯
```

**Regla:** Si la corriente entra por el terminal con punto en ambas bobinas (o sale por ambos), los voltajes mutuos suman. Si una entra y otra sale, restan.

### Ecuaciones de Voltaje

Para dos bobinas acopladas:

$$v_1 = L_1\frac{di_1}{dt} \pm M\frac{di_2}{dt}$$
$$v_2 = L_2\frac{di_2}{dt} \pm M\frac{di_1}{dt}$$

**Signo positivo (+):** Corrientes en la misma dirección relativa a los puntos
**Signo negativo (-):** Corrientes en direcciones opuestas

### Forma Fasorial

$$\mathbf{V}_1 = j\omega L_1 \mathbf{I}_1 \pm j\omega M \mathbf{I}_2$$
$$\mathbf{V}_2 = j\omega L_2 \mathbf{I}_2 \pm j\omega M \mathbf{I}_1$$

### Energía en Inductores Acoplados

$$W = \frac{1}{2}L_1 i_1^2 + \frac{1}{2}L_2 i_2^2 \pm M i_1 i_2$$

Para que la energía sea siempre positiva:
$$M \leq \sqrt{L_1 L_2}$$

Lo que confirma: k ≤ 1

## Conceptos Clave
- M = k√(L₁L₂)
- Los puntos determinan el signo del [voltaje](../../../glossary.md#voltaje) mutuo
- k mide el grado de acoplamiento
