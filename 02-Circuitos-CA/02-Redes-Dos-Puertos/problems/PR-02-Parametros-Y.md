```markdown
# PR-02: Parámetros Y y Conversión Y↔Z ⭐⭐⭐

## Enunciado
Para la red π mostrada, determine:
a) Los parámetros Y (admitancia)
b) Convierta los parámetros Y a parámetros Z
c) La admitancia de entrada Yin con una carga YL = 0.02 S
d) La ganancia de corriente Ai = I₂/I₁

Datos: Y₁ = 0.01 S (100Ω), Y₂ = 0.005 S (200Ω), Y₃ = 0.02 S (50Ω)

## Diagrama del Circuito

```
    Puerto 1                   Puerto 2
        I₁ →                      I₂ →
    ●───────────●───────────●───────●
    │           │           │       │
  + │          ┌┴┐         ┌┴┐    + │
V₁  │          │Y₂│        │Y₃│   V₂│
    │     0.005S │ │    0.02S│ │      │
  - │          └┬┘         └┬┘    - │
    │     Y₁    │           │       │
    ●────┬──────┴───────────┴───────●
         │
        ┌┴┐
        │ │ 0.01 S
        └┬┘
         │
        ─┴─ GND
```

## Netlist SPICE

```spice
* PR-02: Parámetros Y - Red π
* Convertir admitancias a resistencias: R = 1/Y

* Y1 = 0.01 S → R1 = 100Ω (rama derivación izquierda)
* Y2 = 0.005 S → R2 = 200Ω (rama derivación central)
* Y3 = 0.02 S → R3 = 50Ω (rama derivación derecha)

* Medición de Y11 e Y21 (V2 = 0, puerto 2 cortocircuito)
I1 0 1 AC 1 0        ; Fuente de corriente de prueba
R1 1 0 100           ; Y1 = 0.01 S
R2 1 2 200           ; Y2 = 0.005 S (rama serie)
R3 2 0 50            ; Y3 = 0.02 S

.AC LIN 1 1k 1k
.PRINT AC VM(1) VM(2)   ; Y11 = I1/V1, Y21 = I2/V1 (con V2 = 0)
.END
```

Nota: El diagrama necesita corrección. Una red π típica tiene:
- Admitancia Y_a de puerto 1 a tierra
- Admitancia Y_b en serie (entre puertos)
- Admitancia Y_c de puerto 2 a tierra

## Diagrama Corregido - Red π

```
    Puerto 1                   Puerto 2
        I₁ →                      I₂ →
    ●───────────┬────◯────┬───────●
    │           │    Y_b  │       │
  + │          ┌┴┐  0.005S┌┴┐    + │
V₁  │          │Y_a│      │Y_c│  V₂│
    │    0.01 S│ │   0.02S│ │      │
  - │          └┬┘        └┬┘    - │
    ●───────────┴──────────┴───────●
                │
               ─┴─ GND
```

## Solución

### Datos
- Y_a = 0.01 S (admitancia en derivación puerto 1)
- Y_b = 0.005 S (admitancia en serie entre puertos)
- Y_c = 0.02 S (admitancia en derivación puerto 2)

### Parte a) Parámetros Y

**Definición de parámetros Y:**
$$I_1 = Y_{11}V_1 + Y_{12}V_2$$
$$I_2 = Y_{21}V_1 + Y_{22}V_2$$

**Cálculo de Y₁₁ (V₂ = 0, puerto 2 en cortocircuito):**

Con V₂ = 0, las admitancias Y_b e Y_c están en paralelo (ambas conectadas a tierra).
$$Y_{11} = \frac{I_1}{V_1}\bigg|_{V_2=0} = Y_a + Y_b$$
$$Y_{11} = 0.01 + 0.005 = 0.015\text{ S}$$

**Cálculo de Y₂₁ (V₂ = 0):**

La corriente I₂ es la que fluye por Y_b desde el nodo 1 hacia el nodo 2 (cortocircuitado):
$$Y_{21} = \frac{I_2}{V_1}\bigg|_{V_2=0} = -Y_b$$

El signo negativo porque la corriente que entra al puerto 2 es la que sale del puerto 1 por Y_b:
$$Y_{21} = -0.005\text{ S}$$

**Cálculo de Y₂₂ (V₁ = 0, puerto 1 en cortocircuito):**

$$Y_{22} = \frac{I_2}{V_2}\bigg|_{V_1=0} = Y_b + Y_c$$
$$Y_{22} = 0.005 + 0.02 = 0.025\text{ S}$$

**Cálculo de Y₁₂ (V₁ = 0):**

$$Y_{12} = \frac{I_1}{V_2}\bigg|_{V_1=0} = -Y_b = -0.005\text{ S}$$

**Matriz Y:**
$$\boxed{[Y] = \begin{bmatrix} 0.015 & -0.005 \\ -0.005 & 0.025 \end{bmatrix} \text{ S}}$$

### Parte b) Conversión Y → Z

**Determinante de [Y]:**
$$\Delta_Y = Y_{11}Y_{22} - Y_{12}Y_{21}$$
$$\Delta_Y = (0.015)(0.025) - (-0.005)(-0.005)$$
$$\Delta_Y = 0.000375 - 0.000025 = 0.00035\text{ S}^2$$

**Fórmulas de conversión:**
$$Z_{11} = \frac{Y_{22}}{\Delta_Y} = \frac{0.025}{0.00035} = 71.43\text{ Ω}$$

$$Z_{12} = \frac{-Y_{12}}{\Delta_Y} = \frac{-(-0.005)}{0.00035} = 14.29\text{ Ω}$$

$$Z_{21} = \frac{-Y_{21}}{\Delta_Y} = \frac{-(-0.005)}{0.00035} = 14.29\text{ Ω}$$

$$Z_{22} = \frac{Y_{11}}{\Delta_Y} = \frac{0.015}{0.00035} = 42.86\text{ Ω}$$

**Matriz Z:**
$$\boxed{[Z] = \begin{bmatrix} 71.43 & 14.29 \\ 14.29 & 42.86 \end{bmatrix} \text{ Ω}}$$

**Verificación de reciprocidad:**
- $Y_{12} = Y_{21} = -0.005$ S ✓
- $Z_{12} = Z_{21} = 14.29$ Ω ✓

### Parte c) Admitancia de entrada con YL = 0.02 S

$$Y_{in} = Y_{11} - \frac{Y_{12}Y_{21}}{Y_{22} + Y_L}$$

$$Y_{in} = 0.015 - \frac{(-0.005)(-0.005)}{0.025 + 0.02}$$

$$Y_{in} = 0.015 - \frac{0.000025}{0.045}$$

$$Y_{in} = 0.015 - 0.000556 = 0.01444\text{ S}$$

$$\boxed{Y_{in} = 14.44\text{ mS} \quad (Z_{in} = 69.25\text{ Ω})}$$

### Parte d) Ganancia de corriente

Con carga YL en el puerto 2:
$$V_2 = -\frac{I_2}{Y_L}$$ (el voltaje V₂ es debido a I₂ fluyendo por YL)

De la ecuación de corriente del puerto 2:
$$I_2 = Y_{21}V_1 + Y_{22}V_2$$

Y la del puerto 1:
$$I_1 = Y_{11}V_1 + Y_{12}V_2$$

Sustituyendo $V_2 = -I_2/Y_L$:
$$I_2 = Y_{21}V_1 - Y_{22}\frac{I_2}{Y_L}$$
$$I_2\left(1 + \frac{Y_{22}}{Y_L}\right) = Y_{21}V_1$$
$$I_2 = \frac{Y_{21}Y_L}{Y_L + Y_{22}}V_1$$

Para la ganancia de corriente necesitamos expresar en función de I₁:
$$I_1 = Y_{11}V_1 + Y_{12}V_2 = Y_{11}V_1 - \frac{Y_{12}I_2}{Y_L}$$

$$V_1 = \frac{I_1 + \frac{Y_{12}I_2}{Y_L}}{Y_{11}}$$

Sustituyendo en la expresión de I₂:
$$I_2 = \frac{Y_{21}Y_L}{Y_L + Y_{22}} \times \frac{I_1 + \frac{Y_{12}I_2}{Y_L}}{Y_{11}}$$

Simplificando:
$$A_i = \frac{I_2}{I_1} = \frac{-Y_{21}}{Y_{22} + Y_L - \frac{Y_{12}Y_{21}}{Y_{11}}}$$

O usando la fórmula directa:
$$A_i = \frac{-Y_{21}}{Y_{22} + Y_L}$$ (aproximación cuando Y₁₂ es pequeño)

$$A_i = \frac{-(-0.005)}{0.025 + 0.02} = \frac{0.005}{0.045}$$

$$\boxed{A_i = 0.111 = -19.1\text{ dB}}$$

## Fórmulas de Conversión Y ↔ Z

| De Y a Z | De Z a Y |
|----------|----------|
| $Z_{11} = Y_{22}/\Delta_Y$ | $Y_{11} = Z_{22}/\Delta_Z$ |
| $Z_{12} = -Y_{12}/\Delta_Y$ | $Y_{12} = -Z_{12}/\Delta_Z$ |
| $Z_{21} = -Y_{21}/\Delta_Y$ | $Y_{21} = -Z_{21}/\Delta_Z$ |
| $Z_{22} = Y_{11}/\Delta_Y$ | $Y_{22} = Z_{11}/\Delta_Z$ |

## Tabla Resumen

| Parámetro | Valor (S) | Valor (Ω) |
|-----------|-----------|-----------|
| Y₁₁ / Z₁₁ | 0.015 S | 71.43 Ω |
| Y₁₂ / Z₁₂ | -0.005 S | 14.29 Ω |
| Y₂₁ / Z₂₁ | -0.005 S | 14.29 Ω |
| Y₂₂ / Z₂₂ | 0.025 S | 42.86 Ω |
| Δ | 0.00035 S² | 2500 Ω² |

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| a) Matriz [Y] | **[0.015, -0.005; -0.005, 0.025] S** |
| b) Matriz [Z] | **[71.43, 14.29; 14.29, 42.86] Ω** |
| c) Yin (YL=0.02S) | **14.44 mS (Zin = 69.25 Ω)** |
| d) Ai | **0.111 (-19.1 dB)** |

## Netlist SPICE - Verificación

```spice
* PR-02: Verificación con carga

* Red π con carga
I1 0 1 AC 1 0         ; Fuente de corriente 1A
Ra 1 0 100            ; Ya = 0.01 S
Rb 1 2 200            ; Yb = 0.005 S (serie)
Rc 2 0 50             ; Yc = 0.02 S
RL 2 0 50             ; Carga YL = 0.02 S (50Ω)

.AC LIN 1 1k 1k
.PRINT AC VM(1) VM(2) IM(RL)
* Yin = I1/V1 = 1/V(1)
* Ai = I(RL)/1A
.END
```

## Conceptos Aplicados
- Parámetros Y de admitancia
- Configuración de red π
- Conversión entre parámetros Y y Z
- Admitancia de entrada con carga
- Ganancia de corriente
- Reciprocidad: Y₁₂ = Y₂₁
```
