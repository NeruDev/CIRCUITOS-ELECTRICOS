# PR-02: Análisis Nodal en CA con Fasores ⭐⭐⭐

## Enunciado
En el [circuito](../../../glossary.md#circuito) mostrado, las fuentes son v₁(t) = 10cos(1000t)V y v₂(t) = 20cos(1000t + 45°)V. Usando análisis nodal en el dominio fasorial, determine:
a) Los voltajes fasoriales V₁ y V₂ en los nodos 1 y 2
b) La [corriente](../../../glossary.md#corriente) en el [inductor](../../../glossary.md#inductancia) IL
c) Las expresiones en el dominio del tiempo v₁(t), v₂(t), iL(t)

Datos: R₁ = 10Ω, R₂ = 20Ω, L = 10mH, C = 100μF, ω = 1000 rad/s

## Diagrama del Circuito

```
              Nodo 1           Nodo 2
                ●───/\/\/───────●───/\/\/───┐
                │    R₁=10Ω    │    R₂=20Ω │
              + │              │          + │
        10∠0° (─)            ┌─┴─┐     20∠45°(─)
              - │            │ L │        - │
                │            │10mH         │
                │            └─┬─┘         │
                │      ┌──────┴──────┐     │
                │      │      C      │     │
                │      │    100μF    │     │
                │      └──────┬──────┘     │
                └─────────────┴────────────┘
                              │
                             ─┴─ GND
```

## Netlist SPICE

```spice
* PR-02: Análisis Nodal en CA
* Dos fuentes con diferente fase

V1 1 0 AC 10 0       ; Fuente 1: 10V, 0°
V2 3 0 AC 20 45      ; Fuente 2: 20V, 45°
R1 1 2 10            ; R1 = 10Ω
R2 2 3 20            ; R2 = 20Ω
L1 2 0 10m           ; L = 10mH
C1 2 0 100u          ; C = 100μF

.AC LIN 1 159.15 159.15  ; f = ω/2π = 159.15 Hz
.PRINT AC VM(2) VP(2) IM(L1) IP(L1)
.END
```

## Solución

### Datos
- V₁ = 10∠0° V
- V₂ = 20∠45° V
- R₁ = 10 Ω
- R₂ = 20 Ω
- L = 10 mH
- C = 100 μF
- ω = 1000 rad/s

### Cálculo de impedancias y admitancias

**Resistencias:**
$$Y_{R1} = \frac{1}{R_1} = \frac{1}{10} = 0.1\text{ S}$$
$$Y_{R2} = \frac{1}{R_2} = \frac{1}{20} = 0.05\text{ S}$$

**[Reactancia](../../../glossary.md#reactancia) inductiva:**
$$X_L = \omega L = 1000 \times 0.01 = 10\text{ Ω}$$
$$Y_L = \frac{1}{jX_L} = \frac{1}{j10} = -j0.1\text{ S}$$

**Reactancia capacitiva:**
$$X_C = \frac{1}{\omega C} = \frac{1}{1000 \times 100 \times 10^{-6}} = 10\text{ Ω}$$
$$Y_C = j\omega C = j(1000)(100 \times 10^{-6}) = j0.1\text{ S}$$

### Parte a) Análisis nodal

**[Nodo](../../../glossary.md#nodo) 1:** (tomando el nodo inferior como referencia)
La fuente V₁ fija directamente el [voltaje](../../../glossary.md#voltaje):
$$\mathbf{V}_1 = 10\angle 0° \text{ V}$$

**Nodo 2:**
Aplicando LCK en forma de admitancias:
$$\frac{\mathbf{V}_2 - \mathbf{V}_1}{Z_{R1}} + \frac{\mathbf{V}_2}{Z_L} + \frac{\mathbf{V}_2}{Z_C} + \frac{\mathbf{V}_2 - \mathbf{V}_3}{Z_{R2}} = 0$$

Donde V₃ = 20∠45° V (fijado por la fuente V₂)

$$Y_{R1}(\mathbf{V}_2 - \mathbf{V}_1) + Y_L \mathbf{V}_2 + Y_C \mathbf{V}_2 + Y_{R2}(\mathbf{V}_2 - \mathbf{V}_3) = 0$$

$$\mathbf{V}_2(Y_{R1} + Y_L + Y_C + Y_{R2}) = Y_{R1}\mathbf{V}_1 + Y_{R2}\mathbf{V}_3$$

**Suma de admitancias:**
$$Y_{total} = 0.1 + (-j0.1) + (j0.1) + 0.05 = 0.15 + j0\text{ S}$$

Nota: La reactancia inductiva y capacitiva se cancelan (resonancia).

**Cálculo de V₂:**
$$\mathbf{V}_2 = \frac{Y_{R1}\mathbf{V}_1 + Y_{R2}\mathbf{V}_3}{Y_{total}}$$

$$\mathbf{V}_2 = \frac{0.1(10\angle 0°) + 0.05(20\angle 45°)}{0.15}$$

Convertimos a rectangular:
- $0.1 \times 10 = 1$
- $0.05 \times 20\angle 45° = 1\angle 45° = 0.707 + j0.707$

$$\mathbf{V}_2 = \frac{1 + 0.707 + j0.707}{0.15} = \frac{1.707 + j0.707}{0.15}$$

$$\mathbf{V}_2 = 11.38 + j4.71 = 12.32\angle 22.5° \text{ V}$$

$$\boxed{\mathbf{V}_1 = 10\angle 0° \text{ V}}$$
$$\boxed{\mathbf{V}_2 = 12.32\angle 22.5° \text{ V}}$$

### Parte b) Corriente en el inductor

$$\mathbf{I}_L = \frac{\mathbf{V}_2}{Z_L} = \frac{12.32\angle 22.5°}{10\angle 90°}$$

$$\mathbf{I}_L = 1.232\angle (22.5° - 90°) = 1.232\angle -67.5° \text{ A}$$

$$\boxed{\mathbf{I}_L = 1.232\angle -67.5° \text{ A}}$$

**Verificación:** La corriente en el inductor atrasa 90° respecto al voltaje en él (comportamiento esperado).

### Parte c) Expresiones en el dominio del tiempo

$$\boxed{v_1(t) = 10\cos(1000t)\text{ V}}$$ (dato original)

$$\boxed{v_2(t) = 12.32\cos(1000t + 22.5°)\text{ V}}$$

$$\boxed{i_L(t) = 1.232\cos(1000t - 67.5°)\text{ A}}$$

### Corrientes adicionales (verificación)

**Corriente en R₁:**
$$\mathbf{I}_{R1} = \frac{\mathbf{V}_1 - \mathbf{V}_2}{R_1} = \frac{10\angle 0° - 12.32\angle 22.5°}{10}$$

$$\mathbf{I}_{R1} = \frac{10 - (11.38 + j4.71)}{10} = \frac{-1.38 - j4.71}{10}$$

$$\mathbf{I}_{R1} = -0.138 - j0.471 = 0.491\angle -106.3° \text{ A}$$

**Corriente en el [capacitor](../../../glossary.md#capacitancia):**
$$\mathbf{I}_C = \frac{\mathbf{V}_2}{Z_C} = \frac{12.32\angle 22.5°}{10\angle -90°}$$

$$\mathbf{I}_C = 1.232\angle 112.5° \text{ A}$$

**Verificación [LCK](../../../glossary.md#lck) en nodo 2:**
$$\mathbf{I}_{R1} + \mathbf{I}_{R2} = \mathbf{I}_L + \mathbf{I}_C$$

- $\mathbf{I}_{R1} = 0.491\angle -106.3°$
- $\mathbf{I}_L = 1.232\angle -67.5° = 0.471 - j1.14$
- $\mathbf{I}_C = 1.232\angle 112.5° = -0.471 + j1.14$
- $\mathbf{I}_L + \mathbf{I}_C = 0 + j0 = 0$ (se cancelan - resonancia!)

Esto confirma que en resonancia ($X_L = X_C$), las corrientes del inductor y capacitor se cancelan.

## Diagrama Fasorial

```
              Im
              │
              │    V₂ = 12.32∠22.5°
              │   ╱
              │  ╱
              │ ╱
    ──────────●─────────── Re
             ╱│
            ╱ │ V₁ = 10∠0°
           ╱  │
          ╱   │
         IL   │
    1.23∠-67.5°
```

## Tabla Resumen

| Cantidad | Forma Rectangular | Forma Polar |
|----------|-------------------|-------------|
| V₁ | 10 + j0 V | 10∠0° V |
| V₂ | 11.38 + j4.71 V | 12.32∠22.5° V |
| IL | 0.471 - j1.14 A | 1.232∠-67.5° A |
| IC | -0.471 + j1.14 A | 1.232∠112.5° A |
| IR1 | -0.138 - j0.471 A | 0.491∠-106.3° A |

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| XL | **10 Ω** |
| XC | **10 Ω** |
| Condición | **Resonancia (XL = XC)** |
| a) V₁ | **10∠0° V** |
| a) V₂ | **12.32∠22.5° V** |
| b) IL | **1.232∠-67.5° A** |
| c) v₂(t) | **12.32cos(1000t + 22.5°) V** |
| c) iL(t) | **1.232cos(1000t - 67.5°) A** |

## Simulación SPICE - Resultados Esperados
```
Análisis AC (f = 159.15 Hz, ω = 1000 rad/s):
VM(2) = 12.32V,  VP(2) = 22.5°
IM(L1) = 1.232A, IP(L1) = -67.5°
```

## Conceptos Aplicados
- Análisis nodal con fasores
- Admitancias: Y = 1/Z
- Condición de resonancia: XL = XC
- Cancelación de corrientes reactivas
- Transformación tiempo ↔ frecuencia