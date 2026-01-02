# PR-05: Divisor de Corriente ⭐

## Enunciado
En el [circuito](../../../glossary.md#circuito) mostrado, una fuente de [corriente](../../../glossary.md#corriente) de 20mA alimenta dos resistencias en paralelo: R₁ = 4kΩ y R₂ = 6kΩ. Determine:
a) La corriente a través de cada [resistencia](../../../glossary.md#resistencia) usando la regla del [divisor de corriente](../../../glossary.md#divisor-corriente)
b) El [voltaje](../../../glossary.md#voltaje) en el [nodo](../../../glossary.md#nodo) común
c) La potencia disipada en cada resistencia

## Diagrama del Circuito

```
              i₁↓        i₂↓
           ┌───────┬───────┐
           │       │       │
      Is   │      R₁      R₂
     20mA  ↓      4kΩ     6kΩ
       ○───┤       │       │
           │       │       │
           └───────┴───────┘
                   │
                  GND
```

## Netlist SPICE

```spice
* PR-05: Divisor de Corriente
* Dos resistencias en paralelo con fuente de corriente

I1 0 1 DC 20mA     ; Fuente de corriente 20mA
R1 1 0 4k          ; R1 = 4kΩ
R2 1 0 6k          ; R2 = 6kΩ

.OP
.PRINT DC V(1) I(R1) I(R2)
.END
```

## Solución

### Datos
- Is = 20 mA
- R₁ = 4 kΩ
- R₂ = 6 kΩ

### Parte a) Corrientes por divisor de corriente

**Fórmula del divisor de corriente (dos resistencias):**
$$i_1 = I_s \cdot \frac{R_2}{R_1 + R_2}$$
$$i_2 = I_s \cdot \frac{R_1}{R_1 + R_2}$$

**Nota importante:** La corriente se divide de forma inversamente proporcional a la resistencia. La resistencia opuesta va en el numerador.

**Cálculo de i₁:**
$$i_1 = 20\text{ mA} \cdot \frac{6\text{k}}{4\text{k} + 6\text{k}} = 20 \cdot \frac{6}{10} = 20 \cdot 0.6 = 12\text{ mA}$$

**Cálculo de i₂:**
$$i_2 = 20\text{ mA} \cdot \frac{4\text{k}}{4\text{k} + 6\text{k}} = 20 \cdot \frac{4}{10} = 20 \cdot 0.4 = 8\text{ mA}$$

**Verificación ([LCK](../../../glossary.md#lck)):**
$$I_s = i_1 + i_2 = 12 + 8 = 20\text{ mA} \checkmark$$

### Parte b) Voltaje en el nodo

Calculando la resistencia equivalente:
$$R_{eq} = \frac{R_1 \cdot R_2}{R_1 + R_2} = \frac{(4\text{k})(6\text{k})}{10\text{k}} = \frac{24\text{M}}{10\text{k}} = 2.4\text{ kΩ}$$

$$V = I_s \cdot R_{eq} = (20\text{ mA})(2.4\text{ kΩ}) = 48\text{ V}$$

**Verificación con Ley de Ohm:**
$$V = i_1 \cdot R_1 = (12\text{ mA})(4\text{ kΩ}) = 48\text{ V} \checkmark$$
$$V = i_2 \cdot R_2 = (8\text{ mA})(6\text{ kΩ}) = 48\text{ V} \checkmark$$

### Parte c) Potencia en cada resistencia

$$P_1 = i_1^2 \cdot R_1 = (12\text{ mA})^2 (4\text{ kΩ}) = (144 \times 10^{-6})(4000) = 576\text{ mW}$$

$$P_2 = i_2^2 \cdot R_2 = (8\text{ mA})^2 (6\text{ kΩ}) = (64 \times 10^{-6})(6000) = 384\text{ mW}$$

**Potencia total entregada por la fuente:**
$$P_{total} = V \cdot I_s = (48\text{ V})(20\text{ mA}) = 960\text{ mW}$$

**Verificación:**
$$P_1 + P_2 = 576 + 384 = 960\text{ mW} \checkmark$$

## Respuestas

| Magnitud | Valor |
|----------|-------|
| a) i₁ | **12 mA** |
| a) i₂ | **8 mA** |
| b) V | **48 V** |
| c) P₁ | **576 mW** |
| c) P₂ | **384 mW** |

## Simulación SPICE - Resultados Esperados
```
Operating Point:
V(1) = 48.0000
I(R1) = 1.2000E-02  (12 mA)
I(R2) = 8.0000E-03  (8 mA)
```

## Observación
La resistencia menor (R₁ = 4kΩ) conduce más corriente (12mA) que la mayor (R₂ = 6kΩ que conduce 8mA). Esto es consistente con la naturaleza del divisor de corriente.

## Conceptos Aplicados
- Divisor de corriente: i₁ = Is·R₂/(R₁+R₂)
- La corriente es inversamente proporcional a la resistencia
- Conservación de potencia