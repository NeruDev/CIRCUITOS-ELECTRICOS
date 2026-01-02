# PR-03: Resistencias en Paralelo ⭐

## Enunciado
Una fuente de corriente de 12mA alimenta tres resistencias en paralelo: R₁ = 6kΩ, R₂ = 3kΩ, R₃ = 2kΩ. Determine:
a) La resistencia equivalente
b) El voltaje en las resistencias
c) La corriente a través de cada resistencia
d) Verifique la LCK en el nodo superior

## Diagrama del Circuito

```
           ┌────────┬────────┬────────┐
           │        │        │        │
      Is   │       R₁       R₂       R₃
     12mA  ↓       6kΩ      3kΩ      2kΩ
       ○   │        │        │        │
           │        │        │        │
           └────────┴────────┴────────┘
                    │
                   GND
```

## Netlist SPICE

```spice
* PR-03: Resistencias en Paralelo
* Circuito paralelo con fuente de corriente

I1 0 1 DC 12mA     ; Fuente de corriente 12mA (de nodo 0 a nodo 1)
R1 1 0 6k          ; R1 = 6kΩ en paralelo
R2 1 0 3k          ; R2 = 3kΩ en paralelo
R3 1 0 2k          ; R3 = 2kΩ en paralelo

.OP
.PRINT DC V(1) I(R1) I(R2) I(R3)
.END
```

## Solución

### Datos
- Is = 12 mA
- R₁ = 6 kΩ, R₂ = 3 kΩ, R₃ = 2 kΩ

### Parte a) Resistencia equivalente

Para resistencias en paralelo:
$$\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}$$

$$\frac{1}{R_{eq}} = \frac{1}{6\text{k}} + \frac{1}{3\text{k}} + \frac{1}{2\text{k}}$$

$$\frac{1}{R_{eq}} = \frac{1}{6000} + \frac{1}{3000} + \frac{1}{2000}$$

$$\frac{1}{R_{eq}} = \frac{1 + 2 + 3}{6000} = \frac{6}{6000} = \frac{1}{1000}$$

$$R_{eq} = 1\text{ kΩ}$$

### Parte b) Voltaje en las resistencias

En paralelo, todas las resistencias tienen el mismo voltaje:
$$V = I_s \cdot R_{eq} = (12\text{ mA})(1\text{ kΩ}) = 12\text{ V}$$

### Parte c) Corriente en cada resistencia

$$I_1 = \frac{V}{R_1} = \frac{12\text{ V}}{6\text{ kΩ}} = 2\text{ mA}$$

$$I_2 = \frac{V}{R_2} = \frac{12\text{ V}}{3\text{ kΩ}} = 4\text{ mA}$$

$$I_3 = \frac{V}{R_3} = \frac{12\text{ V}}{2\text{ kΩ}} = 6\text{ mA}$$

### Parte d) Verificación con LCK

En el nodo superior:
$$I_s = I_1 + I_2 + I_3$$
$$12\text{ mA} = 2\text{ mA} + 4\text{ mA} + 6\text{ mA}$$
$$12\text{ mA} = 12\text{ mA} \checkmark$$

## Respuestas

| Magnitud | Valor |
|----------|-------|
| a) Req | **1 kΩ** |
| b) V | **12 V** |
| c) I₁ | **2 mA** |
| c) I₂ | **4 mA** |
| c) I₃ | **6 mA** |

## Simulación SPICE - Resultados Esperados
```
Operating Point:
V(1) = 12.0000
I(R1) = 2.0000E-03
I(R2) = 4.0000E-03
I(R3) = 6.0000E-03
```

## Nota Importante
Observe que la resistencia más pequeña (R₃ = 2kΩ) lleva la mayor corriente (6mA). En paralelo, la corriente se divide inversamente proporcional a la resistencia.

## Conceptos Aplicados
- Resistencias en paralelo: 1/Req = 1/R₁ + 1/R₂ + ... + 1/Rₙ
- Voltaje igual en paralelo
- Ley de Corrientes de Kirchhoff (LCK)