<!--
::METADATA::
type: theory
topic_id: ca-01-analisis-ca-estado-estacionario
file_id: TH-04-Notacion-fasorial-impedancia-admitancia
status: stable
audience: both
last_updated: 2026-01-05
-->

# TH-04: Notación Fasorial, Impedancia y Admitancia Compleja

## Objetivos
- Representar señales senoidales como fasores
- Definir [impedancia](../../../glossary.md#impedancia) y [admitancia](../../../glossary.md#admitancia) de elementos
- Aplicar la [Ley de](../../../glossary.md#ley-ohm) [Ohm](../../../glossary.md#ohm-unidad) en forma fasorial

## Contenido

### Concepto de Fasor

Un **[fasor](../../../glossary.md#fasor)** es la representación compleja de una señal senoidal que contiene información de amplitud y fase.

Para: $v(t) = V_m \cos(\omega t + \phi)$

El fasor es: $\mathbf{V} = V_m\angle\phi$ o $\mathbf{V} = V_m e^{j\phi}$

### Transformación al Dominio Fasorial

| Dominio del tiempo | Dominio fasorial |
|--------------------|------------------|
| v(t) = Vm cos(ωt + φ) | **V** = Vm∠φ |
| dv/dt | jω**V** |
| ∫v dt | **V**/(jω) |

### Impedancia (Z)

La **impedancia** es la oposición total al flujo de [corriente](../../../glossary.md#corriente) en CA.

$$\mathbf{Z} = \frac{\mathbf{V}}{\mathbf{I}}$$

Forma general:
$$\mathbf{Z} = R + jX$$

Donde:
- R = [resistencia](../../../glossary.md#resistencia) (parte real)
- X = [reactancia](../../../glossary.md#reactancia) (parte imaginaria)
- |Z| = √(R² + X²)
- θ = arctan(X/R)

### Impedancia de Elementos

**Resistor:**
$$\mathbf{Z}_R = R$$
- Voltaje y corriente en fase

**Inductor:**
$$\mathbf{Z}_L = j\omega L = \omega L\angle 90°$$
- Corriente atrasa al [voltaje](../../../glossary.md#voltaje) 90°

**[Capacitor](../../../glossary.md#capacitancia):**
$$\mathbf{Z}_C = \frac{1}{j\omega C} = -j\frac{1}{\omega C} = \frac{1}{\omega C}\angle -90°$$
- Corriente adelanta al voltaje 90°

### Admitancia (Y)

La **admitancia** es el recíproco de la impedancia.

$$\mathbf{Y} = \frac{1}{\mathbf{Z}} = \frac{\mathbf{I}}{\mathbf{V}} = G + jB$$

Donde:
- G = conductancia
- B = susceptancia

### Admitancia de Elementos

**Resistor:**
$$\mathbf{Y}_R = G = \frac{1}{R}$$

**Inductor:**
$$\mathbf{Y}_L = \frac{1}{j\omega L} = -j\frac{1}{\omega L}$$

**Capacitor:**
$$\mathbf{Y}_C = j\omega C$$

### Ley de Ohm en Forma Fasorial

$$\mathbf{V} = \mathbf{Z} \cdot \mathbf{I}$$
$$\mathbf{I} = \mathbf{Y} \cdot \mathbf{V}$$

### Combinación de Impedancias

**Serie:**
$$\mathbf{Z}_{eq} = \mathbf{Z}_1 + \mathbf{Z}_2 + ... + \mathbf{Z}_n$$

**Paralelo:**
$$\frac{1}{\mathbf{Z}_{eq}} = \frac{1}{\mathbf{Z}_1} + \frac{1}{\mathbf{Z}_2} + ... + \frac{1}{\mathbf{Z}_n}$$

o

$$\mathbf{Y}_{eq} = \mathbf{Y}_1 + \mathbf{Y}_2 + ... + \mathbf{Y}_n$$

### Ejemplo

[Circuito](../../../glossary.md#circuito) serie: R = 4Ω, L = 0.1H, C = 100μF, f = 60Hz

**Cálculos:**
- ω = 2π(60) = 377 rad/s
- ZR = 4Ω
- ZL = j(377)(0.1) = j37.7Ω
- ZC = 1/[j(377)(100×10⁻⁶)] = -j26.5Ω
- Zeq = 4 + j37.7 - j26.5 = 4 + j11.2Ω
- |Zeq| = √(16 + 125.4) = 11.9Ω
- θ = arctan(11.2/4) = 70.3°

## Conceptos Clave
- Fasor = magnitud + fase
- Z = R + jX
- ZL es inductivo (+j), ZC es capacitivo (-j)
