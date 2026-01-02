# PR-06: Circuito Mixto Serie-Paralelo ⭐⭐

## Enunciado
Para el circuito mostrado con Vs = 36V, R₁ = 6kΩ, R₂ = 4kΩ, R₃ = 12kΩ, determine:
a) La resistencia equivalente total
b) La corriente total del circuito
c) El voltaje y corriente en cada resistencia
d) La potencia total disipada

## Diagrama del Circuito

```
         R₁=6kΩ
    ┌───/\/\/───┬───────────┐
    │           │           │
  + │          R₂          R₃
(Vs)│ 36V      4kΩ        12kΩ
  - │           │           │
    │           │           │
    └───────────┴───────────┘
                │
               GND
```

R₂ y R₃ están en paralelo, y ese paralelo está en serie con R₁.

## Netlist SPICE

```spice
* PR-06: Circuito Mixto Serie-Paralelo
* R1 en serie con (R2 || R3)

V1 1 0 DC 36V      ; Fuente de voltaje 36V
R1 1 2 6k          ; R1 = 6kΩ en serie
R2 2 0 4k          ; R2 = 4kΩ en paralelo con R3
R3 2 0 12k         ; R3 = 12kΩ en paralelo con R2

.OP
.PRINT DC V(1) V(2) I(R1) I(R2) I(R3)
.END
```

## Solución

### Datos
- Vs = 36 V
- R₁ = 6 kΩ, R₂ = 4 kΩ, R₃ = 12 kΩ

### Parte a) Resistencia equivalente

**Paso 1:** Calcular R₂ || R₃
$$R_{23} = \frac{R_2 \cdot R_3}{R_2 + R_3} = \frac{(4\text{k})(12\text{k})}{4\text{k} + 12\text{k}} = \frac{48\text{M}}{16\text{k}} = 3\text{ kΩ}$$

**Paso 2:** Sumar R₁ en serie
$$R_{eq} = R_1 + R_{23} = 6\text{ kΩ} + 3\text{ kΩ} = 9\text{ kΩ}$$

### Parte b) Corriente total

$$I_T = \frac{V_s}{R_{eq}} = \frac{36\text{ V}}{9\text{ kΩ}} = 4\text{ mA}$$

### Parte c) Voltajes y corrientes

**Voltaje en R₁:**
$$V_1 = I_T \cdot R_1 = (4\text{ mA})(6\text{ kΩ}) = 24\text{ V}$$

**Voltaje en R₂ y R₃ (nodo 2):**
$$V_{23} = V_s - V_1 = 36 - 24 = 12\text{ V}$$

O también:
$$V_{23} = I_T \cdot R_{23} = (4\text{ mA})(3\text{ kΩ}) = 12\text{ V}$$

**Corriente en R₂:**
$$I_2 = \frac{V_{23}}{R_2} = \frac{12\text{ V}}{4\text{ kΩ}} = 3\text{ mA}$$

**Corriente en R₃:**
$$I_3 = \frac{V_{23}}{R_3} = \frac{12\text{ V}}{12\text{ kΩ}} = 1\text{ mA}$$

**Verificación LCK en nodo 2:**
$$I_T = I_2 + I_3 \Rightarrow 4\text{ mA} = 3\text{ mA} + 1\text{ mA} \checkmark$$

### Parte d) Potencia total

$$P_1 = I_T^2 \cdot R_1 = (4\text{ mA})^2 (6\text{ kΩ}) = 96\text{ mW}$$
$$P_2 = I_2^2 \cdot R_2 = (3\text{ mA})^2 (4\text{ kΩ}) = 36\text{ mW}$$
$$P_3 = I_3^2 \cdot R_3 = (1\text{ mA})^2 (12\text{ kΩ}) = 12\text{ mW}$$

$$P_{total} = P_1 + P_2 + P_3 = 96 + 36 + 12 = 144\text{ mW}$$

**Verificación:**
$$P_{fuente} = V_s \cdot I_T = (36\text{ V})(4\text{ mA}) = 144\text{ mW} \checkmark$$

## Respuestas

| Magnitud | Valor |
|----------|-------|
| a) Req | **9 kΩ** |
| b) IT | **4 mA** |
| c) V₁ | **24 V** |
| c) V₂ = V₃ | **12 V** |
| c) I₁ | **4 mA** |
| c) I₂ | **3 mA** |
| c) I₃ | **1 mA** |
| d) Ptotal | **144 mW** |

## Simulación SPICE - Resultados Esperados
```
Operating Point:
V(1) = 36.0000
V(2) = 12.0000
I(R1) = 4.0000E-03
I(R2) = 3.0000E-03
I(R3) = 1.0000E-03
```

## Conceptos Aplicados
- Reducción de circuitos serie-paralelo
- División de corriente en ramas paralelas
- Conservación de energía
- LCK y LVK