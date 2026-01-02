# PR-02: Teorema de Thévenin ⭐⭐

## Enunciado
Encuentre el [circuito](../../../glossary.md#circuito) equivalente de [Thévenin](../../../glossary.md#thevenin) visto desde los terminales a-b. Luego calcule la [corriente](../../../glossary.md#corriente) que circula por una [carga](../../../glossary.md#carga) RL = 5Ω conectada entre dichos terminales.
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
* PR-02: Teorema de Thevenin
* Circuito original

V1 1 0 DC 32V      ; Fuente de voltaje 32V
R1 1 2 4           ; R1 = 4Ω
R2 2 0 12          ; R2 = 12Ω
R3 2 3 6           ; R3 = 6Ω
* Terminal a = nodo 3, Terminal b = nodo 0

.OP
.PRINT DC V(3)      ; Voltaje Vth (circuito abierto)
.END
```

```spice
* PR-02b: Calculo de Rth (fuentes apagadas)

V1 1 0 DC 0V       ; Fuente cortocircuitada
R1 1 2 4           
R2 2 0 12          
R3 2 3 6           
Vtest 3 0 DC 1V    ; Fuente de prueba para medir Rth

.OP
.PRINT DC I(Vtest)  ; Rth = 1V / I(Vtest)
.END
```

```spice
* PR-02c: Circuito equivalente con carga

Vth 1 0 DC 24V     ; Voltaje Thevenin calculado
Rth 1 2 9          ; Resistencia Thevenin calculada
RL 2 0 5           ; Carga de 5Ω

.OP
.PRINT DC I(RL)
.END
```

## Solución

### Paso 1: Calcular Vth (Voltaje de Thévenin)

Vth es el [voltaje](../../../glossary.md#voltaje) de circuito abierto entre los terminales a-b.

**Con terminales abiertos:**
- No circula corriente por R₃ (está en serie con circuito abierto)
- R₁ y R₂ forman un [divisor de tensión](../../../glossary.md#divisor-tension)

$$V_{th} = V_s \times \frac{R_2}{R_1 + R_2} = 32 \times \frac{12}{4 + 12} = 32 \times \frac{12}{16} = 32 \times 0.75$$

$$V_{th} = 24\text{ V}$$

### Paso 2: Calcular Rth (Resistencia de Thévenin)

Rth es la [resistencia](../../../glossary.md#resistencia) vista desde a-b con todas las fuentes independientes apagadas.

**Apagando Vs (cortocircuito):**

```
           R₁=4Ω          R₃=6Ω
    ┌─────/\/\/────┬─────/\/\/─────○ a
    │              │               
cortocircuito     R₂=12Ω          
    │              │               
    └──────────────┴───────────────○ b
```

**Vista desde a-b:**
- R₃ está en serie con (R₁ || R₂)

$$R_1 \| R_2 = \frac{R_1 \times R_2}{R_1 + R_2} = \frac{4 \times 12}{4 + 12} = \frac{48}{16} = 3\text{ Ω}$$

$$R_{th} = R_3 + (R_1 \| R_2) = 6 + 3 = 9\text{ Ω}$$

### Paso 3: Circuito Equivalente de Thévenin

```
        Rth=9Ω
    ○───/\/\/───○ a
    │           
  + │           
(Vth)           
 24V            
  - │           
    │           
    ○───────────○ b
```

### Paso 4: Corriente en la carga RL = 5Ω

Conectando RL entre a-b:

$$I_L = \frac{V_{th}}{R_{th} + R_L} = \frac{24}{9 + 5} = \frac{24}{14} = 1.714\text{ A}$$

**Voltaje en la carga:**
$$V_L = I_L \times R_L = 1.714 \times 5 = 8.57\text{ V}$$

**Potencia en la carga:**
$$P_L = I_L^2 \times R_L = (1.714)^2 \times 5 = 14.7\text{ W}$$

## Verificación Directa

**Análisis del circuito original con RL conectada:**

Usando análisis nodal en el nodo 2:
$$\frac{V_2 - 32}{4} + \frac{V_2}{12} + \frac{V_2 - V_a}{6} = 0$$

Con $V_a = I_L \times 5$ y $I_L = \frac{V_2 - V_a}{6}$:

Resolviendo el sistema:
$$I_L = 1.714\text{ A} \checkmark$$

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| Vth | **24 V** |
| Rth | **9 Ω** |
| IL (con RL=5Ω) | **1.714 A** |
| VL | **8.57 V** |
| PL | **14.7 W** |

## Simulación SPICE - Resultados Esperados
```
Circuito abierto:
V(3) = 24.0000  (Vth)

Con fuente de prueba:
I(Vtest) = 0.1111  → Rth = 1/0.1111 = 9Ω

Con carga:
I(RL) = 1.7143E+00
```

## Diagrama del Equivalente de Thévenin

```
    ┌────/\/\/────○ a
    │   Rth=9Ω    │
  + │             │
(Vth)            RL
 24V             5Ω
  - │             │
    │             │
    └─────────────○ b
```

## Conceptos Aplicados
- Voltaje de circuito abierto = Vth
- Resistencia con fuentes apagadas = Rth
- Simplificación de circuitos
- Análisis de carga variable