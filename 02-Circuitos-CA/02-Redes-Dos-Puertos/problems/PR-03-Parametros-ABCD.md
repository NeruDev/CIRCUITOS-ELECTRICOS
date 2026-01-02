# PR-03: Parámetros ABCD (Transmisión) ⭐⭐⭐

## Enunciado
Para el cuadripolo mostrado, determine:
a) Los parámetros ABCD
b) La impedancia de entrada con carga ZL = 100Ω
c) La ganancia de voltaje Av = V₂/V₁
d) Los parámetros ABCD cuando dos redes idénticas se conectan en cascada

Datos: R₁ = 50Ω, R₂ = 100Ω (configuración L)

## Diagrama del Circuito

```
    Puerto 1              Puerto 2
        I₁ →                 ← I₂
    ●────/\/\/────┬────────●
    │   R₁=50Ω   │        │
  + │           ┌┴┐     + │
V₁  │           │R₂│    V₂│
    │       100Ω│ │       │
  - │           └┬┘     - │
    ●────────────┴────────●

Nota: I₂ entra al puerto 2 (convención ABCD)
```

## Netlist SPICE

```spice
* PR-03: Parámetros ABCD - Red L
* Configuración para medir A y C (puerto 2 abierto)

V1 1 0 AC 1 0         ; Fuente 1V de prueba
R1 1 2 50             ; R1 = 50Ω (serie)
R2 2 0 100            ; R2 = 100Ω (derivación)

.AC LIN 1 1k 1k
.PRINT AC VM(2) IM(V1)
* A = V1/V2 (I2=0), C = I1/V2 (I2=0)
.END

* Para B y D: cortocircuitar puerto 2
* B = V1/I2 (V2=0), D = I1/I2 (V2=0)
```

## Solución

### Definición de Parámetros ABCD

$$V_1 = AV_2 + BI_2$$
$$I_1 = CV_2 + DI_2$$

O en forma matricial:
$$\begin{bmatrix} V_1 \\ I_1 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} V_2 \\ I_2 \end{bmatrix}$$

**Nota importante:** En la convención ABCD, I₂ **entra** al puerto 2.

### Parte a) Cálculo de Parámetros ABCD

**Parámetro A (V₂ ≠ 0, I₂ = 0):**
Puerto 2 abierto. La corriente I₁ fluye por R₁ y R₂.

$$A = \frac{V_1}{V_2}\bigg|_{I_2=0}$$

Por divisor de voltaje (V₂ es el voltaje en R₂):
$$V_2 = V_1 \times \frac{R_2}{R_1 + R_2} = V_1 \times \frac{100}{50 + 100} = V_1 \times \frac{2}{3}$$

$$A = \frac{V_1}{V_2} = \frac{V_1}{V_1 \times \frac{2}{3}} = \frac{3}{2} = 1.5$$

$$\boxed{A = 1.5}$$ (adimensional)

**Parámetro C (V₂ ≠ 0, I₂ = 0):**
$$C = \frac{I_1}{V_2}\bigg|_{I_2=0}$$

$$I_1 = \frac{V_1}{R_1 + R_2} = \frac{V_1}{150}$$

$$V_2 = \frac{2}{3}V_1 \Rightarrow V_1 = \frac{3}{2}V_2$$

$$I_1 = \frac{\frac{3}{2}V_2}{150} = \frac{V_2}{100}$$

$$C = \frac{I_1}{V_2} = \frac{1}{100} = 0.01\text{ S}$$

$$\boxed{C = 0.01\text{ S} = 10\text{ mS}}$$

**Parámetro B (V₁ ≠ 0, V₂ = 0):**
Puerto 2 en cortocircuito. R₂ queda en paralelo con el cortocircuito (R₂ efectivo = 0).

$$B = \frac{V_1}{I_2}\bigg|_{V_2=0}$$

Con V₂ = 0: La corriente I₁ = V₁/R₁ (toda va por R₁).
La corriente I₂ que entra al puerto 2 es la que sale de R₂ hacia el cortocircuito.

Con cortocircuito en puerto 2: I₂ = -I₁ (la corriente que entra es igual a la que sale, pero I₂ entra al puerto 2)

Espera, analicemos mejor:
- V₂ = 0 significa cortocircuito
- I₁ fluye por R₁, llega al nodo, y se divide entre R₂ (a tierra) y el cortocircuito (puerto 2)
- Pero con V₂ = 0, todo el voltaje V₁ cae en R₁
- La corriente por R₂ = V(nodo)/R₂ = 0/R₂ = 0 (el nodo está a 0V)
- I₂ = I₁ (toda la corriente va al cortocircuito)

$$I_1 = \frac{V_1}{R_1} = \frac{V_1}{50}$$
$$I_2 = I_1 = \frac{V_1}{50}$$ (entra al puerto 2)

$$B = \frac{V_1}{I_2} = \frac{V_1}{\frac{V_1}{50}} = 50\text{ Ω}$$

$$\boxed{B = 50\text{ Ω}}$$

**Parámetro D (I₁ ≠ 0, V₂ = 0):**
$$D = \frac{I_1}{I_2}\bigg|_{V_2=0}$$

Del análisis anterior: I₁ = I₂

$$D = \frac{I_1}{I_2} = 1$$

$$\boxed{D = 1}$$ (adimensional)

**Matriz ABCD:**
$$\boxed{[ABCD] = \begin{bmatrix} 1.5 & 50 \\ 0.01 & 1 \end{bmatrix}}$$

**Verificación: AD - BC = 1** (condición de reciprocidad)
$$AD - BC = (1.5)(1) - (50)(0.01) = 1.5 - 0.5 = 1 \checkmark$$

### Parte b) Impedancia de entrada con ZL = 100Ω

$$Z_{in} = \frac{AZ_L + B}{CZ_L + D}$$

$$Z_{in} = \frac{(1.5)(100) + 50}{(0.01)(100) + 1}$$

$$Z_{in} = \frac{150 + 50}{1 + 1} = \frac{200}{2}$$

$$\boxed{Z_{in} = 100\text{ Ω}}$$

### Parte c) Ganancia de voltaje

$$A_v = \frac{V_2}{V_1} = \frac{Z_L}{AZ_L + B}$$

$$A_v = \frac{100}{(1.5)(100) + 50} = \frac{100}{200}$$

$$\boxed{A_v = 0.5 = -6\text{ dB}}$$

### Parte d) Dos redes en cascada

La ventaja de los parámetros ABCD es que para redes en cascada, la matriz total es el producto de las matrices individuales:

$$[ABCD]_{total} = [ABCD]_1 \times [ABCD]_2$$

Para dos redes idénticas:
$$[ABCD]_{total} = \begin{bmatrix} 1.5 & 50 \\ 0.01 & 1 \end{bmatrix} \times \begin{bmatrix} 1.5 & 50 \\ 0.01 & 1 \end{bmatrix}$$

**Multiplicación de matrices:**
$$A_{total} = A_1 A_2 + B_1 C_2 = (1.5)(1.5) + (50)(0.01) = 2.25 + 0.5 = 2.75$$

$$B_{total} = A_1 B_2 + B_1 D_2 = (1.5)(50) + (50)(1) = 75 + 50 = 125\text{ Ω}$$

$$C_{total} = C_1 A_2 + D_1 C_2 = (0.01)(1.5) + (1)(0.01) = 0.015 + 0.01 = 0.025\text{ S}$$

$$D_{total} = C_1 B_2 + D_1 D_2 = (0.01)(50) + (1)(1) = 0.5 + 1 = 1.5$$

$$\boxed{[ABCD]_{cascada} = \begin{bmatrix} 2.75 & 125 \\ 0.025 & 1.5 \end{bmatrix}}$$

**Verificación:** $A_{tot}D_{tot} - B_{tot}C_{tot} = (2.75)(1.5) - (125)(0.025) = 4.125 - 3.125 = 1$ ✓

## Diagrama de Cascada

```
    Red 1                  Red 2
┌─────────────┐       ┌─────────────┐
│   50Ω      │       │   50Ω      │
●──/\/\/──┬──●───────●──/\/\/──┬──●
│        ┌┴┐ │       │        ┌┴┐ │
│        │ │100Ω    │        │ │100Ω
│        └┬┘ │       │        └┬┘ │
●─────────┴──●───────●─────────┴──●
```

## Tabla Resumen

| Parámetro | Red Simple | Cascada (2 redes) |
|-----------|------------|-------------------|
| A | 1.5 | 2.75 |
| B | 50 Ω | 125 Ω |
| C | 0.01 S | 0.025 S |
| D | 1 | 1.5 |
| AD - BC | 1 | 1 |

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| a) A | **1.5** |
| a) B | **50 Ω** |
| a) C | **0.01 S** |
| a) D | **1** |
| b) Zin (ZL=100Ω) | **100 Ω** |
| c) Av | **0.5 (-6 dB)** |
| d) [ABCD] cascada | **[2.75, 125; 0.025, 1.5]** |

## Netlist SPICE - Verificación Cascada

```spice
* PR-03: Verificación cascada de dos redes L

V1 1 0 AC 1 0
* Primera red L
R1a 1 2 50
R2a 2 0 100
* Segunda red L
R1b 2 3 50
R2b 3 0 100
* Carga
RL 3 0 100

.AC LIN 1 1k 1k
.PRINT AC VM(3) IM(V1)
* Av_total = V(3)/1V
.END
```

## Conceptos Aplicados
- Parámetros ABCD de transmisión
- Convención de corriente I₂ entrante
- Multiplicación de matrices para cascada
- Condición de reciprocidad: AD - BC = 1
- Impedancia de entrada y ganancia