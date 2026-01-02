```markdown
# PR-04: Teorema de Thévenin en CA ⭐⭐⭐

## Enunciado
Para el circuito mostrado, determine el equivalente de Thévenin visto desde los terminales a-b y luego calcule la corriente en una carga ZL = 10 + j5 Ω conectada entre dichos terminales.

Datos: Vs = 50∠30° V, R₁ = 10Ω, R₂ = 20Ω, XL = 15Ω, XC = 25Ω, ω = 1000 rad/s

## Diagrama del Circuito

```
    ┌────/\/\/────┬────────────────● a
    │   R₁=10Ω   │                │
  + │            │                │
Vs (─)         ┌─┴─┐              │
50∠30°         │ L │           ┌──┴──┐
  - │          │XL=15Ω        │ ZL? │ (carga)
    │          └─┬─┘          └──┬──┘
    │   R₂=20Ω  │                │
    ├────/\/\/──┤                │
    │           │                │
    │        ┌──┴──┐             │
    │        │  C  │             │
    │        │XC=25Ω             │
    │        └──┬──┘             │
    └───────────┴────────────────● b
```

## Netlist SPICE

```spice
* PR-04: Equivalente Thévenin en CA

* Para ω = 1000 rad/s (f = 159.15 Hz)
* XL = 15Ω → L = 15mH
* XC = 25Ω → C = 40μF

V1 1 0 AC 50 30      ; Fuente 50V∠30°
R1 1 2 10            ; R1 = 10Ω
L1 2 0 15m           ; L para XL = 15Ω
R2 1 3 20            ; R2 = 20Ω
C1 3 0 40u           ; C para XC = 25Ω

* Terminales Thévenin: nodos 2 y 3

.AC LIN 1 159.15 159.15
.PRINT AC VM(2,3) VP(2,3)  ; Vth = V(2) - V(3)
.END

* Para Zth: desactivar fuente y calcular impedancia
```

## Solución

### Datos
- Vs = 50∠30° V
- R₁ = 10 Ω
- R₂ = 20 Ω
- ZL = j15 Ω (inductor)
- ZC = -j25 Ω (capacitor)

### Paso 1: Calcular Vth (voltaje de circuito abierto)

Con los terminales a-b abiertos, no fluye corriente por el inductor ni el capacitor en esa rama.

**Análisis del circuito:**
El circuito se puede ver como dos divisores de voltaje en paralelo desde la fuente.

**Rama 1 (R₁ y L):**
$$\mathbf{V}_a = V_s \times \frac{Z_L}{R_1 + Z_L} = 50\angle 30° \times \frac{j15}{10 + j15}$$

$$Z_{R1+L} = 10 + j15 = 18.03\angle 56.31°\text{ Ω}$$

$$\mathbf{V}_a = 50\angle 30° \times \frac{15\angle 90°}{18.03\angle 56.31°}$$
$$\mathbf{V}_a = 50\angle 30° \times 0.832\angle 33.69°$$
$$\mathbf{V}_a = 41.6\angle 63.69°\text{ V}$$

**Rama 2 (R₂ y C):**
$$\mathbf{V}_b = V_s \times \frac{Z_C}{R_2 + Z_C} = 50\angle 30° \times \frac{-j25}{20 - j25}$$

$$Z_{R2+C} = 20 - j25 = 32.02\angle -51.34°\text{ Ω}$$

$$\mathbf{V}_b = 50\angle 30° \times \frac{25\angle -90°}{32.02\angle -51.34°}$$
$$\mathbf{V}_b = 50\angle 30° \times 0.781\angle -38.66°$$
$$\mathbf{V}_b = 39.05\angle -8.66°\text{ V}$$

**Voltaje Thévenin:**
$$\mathbf{V}_{th} = \mathbf{V}_a - \mathbf{V}_b$$

Convertimos a rectangular:
- $\mathbf{V}_a = 41.6\angle 63.69° = 18.46 + j37.27$ V
- $\mathbf{V}_b = 39.05\angle -8.66° = 38.60 - j5.88$ V

$$\mathbf{V}_{th} = (18.46 - 38.60) + j(37.27 + 5.88)$$
$$\mathbf{V}_{th} = -20.14 + j43.15\text{ V}$$

$$\boxed{\mathbf{V}_{th} = 47.62\angle 115.0° \text{ V}}$$

### Paso 2: Calcular Zth (impedancia equivalente)

Desactivando la fuente (Vs = 0, cortocircuito):

**Vista desde a-b:**
$$Z_{th} = (R_1 \parallel Z_L) + (R_2 \parallel Z_C)$$

**R₁ en paralelo con L:**
$$Z_1 = \frac{R_1 \times Z_L}{R_1 + Z_L} = \frac{10 \times j15}{10 + j15}$$
$$Z_1 = \frac{150\angle 90°}{18.03\angle 56.31°} = 8.32\angle 33.69°$$
$$Z_1 = 6.92 + j4.61\text{ Ω}$$

**R₂ en paralelo con C:**
$$Z_2 = \frac{R_2 \times Z_C}{R_2 + Z_C} = \frac{20 \times (-j25)}{20 - j25}$$
$$Z_2 = \frac{500\angle -90°}{32.02\angle -51.34°} = 15.62\angle -38.66°$$
$$Z_2 = 12.19 - j9.76\text{ Ω}$$

**Impedancia Thévenin total:**
$$Z_{th} = Z_1 + Z_2 = (6.92 + j4.61) + (12.19 - j9.76)$$
$$Z_{th} = 19.11 - j5.15\text{ Ω}$$

$$\boxed{Z_{th} = 19.82\angle -15.08° \text{ Ω}}$$

### Paso 3: Corriente en la carga ZL = 10 + j5 Ω

**Circuito equivalente:**
```
    Zth
┌────◯────┐
│         │
○ Vth     ○ ZL
│         │
└────●────┘
```

$$\mathbf{I}_L = \frac{\mathbf{V}_{th}}{Z_{th} + Z_L}$$

$$Z_{total} = Z_{th} + Z_L = (19.11 - j5.15) + (10 + j5) = 29.11 - j0.15\text{ Ω}$$

$$Z_{total} = 29.11\angle -0.30°\text{ Ω}$$

$$\mathbf{I}_L = \frac{47.62\angle 115.0°}{29.11\angle -0.30°}$$

$$\boxed{\mathbf{I}_L = 1.636\angle 115.3° \text{ A}}$$

### Verificación: Potencia en la carga

$$\mathbf{S}_L = |\mathbf{I}_L|^2 \times Z_L = (1.636)^2 \times (10 + j5)$$
$$\mathbf{S}_L = 2.676 \times (10 + j5) = 26.76 + j13.38\text{ VA}$$

- Potencia activa: P = 26.76 W
- Potencia reactiva: Q = 13.38 VAR

## Diagrama del Circuito Equivalente

```
        Zth = 19.82∠-15.08° Ω
    ┌────────◯────────┐
    │                 │
  + │               ┌─┴─┐
(Vth)               │ZL │ 10+j5 Ω
47.62∠115°          └─┬─┘
  - │                 │
    └────────●────────┘
        IL = 1.636∠115.3° A
```

## Tabla Resumen

| Cantidad | Rectangular | Polar |
|----------|-------------|-------|
| Va | 18.46 + j37.27 V | 41.6∠63.69° V |
| Vb | 38.60 - j5.88 V | 39.05∠-8.66° V |
| Vth | -20.14 + j43.15 V | 47.62∠115° V |
| Zth | 19.11 - j5.15 Ω | 19.82∠-15.08° Ω |
| IL | -0.70 + j1.48 A | 1.636∠115.3° A |

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| Vth | **47.62∠115° V** |
| Zth | **19.82∠-15.08° Ω** |
| IL (con carga) | **1.636∠115.3° A** |
| iL(t) | **1.636cos(1000t + 115.3°) A** |
| Potencia en carga | **26.76 + j13.38 VA** |

## Netlist SPICE - Circuito Equivalente

```spice
* PR-04: Verificación con equivalente Thévenin
* Circuito reducido

Vth 1 0 AC 47.62 115    ; Vth = 47.62∠115° V
Rth 1 2 19.11           ; Parte real de Zth
Xth 2 3 -5.15           ; Parte imaginaria (capacitivo)
* En SPICE: C = 1/(ω·Xc) = 1/(1000·5.15) = 194μF
Cth 2 3 194u
RL 3 0 10               ; Parte real de ZL
LL 3 0 5m               ; XL = 5Ω → L = 5mH

.AC LIN 1 159.15 159.15
.PRINT AC IM(RL) IP(RL)
.END
```

## Simulación SPICE - Resultados Esperados
```
Circuito original:
VM(2,3) = 47.62V,  VP(2,3) = 115°  (Vth)

Con carga:
IM(carga) = 1.636A, IP(carga) = 115.3°
```

## Conceptos Aplicados
- Teorema de Thévenin en CA
- Divisores de voltaje con impedancias
- Impedancias en paralelo
- Superposición de voltajes
- Reducción de circuitos
```
