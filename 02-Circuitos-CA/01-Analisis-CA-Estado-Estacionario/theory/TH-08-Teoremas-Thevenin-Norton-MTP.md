# TH-08: Teoremas de Thévenin, Norton y Máxima Transferencia de Potencia en CA

## Objetivos
- Obtener equivalentes de [Thévenin](../../../glossary.md#thevenin) y [Norton](../../../glossary.md#norton) en CA
- Calcular la condición de máxima transferencia de potencia en CA
- Aplicar adaptación de impedancias

## Contenido

### Teorema de Thévenin en CA

Cualquier [circuito](../../../glossary.md#circuito) lineal de dos terminales puede reemplazarse por una fuente de [voltaje](../../../glossary.md#voltaje) fasorial **Vth** en serie con una [impedancia](../../../glossary.md#impedancia) **Zth**.

```
Equivalente Thévenin:
        Zth
○───────⬚───────○ a
│
Vth
│
○───────────────○ b
```

### Cálculo de Vth y Zth

**Voltaje de Thévenin:**
$$\mathbf{V}_{th} = \mathbf{V}_{ab(circuito\ abierto)}$$

**Impedancia de Thévenin:**
$$\mathbf{Z}_{th} = \mathbf{Z}_{ab(fuentes\ apagadas)}$$

O usando:
$$\mathbf{Z}_{th} = \frac{\mathbf{V}_{th}}{\mathbf{I}_{sc}}$$

### Teorema de Norton en CA

Equivalente con fuente de corriente **In** en paralelo con impedancia **Zn**.

```
Equivalente Norton:
        ○───┬───○ a
            │
       In ↑ ═ Zn
            │
        ○───┴───○ b
```

$$\mathbf{I}_N = \frac{\mathbf{V}_{th}}{\mathbf{Z}_{th}}$$
$$\mathbf{Z}_N = \mathbf{Z}_{th}$$

### Máxima Transferencia de Potencia en CA

Para **máxima transferencia de potencia** a la carga ZL:

$$\mathbf{Z}_L = \mathbf{Z}_{th}^*$$

Donde Zth* es el conjugado complejo de Zth.

**Si Zth = Rth + jXth, entonces:**
$$\mathbf{Z}_L = R_{th} - jX_{th}$$

### Potencia Máxima

$$P_{max} = \frac{|\mathbf{V}_{th}|^2}{8R_{th}}$$

### Casos Especiales

**Si ZL es puramente resistiva (RL):**
$$R_L = |\mathbf{Z}_{th}| = \sqrt{R_{th}^2 + X_{th}^2}$$

$$P_{max} = \frac{|\mathbf{V}_{th}|^2}{4(R_{th} + |\mathbf{Z}_{th}|)}$$

### Adaptación de Impedancias

La condición ZL = Zth* se llama **adaptación conjugada**.

**Importancia:**
- Maximiza la potencia entregada a la [carga](../../../glossary.md#carga)
- Esencial en sistemas de comunicación y RF
- Usado en diseño de amplificadores

### Ejemplo Completo

**Circuito:**
```
       10Ω      j20Ω
    ○───/\/\/───⌇⌇⌇───┬───○ a
    │                 │
100∠0°              -j10Ω
    │                 │
    ○─────────────────┴───○ b
```

**Paso 1: Calcular Vth**

Con terminales a-b abiertos:
Divisor de voltaje con Z = 10 + j20 - j10 = 10 + j10

$$\mathbf{V}_{th} = 100\angle 0° \times \frac{-j10}{10 + j10}$$

$$\mathbf{V}_{th} = 100 \times \frac{-j10}{10 + j10} = \frac{-j1000}{10 + j10}$$

Convirtiendo a forma polar:
- Numerador: |-j1000| = 1000, ∠(-j1000) = -90°
- Denominador: |10 + j10| = √(100+100) = 14.14, ∠(10 + j10) = arctan(10/10) = 45°

$$\mathbf{V}_{th} = \frac{1000\angle -90°}{14.14\angle 45°} = 70.7\angle -135° \text{ V}$$

**Paso 2: Calcular Zth**

Apagando la fuente:
$$\mathbf{Z}_{th} = (10 + j20) \| (-j10)$$

$$\mathbf{Z}_{th} = \frac{(10 + j20)(-j10)}{10 + j20 - j10} = \frac{200 - j100}{10 + j10}$$

$$\mathbf{Z}_{th} = \frac{223.6\angle -26.6°}{14.14\angle 45°} = 15.8\angle -71.6° = 5 - j15 \text{ Ω}$$

**Paso 3: Carga óptima**
$$\mathbf{Z}_L = 5 + j15 \text{ Ω}$$

**Paso 4: Potencia máxima**
$$P_{max} = \frac{(70.7)^2}{8 \times 5} = \frac{4998}{40} = 125 \text{ W}$$

## Conceptos Clave
- Thévenin/Norton: mismas técnicas que CD, con impedancias
- MTP: ZL = Zth* (conjugado)
- Pmax = |Vth|²/(8Rth)
