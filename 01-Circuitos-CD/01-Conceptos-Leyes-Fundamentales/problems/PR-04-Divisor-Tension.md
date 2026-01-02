# PR-04: Divisor de Tensión ⭐

## Enunciado
Diseñe un divisor de tensión que entregue 5V a partir de una fuente de 15V. La corriente total del divisor debe ser de 1mA.
a) Calcule los valores de R₁ y R₂
b) Si se conecta una carga RL = 10kΩ en paralelo con R₂, ¿cuál es el nuevo voltaje de salida?

## Diagrama del Circuito

```
         R₁
    ┌───/\/\/───┬─────── Vout
    │           │
  + │          R₂
(Vs)│ 15V       │
  - │           │
    │           │
    └───────────┴─────── GND
```

**Con carga:**
```
         R₁
    ┌───/\/\/───┬─────── Vout
    │           │
  + │          R₂ ║ RL
(Vs)│ 15V       │
  - │           │
    │           │
    └───────────┴─────── GND
```

## Netlist SPICE

```spice
* PR-04: Divisor de Tension
* Parte a) Sin carga

V1 1 0 DC 15V      ; Fuente de voltaje 15V
R1 1 2 10k         ; R1 = 10kΩ (calculado)
R2 2 0 5k          ; R2 = 5kΩ (calculado)

.OP
.PRINT DC V(2)
.END
```

```spice
* PR-04b: Divisor de Tension con carga

V1 1 0 DC 15V      ; Fuente de voltaje 15V
R1 1 2 10k         ; R1 = 10kΩ
R2 2 0 5k          ; R2 = 5kΩ
RL 2 0 10k         ; Carga RL = 10kΩ

.OP
.PRINT DC V(2)
.END
```

## Solución

### Parte a) Diseño del divisor

**Datos:**
- Vs = 15 V
- Vout = 5 V
- I = 1 mA

**Cálculo de resistencia total:**
$$R_{total} = \frac{V_s}{I} = \frac{15\text{ V}}{1\text{ mA}} = 15\text{ kΩ}$$

**Fórmula del divisor de tensión:**
$$V_{out} = V_s \cdot \frac{R_2}{R_1 + R_2}$$

$$5 = 15 \cdot \frac{R_2}{R_1 + R_2}$$

$$\frac{R_2}{R_1 + R_2} = \frac{5}{15} = \frac{1}{3}$$

**Solución:**
- R₁ + R₂ = 15 kΩ
- R₂ = (1/3)(15 kΩ) = 5 kΩ
- R₁ = 15 kΩ - 5 kΩ = **10 kΩ**
- R₂ = **5 kΩ**

**Verificación:**
$$V_{out} = 15 \cdot \frac{5\text{k}}{10\text{k} + 5\text{k}} = 15 \cdot \frac{1}{3} = 5\text{ V} \checkmark$$

### Parte b) Con carga conectada

**Resistencia equivalente de R₂ || RL:**
$$R_{2,eq} = R_2 \| R_L = \frac{R_2 \cdot R_L}{R_2 + R_L} = \frac{(5\text{k})(10\text{k})}{5\text{k} + 10\text{k}} = \frac{50\text{M}}{15\text{k}} = 3.33\text{ kΩ}$$

**Nuevo voltaje de salida:**
$$V_{out,carga} = V_s \cdot \frac{R_{2,eq}}{R_1 + R_{2,eq}}$$

$$V_{out,carga} = 15 \cdot \frac{3.33\text{k}}{10\text{k} + 3.33\text{k}} = 15 \cdot \frac{3.33}{13.33}$$

$$V_{out,carga} = 15 \cdot 0.25 = 3.75\text{ V}$$

**Error por efecto de carga:**
$$\Delta V = 5 - 3.75 = 1.25\text{ V}$$
$$\% \text{ error} = \frac{1.25}{5} \times 100 = 25\%$$

## Respuestas

| Magnitud | Valor |
|----------|-------|
| a) R₁ | **10 kΩ** |
| a) R₂ | **5 kΩ** |
| b) Vout con carga | **3.75 V** |
| Error por carga | **25%** |

## Simulación SPICE - Resultados Esperados
```
Sin carga:
V(2) = 5.0000

Con carga:
V(2) = 3.7500
```

## Nota de Diseño
Para minimizar el efecto de carga, la impedancia de carga debe ser mucho mayor que R₂ (regla práctica: RL ≥ 10·R₂). En este caso, como RL = 2·R₂, el efecto de carga es significativo.

## Conceptos Aplicados
- Divisor de tensión: Vout = Vs · R₂/(R₁+R₂)
- Efecto de carga en divisores
- Resistencias en paralelo