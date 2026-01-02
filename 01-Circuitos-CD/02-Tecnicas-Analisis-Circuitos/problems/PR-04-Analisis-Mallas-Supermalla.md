# PR-04: Análisis de Mallas con Supermalla ⭐⭐⭐

## Enunciado
Utilizando el método de mallas con supermalla, determine las corrientes de [malla](../../../glossary.md#malla) en el [circuito](../../../glossary.md#circuito).
- Vs = 24V
- Is = 3A (fuente de [corriente](../../../glossary.md#corriente) en rama compartida)
- R₁ = 4Ω, R₂ = 8Ω, R₃ = 6Ω, R₄ = 2Ω

## Diagrama del Circuito

```
           R₁=4Ω           R₃=6Ω
    ┌─────/\/\/─────┬─────/\/\/─────┐
    │               │               │
  + │               ↓               │
(Vs)│   i₁ ⟳      Is=3A    i₂ ⟳   │
 24V│               │               │
  - │               │               │
    │    R₂=8Ω     │     R₄=2Ω    │
    └────/\/\/──────┴────/\/\/──────┘
```

La fuente de corriente Is está en la rama compartida entre las mallas 1 y 2.

## Netlist SPICE

```spice
* PR-04: Analisis de Mallas con Supermalla
* Fuente de corriente en rama compartida

V1 1 0 DC 24V      ; Fuente de voltaje 24V
R1 1 2 4           ; R1 = 4Ω
R2 1 3 8           ; R2 = 8Ω (rama inferior malla 1)
I1 2 3 DC 3A       ; Fuente de corriente 3A (de nodo 2 a nodo 3)
R3 2 4 6           ; R3 = 6Ω
R4 3 4 2           ; R4 = 2Ω (rama inferior malla 2)
Rg 4 0 1m          ; Conexión a tierra (cortocircuito)

.OP
.PRINT DC I(R1) I(R2) I(R3) I(R4)
.END
```

## Solución

### Datos
- Vs = 24 V
- Is = 3 A
- R₁ = 4 Ω, R₂ = 8 Ω, R₃ = 6 Ω, R₄ = 2 Ω

### Identificación de la Supermalla

La fuente de corriente Is está en la rama compartida entre mallas 1 y 2. Debemos:
1. Formar una supermalla que englobe ambas mallas (evitando la fuente de corriente)
2. Añadir la ecuación de restricción de la fuente de corriente

### Paso 1: Ecuación de restricción

La fuente de corriente define la relación:
$$i_1 - i_2 = I_s = 3\text{ A} \quad \text{...(1)}$$

### Paso 2: Ecuación de la Supermalla (LVK)

Recorriendo el contorno exterior de ambas mallas (evitando Is):
$$-V_s + i_1 R_1 + i_2 R_3 + i_2 R_4 + i_1 R_2 = 0$$

$$-24 + 4i_1 + 6i_2 + 2i_2 + 8i_1 = 0$$

$$12i_1 + 8i_2 = 24$$

Dividiendo por 4:
$$3i_1 + 2i_2 = 6 \quad \text{...(2)}$$

### Paso 3: Resolver el sistema

De (1): $i_1 = i_2 + 3$

Sustituyendo en (2):
$$3(i_2 + 3) + 2i_2 = 6$$
$$3i_2 + 9 + 2i_2 = 6$$
$$5i_2 = -3$$
$$i_2 = -0.6\text{ A}$$

$$i_1 = -0.6 + 3 = 2.4\text{ A}$$

### Paso 4: Corrientes de rama

**Corriente por R₁:**
$$I_{R1} = i_1 = 2.4\text{ A}$$

**Corriente por R₂:**
$$I_{R2} = i_1 = 2.4\text{ A}$$

**Corriente por R₃:**
$$I_{R3} = i_2 = -0.6\text{ A}$$ (fluye en dirección opuesta a i₂)

**Corriente por R₄:**
$$I_{R4} = i_2 = -0.6\text{ A}$$

**Corriente por la fuente Is:**
$$I_{Is} = i_1 - i_2 = 2.4 - (-0.6) = 3\text{ A} \checkmark$$

### Verificación con LVK

**Malla 1 (evitando Is, usando la rama R₂):**
$$-24 + 4(2.4) + 8(2.4) = -24 + 9.6 + 19.2 = 4.8 \neq 0$$

Esto indica que necesitamos incluir el [voltaje](../../../glossary.md#voltaje) de la fuente de corriente.

**Verificación alternativa - Balance de potencia:**

$$P_{Vs} = V_s \cdot i_1 = 24 \times 2.4 = 57.6\text{ W (entregada)}$$

$$P_{R1} = i_1^2 R_1 = (2.4)^2 \times 4 = 23.04\text{ W}$$
$$P_{R2} = i_1^2 R_2 = (2.4)^2 \times 8 = 46.08\text{ W}$$
$$P_{R3} = i_2^2 R_3 = (0.6)^2 \times 6 = 2.16\text{ W}$$
$$P_{R4} = i_2^2 R_4 = (0.6)^2 \times 2 = 0.72\text{ W}$$

$$P_{resistencias} = 23.04 + 46.08 + 2.16 + 0.72 = 72\text{ W}$$

La diferencia es absorbida/entregada por la fuente de corriente:
$$P_{Is} = 72 - 57.6 = 14.4\text{ W}$$

## Respuestas

| Variable | Valor |
|----------|-------|
| i₁ | **2.4 A** |
| i₂ | **-0.6 A** |
| I_{R1} | **2.4 A** |
| I_{R2} | **2.4 A** |
| I_{R3} | **0.6 A** (dirección opuesta) |
| I_{R4} | **0.6 A** (dirección opuesta) |

## Simulación SPICE - Resultados Esperados
```
Operating Point:
I(R1) = 2.4000E+00
I(R2) = 2.4000E+00
I(R3) = -6.0000E-01
I(R4) = -6.0000E-01
```

## Procedimiento para Supermallas

1. **Identificar** fuentes de corriente en ramas compartidas
2. **Formar supermalla** que englobe las mallas adyacentes
3. **Escribir ecuación de restricción:** i₁ - i₂ = Is
4. **Aplicar LVK** al contorno exterior de la supermalla
5. **Resolver** el sistema de ecuaciones

## Conceptos Aplicados
- Supermalla para fuentes de corriente
- Ecuación de restricción de corriente
- LVK en supermallas