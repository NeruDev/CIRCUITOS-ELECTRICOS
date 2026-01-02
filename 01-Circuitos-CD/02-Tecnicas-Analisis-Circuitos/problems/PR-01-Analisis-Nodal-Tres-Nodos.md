# PR-01: Análisis Nodal - Circuito con Tres Nodos ⭐⭐

## Enunciado
Usando el método de nodos, determine los voltajes V₁ y V₂, y las corrientes en cada resistencia.
- Is = 5A (fuente de corriente)
- R₁ = 2Ω, R₂ = 4Ω, R₃ = 8Ω, R₄ = 4Ω

## Diagrama del Circuito

```
        R₁=2Ω          R₃=8Ω
    ┌───/\/\/───┬───/\/\/───┐
    │           │           │
    │     V₁    │    V₂     │
   Is↓          R₂         R₄
   5A          4Ω          4Ω
    │           │           │
    └───────────┴───────────┘
                │
               GND (Ref)
```

## Netlist SPICE

```spice
* PR-01: Analisis Nodal - Tres Nodos
* Metodo de nodos con fuente de corriente

I1 0 1 DC 5A       ; Fuente de corriente 5A (de tierra a nodo 1)
R1 1 0 2           ; R1 = 2Ω entre nodo 1 y tierra
R2 1 2 4           ; R2 = 4Ω entre nodos 1 y 2
R3 2 0 8           ; R3 = 8Ω entre nodo 2 y tierra
R4 2 3 4           ; R4 = 4Ω (continuación)
Rg 3 0 1m          ; Conexión a tierra

.OP
.PRINT DC V(1) V(2) I(R1) I(R2) I(R3) I(R4)
.END
```

**Nota:** El circuito simplificado tiene R₄ en paralelo con R₃.

```spice
* PR-01 Simplificado: Analisis Nodal

I1 0 1 DC 5A       ; Fuente de corriente 5A
R1 1 0 2           ; R1 = 2Ω
R2 1 2 4           ; R2 = 4Ω
R3 2 0 8           ; R3 = 8Ω
R4 2 0 4           ; R4 = 4Ω en paralelo con R3

.OP
.PRINT DC V(1) V(2)
.END
```

## Solución

### Datos
- Is = 5 A
- R₁ = 2 Ω, R₂ = 4 Ω, R₃ = 8 Ω, R₄ = 4 Ω
- Nodo de referencia: tierra (GND)
- Variables: V₁ y V₂

### Paso 1: Ecuaciones nodales

**Nodo 1:** (LCK: suma de corrientes = 0)

Las corrientes que salen del nodo 1:
$$\frac{V_1 - 0}{R_1} + \frac{V_1 - V_2}{R_2} = I_s$$

$$\frac{V_1}{2} + \frac{V_1 - V_2}{4} = 5$$

Multiplicando por 4:
$$2V_1 + V_1 - V_2 = 20$$
$$3V_1 - V_2 = 20 \quad \text{...(1)}$$

**Nodo 2:** (LCK)

$$\frac{V_2 - V_1}{R_2} + \frac{V_2}{R_3} + \frac{V_2}{R_4} = 0$$

$$\frac{V_2 - V_1}{4} + \frac{V_2}{8} + \frac{V_2}{4} = 0$$

Multiplicando por 8:
$$2(V_2 - V_1) + V_2 + 2V_2 = 0$$
$$-2V_1 + 2V_2 + V_2 + 2V_2 = 0$$
$$-2V_1 + 5V_2 = 0 \quad \text{...(2)}$$

### Paso 2: Resolver el sistema

De (2): $V_1 = \frac{5V_2}{2} = 2.5V_2$

Sustituyendo en (1):
$$3(2.5V_2) - V_2 = 20$$
$$7.5V_2 - V_2 = 20$$
$$6.5V_2 = 20$$
$$V_2 = \frac{20}{6.5} = \frac{40}{13} = 3.077\text{ V}$$

$$V_1 = 2.5(3.077) = 7.692\text{ V}$$

### Paso 3: Calcular corrientes

$$I_{R1} = \frac{V_1}{R_1} = \frac{7.692}{2} = 3.846\text{ A}$$

$$I_{R2} = \frac{V_1 - V_2}{R_2} = \frac{7.692 - 3.077}{4} = \frac{4.615}{4} = 1.154\text{ A}$$

$$I_{R3} = \frac{V_2}{R_3} = \frac{3.077}{8} = 0.385\text{ A}$$

$$I_{R4} = \frac{V_2}{R_4} = \frac{3.077}{4} = 0.769\text{ A}$$

### Verificación con LCK

**Nodo 1:**
$$I_s = I_{R1} + I_{R2}$$
$$5 = 3.846 + 1.154 = 5\text{ A} \checkmark$$

**Nodo 2:**
$$I_{R2} = I_{R3} + I_{R4}$$
$$1.154 = 0.385 + 0.769 = 1.154\text{ A} \checkmark$$

## Respuestas

| Variable | Valor | Exacto |
|----------|-------|--------|
| V₁ | **7.692 V** | 100/13 V |
| V₂ | **3.077 V** | 40/13 V |
| I_{R1} | **3.846 A** | 50/13 A |
| I_{R2} | **1.154 A** | 15/13 A |
| I_{R3} | **0.385 A** | 5/13 A |
| I_{R4} | **0.769 A** | 10/13 A |

## Simulación SPICE - Resultados Esperados
```
Operating Point:
V(1) = 7.6923
V(2) = 3.0769
I(R1) = 3.8462E+00
I(R2) = 1.1538E+00
I(R3) = 3.8462E-01
I(R4) = 7.6923E-01
```

## Forma Matricial

$$\begin{bmatrix} G_{11} & G_{12} \\ G_{21} & G_{22} \end{bmatrix} \begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} I_1 \\ I_2 \end{bmatrix}$$

Donde:
- $G_{11} = \frac{1}{R_1} + \frac{1}{R_2} = \frac{1}{2} + \frac{1}{4} = 0.75$ S
- $G_{22} = \frac{1}{R_2} + \frac{1}{R_3} + \frac{1}{R_4} = \frac{1}{4} + \frac{1}{8} + \frac{1}{4} = 0.625$ S
- $G_{12} = G_{21} = -\frac{1}{R_2} = -0.25$ S

$$\begin{bmatrix} 0.75 & -0.25 \\ -0.25 & 0.625 \end{bmatrix} \begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} 5 \\ 0 \end{bmatrix}$$

## Conceptos Aplicados
- Análisis nodal sistemático
- Matriz de conductancias
- LCK en cada nodo