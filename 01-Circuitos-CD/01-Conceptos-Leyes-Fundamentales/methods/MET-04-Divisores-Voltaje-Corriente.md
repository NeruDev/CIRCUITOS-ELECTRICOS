# MET-04: Método del Divisor de Voltaje y Divisor de Corriente

## Descripción del Método

Estos métodos permiten calcular voltajes y corrientes en circuitos serie y paralelo SIN necesidad de calcular primero la [resistencia](../../../glossary.md#resistencia) equivalente.

---

## Parte A: Divisor de Voltaje

### Fórmula Fundamental
Para resistencias en **serie**, el [voltaje](../../../glossary.md#voltaje) se divide proporcionalmente a las resistencias:

$$V_x = V_T \cdot \frac{R_x}{R_{total}}$$

### Diagrama Conceptual
```
       ●────────┬────────●
       │   +VT  │        │
       │      ┌─┴─┐      │
       │   +  │R₁ │      │
       │  V₁  └─┬─┘      │
       │   -    │        │
       │      ┌─┴─┐      │
       │   +  │R₂ │      │
       │  V₂  └─┬─┘      │
       │   -    │        │
       ●────────┴────────●
       
V₁ = VT × R₁/(R₁+R₂)
V₂ = VT × R₂/(R₁+R₂)
```

### Pasos del Método

1. **Verificar:** Las resistencias deben estar en SERIE
2. **Identificar:** Voltaje total (VT) aplicado al conjunto
3. **Calcular:** Resistencia total RT = R₁ + R₂ + ...
4. **Aplicar:** $V_x = V_T \times (R_x / R_T)$

---

## Ejemplo Clásico 1: Divisor de Voltaje Simple

### Enunciado
Un divisor de voltaje tiene R₁ = 10 kΩ y R₂ = 20 kΩ conectados a una fuente de 15 V. Calcule V₁ y V₂.

### Diagrama
```
      ●────────┬────────●
      │  +15V  │        │
      │      ┌─┴─┐      │
      │   +  │R₁ │      │
      │  V₁  │10k│      │
      │   -  └─┬─┘      │
      │        ●──────● Vout = V₂
      │      ┌─┴─┐      │
      │   +  │R₂ │      │
      │  V₂  │20k│      │
      │   -  └─┬─┘      │
      ●────────┴────────●
             GND
```

### Solución Paso a Paso

**Paso 1: Verificar conexión serie**
- R₁ y R₂ están en serie (misma corriente) ✓

**Paso 2: Calcular RT**
$$R_T = R_1 + R_2 = 10k + 20k = 30\text{ kΩ}$$

**Paso 3: Aplicar divisor de voltaje**

Para V₁:
$$V_1 = V_T \times \frac{R_1}{R_T} = 15 \times \frac{10k}{30k} = 15 \times \frac{1}{3}$$
$$V_1 = 5\text{ V}$$

Para V₂:
$$V_2 = V_T \times \frac{R_2}{R_T} = 15 \times \frac{20k}{30k} = 15 \times \frac{2}{3}$$
$$V_2 = 10\text{ V}$$

**Paso 4: Verificación**
$$V_1 + V_2 = 5 + 10 = 15\text{ V} = V_T$$ ✓

### Respuesta
$$\boxed{V_1 = 5\text{ V}, \quad V_2 = 10\text{ V}}$$

### Explicación de la Respuesta
El voltaje se divide en proporción 1:2 (igual que la proporción de resistencias 10k:20k). La resistencia mayor (R₂) tiene el mayor voltaje. Esto tiene sentido: a mayor resistencia, mayor caída de voltaje para la misma [corriente](../../../glossary.md#corriente) (V = IR). El punto medio (Vout = V₂ = 10V) es útil como referencia de voltaje.

---

## Ejemplo Clásico 2: Divisor de Voltaje con Tres Resistencias

### Enunciado
Un [circuito](../../../glossary.md#circuito) tiene R₁ = 1 kΩ, R₂ = 2 kΩ, R₃ = 3 kΩ en serie con una fuente de 12 V. Encuentre el voltaje en cada resistencia.

### Diagrama
```
         I →
    ●────/\/\/────/\/\/────/\/\/────●
    │     R₁=1k    R₂=2k    R₃=3k   │
  + │                               │
 12V│   V₁        V₂        V₃      │
  - │                               │
    ●───────────────────────────────●
```

### Solución

$$R_T = 1k + 2k + 3k = 6\text{ kΩ}$$

$$V_1 = 12 \times \frac{1}{6} = 2\text{ V}$$

$$V_2 = 12 \times \frac{2}{6} = 4\text{ V}$$

$$V_3 = 12 \times \frac{3}{6} = 6\text{ V}$$

**Verificación:** $2 + 4 + 6 = 12$ V ✓

### Respuesta
$$\boxed{V_1 = 2\text{ V}, \quad V_2 = 4\text{ V}, \quad V_3 = 6\text{ V}}$$

### Explicación de la Respuesta
Los voltajes guardan la misma proporción que las resistencias (1:2:3). Este es el principio fundamental del divisor: el voltaje se reparte proporcionalmente. La resistencia más grande siempre tendrá la mayor caída de voltaje.

---

## Parte B: Divisor de Corriente

### Fórmula Fundamental
Para resistencias en **paralelo**, la corriente se divide inversamente proporcional a las resistencias:

**Dos resistencias:**
$$I_1 = I_T \cdot \frac{R_2}{R_1 + R_2}$$
$$I_2 = I_T \cdot \frac{R_1}{R_1 + R_2}$$

**Forma general (usando conductancias):**
$$I_x = I_T \cdot \frac{G_x}{G_{total}} = I_T \cdot \frac{1/R_x}{\sum(1/R_i)}$$

### Diagrama Conceptual
```
         I_T →
    ●─────────┬─────────●
              │
        I₁↓ ┌─┴─┐ ↓I₂
           ─┤R₁ ├─
            └─┬─┘
        I₂↓ ┌─┴─┐
           ─┤R₂ ├─
            └─┬─┘
              │
    ●─────────┴─────────●

I₁ = IT × R₂/(R₁+R₂)  ← ¡Nota: usa la OTRA resistencia!
I₂ = IT × R₁/(R₁+R₂)
```

### Regla Nemotécnica
> "La corriente toma el camino de MENOR resistencia"  
> La rama con MENOR R lleva MAYOR corriente

---

## Ejemplo Clásico 3: Divisor de Corriente Simple

### Enunciado
Una corriente de 12 A se divide entre dos resistencias en paralelo: R₁ = 4 Ω y R₂ = 12 Ω. Calcule I₁ e I₂.

### Diagrama
```
       IT = 12A →
    ●───────────┬───────────●
                │
          I₁↓ ┌─┴─┐
             ─┤R₁ ├─ 4Ω
              └─┬─┘
          I₂↓ ┌─┴─┐
             ─┤R₂ ├─ 12Ω
              └─┬─┘
                │
    ●───────────┴───────────●
```

### Solución Paso a Paso

**Paso 1: Verificar conexión paralelo**
- R₁ y R₂ comparten el mismo voltaje ✓

**Paso 2: Aplicar [divisor de corriente](../../../glossary.md#divisor-corriente)**

Para I₁ (usa R₂ en el numerador):
$$I_1 = I_T \times \frac{R_2}{R_1 + R_2} = 12 \times \frac{12}{4 + 12} = 12 \times \frac{12}{16}$$
$$I_1 = 12 \times 0.75 = 9\text{ A}$$

Para I₂ (usa R₁ en el numerador):
$$I_2 = I_T \times \frac{R_1}{R_1 + R_2} = 12 \times \frac{4}{4 + 12} = 12 \times \frac{4}{16}$$
$$I_2 = 12 \times 0.25 = 3\text{ A}$$

**Paso 3: Verificación ([LCK](../../../glossary.md#lck))**
$$I_1 + I_2 = 9 + 3 = 12\text{ A} = I_T$$ ✓

### Respuesta
$$\boxed{I_1 = 9\text{ A}, \quad I_2 = 3\text{ A}}$$

### Explicación de la Respuesta
La corriente se divide en proporción inversa a las resistencias:
- R₁ = 4 Ω (menor) → lleva 9 A (mayor corriente)
- R₂ = 12 Ω (mayor) → lleva 3 A (menor corriente)

Proporción de resistencias: 4:12 = 1:3  
Proporción de corrientes: 9:3 = 3:1 (inversa)

La corriente "prefiere" el camino de menor resistencia.

---

## Ejemplo Clásico 4: Tres Resistencias en Paralelo

### Enunciado
IT = 30 mA se divide entre R₁ = 100 Ω, R₂ = 200 Ω y R₃ = 200 Ω en paralelo. Calcule cada corriente.

### Diagrama
```
       IT = 30mA →
    ●───────────┬───────────●
          I₁↓ ┌─┴─┐
             ─┤100├─ R₁
          I₂↓ ├───┤
             ─┤200├─ R₂
          I₃↓ ├───┤
             ─┤200├─ R₃
              └─┬─┘
    ●───────────┴───────────●
```

### Solución

**Método: Usar conductancias**

$$G_1 = \frac{1}{100} = 0.01\text{ S}$$
$$G_2 = \frac{1}{200} = 0.005\text{ S}$$
$$G_3 = \frac{1}{200} = 0.005\text{ S}$$
$$G_T = 0.01 + 0.005 + 0.005 = 0.02\text{ S}$$

$$I_1 = I_T \times \frac{G_1}{G_T} = 30 \times \frac{0.01}{0.02} = 30 \times 0.5 = 15\text{ mA}$$

$$I_2 = I_T \times \frac{G_2}{G_T} = 30 \times \frac{0.005}{0.02} = 30 \times 0.25 = 7.5\text{ mA}$$

$$I_3 = I_T \times \frac{G_3}{G_T} = 30 \times \frac{0.005}{0.02} = 30 \times 0.25 = 7.5\text{ mA}$$

**Verificación:** $15 + 7.5 + 7.5 = 30$ mA ✓

### Respuesta
$$\boxed{I_1 = 15\text{ mA}, \quad I_2 = 7.5\text{ mA}, \quad I_3 = 7.5\text{ mA}}$$

### Explicación de la Respuesta
R₁ tiene la mitad de resistencia que R₂ y R₃, por lo tanto lleva el doble de corriente (15 mA vs 7.5 mA). Las corrientes son directamente proporcionales a las conductancias. R₂ y R₃, siendo iguales, llevan corrientes iguales.

---

## Ejemplo Clásico 5: Combinación de Divisores

### Enunciado
En el circuito mostrado, calcule V₃ y I₂.

### Diagrama
```
         ●────────┬────────●
         │  +36V  │        │
         │      ┌─┴─┐      │
         │      │R₁ │      │
         │      │6Ω │      │
         │      └─┬─┘      │
         │   I₂↙  │  ↘I₃   │
         │      ┌─┴──┴─┐   │
         │      │R₂  R₃│   │
         │      │12Ω 6Ω│   │
         │      └──┬───┘   │
         │         │       │
         ●─────────┴───────●
```

### Solución

**Paso 1: Combinar R₂ || R₃**
$$R_{23} = \frac{12 \times 6}{12 + 6} = \frac{72}{18} = 4\text{ Ω}$$

**Paso 2: Divisor de voltaje para V₂₃**
$$V_{23} = 36 \times \frac{R_{23}}{R_1 + R_{23}} = 36 \times \frac{4}{6 + 4} = 36 \times \frac{4}{10}$$
$$V_{23} = 14.4\text{ V}$$

Como R₂ y R₃ están en paralelo: $V_2 = V_3 = V_{23} = 14.4$ V

**Paso 3: Calcular corriente total**
$$I_T = \frac{36}{R_1 + R_{23}} = \frac{36}{10} = 3.6\text{ A}$$

**Paso 4: Divisor de corriente para I₂**
$$I_2 = I_T \times \frac{R_3}{R_2 + R_3} = 3.6 \times \frac{6}{12 + 6} = 3.6 \times \frac{6}{18}$$
$$I_2 = 1.2\text{ A}$$

**Verificación alternativa:**
$$I_2 = \frac{V_{23}}{R_2} = \frac{14.4}{12} = 1.2\text{ A}$$ ✓

### Respuesta
$$\boxed{V_3 = 14.4\text{ V}, \quad I_2 = 1.2\text{ A}}$$

### Explicación de la Respuesta
Primero usamos divisor de voltaje para encontrar el voltaje en el [nodo](../../../glossary.md#nodo) del paralelo. Luego, dentro del paralelo, usamos divisor de corriente. Nótese que I₂ (por 12 Ω) es menor que I₃ (por 6 Ω), cumpliendo la regla de que menor resistencia lleva mayor corriente.

---

## Resumen de Fórmulas

| Tipo | Configuración | Fórmula |
|------|---------------|---------|
| Divisor de Voltaje | Serie | $V_x = V_T \times \frac{R_x}{R_T}$ |
| Divisor de Corriente | Paralelo (2R) | $I_1 = I_T \times \frac{R_2}{R_1+R_2}$ |
| Divisor de Corriente | Paralelo (nR) | $I_x = I_T \times \frac{G_x}{G_T}$ |

## Errores Comunes

1. **Divisor de voltaje:** El voltaje es proporcional a R (misma R en numerador)
2. **Divisor de corriente:** La corriente es INVERSAMENTE proporcional (R opuesta en numerador)
3. **Confundir configuraciones:** Serie = mismo I, Paralelo = mismo V
4. **Olvidar verificar:** Siempre comprobar que las corrientes/voltajes sumen correctamente

## Conceptos Relacionados
- [Ley de](../../../glossary.md#ley-ohm) [Ohm](../../../glossary.md#ohm-unidad)
- Combinación de resistencias
- Leyes de [Kirchhoff](../../../glossary.md#lvk)
