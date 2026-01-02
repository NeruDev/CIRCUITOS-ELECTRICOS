# MET-02: Método de Aplicación de las Leyes de Kirchhoff

## Descripción del Método

Las **Leyes de Kirchhoff** son dos principios fundamentales basados en la conservación de la carga y la energía, que permiten analizar cualquier circuito eléctrico.

### Ley de Corrientes de Kirchhoff (LCK)
> La suma algebraica de las corrientes que entran a un nodo es igual a cero.

$$\sum_{k=1}^{n} I_k = 0$$

*Corrientes entrantes (+) = Corrientes salientes (-)*

### Ley de Voltajes de Kirchhoff (LVK)
> La suma algebraica de los voltajes alrededor de cualquier lazo cerrado es igual a cero.

$$\sum_{k=1}^{n} V_k = 0$$

*Suma de subidas de voltaje = Suma de caídas de voltaje*

---

## Método para LCK (Ley de Corrientes)

### Pasos del Método

1. **Identificar todos los nodos** del circuito
2. **Asignar direcciones** a las corrientes (arbitrariamente)
3. **Aplicar LCK** en cada nodo: ΣI_entrantes = ΣI_salientes
4. **Resolver** el sistema de ecuaciones
5. **Interpretar:** Si una corriente resulta negativa, fluye en dirección opuesta a la asumida

### Convención de Signos
```
         I₁ ↓     ↑ I₂
           ╲     ╱
            ●───●  ← Nodo
           ╱     ╲
         I₃ ↑     ↓ I₄

LCK: I₁ + I₃ = I₂ + I₄
  o: I₁ - I₂ + I₃ - I₄ = 0
```

---

## Ejemplo Clásico 1: LCK en un Nodo

### Enunciado
En el circuito mostrado, las corrientes I₁ = 5 A e I₂ = 3 A entran al nodo, mientras que I₃ = 2 A sale del nodo. Determine la corriente I₄.

### Diagrama
```
       I₁=5A        I₂=3A
         ↓            ↓
          ╲          ╱
           ╲        ╱
            ●──────●
           ╱        ╲
          ╱          ╲
         ↓            ↓
       I₃=2A        I₄=?
```

### Solución Paso a Paso

**Paso 1: Identificar el nodo**
- Nodo central donde convergen las 4 corrientes

**Paso 2: Establecer convención**
- Entrantes: I₁, I₂ (positivas)
- Salientes: I₃, I₄ (negativas)

**Paso 3: Aplicar LCK**
$$\sum I_{entrantes} = \sum I_{salientes}$$
$$I_1 + I_2 = I_3 + I_4$$

**Paso 4: Sustituir y resolver**
$$5 + 3 = 2 + I_4$$
$$8 = 2 + I_4$$
$$I_4 = 6\text{ A}$$

**Paso 5: Verificación**
$$I_1 + I_2 = I_3 + I_4$$
$$5 + 3 = 2 + 6$$
$$8 = 8$$ ✓

### Respuesta
$$\boxed{I_4 = 6\text{ A (saliendo del nodo)}}$$

### Explicación de la Respuesta
La corriente I₄ = 6 A es positiva, confirmando que sale del nodo como se asumió. El nodo recibe 8 A en total (5 + 3) y debe entregar los mismos 8 A (2 + 6) para conservar la carga. Ninguna corriente se acumula en el nodo; todo lo que entra, sale.

---

## Método para LVK (Ley de Voltajes)

### Pasos del Método

1. **Identificar todos los lazos** cerrados del circuito
2. **Asignar sentido de recorrido** (horario o antihorario)
3. **Asignar polaridades** a las fuentes y elementos
4. **Recorrer el lazo** sumando voltajes:
   - Subida de voltaje: +V (de - a +)
   - Caída de voltaje: -V (de + a -)
5. **Igualar la suma a cero** y resolver

### Convención de Signos
```
Recorrido horario →

    ┌──────/\/\/──────┐
    │   +    R    -   │
    │                 │
  + │                 │ -
   ─┴─               ─┴─
   Vs                VR
   ─┬─               ─┬─
  - │                 │ +
    │                 │
    └─────────────────┘

LVK (horario): +Vs - VR = 0 → Vs = VR
```

---

## Ejemplo Clásico 2: LVK en un Lazo Simple

### Enunciado
Un circuito serie tiene una fuente de 24 V y tres resistencias: R₁ = 2 Ω, R₂ = 4 Ω, R₃ = 6 Ω. Calcule la corriente y el voltaje en cada resistencia.

### Diagrama
```
         I →
    ●────/\/\/────●────/\/\/────●
    │     R₁=2Ω       R₂=4Ω     │
    │                           │
  + │                         ┌─┴─┐
 24V│                         │R₃ │
    │                         │6Ω │
  - │                         └─┬─┘
    │                           │
    ●───────────────────────────●
```

### Solución Paso a Paso

**Paso 1: Identificar el lazo**
- Un solo lazo serie: Fuente → R₁ → R₂ → R₃ → Fuente

**Paso 2: Sentido de recorrido**
- Horario, siguiendo la corriente I

**Paso 3: Asignar polaridades**
- Fuente: + arriba, - abajo (da energía)
- Resistencias: + donde entra I, - donde sale (absorben energía)

**Paso 4: Aplicar LVK**
Recorriendo en sentido horario desde la fuente:
$$+V_s - V_{R1} - V_{R2} - V_{R3} = 0$$

Usando Ley de Ohm: $V_R = IR$
$$+24 - I(2) - I(4) - I(6) = 0$$
$$24 - 12I = 0$$
$$I = 2\text{ A}$$

**Paso 5: Calcular voltajes individuales**
$$V_{R1} = IR_1 = 2 \times 2 = 4\text{ V}$$
$$V_{R2} = IR_2 = 2 \times 4 = 8\text{ V}$$
$$V_{R3} = IR_3 = 2 \times 6 = 12\text{ V}$$

**Paso 6: Verificación con LVK**
$$V_s = V_{R1} + V_{R2} + V_{R3}$$
$$24 = 4 + 8 + 12 = 24\text{ V}$$ ✓

### Respuesta
$$\boxed{I = 2\text{ A}, \quad V_{R1} = 4\text{ V}, \quad V_{R2} = 8\text{ V}, \quad V_{R3} = 12\text{ V}}$$

### Explicación de la Respuesta
La corriente de 2 A es la misma en todo el circuito serie. Los voltajes se distribuyen proporcionalmente a las resistencias: R₃ (la mayor) tiene la mayor caída de voltaje. La suma de las caídas (4+8+12=24 V) iguala al voltaje de la fuente, cumpliendo la conservación de energía.

---

## Ejemplo Clásico 3: LCK y LVK Combinadas

### Enunciado
En el circuito de dos mallas mostrado, determine las corrientes I₁, I₂ e I₃.

### Diagrama
```
       I₁→      R₁=4Ω     I₃→      R₃=6Ω
    ●────────/\/\/────●────────/\/\/────●
    │                 │                 │
  + │               ┌─┴─┐             ┌─┴─┐
 12V│               │R₂ │             │R₄ │
    │               │2Ω │             │3Ω │
  - │               └─┬─┘             └─┬─┘
    │       ↓I₂       │                 │
    ●─────────────────●─────────────────●
```

### Solución Paso a Paso

**Paso 1: Aplicar LCK en el nodo central**
$$I_1 = I_2 + I_3$$

**Paso 2: Aplicar LVK en la malla izquierda (horario)**
$$+12 - I_1 R_1 - I_2 R_2 = 0$$
$$12 - 4I_1 - 2I_2 = 0 \quad \text{...(Ec. 1)}$$

**Paso 3: Aplicar LVK en la malla derecha (horario)**
$$+I_2 R_2 - I_3 R_3 - I_3 R_4 = 0$$
$$2I_2 - 6I_3 - 3I_3 = 0$$
$$2I_2 - 9I_3 = 0$$
$$I_2 = 4.5 I_3 \quad \text{...(Ec. 2)}$$

**Paso 4: Sustituir LCK en Ec. 1**
De LCK: $I_1 = I_2 + I_3$
$$12 - 4(I_2 + I_3) - 2I_2 = 0$$
$$12 - 4I_2 - 4I_3 - 2I_2 = 0$$
$$12 - 6I_2 - 4I_3 = 0 \quad \text{...(Ec. 3)}$$

**Paso 5: Sustituir Ec. 2 en Ec. 3**
$$12 - 6(4.5I_3) - 4I_3 = 0$$
$$12 - 27I_3 - 4I_3 = 0$$
$$12 = 31I_3$$
$$I_3 = \frac{12}{31} = 0.387\text{ A}$$

**Paso 6: Calcular I₂ e I₁**
$$I_2 = 4.5 \times 0.387 = 1.742\text{ A}$$
$$I_1 = I_2 + I_3 = 1.742 + 0.387 = 2.129\text{ A}$$

**Paso 7: Verificación con LVK malla externa**
$$12 - I_1 R_1 - I_3 R_3 - I_3 R_4 = 0$$
$$12 - (2.129)(4) - (0.387)(6) - (0.387)(3)$$
$$12 - 8.516 - 2.322 - 1.161 = 0.001 \approx 0$$ ✓

### Respuesta
$$\boxed{I_1 = 2.13\text{ A}, \quad I_2 = 1.74\text{ A}, \quad I_3 = 0.387\text{ A}}$$

### Explicación de la Respuesta
- I₁ = 2.13 A es la corriente total suministrada por la fuente
- I₂ = 1.74 A pasa por R₂ (la mayor parte, por ser el camino de menor resistencia)
- I₃ = 0.387 A pasa por R₃ y R₄ (menor corriente por mayor resistencia total)

La corriente se divide en el nodo proporcionalmente a las conductancias de cada rama. La rama con R₂ = 2 Ω tiene mayor conductancia que la rama con R₃ + R₄ = 9 Ω, por lo que lleva más corriente.

---

## Resumen de Estrategias

### Cuándo usar LCK
- Calcular corrientes desconocidas en nodos
- Circuitos con ramas en paralelo
- Verificar que las corrientes se conserven

### Cuándo usar LVK
- Calcular voltajes en elementos de un lazo
- Circuitos con elementos en serie
- Encontrar relaciones entre corrientes de malla

### Número de Ecuaciones Necesarias
- **Nodos:** n - 1 ecuaciones LCK (n = número de nodos)
- **Mallas:** m ecuaciones LVK (m = número de mallas independientes)
- **Relación:** m = b - n + 1 (b = número de ramas)

---

## Errores Comunes a Evitar

1. **Signos incorrectos:** Mantener consistencia en la convención de signos
2. **Nodos redundantes:** No todas las ecuaciones de nodos son independientes
3. **Lazos dependientes:** Usar solo lazos independientes (mallas)
4. **Olvidar elementos:** Incluir TODOS los elementos al recorrer un lazo
5. **Polaridad de fuentes:** La fuente de voltaje SUBE el potencial de - a +

## Conceptos Relacionados
- Análisis nodal
- Análisis de mallas
- Superposición
- Circuitos equivalentes
