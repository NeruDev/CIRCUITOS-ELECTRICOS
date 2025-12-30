# TH-07: Teorema de Reciprocidad en CA

## Objetivos
- Aplicar el teorema de reciprocidad a circuitos CA
- Identificar las condiciones de aplicabilidad
- Verificar la reciprocidad en circuitos con elementos reactivos

## Contenido

### Enunciado para CA

En un circuito lineal, bilateral, sin fuentes dependientes y con una sola frecuencia, si una fuente de excitación en la posición 1 produce una respuesta en la posición 2, entonces la misma fuente colocada en la posición 2 producirá la misma respuesta en la posición 1.

### Condiciones de Aplicabilidad

1. **Circuito lineal**
2. **Elementos bilaterales** (R, L, C, transformadores sin núcleo de hierro)
3. **Sin fuentes dependientes**
4. **Una sola fuente independiente**
5. **Misma frecuencia de operación**

### Formas del Teorema en CA

**Forma 1: Fuente de Voltaje - Corriente**
Si una fuente **Vs** en la rama k produce una corriente **I** en la rama j, entonces **Vs** en la rama j produce la misma corriente **I** en la rama k.

**Forma 2: Fuente de Corriente - Voltaje**
Si una fuente **Is** en la rama k produce un voltaje **V** en la rama j, entonces **Is** en la rama j produce el mismo voltaje **V** en la rama k.

### Relación con Parámetros Z e Y

Para una red de dos puertos recíproca:
$$\mathbf{Z}_{12} = \mathbf{Z}_{21}$$
$$\mathbf{Y}_{12} = \mathbf{Y}_{21}$$

### Ejemplo de Aplicación

```
Configuración A:
       Z₁         Z₂
    ○───⬚───┬───⬚───○
    │       │       │
  Vs∠0°    Z₃      (I₂)
    │       │       │
    ○───────┴───────○

Configuración B:
       Z₁         Z₂
    ○───⬚───┬───⬚───○
    │       │       │
  (I₁)     Z₃     Vs∠0°
    │       │       │
    ○───────┴───────○
```

Por reciprocidad: **I₂** en Config. A = **I₁** en Config. B

### Verificación

Para verificar reciprocidad:
1. Resolver el circuito en configuración A
2. Intercambiar fuente y medición (configuración B)
3. Resolver nuevamente
4. Comparar las respuestas

### No Aplica Cuando...

- Hay fuentes dependientes (amplificadores operacionales, transistores)
- Elementos activos no lineales
- Materiales magnéticos no lineales
- Hay múltiples frecuencias mezcladas

### Utilidad Práctica

1. **Reducción de cálculos:** Solo se necesita resolver una configuración
2. **Diseño de redes:** Útil en diseño de filtros y redes de adaptación
3. **Mediciones:** Permite verificar comportamiento de redes pasivas
4. **Análisis de antenas:** Importante en teoría de antenas

### Ejemplo Numérico

**Circuito:** Z₁ = 10Ω, Z₂ = j20Ω, Z₃ = -j10Ω

**Config. A:** Vs = 100∠0° en posición de Z₁
Calcular corriente en Z₂.

**Config. B:** Vs = 100∠0° en posición de Z₂
Calcular corriente en Z₁.

Por reciprocidad, ambas corrientes son iguales.

## Conceptos Clave
- Aplica a circuitos pasivos lineales en CA
- Z₁₂ = Z₂₁ implica reciprocidad
- No aplica con fuentes dependientes o no linealidades
