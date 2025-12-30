# TH-04: Teorema de Reciprocidad

## Objetivos
- Comprender el teorema de reciprocidad
- Aplicar el teorema en análisis de circuitos
- Identificar las condiciones de aplicabilidad

## Contenido

### Enunciado del Teorema

> En un circuito lineal bilateral sin fuentes dependientes, si una fuente de excitación en la rama k produce una respuesta en la rama j, entonces la misma fuente colocada en la rama j producirá la misma respuesta en la rama k.

### Condiciones de Aplicabilidad

El teorema de reciprocidad aplica cuando el circuito es:

1. **Lineal:** Contiene solo elementos lineales
2. **Bilateral:** Los elementos conducen igual en ambas direcciones
3. **Sin fuentes dependientes**
4. **Una sola fuente independiente**

### Formas del Teorema

#### Forma 1: Fuente de Voltaje - Respuesta de Corriente

Si una fuente de voltaje V en la posición 1 produce una corriente I en la posición 2, entonces la misma fuente V en la posición 2 producirá la misma corriente I en la posición 1.

```
Caso A:                      Caso B:
   ┌──[V]──○───R───○           ┌──────○───R───○
   │               │           │               │
   │    Red        │i₂         │    Red        │i₁
   │   Lineal      │      →    │   Lineal      │
   │               │           │               │
   └───────────────┘           └──[V]──────────┘

         i₂ = i₁
```

#### Forma 2: Fuente de Corriente - Respuesta de Voltaje

Si una fuente de corriente I en la posición 1 produce un voltaje V en la posición 2, entonces la misma fuente I en la posición 2 producirá el mismo voltaje V en la posición 1.

### Relación con Parámetros de Red

Para redes de dos puertos, el teorema de reciprocidad implica:
- z₁₂ = z₂₁ (parámetros de impedancia)
- y₁₂ = y₂₁ (parámetros de admitancia)

### Ejemplo de Aplicación

```
    2Ω         4Ω
 ○──/\/\/──┬──/\/\/──○
 │         │         │
[V]=10V   6Ω        (A)
 │         │         │
 ○─────────┴─────────○
```

**Caso A:** Fuente en posición izquierda, amperímetro en derecha
- Calcular corriente por A

**Caso B:** Intercambiar fuente y amperímetro
- Por reciprocidad, la corriente es la misma

### Verificación del Teorema

1. Resolver el circuito en la configuración original
2. Intercambiar fuente y punto de medición
3. Resolver nuevamente
4. Comparar resultados

### Utilidad Práctica

- Simplifica el análisis cuando hay simetría
- Reduce el número de cálculos necesarios
- Útil en el diseño de redes de comunicación
- Aplicable en análisis de filtros pasivos

### Limitaciones

El teorema **NO aplica** cuando:
- Hay fuentes dependientes en el circuito
- Los elementos son no lineales (diodos, transistores)
- Los elementos son unilaterales

## Conceptos Clave
- Reciprocidad = intercambiabilidad de entrada/salida
- Solo para circuitos lineales bilaterales
- No aplica con fuentes dependientes
