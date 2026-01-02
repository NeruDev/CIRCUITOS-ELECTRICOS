```markdown
# PR-01: Aplicación Básica de la Ley de Ohm ⭐

## Enunciado
En el circuito mostrado, una fuente de voltaje de 12V alimenta una resistencia de 4kΩ. Determine:
a) La corriente que circula por el circuito
b) La potencia disipada en la resistencia
c) La energía consumida en 2 horas

## Diagrama del Circuito

```
     +  R = 4kΩ   
   ┌──/\/\/\/──┐
   │           │
 + │           │
  (V) 12V      │
 - │           │
   │           │
   └───────────┘
```

## Netlist SPICE

```spice
* PR-01: Ley de Ohm Basico
* Circuito simple con fuente DC y resistencia

V1 1 0 DC 12V      ; Fuente de voltaje 12V entre nodo 1 y tierra
R1 1 0 4k          ; Resistencia de 4kΩ entre nodo 1 y tierra

.OP                 ; Análisis de punto de operación DC
.END
```

## Solución

### Datos
- Vs = 12 V
- R = 4 kΩ = 4000 Ω
- t = 2 h = 7200 s

### Parte a) Corriente en el circuito

Aplicando la Ley de Ohm:
$$I = \frac{V}{R} = \frac{12\text{ V}}{4000\text{ Ω}} = 0.003\text{ A} = 3\text{ mA}$$

### Parte b) Potencia disipada

Usando las fórmulas de potencia:
$$P = VI = (12\text{ V})(3\text{ mA}) = 36\text{ mW}$$

Verificación:
$$P = I^2R = (0.003)^2(4000) = 36\text{ mW}$$
$$P = \frac{V^2}{R} = \frac{(12)^2}{4000} = 36\text{ mW}$$

### Parte c) Energía consumida

$$W = P \cdot t = (36 \times 10^{-3}\text{ W})(7200\text{ s}) = 259.2\text{ J}$$

O en kWh:
$$W = (36 \times 10^{-3}\text{ W})(2\text{ h}) = 72 \times 10^{-3}\text{ Wh} = 0.072\text{ Wh}$$

## Respuestas
| Magnitud | Valor |
|----------|-------|
| a) Corriente | **I = 3 mA** |
| b) Potencia | **P = 36 mW** |
| c) Energía | **W = 259.2 J = 0.072 Wh** |

## Simulación SPICE - Resultados Esperados
```
Operating Point:
V(1) = 12.0000
I(V1) = -3.0000E-03
```

## Conceptos Aplicados
- Ley de Ohm: V = IR
- Potencia eléctrica: P = VI = I²R = V²/R
- Energía: W = Pt
```
