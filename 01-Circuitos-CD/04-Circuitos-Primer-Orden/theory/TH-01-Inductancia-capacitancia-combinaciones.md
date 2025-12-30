# TH-01: Inductancia y Capacitancia - Combinación de Elementos

## Objetivos
- Comprender el comportamiento del inductor y capacitor
- Calcular energía almacenada en L y C
- Combinar inductores y capacitores en serie y paralelo

## Contenido

### El Capacitor

El capacitor almacena energía en un campo eléctrico.

**Relación v-i:**
$$i = C\frac{dv}{dt}$$
$$v = \frac{1}{C}\int_{t_0}^{t} i \, d\tau + v(t_0)$$

**Energía almacenada:**
$$w_C = \frac{1}{2}Cv^2$$

**Propiedades:**
- No puede cambiar instantáneamente de voltaje
- En CD (estado estable): se comporta como circuito abierto
- El voltaje es una variable de estado

### El Inductor

El inductor almacena energía en un campo magnético.

**Relación v-i:**
$$v = L\frac{di}{dt}$$
$$i = \frac{1}{L}\int_{t_0}^{t} v \, d\tau + i(t_0)$$

**Energía almacenada:**
$$w_L = \frac{1}{2}Li^2$$

**Propiedades:**
- No puede cambiar instantáneamente de corriente
- En CD (estado estable): se comporta como cortocircuito
- La corriente es una variable de estado

### Combinación de Capacitores

**En serie:**
$$\frac{1}{C_{eq}} = \frac{1}{C_1} + \frac{1}{C_2} + ... + \frac{1}{C_n}$$

**En paralelo:**
$$C_{eq} = C_1 + C_2 + ... + C_n$$

### Combinación de Inductores

**En serie:**
$$L_{eq} = L_1 + L_2 + ... + L_n$$

**En paralelo:**
$$\frac{1}{L_{eq}} = \frac{1}{L_1} + \frac{1}{L_2} + ... + \frac{1}{L_n}$$

### Comparación L, R, C

| Propiedad | Resistor | Capacitor | Inductor |
|-----------|----------|-----------|----------|
| Relación v-i | v = iR | i = C(dv/dt) | v = L(di/dt) |
| Energía | Disipa | Almacena | Almacena |
| En CD | v = iR | Abierto | Corto |
| En serie | Suma R | Suma 1/C | Suma L |
| En paralelo | Suma 1/R | Suma C | Suma 1/L |

## Conceptos Clave
- Continuidad de voltaje en capacitor
- Continuidad de corriente en inductor
- Dualidad entre L y C
