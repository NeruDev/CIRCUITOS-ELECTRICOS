```markdown
# PR-02: Análisis Nodal con Supernodo ⭐⭐⭐

## Enunciado
Utilizando el método de nodos con supernodo, encuentre los voltajes en todos los nodos del circuito.
- Vs = 10V (fuente de voltaje)
- Is = 2A (fuente de corriente)
- R₁ = 2Ω, R₂ = 4Ω, R₃ = 6Ω, R₄ = 3Ω

## Diagrama del Circuito

```
             R₁=2Ω
    ┌────────/\/\/────────┐
    │                     │
    │     V₁    + Vs -   V₂          V₃
    │      ○─────┤├─────○───/\/\/───○
    │      │    10V      │   R₃=6Ω   │
   Is↑    R₂             │           R₄
   2A     4Ω             │           3Ω
    │      │             │           │
    └──────┴─────────────┴───────────┘
                         │
                        GND
```

## Netlist SPICE

```spice
* PR-02: Analisis Nodal con Supernodo
* Circuito con fuente de voltaje entre nodos no referenciados

I1 0 1 DC 2A       ; Fuente de corriente 2A
R1 1 2 2           ; R1 = 2Ω
R2 1 0 4           ; R2 = 4Ω
V1 1 2 DC 10V      ; Fuente de voltaje 10V (V1 - V2 = 10V)
R3 2 3 6           ; R3 = 6Ω
R4 3 0 3           ; R4 = 3Ω

.OP
.PRINT DC V(1) V(2) V(3)
.END
```

## Solución

### Datos
- Vs = 10 V (entre nodos 1 y 2)
- Is = 2 A
- R₁ = 2 Ω, R₂ = 4 Ω, R₃ = 6 Ω, R₄ = 3 Ω

### Identificación del Supernodo

La fuente de voltaje Vs conecta los nodos V₁ y V₂ sin pasar por tierra. Estos dos nodos forman un **supernodo**.

### Paso 1: Ecuación de restricción del supernodo

$$V_1 - V_2 = 10\text{ V} \quad \text{...(1)}$$

### Paso 2: Aplicar LCK al supernodo (V₁ y V₂ juntos)

Sumando todas las corrientes que entran y salen del supernodo:

$$I_s - \frac{V_1}{R_2} - \frac{V_1 - 0}{R_1}^* - \frac{V_2 - V_3}{R_3} = 0$$

*Nota: R₁ está dentro del supernodo, así que no se considera en LCK del supernodo.*

Corrigiendo la ecuación:
$$I_s - \frac{V_1}{R_2} - \frac{V_2 - V_3}{R_3} = 0$$

$$2 - \frac{V_1}{4} - \frac{V_2 - V_3}{6} = 0$$

Multiplicando por 12:
$$24 - 3V_1 - 2(V_2 - V_3) = 0$$
$$24 - 3V_1 - 2V_2 + 2V_3 = 0$$
$$3V_1 + 2V_2 - 2V_3 = 24 \quad \text{...(2)}$$

### Paso 3: Ecuación en el nodo V₃

$$\frac{V_2 - V_3}{R_3} - \frac{V_3}{R_4} = 0$$

$$\frac{V_2 - V_3}{6} - \frac{V_3}{3} = 0$$

Multiplicando por 6:
$$V_2 - V_3 - 2V_3 = 0$$
$$V_2 - 3V_3 = 0$$
$$V_2 = 3V_3 \quad \text{...(3)}$$

### Paso 4: Resolver el sistema

De (1): $V_1 = V_2 + 10$

De (3): $V_2 = 3V_3$, entonces $V_1 = 3V_3 + 10$

Sustituyendo en (2):
$$3(3V_3 + 10) + 2(3V_3) - 2V_3 = 24$$
$$9V_3 + 30 + 6V_3 - 2V_3 = 24$$
$$13V_3 = -6$$
$$V_3 = -\frac{6}{13} = -0.462\text{ V}$$

$$V_2 = 3(-0.462) = -1.385\text{ V}$$

$$V_1 = -1.385 + 10 = 8.615\text{ V}$$

### Paso 5: Calcular corrientes

$$I_{R1} = \frac{V_1 - V_2}{R_1} = \frac{8.615 - (-1.385)}{2} = \frac{10}{2} = 5\text{ A}$$

$$I_{R2} = \frac{V_1}{R_2} = \frac{8.615}{4} = 2.154\text{ A}$$

$$I_{R3} = \frac{V_2 - V_3}{R_3} = \frac{-1.385 - (-0.462)}{6} = \frac{-0.923}{6} = -0.154\text{ A}$$

$$I_{R4} = \frac{V_3}{R_4} = \frac{-0.462}{3} = -0.154\text{ A}$$

### Verificación

**LCK en nodo V₃:**
$$I_{R3} = I_{R4}$$
$$-0.154 = -0.154 \checkmark$$

## Respuestas

| Variable | Valor | Exacto |
|----------|-------|--------|
| V₁ | **8.615 V** | 112/13 V |
| V₂ | **-1.385 V** | -18/13 V |
| V₃ | **-0.462 V** | -6/13 V |
| I_{R1} | **5 A** | A través de la fuente |
| I_{R2} | **2.154 A** | 28/13 A |
| I_{R3} | **-0.154 A** | -2/13 A |
| I_{R4} | **-0.154 A** | -2/13 A |

## Simulación SPICE - Resultados Esperados
```
Operating Point:
V(1) = 8.6154
V(2) = -1.3846
V(3) = -4.6154E-01
```

## Procedimiento para Supernodos

1. **Identificar** fuentes de voltaje entre nodos no referenciados
2. **Crear supernodo** englobando los nodos conectados por la fuente
3. **Escribir ecuación de restricción:** V₁ - V₂ = Vs
4. **Aplicar LCK** al contorno del supernodo
5. **Resolver** el sistema de ecuaciones

## Conceptos Aplicados
- Supernodo para manejar fuentes de voltaje
- Ecuación de restricción
- LCK en supernodos
```
