# PR-03: Teorema de Norton ⭐⭐

## Enunciado
Encuentre el [circuito](../../../glossary.md#circuito) equivalente de [Norton](../../../glossary.md#norton) visto desde los terminales a-b para el mismo circuito del problema anterior.
- Vs = 32V
- R₁ = 4Ω, R₂ = 12Ω, R₃ = 6Ω

## Diagrama del Circuito

```
           R₁=4Ω          R₃=6Ω
    ┌─────/\/\/────┬─────/\/\/─────○ a
    │              │               
  + │              │               
(Vs)│             R₂=12Ω          
 32V│              │               
  - │              │               
    │              │               
    └──────────────┴───────────────○ b
```

## Netlist SPICE

```spice
* PR-03: Teorema de Norton
* Calculo de corriente de cortocircuito In

V1 1 0 DC 32V      ; Fuente de voltaje 32V
R1 1 2 4           ; R1 = 4Ω
R2 2 0 12          ; R2 = 12Ω
R3 2 3 6           ; R3 = 6Ω
Vsc 3 0 DC 0V      ; Cortocircuito para medir In

.OP
.PRINT DC I(Vsc)    ; Corriente Norton In
.END
```

```spice
* PR-03b: Circuito equivalente de Norton con carga

In 0 1 DC 2.667A   ; Fuente de corriente Norton
Rn 1 0 9           ; Resistencia Norton (igual a Rth)
RL 1 0 5           ; Carga de 5Ω

.OP
.PRINT DC I(RL)
.END
```

## Solución

### Recordatorio: Datos del Thévenin

Del problema anterior:
- Vth = 24 V
- Rth = 9 Ω

### Método 1: Relación Thévenin-Norton

$$I_N = \frac{V_{th}}{R_{th}} = \frac{24}{9} = 2.667\text{ A}$$

$$R_N = R_{th} = 9\text{ Ω}$$

### Método 2: Corriente de Cortocircuito

**Cortocircuitando los terminales a-b:**

```
           R₁=4Ω          R₃=6Ω
    ┌─────/\/\/────┬─────/\/\/─────┐
    │              │               │
  + │              │              In↓
(Vs)│             R₂=12Ω          │
 32V│              │               │
  - │              │               │
    │              │               │
    └──────────────┴───────────────┘
```

**Análisis del circuito:**
R₃ está en paralelo con el cortocircuito → R₃ = 0 (efectivamente)
R₂ queda en paralelo con un cortocircuito a través de R₃ → R₂ también se cortocircuita

Simplificando: Solo R₁ limita la [corriente](../../../glossary.md#corriente) desde Vs.

**Pero espera**, R₂ no está directamente en paralelo con el cortocircuito. Analicemos más cuidadosamente:

**[Nodo](../../../glossary.md#nodo) 2:**
$$\frac{V_2 - 32}{4} + \frac{V_2}{12} + \frac{V_2 - 0}{6} = 0$$

El tercer término es porque Va = Vb = 0 (cortocircuito).

$$\frac{V_2 - 32}{4} + \frac{V_2}{12} + \frac{V_2}{6} = 0$$

Multiplicando por 12:
$$3(V_2 - 32) + V_2 + 2V_2 = 0$$
$$3V_2 - 96 + V_2 + 2V_2 = 0$$
$$6V_2 = 96$$
$$V_2 = 16\text{ V}$$

**Corriente de Norton:**
$$I_N = \frac{V_2 - 0}{R_3} = \frac{16}{6} = 2.667\text{ A}$$

### Circuito Equivalente de Norton

```
    ○─────────┬─────○ a
              │     
        In ↑  ║  Rn
      2.667A  ║  9Ω
              │     
    ○─────────┴─────○ b
```

### Verificación: Corriente en carga RL = 5Ω

Usando divisor de corriente:
$$I_L = I_N \times \frac{R_N}{R_N + R_L} = 2.667 \times \frac{9}{9 + 5} = 2.667 \times \frac{9}{14}$$

$$I_L = 2.667 \times 0.643 = 1.714\text{ A}$$

Este resultado coincide con el obtenido usando Thévenin ✓

### Comparación Thévenin vs Norton

| Parámetro | Thévenin | Norton |
|-----------|----------|--------|
| Fuente | Vth = 24V (voltaje) | In = 2.667A (corriente) |
| Resistencia | Rth = 9Ω (serie) | Rn = 9Ω (paralelo) |
| Configuración | Fuente + R en serie | Fuente + R en paralelo |

### Transformación entre equivalentes

```
Thévenin:                    Norton:
    Rth                      
○──/\/\/──○ a            ○───┬───○ a
│                            │
+ Vth                   In ↑ ║ Rn
-                            │
○─────────○ b            ○───┴───○ b

    Vth = In × Rn
    In = Vth / Rth
    Rn = Rth
```

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| In | **2.667 A** |
| Rn | **9 Ω** |
| IL (con RL=5Ω) | **1.714 A** |

## Simulación SPICE - Resultados Esperados
```
Corriente cortocircuito:
I(Vsc) = -2.6667E+00  (In = 2.667 A)

Con carga:
I(RL) = 1.7143E+00
```

## Cuándo usar cada equivalente

| Situación | Preferir |
|-----------|----------|
| Carga varía mucho | Thévenin |
| Fuente de corriente | Norton |
| Análisis de corriente | Norton |
| Análisis de voltaje | Thévenin |
| Cargas en paralelo | Norton |
| Cargas en serie | Thévenin |

## Conceptos Aplicados
- Corriente de cortocircuito = In
- Equivalencia Thévenin-Norton
- Rn = Rth siempre
- Transformación de fuentes