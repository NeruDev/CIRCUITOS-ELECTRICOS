# PR-02: Resistencias en Serie ⭐

## Enunciado
Para el [circuito](../../../glossary.md#circuito) serie mostrado con una fuente de 24V y tres resistencias R₁ = 2kΩ, R₂ = 3kΩ, R₃ = 1kΩ, calcule:
a) La [resistencia](../../../glossary.md#resistencia) equivalente del circuito
b) La [corriente](../../../glossary.md#corriente) total del circuito
c) El [voltaje](../../../glossary.md#voltaje) en cada resistencia
d) Verifique la [LVK](../../../glossary.md#lvk)

## Diagrama del Circuito

```
         R₁=2kΩ      R₂=3kΩ      R₃=1kΩ
    ┌───/\/\/\/───/\/\/\/───/\/\/\/───┐
    │      +v₁-     +v₂-     +v₃-     │
  + │                                 │
(Vs)│ 24V                             │
  - │                                 │
    │                                 │
    └─────────────────────────────────┘
```

## Netlist SPICE

```spice
* PR-02: Resistencias en Serie
* Circuito serie con tres resistencias

V1 1 0 DC 24V      ; Fuente de voltaje 24V
R1 1 2 2k          ; R1 = 2kΩ entre nodos 1 y 2
R2 2 3 3k          ; R2 = 3kΩ entre nodos 2 y 3
R3 3 0 1k          ; R3 = 1kΩ entre nodo 3 y tierra

.OP                 ; Análisis DC
.PRINT DC V(1) V(2) V(3) I(R1) I(R2) I(R3)
.END
```

## Solución

### Datos
- Vs = 24 V
- R₁ = 2 kΩ, R₂ = 3 kΩ, R₃ = 1 kΩ

### Parte a) Resistencia equivalente

En serie, las resistencias se suman:
$$R_{eq} = R_1 + R_2 + R_3 = 2 + 3 + 1 = 6\text{ kΩ}$$

### Parte b) Corriente total

$$I = \frac{V_s}{R_{eq}} = \frac{24\text{ V}}{6\text{ kΩ}} = 4\text{ mA}$$

En un circuito serie, la misma corriente fluye por todos los elementos.

### Parte c) Voltaje en cada resistencia

Aplicando [Ley de](../../../glossary.md#ley-ohm) [Ohm](../../../glossary.md#ohm-unidad) a cada resistencia:

$$V_1 = I \cdot R_1 = (4\text{ mA})(2\text{ kΩ}) = 8\text{ V}$$
$$V_2 = I \cdot R_2 = (4\text{ mA})(3\text{ kΩ}) = 12\text{ V}$$
$$V_3 = I \cdot R_3 = (4\text{ mA})(1\text{ kΩ}) = 4\text{ V}$$

### Parte d) Verificación con LVK

Recorriendo la malla en sentido horario:
$$-V_s + V_1 + V_2 + V_3 = 0$$
$$-24 + 8 + 12 + 4 = 0 \checkmark$$

## Respuestas

| Magnitud | Valor |
|----------|-------|
| a) Req | **6 kΩ** |
| b) I | **4 mA** |
| c) V₁ | **8 V** |
| c) V₂ | **12 V** |
| c) V₃ | **4 V** |

## Simulación SPICE - Resultados Esperados
```
Operating Point:
V(1) = 24.0000
V(2) = 16.0000    ; V1 = V(1)-V(2) = 8V
V(3) = 4.0000     ; V2 = V(2)-V(3) = 12V
                  ; V3 = V(3) = 4V
I(R1) = I(R2) = I(R3) = 4.0000E-03
```

## Conceptos Aplicados
- Resistencias en serie: Req = R₁ + R₂ + ... + Rₙ
- Corriente igual en serie
- Ley de Voltajes de Kirchhoff (LVK)