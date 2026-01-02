```markdown
# PR-03: Análisis de Mallas en CA ⭐⭐⭐

## Enunciado
Para el circuito CA mostrado, usando análisis de mallas en el dominio fasorial, determine:
a) Las corrientes de malla I₁ e I₂
b) El voltaje en el capacitor VC
c) La potencia compleja entregada por la fuente
d) Las expresiones en el dominio del tiempo

Datos: Vs = 120∠0° V, R₁ = 30Ω, R₂ = 40Ω, XL = 20Ω, XC = 60Ω, ω = 377 rad/s

## Diagrama del Circuito

```
    ┌────/\/\/────┬────────────────┬────────┐
    │   R₁=30Ω   │                │        │
  + │            │              + │       ┌┴┐
Vs (─)         ┌─┴─┐           Vc │       │R₂│
120∠0°│         │ L │             │    40Ω│ │
  - │         │XL=20Ω            │       └┬┘
    │         └─┬─┘              │        │
    │    I₁ →  │      I₂ →   ┌──┴──┐     │
    │          │             │  C  │     │
    │          │             │XC=60Ω     │
    │          │             └──┬──┘     │
    └──────────┴────────────────┴────────┘
```

## Netlist SPICE

```spice
* PR-03: Análisis de Mallas en CA
* Circuito con R, L y C

* Para ω = 377 rad/s (f = 60 Hz)
* XL = 20Ω → L = XL/ω = 53.05mH
* XC = 60Ω → C = 1/(ω·XC) = 44.21μF

V1 1 0 AC 120 0      ; Fuente 120V∠0°
R1 1 2 30            ; R1 = 30Ω
L1 2 0 53.05m        ; L para XL = 20Ω
C1 2 3 44.21u        ; C para XC = 60Ω
R2 3 0 40            ; R2 = 40Ω

.AC LIN 1 60 60      ; Análisis a 60 Hz
.PRINT AC IM(R1) IP(R1) IM(R2) IP(R2) VM(2) VP(2) VM(3) VP(3)
.END
```

## Solución

### Datos
- Vs = 120∠0° V
- R₁ = 30 Ω
- R₂ = 40 Ω
- ZL = j20 Ω (inductivo)
- ZC = -j60 Ω (capacitivo)

### Definición de mallas

**Malla 1:** Contiene Vs, R₁, ZL
**Malla 2:** Contiene ZL (compartido), ZC, R₂

### Parte a) Ecuaciones de mallas

**Malla 1:**
$$V_s = \mathbf{I}_1 Z_{R1} + (\mathbf{I}_1 - \mathbf{I}_2)Z_L$$
$$120\angle 0° = \mathbf{I}_1(30) + (\mathbf{I}_1 - \mathbf{I}_2)(j20)$$
$$120 = \mathbf{I}_1(30 + j20) - \mathbf{I}_2(j20)$$

**Malla 2:**
$$0 = (\mathbf{I}_2 - \mathbf{I}_1)Z_L + \mathbf{I}_2 Z_C + \mathbf{I}_2 R_2$$
$$0 = -\mathbf{I}_1(j20) + \mathbf{I}_2(j20 - j60 + 40)$$
$$0 = -\mathbf{I}_1(j20) + \mathbf{I}_2(40 - j40)$$

**Sistema de ecuaciones en forma matricial:**
$$\begin{bmatrix} 30 + j20 & -j20 \\ -j20 & 40 - j40 \end{bmatrix} \begin{bmatrix} \mathbf{I}_1 \\ \mathbf{I}_2 \end{bmatrix} = \begin{bmatrix} 120 \\ 0 \end{bmatrix}$$

**Determinante:**
$$\Delta = (30 + j20)(40 - j40) - (-j20)(-j20)$$
$$\Delta = 1200 - j1200 + j800 + 800 - j^2(400)$$
$$\Delta = 1200 - j1200 + j800 + 800 + 400$$
$$\Delta = 2400 - j400 = 2433.1\angle -9.46°$$

**Solución para I₁:**
$$\Delta_1 = \begin{vmatrix} 120 & -j20 \\ 0 & 40 - j40 \end{vmatrix} = 120(40 - j40) = 4800 - j4800$$

$$\mathbf{I}_1 = \frac{\Delta_1}{\Delta} = \frac{4800 - j4800}{2400 - j400}$$

Convertimos a polar:
- $\Delta_1 = 6788.2\angle -45°$
- $\Delta = 2433.1\angle -9.46°$

$$\mathbf{I}_1 = \frac{6788.2\angle -45°}{2433.1\angle -9.46°} = 2.79\angle -35.54°\text{ A}$$

$$\boxed{\mathbf{I}_1 = 2.79\angle -35.54° \text{ A}}$$

**Solución para I₂:**
$$\Delta_2 = \begin{vmatrix} 30 + j20 & 120 \\ -j20 & 0 \end{vmatrix} = 0 - (120)(-j20) = j2400$$

$$\mathbf{I}_2 = \frac{\Delta_2}{\Delta} = \frac{2400\angle 90°}{2433.1\angle -9.46°} = 0.986\angle 99.46°\text{ A}$$

$$\boxed{\mathbf{I}_2 = 0.986\angle 99.46° \text{ A}}$$

### Parte b) Voltaje en el capacitor

$$\mathbf{V}_C = \mathbf{I}_2 \times Z_C = 0.986\angle 99.46° \times 60\angle -90°$$

$$\mathbf{V}_C = 59.16\angle 9.46°\text{ V}$$

$$\boxed{\mathbf{V}_C = 59.16\angle 9.46° \text{ V}}$$

### Parte c) Potencia compleja entregada por la fuente

$$\mathbf{S} = \mathbf{V}_s \times \mathbf{I}_1^*$$

$$\mathbf{I}_1^* = 2.79\angle +35.54°\text{ A}$$ (conjugado)

$$\mathbf{S} = 120\angle 0° \times 2.79\angle 35.54°$$

$$\mathbf{S} = 334.8\angle 35.54° = 272.3 + j194.7\text{ VA}$$

$$\boxed{\mathbf{S} = 334.8\angle 35.54° \text{ VA}}$$

**Componentes de potencia:**
- Potencia activa: $P = 272.3$ W
- Potencia reactiva: $Q = 194.7$ VAR (inductiva positiva)
- Potencia aparente: $|S| = 334.8$ VA
- Factor de potencia: $\cos(35.54°) = 0.813$ en atraso

### Parte d) Expresiones en el dominio del tiempo

$$\boxed{i_1(t) = 2.79\cos(377t - 35.54°)\text{ A}}$$

$$\boxed{i_2(t) = 0.986\cos(377t + 99.46°)\text{ A}}$$

$$\boxed{v_C(t) = 59.16\cos(377t + 9.46°)\text{ V}}$$

### Verificación

**Voltaje en el inductor:**
$$\mathbf{V}_L = (\mathbf{I}_1 - \mathbf{I}_2) \times Z_L$$

$$\mathbf{I}_1 - \mathbf{I}_2 = 2.79\angle -35.54° - 0.986\angle 99.46°$$
$$= (2.27 - j1.62) - (-0.162 + j0.972) = 2.43 - j2.59$$
$$= 3.55\angle -46.83°\text{ A}$$

$$\mathbf{V}_L = 3.55\angle -46.83° \times 20\angle 90° = 71.0\angle 43.17°\text{ V}$$

**Verificación LVK (Malla 1):**
$$V_s = V_{R1} + V_L$$

- $V_{R1} = I_1 \times R_1 = 2.79\angle -35.54° \times 30 = 83.7\angle -35.54°$ V
- $V_L = 71.0\angle 43.17°$ V

Sumando (rectangular):
- $V_{R1} = 68.1 - j48.6$ V
- $V_L = 51.8 + j48.6$ V
- Suma = $119.9 + j0 ≈ 120\angle 0°$ V ✓

## Tabla Resumen

| Cantidad | Rectangular | Polar |
|----------|-------------|-------|
| I₁ | 2.27 - j1.62 A | 2.79∠-35.54° A |
| I₂ | -0.162 + j0.97 A | 0.986∠99.46° A |
| VC | 58.3 + j9.72 V | 59.16∠9.46° V |
| VL | 51.8 + j48.6 V | 71.0∠43.17° V |
| S | 272.3 + j194.7 VA | 334.8∠35.54° VA |

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| a) I₁ | **2.79∠-35.54° A** |
| a) I₂ | **0.986∠99.46° A** |
| b) VC | **59.16∠9.46° V** |
| c) S | **334.8∠35.54° VA** |
| c) P | **272.3 W** |
| c) Q | **194.7 VAR** |
| c) FP | **0.813 en atraso** |
| d) i₁(t) | **2.79cos(377t - 35.54°) A** |
| d) i₂(t) | **0.986cos(377t + 99.46°) A** |

## Simulación SPICE - Resultados Esperados
```
Análisis AC (f = 60 Hz):
IM(R1) = 2.79A,  IP(R1) = -35.54°  (I₁)
IM(R2) = 0.99A,  IP(R2) = 99.46°   (I₂)
VM(3) = 59.16V,  VP(3) = 9.46°     (VC)
```

## Conceptos Aplicados
- Análisis de mallas con impedancias
- Regla de Cramer para sistemas complejos
- Potencia compleja: S = VI*
- Factor de potencia
- Verificación con LVK
```
