# PR-02: Máxima Transferencia de Potencia en CA ⭐⭐⭐

## Enunciado
Una fuente de [voltaje](../../../glossary.md#voltaje) Vs = 100∠0° V tiene una [impedancia](../../../glossary.md#impedancia) interna Zs = 40 + j30 Ω. Determine:
a) La impedancia de [carga](../../../glossary.md#carga) ZL para máxima transferencia de potencia
b) La potencia máxima transferida a la carga
c) La potencia disipada en la fuente cuando se entrega potencia máxima
d) La eficiencia del sistema en condición de máxima potencia

## Diagrama del Circuito

```
    Fuente                      Carga
    
         Zs = 40 + j30 Ω         ZL = ?
    ●─────────◯─────────────●─────────●
    │                       │         │
  + │                     ┌─┴─┐       │
Vs (─)                    │ZL │       │
100V│                     │   │       │
  - │                     └─┬─┘       │
    ●───────────────────────┴─────────┘
    
Para máxima potencia: ZL = Zs*
```

## Netlist SPICE

```spice
* PR-02: Máxima Transferencia de Potencia en CA
* Con ZL = Zs* (conjugado)

V1 1 0 AC 100 0       ; Fuente 100V∠0°

* Impedancia fuente: Zs = 40 + j30 Ω
Rs 1 2 40             ; Parte resistiva
* XL = 30Ω → L = 30/(2π×60) = 79.6mH (a 60Hz)
Ls 2 3 79.6m          ; Parte inductiva

* Impedancia de carga óptima: ZL = 40 - j30 Ω (conjugado)
RL 3 0 40             ; Parte resistiva
* XC = 30Ω → C = 1/(2π×60×30) = 88.4μF
CL 3 0 88.4u          ; Parte capacitiva

.AC LIN 1 60 60
.PRINT AC VM(3) IM(Rs) 
.END
```

## Solución

### Datos
- Vs = 100∠0° V
- Zs = 40 + j30 Ω = 50∠36.87° Ω
- f = 60 Hz (asumida)

### Parte a) Impedancia de carga para máxima potencia

**[Teorema de](../../../glossary.md#norton) máxima transferencia de potencia en CA:**

Para transferir máxima potencia a la carga, la impedancia de carga debe ser el **conjugado complejo** de la impedancia de la fuente:

$$Z_L = Z_s^* = (40 + j30)^* = 40 - j30\text{ Ω}$$

$$\boxed{Z_L = 40 - j30\text{ Ω} = 50\angle -36.87°\text{ Ω}}$$

Esto significa:
- RL = Rs = 40 Ω (resistencias iguales)
- XL = -Xs = -30 Ω ([reactancia](../../../glossary.md#reactancia) capacitiva para cancelar la inductiva)

### Parte b) Potencia máxima transferida

**Impedancia total del [circuito](../../../glossary.md#circuito):**
$$Z_{total} = Z_s + Z_L = (40 + j30) + (40 - j30) = 80 + j0 = 80\text{ Ω}$$

La parte reactiva se cancela completamente.

**Corriente en el circuito:**
$$I = \frac{V_s}{Z_{total}} = \frac{100\angle 0°}{80\angle 0°} = 1.25\angle 0°\text{ A}$$

**Potencia máxima en la carga:**
$$P_{max} = |I|^2 \times R_L = (1.25)^2 \times 40$$

$$\boxed{P_{max} = 62.5\text{ W}}$$

**Fórmula alternativa:**
$$P_{max} = \frac{|V_s|^2}{4R_s} = \frac{100^2}{4 \times 40} = \frac{10000}{160} = 62.5\text{ W ✓}$$

### Parte c) Potencia disipada en la fuente

**Potencia en la resistencia de la fuente:**
$$P_s = |I|^2 \times R_s = (1.25)^2 \times 40$$

$$\boxed{P_{fuente} = 62.5\text{ W}}$$

La potencia en la parte reactiva de Zs es reactiva (no disipada):
$$Q_s = |I|^2 \times X_s = (1.25)^2 \times 30 = 46.875\text{ VAR}$$

Pero esta [potencia reactiva](../../../glossary.md#potencia-reactiva) es cancelada por la parte capacitiva de ZL:
$$Q_L = |I|^2 \times X_L = (1.25)^2 \times (-30) = -46.875\text{ VAR}$$

$$Q_{total} = Q_s + Q_L = 0\text{ VAR}$$

### Parte d) Eficiencia del sistema

$$\eta = \frac{P_{carga}}{P_{total}} = \frac{P_L}{P_L + P_s}$$

$$\eta = \frac{62.5}{62.5 + 62.5} = \frac{62.5}{125}$$

$$\boxed{\eta = 0.5 = 50\%}$$

**Conclusión importante:** En condición de máxima transferencia de potencia, la eficiencia siempre es 50%. Esto es porque la potencia en la carga es igual a la potencia disipada en la fuente.

## Análisis de Potencia vs Impedancia de Carga

¿Qué pasa si ZL ≠ Zs*?

### Caso 1: Solo resistencia (XL = 0)

Si ZL = RL (puramente resistiva):

La potencia máxima ocurre cuando:
$$R_L = |Z_s| = \sqrt{R_s^2 + X_s^2} = \sqrt{40^2 + 30^2} = 50\text{ Ω}$$

$$P = \frac{|V_s|^2 R_L}{(R_s + R_L)^2 + X_s^2}$$

Con RL = 50Ω:
$$P = \frac{100^2 \times 50}{(40 + 50)^2 + 30^2} = \frac{500000}{8100 + 900} = \frac{500000}{9000} = 55.56\text{ W}$$

Esta potencia es **menor** que los 62.5W con ZL = Zs*.

### Caso 2: Comparación

| Condición | ZL | P_carga | Eficiencia |
|-----------|-----|---------|------------|
| Máx. potencia | 40-j30 Ω | 62.5 W | 50% |
| Solo R óptima | 50+j0 Ω | 55.56 W | 55.2% |
| R = Rs | 40+j0 Ω | 48 W | 50% |

## Gráfica de Potencia vs RL (con XL fija)

```
P (W)
    │
62.5├────────●──────── Máximo (ZL = Zs*)
    │       ╱│╲
 55 │      ╱ │ ╲
    │     ╱  │  ╲ Con XL = 0
 50 │────╱───┼───╲────
    │   ╱    │    ╲
 40 │  ╱     │     ╲
    │ ╱      │      ╲
    │╱       │       ╲
  0 └─┴──────┴────────┴──► RL (Ω)
      0     40    50   80
            Rs   |Zs|  2Rs
```

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| a) ZL óptima | **40 - j30 Ω** |
| a) |ZL| | **50 Ω** |
| b) P máxima | **62.5 W** |
| c) P fuente | **62.5 W** |
| d) Eficiencia | **50%** |
| I circuito | **1.25 A** |

## Componentes para ZL = 40 - j30 Ω @ 60 Hz

- **[Resistencia](../../../glossary.md#resistencia):** RL = 40 Ω
- **[Capacitancia](../../../glossary.md#capacitancia):** C = 1/(ωXC) = 1/(377×30) = 88.4 μF

## Netlist SPICE - Verificación

```spice
* Verificación con diferentes cargas

* Caso 1: ZL = Zs* (máxima potencia)
V1 1 0 AC 100 0
Rs1 1 2 40
Ls1 2 3 79.6m
RL1 3 0 40
CL1 3 0 88.4u
* Resultado esperado: P = 62.5W

* Caso 2: ZL puramente resistiva óptima
V2 11 0 AC 100 0
Rs2 11 12 40
Ls2 12 13 79.6m
RL2 13 0 50
* Resultado esperado: P = 55.56W

.AC LIN 1 60 60
.PRINT AC IM(Rs1) VM(3) IM(Rs2) VM(13)
.END
```

## Conceptos Aplicados
- [Teorema de](../../../glossary.md#thevenin) máxima transferencia de potencia en CA
- Conjugado complejo de impedancia
- Cancelación de reactancias
- Compromiso potencia vs eficiencia
- [Factor de potencia](../../../glossary.md#factor-potencia) unitario en máxima transferencia