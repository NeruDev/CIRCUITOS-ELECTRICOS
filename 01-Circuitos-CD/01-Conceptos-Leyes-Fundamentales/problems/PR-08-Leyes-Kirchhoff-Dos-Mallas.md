# PR-08: Leyes de Kirchhoff - Circuito con Dos Mallas ⭐⭐

## Enunciado
En el circuito mostrado, determine las corrientes I₁, I₂ e I₃ usando las Leyes de Kirchhoff.
- V₁ = 12V, V₂ = 6V
- R₁ = 2Ω, R₂ = 4Ω, R₃ = 6Ω

## Diagrama del Circuito

```
      I₁→    R₁=2Ω    I₃↓    R₂=4Ω    ←I₂
    ┌──────/\/\/──────┬────/\/\/──────┐
    │                 │               │
  + │                 │               │ +
   (V₁)              R₃              (V₂)
   12V               6Ω               6V
  - │                 │               │ -
    │                 │               │
    └─────────────────┴───────────────┘
```

## Netlist SPICE

```spice
* PR-08: Leyes de Kirchhoff - Dos Mallas
* Circuito con dos fuentes de voltaje

V1 1 0 DC 12V      ; Fuente V1 = 12V
V2 3 0 DC 6V       ; Fuente V2 = 6V
R1 1 2 2           ; R1 = 2Ω
R2 2 3 4           ; R2 = 4Ω
R3 2 0 6           ; R3 = 6Ω

.OP
.PRINT DC I(R1) I(R2) I(R3)
.END
```

## Solución

### Datos
- V₁ = 12 V, V₂ = 6 V
- R₁ = 2 Ω, R₂ = 4 Ω, R₃ = 6 Ω

### Método: LCK + LVK

**Paso 1: Definir corrientes**
- I₁: corriente desde V₁ a través de R₁ (hacia la derecha)
- I₂: corriente hacia V₂ a través de R₂ (hacia la izquierda)
- I₃: corriente a través de R₃ (hacia abajo)

**Paso 2: Aplicar LCK en el nodo central**
$$I_1 = I_2 + I_3 \quad \text{...(1)}$$

**Paso 3: Aplicar LVK a la Malla 1 (izquierda, sentido horario)**
$$-V_1 + I_1 R_1 + I_3 R_3 = 0$$
$$-12 + 2I_1 + 6I_3 = 0$$
$$2I_1 + 6I_3 = 12 \quad \text{...(2)}$$

**Paso 4: Aplicar LVK a la Malla 2 (derecha, sentido horario)**
$$-I_3 R_3 + I_2 R_2 + V_2 = 0$$
$$-6I_3 + 4I_2 + 6 = 0$$
$$4I_2 - 6I_3 = -6 \quad \text{...(3)}$$

**Paso 5: Resolver el sistema de ecuaciones**

De (1): $I_1 = I_2 + I_3$

Sustituyendo en (2):
$$2(I_2 + I_3) + 6I_3 = 12$$
$$2I_2 + 2I_3 + 6I_3 = 12$$
$$2I_2 + 8I_3 = 12 \quad \text{...(4)}$$

De (3): $I_2 = \frac{6I_3 - 6}{4} = 1.5I_3 - 1.5$

Sustituyendo en (4):
$$2(1.5I_3 - 1.5) + 8I_3 = 12$$
$$3I_3 - 3 + 8I_3 = 12$$
$$11I_3 = 15$$
$$I_3 = \frac{15}{11} = 1.364\text{ A}$$

**Calculando I₂:**
$$I_2 = 1.5(1.364) - 1.5 = 2.045 - 1.5 = 0.545\text{ A}$$

**Calculando I₁:**
$$I_1 = I_2 + I_3 = 0.545 + 1.364 = 1.909\text{ A}$$

### Verificación

**LVK Malla 1:**
$$-12 + 2(1.909) + 6(1.364) = -12 + 3.818 + 8.182 = 0 \checkmark$$

**LVK Malla 2:**
$$-6(1.364) + 4(0.545) + 6 = -8.182 + 2.182 + 6 = 0 \checkmark$$

## Respuestas

| Corriente | Valor | Dirección |
|-----------|-------|-----------|
| I₁ | **1.909 A** | Hacia la derecha |
| I₂ | **0.545 A** | Hacia la izquierda |
| I₃ | **1.364 A** | Hacia abajo |

O en fracciones exactas:

| Corriente | Valor exacto |
|-----------|--------------|
| I₁ | **21/11 A ≈ 1.909 A** |
| I₂ | **6/11 A ≈ 0.545 A** |
| I₃ | **15/11 A ≈ 1.364 A** |

## Simulación SPICE - Resultados Esperados
```
Operating Point:
I(R1) = 1.9091E+00  (1.909 A)
I(R2) = 5.4545E-01  (0.545 A)
I(R3) = 1.3636E+00  (1.364 A)
V(2) = 8.1818       (Voltaje en nodo central)
```

## Conceptos Aplicados
- Ley de Corrientes de Kirchhoff (LCK)
- Ley de Voltajes de Kirchhoff (LVK)
- Sistemas de ecuaciones lineales
- Convención de signos