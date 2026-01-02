# PR-01: Parámetros Z de una Red de Dos Puertos ⭐⭐

## Enunciado
Para la red de dos puertos mostrada, determine:
a) Los parámetros Z ([impedancia](../../../glossary.md#impedancia))
b) La impedancia de entrada Zin con una [carga](../../../glossary.md#carga) ZL = 50Ω
c) La ganancia de [voltaje](../../../glossary.md#voltaje) Av = V₂/V₁ con la carga ZL
d) Verifique la condición de reciprocidad

Datos: R₁ = 100Ω, R₂ = 200Ω, R₃ = 50Ω

## Diagrama del Circuito

```
    Puerto 1              Puerto 2
        I₁ →                  I₂ →
    ●───────┬────/\/\/────┬───────●
    │       │    R₂=200Ω  │       │
  + │      ┌┴┐           ┌┴┐    + │
V₁  │      │R₁│          │R₃│   V₂│
    │  100Ω│ │        50Ω│ │      │
  - │      └┬┘           └┬┘    - │
    ●───────┴─────────────┴───────●
```

## Netlist SPICE

```spice
* PR-01: Parámetros Z - Red de dos puertos
* Configuración T

* Medición de Z11 y Z21 (I2 = 0, puerto 2 abierto)
V1 1 0 AC 1 0        ; Fuente de prueba 1V
R1 1 2 100           ; R1 = 100Ω
R2 2 3 200           ; R2 = 200Ω
R3 3 0 50            ; R3 = 50Ω

.AC LIN 1 1k 1k
.PRINT AC VM(1) IM(V1) VM(3)  ; Z11 = V1/I1, Z21 = V2/I1
.END

* Nota: Para Z22 y Z12, intercambiar fuente al puerto 2
```

## Solución

### Análisis de la Red T

La red mostrada es una configuración T con:
- R₁ en la rama serie izquierda (puerto 1)
- R₂ en la rama serie central
- R₃ en la rama derivación derecha (puerto 2)

### Parte a) Parámetros Z

**Definición de parámetros Z:**
$$V_1 = Z_{11}I_1 + Z_{12}I_2$$
$$V_2 = Z_{21}I_1 + Z_{22}I_2$$

**Cálculo de Z₁₁ (I₂ = 0, puerto 2 abierto):**

Con I₂ = 0, la [corriente](../../../glossary.md#corriente) I₁ fluye por R₁, R₂ y R₃ en serie:
$$Z_{11} = \frac{V_1}{I_1}\bigg|_{I_2=0} = R_1 + R_2 + R_3$$
$$Z_{11} = 100 + 200 + 50 = 350\text{ Ω}$$

**Cálculo de Z₂₁ (I₂ = 0, puerto 2 abierto):**

El voltaje V₂ es el voltaje en R₃:
$$Z_{21} = \frac{V_2}{I_1}\bigg|_{I_2=0} = R_3 = 50\text{ Ω}$$

**Cálculo de Z₂₂ (I₁ = 0, puerto 1 abierto):**

Con I₁ = 0, la corriente I₂ fluye por R₃, R₂ y R₁ en serie:
$$Z_{22} = \frac{V_2}{I_2}\bigg|_{I_1=0} = R_3 + R_2 + R_1$$
$$Z_{22} = 50 + 200 + 100 = 350\text{ Ω}$$

**Cálculo de Z₁₂ (I₁ = 0, puerto 1 abierto):**

El voltaje V₁ es el voltaje en R₁:
$$Z_{12} = \frac{V_1}{I_2}\bigg|_{I_1=0} = R_1 = 100\text{ Ω}$$

**Espera, esto no es correcto para una red T.** Reanalicemos:

Para una red T simétrica, el voltaje de transferencia se calcula con la [resistencia](../../../glossary.md#resistencia) compartida:

En la red T:
- Rama serie izquierda: R₁ (conecta puerto 1 al [nodo](../../../glossary.md#nodo) central)
- Rama derivación: R₃ (conecta nodo central a tierra)
- Rama serie derecha: R₂ (conecta nodo central al puerto 2)

**Recálculo Z₁₁:**
Con I₂ = 0 (puerto 2 abierto), I₁ fluye por R₁ y luego se divide... No, con puerto 2 abierto, toda I₁ va por R₁ y luego por (R₂ + R₃ en paralelo con puerto abierto) = R₁ + R₂||∞ + R₃... 

En realidad, con puerto 2 abierto, la corriente va por R₁, luego tiene dos caminos: por R₃ a tierra o por R₂ hacia el puerto 2 abierto (no fluye corriente por R₂ si está abierto).

Vamos a redefinir el [circuito](../../../glossary.md#circuito):

```
    I₁ →         Nodo A         I₂ →
    ●────/\/\/────●────/\/\/────●
    │    R₁=100Ω  │   R₂=200Ω  │
  + │            ┌┴┐          + │
V₁  │            │R₃│         V₂│
    │         50Ω│ │            │
  - │            └┬┘          - │
    ●─────────────┴─────────────●
              GND
```

**Recálculo correcto:**

**Z₁₁ (I₂ = 0):**
Puerto 2 abierto → no hay corriente por R₂ desde el puerto 2.
La corriente I₁ entra, pasa por R₁, llega al nodo A y tiene dos caminos:
- Por R₃ a tierra
- Por R₂ al puerto 2 (pero con I₂ = 0, el puerto está abierto)

Si el puerto 2 está abierto, la corriente que sale del nodo A por R₂ debe ser cero (circuito abierto).
Entonces toda I₁ debe ir por R₃.

$$V_1 = I_1(R_1 + R_3) = I_1(100 + 50) = 150 I_1$$
$$Z_{11} = 150\text{ Ω}$$

**Z₂₁ (I₂ = 0):**
$$V_2 = V_A = I_1 \cdot R_3 = 50 I_1$$
$$Z_{21} = 50\text{ Ω}$$

**Z₂₂ (I₁ = 0):**
Puerto 1 abierto. La corriente I₂ entra, pasa por R₂, llega al nodo A.
Desde A, puede ir por R₃ a tierra o por R₁ al puerto 1 (abierto).
Toda I₂ debe ir por R₃.

$$V_2 = I_2(R_2 + R_3) = I_2(200 + 50) = 250 I_2$$
$$Z_{22} = 250\text{ Ω}$$

**Z₁₂ (I₁ = 0):**
$$V_1 = V_A = I_2 \cdot R_3 = 50 I_2$$
$$Z_{12} = 50\text{ Ω}$$

**Matriz Z:**
$$\boxed{[Z] = \begin{bmatrix} 150 & 50 \\ 50 & 250 \end{bmatrix} \text{ Ω}}$$

### Parte b) Impedancia de entrada con ZL = 50Ω

$$Z_{in} = Z_{11} - \frac{Z_{12}Z_{21}}{Z_{22} + Z_L}$$

$$Z_{in} = 150 - \frac{50 \times 50}{250 + 50}$$

$$Z_{in} = 150 - \frac{2500}{300} = 150 - 8.33$$

$$\boxed{Z_{in} = 141.67\text{ Ω}}$$

### Parte c) Ganancia de voltaje con ZL = 50Ω

$$A_v = \frac{V_2}{V_1} = \frac{Z_{21} Z_L}{Z_{22}Z_L + \Delta_Z}$$

Donde $\Delta_Z = Z_{11}Z_{22} - Z_{12}Z_{21}$

$$\Delta_Z = 150 \times 250 - 50 \times 50 = 37500 - 2500 = 35000\text{ Ω}^2$$

Alternativa más directa:
$$A_v = \frac{Z_{21}}{Z_{22} + Z_L} \times \frac{Z_L}{Z_{in}}... $$

Usemos el enfoque directo:

Con carga ZL en el puerto 2:
$$V_2 = -I_2 Z_L$$ (signo negativo por convención de corriente saliente)

De las ecuaciones de la red:
$$V_2 = Z_{21}I_1 + Z_{22}I_2$$
$$-I_2 Z_L = Z_{21}I_1 + Z_{22}I_2$$
$$I_2 = -\frac{Z_{21}I_1}{Z_{22} + Z_L}$$

$$V_2 = -I_2 Z_L = \frac{Z_{21}Z_L}{Z_{22} + Z_L}I_1$$

$$V_1 = Z_{11}I_1 + Z_{12}I_2 = Z_{11}I_1 - \frac{Z_{12}Z_{21}}{Z_{22} + Z_L}I_1$$
$$V_1 = I_1\left(Z_{11} - \frac{Z_{12}Z_{21}}{Z_{22} + Z_L}\right) = I_1 \times Z_{in}$$

$$A_v = \frac{V_2}{V_1} = \frac{Z_{21}Z_L}{Z_{in}(Z_{22} + Z_L)}$$

$$A_v = \frac{50 \times 50}{141.67 \times (250 + 50)} = \frac{2500}{141.67 \times 300} = \frac{2500}{42500}$$

$$\boxed{A_v = 0.0588 = -24.6\text{ dB}}$$

### Parte d) Condición de reciprocidad

Para una red recíproca (sin fuentes dependientes ni elementos activos):
$$Z_{12} = Z_{21}$$

En nuestro caso:
$$Z_{12} = 50\text{ Ω} = Z_{21}$$

$$\boxed{\text{La red ES RECÍPROCA: } Z_{12} = Z_{21} = 50\text{ Ω ✓}}$$

## Verificación por Simulación

```
Para Z11: Aplicar V1 = 1V, medir I1
         Z11 = V1/I1 = 1/I1

Con R1 = 100Ω, R3 = 50Ω en serie (puerto 2 abierto):
I1 = 1V / 150Ω = 6.67mA
Z11 = 150Ω ✓
```

## Tabla Resumen

| Parámetro | Valor |
|-----------|-------|
| Z₁₁ | 150 Ω |
| Z₁₂ | 50 Ω |
| Z₂₁ | 50 Ω |
| Z₂₂ | 250 Ω |
| ΔZ | 35000 Ω² |

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| a) Matriz [Z] | **[150, 50; 50, 250] Ω** |
| b) Zin (ZL=50Ω) | **141.67 Ω** |
| c) Av | **0.0588 (-24.6 dB)** |
| d) Reciprocidad | **Sí, Z₁₂ = Z₂₁** |

## Netlist SPICE - Verificación

```spice
* PR-01: Verificación de parámetros Z

* Test 1: Medir Z11 (puerto 2 abierto)
V1 1 0 AC 1 0
R1 1 2 100
R3 2 0 50
* R2 desconectado del circuito para puerto 2 abierto
.AC LIN 1 1k 1k
.PRINT AC VM(1) IM(V1)  ; Z11 = VM(1)/IM(V1)
.END

* Test 2: Circuito completo con carga
V1 1 0 AC 1 0
R1 1 2 100
R2 2 3 200
R3 2 0 50
RL 3 0 50              ; Carga ZL = 50Ω
.AC LIN 1 1k 1k
.PRINT AC VM(3) IM(V1)  ; Av = VM(3)/1V
.END
```

## Conceptos Aplicados
- Parámetros Z de impedancia
- Definición de puertos abiertos/cortocircuitados
- Impedancia de entrada con carga
- Ganancia de voltaje
- Condición de reciprocidad
- Determinante de la matriz Z