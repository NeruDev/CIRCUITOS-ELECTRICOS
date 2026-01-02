# MET-03: Método de Combinación de Resistencias

## Descripción del Método

Este método permite simplificar circuitos complejos combinando resistencias en **serie** y **paralelo** hasta obtener una [resistencia](../../../glossary.md#resistencia) equivalente única.

## Fórmulas Fundamentales

### Resistencias en Serie
$$R_{eq} = R_1 + R_2 + R_3 + \cdots + R_n$$

```
●───/\/\/───/\/\/───/\/\/───●  =  ●───/\/\/───●
     R₁       R₂       R₃           R_eq
     
Misma corriente en todas
```

### Resistencias en Paralelo
$$\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \cdots$$

**Caso especial (dos resistencias):**
$$R_{eq} = \frac{R_1 \cdot R_2}{R_1 + R_2}$$

**Caso especial (n resistencias iguales):**
$$R_{eq} = \frac{R}{n}$$

```
    ●───/\/\/───●
    │    R₁     │
    ├───/\/\/───┤  =  ●───/\/\/───●
    │    R₂     │          R_eq
    └───/\/\/───┘
         R₃
         
Mismo voltaje en todas
```

---

## Pasos del Método

### Paso 1: Identificar Conexiones
- Elementos en **serie:** La misma [corriente](../../../glossary.md#corriente) pasa por ambos
- Elementos en **paralelo:** El mismo [voltaje](../../../glossary.md#voltaje) en ambos

### Paso 2: Simplificar de Adentro hacia Afuera
- Comenzar por las combinaciones más internas
- Trabajar progresivamente hacia los terminales externos

### Paso 3: Redibujar el Circuito
- Después de cada simplificación, redibujar
- Esto ayuda a identificar nuevas combinaciones

### Paso 4: Repetir
- Continuar hasta obtener una sola resistencia equivalente

### Paso 5: Calcular (si se requiere)
- Corriente total: $I_T = V_s / R_{eq}$
- Volver a expandir para encontrar corrientes/voltajes individuales

---

## Ejemplo Clásico 1: Combinación Serie-Paralelo Básica

### Enunciado
Calcule la resistencia equivalente entre los terminales A y B.

### Diagrama
```
        R₁=6Ω
    A●───/\/\/───┬───────●B
                 │
               ┌─┴─┐
               │R₂ │
               │3Ω │
               └─┬─┘
                 │
               ┌─┴─┐
               │R₃ │
               │6Ω │
               └─┬─┘
                 │
    A●───────────┴───────●B
```

### Solución Paso a Paso

**Paso 1: Identificar conexiones**
- R₂ y R₃ están en SERIE (misma corriente)
- (R₂ + R₃) está en PARALELO con R₁

**Paso 2: Combinar R₂ y R₃ (serie)**
$$R_{23} = R_2 + R_3 = 3 + 6 = 9\text{ Ω}$$

**Paso 3: Redibujar**
```
        R₁=6Ω
    A●───/\/\/───┬───●B
                 │
               ┌─┴─┐
               │R₂₃│
               │9Ω │
               └─┬─┘
                 │
    A●───────────┴───●B
```

**Paso 4: Combinar R₁ y R₂₃ (paralelo)**
$$R_{eq} = \frac{R_1 \cdot R_{23}}{R_1 + R_{23}} = \frac{6 \times 9}{6 + 9} = \frac{54}{15}$$

$$R_{eq} = 3.6\text{ Ω}$$

**Paso 5: Verificación**
$$\frac{1}{R_{eq}} = \frac{1}{6} + \frac{1}{9} = \frac{3 + 2}{18} = \frac{5}{18}$$
$$R_{eq} = \frac{18}{5} = 3.6\text{ Ω}$$ ✓

### Respuesta
$$\boxed{R_{eq} = 3.6\text{ Ω}}$$

### Explicación de la Respuesta
La resistencia equivalente (3.6 Ω) es menor que cualquiera de las resistencias porque hay caminos paralelos. Es menor que R₁ (6 Ω) porque el paralelo siempre reduce la resistencia total. La corriente tiene dos caminos: uno directo por R₁ y otro por R₂-R₃.

---

## Ejemplo Clásico 2: Red Escalera

### Enunciado
Calcule la resistencia equivalente de la red escalera.

### Diagrama
```
        R₁=2Ω      R₃=2Ω      R₅=2Ω
    A●───/\/\/──┬──/\/\/──┬──/\/\/──●B
                │         │
              ┌─┴─┐     ┌─┴─┐
              │R₂ │     │R₄ │
              │4Ω │     │4Ω │
              └─┬─┘     └─┬─┘
                │         │
    A●──────────┴─────────┴─────────●B
```

### Solución Paso a Paso

**Paso 1: Trabajar desde la derecha**

Combinamos R₅ en serie con R₄:
$$R_{45} = R_4 \| R_5 \text{ (paralelo con nodo B a tierra)}$$

Pero R₅ NO está en paralelo directo con R₄. Analicemos mejor:
- R₄ está entre el nodo central derecho y tierra
- R₅ está entre el nodo central derecho y B

**Paso 2: Identificar correctamente**
```
        R₁=2Ω      R₃=2Ω      R₅=2Ω
    A●───/\/\/──●──/\/\/──●──/\/\/──●B
               N1        N2
                │         │
              ┌─┴─┐     ┌─┴─┐
              │R₂ │     │R₄ │
              │4Ω │     │4Ω │
              └─┬─┘     └─┬─┘
                │         │
                └────●────┘
                    GND
```

Asumiendo B conectado a GND para calcular R_AB:

**Paso 3: Desde la derecha**
R₅ en serie con (R₄ || conexión):
- R₄ y R₅ están en serie vistas desde N2: $R_{45s} = R_4 \| R_5$

Recalculando con B a GND:
$$R_{4,5} = R_4 \| R_5 = \frac{4 \times 2}{4 + 2} = \frac{8}{6} = 1.33\text{ Ω}$$

**Paso 4: Combinar con R₃**
$$R_{345} = R_3 + R_{4,5} = 2 + 1.33 = 3.33\text{ Ω}$$

**Paso 5: Paralelo con R₂**
$$R_{2345} = R_2 \| R_{345} = \frac{4 \times 3.33}{4 + 3.33} = \frac{13.33}{7.33} = 1.82\text{ Ω}$$

**Paso 6: Serie con R₁**
$$R_{eq} = R_1 + R_{2345} = 2 + 1.82 = 3.82\text{ Ω}$$

### Respuesta
$$\boxed{R_{eq} = 3.82\text{ Ω}}$$

### Explicación de la Respuesta
En redes escalera, siempre se trabaja desde el extremo hacia la entrada, combinando resistencias progresivamente. La resistencia equivalente depende de cómo estén conectados los terminales de entrada y salida.

---

## Ejemplo Clásico 3: Calcular Corriente y Voltajes

### Enunciado
Una fuente de 24 V alimenta el siguiente [circuito](../../../glossary.md#circuito). Calcule la corriente total y el voltaje en cada resistencia.

### Diagrama
```
         I_T →
    ●─────────┬────────────●
    │         │            │
  + │       ┌─┴─┐        ┌─┴─┐
 24V│       │R₁ │        │R₂ │
    │       │8Ω │        │24Ω│
  - │       └─┬─┘        └─┬─┘
    │         │            │
    │         └──────┬─────┘
    │              ┌─┴─┐
    │              │R₃ │
    │              │6Ω │
    │              └─┬─┘
    │                │
    ●────────────────┴────────●
```

### Solución Paso a Paso

**Paso 1: Identificar conexiones**
- R₁ y R₂ están en paralelo
- (R₁ || R₂) está en serie con R₃

**Paso 2: Combinar R₁ || R₂**
$$R_{12} = \frac{R_1 \cdot R_2}{R_1 + R_2} = \frac{8 \times 24}{8 + 24} = \frac{192}{32} = 6\text{ Ω}$$

**Paso 3: Combinar con R₃ (serie)**
$$R_{eq} = R_{12} + R_3 = 6 + 6 = 12\text{ Ω}$$

**Paso 4: Calcular corriente total**
$$I_T = \frac{V_s}{R_{eq}} = \frac{24}{12} = 2\text{ A}$$

**Paso 5: Calcular voltajes**

Voltaje en R₃:
$$V_{R3} = I_T \times R_3 = 2 \times 6 = 12\text{ V}$$

Voltaje en el paralelo (R₁ y R₂):
$$V_{12} = I_T \times R_{12} = 2 \times 6 = 12\text{ V}$$

Como R₁ y R₂ están en paralelo, tienen el mismo voltaje:
$$V_{R1} = V_{R2} = 12\text{ V}$$

**Paso 6: Calcular corrientes individuales (opcional)**
$$I_{R1} = \frac{V_{R1}}{R_1} = \frac{12}{8} = 1.5\text{ A}$$
$$I_{R2} = \frac{V_{R2}}{R_2} = \frac{12}{24} = 0.5\text{ A}$$

**Verificación:** $I_{R1} + I_{R2} = 1.5 + 0.5 = 2\text{ A} = I_T$ ✓

### Respuesta
$$\boxed{I_T = 2\text{ A}, \quad V_{R1} = V_{R2} = 12\text{ V}, \quad V_{R3} = 12\text{ V}}$$

### Explicación de la Respuesta
El voltaje de 24 V se divide equitativamente: 12 V en el paralelo R₁||R₂ y 12 V en R₃. Esto ocurre porque R₁₂ = R₃ = 6 Ω (divisor de voltaje 1:1). Las corrientes en R₁ y R₂ son inversamente proporcionales a sus resistencias: R₂ es 3 veces R₁, así que I₂ es 1/3 de I₁.

---

## Técnicas Avanzadas

### Identificar Nodos Equipotenciales
Puntos conectados por un cable tienen el mismo potencial → se pueden unir.

### Transformación Δ-Y (Delta-Estrella)
Cuando no hay combinaciones serie/paralelo directas:

**Delta a Estrella:**
$$R_1 = \frac{R_a R_b}{R_a + R_b + R_c}$$
$$R_2 = \frac{R_b R_c}{R_a + R_b + R_c}$$
$$R_3 = \frac{R_a R_c}{R_a + R_b + R_c}$$

### Simetría
En circuitos simétricos, puntos equivalentes tienen el mismo potencial.

---

## Errores Comunes a Evitar

1. **Confundir serie con paralelo:** Serie = misma corriente, Paralelo = mismo voltaje
2. **Olvidar redibujar:** Cada simplificación merece un diagrama nuevo
3. **Orden incorrecto:** Siempre de adentro hacia afuera
4. **Fórmula incorrecta:** Serie suma, paralelo NO suma directamente
5. **Decimales prematuros:** Mantener fracciones hasta el final cuando sea posible

## Tabla de Referencia Rápida

| Configuración | Fórmula | Resultado |
|--------------|---------|-----------|
| 2 en serie | R₁ + R₂ | Mayor que ambas |
| 2 en paralelo | (R₁×R₂)/(R₁+R₂) | Menor que la menor |
| n iguales serie | n×R | n veces R |
| n iguales paralelo | R/n | R dividido n |

## Conceptos Relacionados
- Divisor de voltaje
- [Divisor de corriente](../../../glossary.md#divisor-corriente)
- Transformación Δ-Y
- Análisis de potencia
