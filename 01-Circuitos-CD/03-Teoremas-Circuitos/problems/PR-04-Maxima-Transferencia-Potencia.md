```markdown
# PR-04: Máxima Transferencia de Potencia ⭐⭐

## Enunciado
Para el circuito mostrado, determine:
a) El valor de RL que permite máxima transferencia de potencia
b) La potencia máxima transferida a la carga
c) La eficiencia del circuito en condición de máxima transferencia

Datos: Vs = 48V, R₁ = 8Ω, R₂ = 24Ω

## Diagrama del Circuito

```
           R₁=8Ω
    ┌─────/\/\/────┬─────────○ a
    │              │         
  + │              │         
(Vs)│             R₂=24Ω    RL
 48V│              │         
  - │              │         
    │              │         
    └──────────────┴─────────○ b
```

## Netlist SPICE

```spice
* PR-04: Maxima Transferencia de Potencia
* Calculo de Thevenin para determinar RL optima

V1 1 0 DC 48V      ; Fuente de voltaje 48V
R1 1 2 8           ; R1 = 8Ω
R2 2 0 24          ; R2 = 24Ω

.OP
.PRINT DC V(2)      ; Vth
.END
```

```spice
* PR-04b: Circuito con RL optima

V1 1 0 DC 48V
R1 1 2 8
R2 2 0 24
RL 2 0 6           ; RL = Rth = 6Ω (valor optimo)

.OP
.PRINT DC V(2) I(RL)
.END
```

```spice
* PR-04c: Barrido de RL para graficar potencia

V1 1 0 DC 48V
R1 1 2 8
R2 2 0 24
RL 2 0 {Rload}

.PARAM Rload = 6
.STEP PARAM Rload 1 20 1
.OP
.PRINT DC I(RL)
.END
```

## Solución

### Paso 1: Encontrar el equivalente de Thévenin

**Voltaje de Thévenin (Vth):**
Circuito abierto entre a-b. R₁ y R₂ forman un divisor de tensión.

$$V_{th} = V_s \times \frac{R_2}{R_1 + R_2} = 48 \times \frac{24}{8 + 24} = 48 \times \frac{24}{32} = 48 \times 0.75 = 36\text{ V}$$

**Resistencia de Thévenin (Rth):**
Con Vs cortocircuitada:

$$R_{th} = R_1 \| R_2 = \frac{R_1 \times R_2}{R_1 + R_2} = \frac{8 \times 24}{8 + 24} = \frac{192}{32} = 6\text{ Ω}$$

### Parte a) Valor de RL para máxima transferencia

Por el teorema de máxima transferencia de potencia:

$$\boxed{R_L = R_{th} = 6\text{ Ω}}$$

### Parte b) Potencia máxima transferida

Cuando RL = Rth:

$$I_L = \frac{V_{th}}{R_{th} + R_L} = \frac{36}{6 + 6} = \frac{36}{12} = 3\text{ A}$$

$$P_{max} = I_L^2 \times R_L = (3)^2 \times 6 = 9 \times 6 = 54\text{ W}$$

**Fórmula alternativa:**
$$P_{max} = \frac{V_{th}^2}{4R_{th}} = \frac{(36)^2}{4 \times 6} = \frac{1296}{24} = 54\text{ W}$$

### Parte c) Eficiencia en máxima transferencia

**Potencia entregada por la fuente equivalente:**
$$P_{fuente} = V_{th} \times I_L = 36 \times 3 = 108\text{ W}$$

**Potencia disipada en Rth:**
$$P_{Rth} = I_L^2 \times R_{th} = (3)^2 \times 6 = 54\text{ W}$$

**Eficiencia:**
$$\eta = \frac{P_L}{P_{fuente}} = \frac{54}{108} = 0.5 = 50\%$$

**Conclusión importante:** En máxima transferencia de potencia, la eficiencia es siempre del 50%. La mitad de la potencia se disipa en la resistencia interna (Rth).

### Análisis de potencia vs RL

| RL (Ω) | IL (A) | PL (W) | η (%) |
|--------|--------|--------|-------|
| 2 | 4.5 | 40.5 | 37.5 |
| 4 | 3.6 | 51.8 | 44.4 |
| **6** | **3.0** | **54.0** | **50.0** |
| 8 | 2.57 | 52.9 | 53.3 |
| 12 | 2.0 | 48.0 | 60.0 |
| 18 | 1.5 | 40.5 | 66.7 |

### Curva de Potencia

```
P(W)
  │
54├───────────●─────────
  │          ╱ ╲
  │         ╱   ╲
  │        ╱     ╲
  │       ╱       ╲
  │      ╱         ╲
  └─────────────────────── RL(Ω)
         6
```

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| Vth | **36 V** |
| Rth | **6 Ω** |
| a) RL óptima | **6 Ω** |
| b) Pmax | **54 W** |
| c) Eficiencia | **50%** |

## Simulación SPICE - Resultados Esperados
```
Thevenin:
V(2) = 36.0000  (Vth con circuito abierto)

Con RL = 6Ω:
V(2) = 18.0000
I(RL) = 3.0000E+00
P(RL) = 54.0000
```

## Aplicaciones Prácticas

1. **Diseño de audio:** Adaptación de impedancia amplificador-altavoz
2. **Comunicaciones:** Adaptación de líneas de transmisión
3. **Energía solar:** Punto de máxima potencia (MPPT)

## Nota sobre Eficiencia vs Potencia Máxima

- **Máxima potencia:** RL = Rth → η = 50%
- **Máxima eficiencia:** RL >> Rth → η → 100% (pero P → 0)

En sistemas de **potencia** (transmisión eléctrica), se prioriza la eficiencia.
En sistemas de **señales** (comunicaciones), se prioriza la máxima transferencia.

## Conceptos Aplicados
- Teorema de máxima transferencia de potencia
- RL = Rth para Pmax
- Pmax = Vth²/(4Rth)
- Eficiencia = 50% en Pmax
```
