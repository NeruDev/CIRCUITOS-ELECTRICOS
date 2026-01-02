```markdown
# PR-01: Potencia Activa, Reactiva y Aparente ⭐⭐

## Enunciado
Una carga consume una corriente i(t) = 10cos(377t - 30°) A cuando se le aplica un voltaje v(t) = 120cos(377t) V. Determine:
a) La potencia activa P
b) La potencia reactiva Q
c) La potencia aparente S
d) El factor de potencia
e) La corriente que debe suministrar un capacitor para corregir el FP a 0.95 en atraso

## Diagrama del Circuito

```
         i(t)
    ●────→────●────────────●
    │         │            │
  + │       ┌─┴─┐       ┌──┴──┐
v(t)│       │   │       │     │
120V│       │ Z │       │ Cc  │ (corrección FP)
  - │       │   │       │     │
    │       └─┬─┘       └──┬──┘
    ●─────────┴────────────┘
    
v(t) = 120cos(377t) V
i(t) = 10cos(377t - 30°) A
θ = 30° (corriente atrasa → carga inductiva)
```

## Netlist SPICE

```spice
* PR-01: Análisis de Potencia CA
* Carga con factor de potencia inductivo

* V = 120∠0°, I = 10∠-30°
* Z = V/I = (120∠0°)/(10∠-30°) = 12∠30° Ω
* Z = 10.39 + j6 Ω

V1 1 0 AC 120 0       ; Fuente 120V∠0°
R1 1 2 10.39          ; Parte resistiva
L1 2 0 15.9m          ; XL = 6Ω → L = 6/(377) = 15.9mH

.AC LIN 1 60 60       ; f = 377/(2π) = 60 Hz
.PRINT AC IM(V1) IP(V1) 
.END
```

## Solución

### Datos
- $v(t) = 120\cos(377t)$ V → $\mathbf{V} = 120\angle 0°$ V
- $i(t) = 10\cos(377t - 30°)$ A → $\mathbf{I} = 10\angle -30°$ A
- ω = 377 rad/s → f = 60 Hz

### Valores RMS
$$V_{rms} = \frac{V_m}{\sqrt{2}} = \frac{120}{\sqrt{2}} = 84.85\text{ V}$$
$$I_{rms} = \frac{I_m}{\sqrt{2}} = \frac{10}{\sqrt{2}} = 7.07\text{ A}$$

### Ángulo de impedancia
$$\theta = \theta_v - \theta_i = 0° - (-30°) = 30°$$

La corriente atrasa al voltaje → **carga inductiva**.

### Parte a) Potencia activa

$$P = V_{rms} \times I_{rms} \times \cos\theta$$
$$P = 84.85 \times 7.07 \times \cos(30°)$$
$$P = 600 \times 0.866$$

$$\boxed{P = 519.6\text{ W}}$$

Verificación con valores pico:
$$P = \frac{V_m I_m}{2}\cos\theta = \frac{120 \times 10}{2} \times 0.866 = 519.6\text{ W ✓}$$

### Parte b) Potencia reactiva

$$Q = V_{rms} \times I_{rms} \times \sin\theta$$
$$Q = 84.85 \times 7.07 \times \sin(30°)$$
$$Q = 600 \times 0.5$$

$$\boxed{Q = 300\text{ VAR}}$$ (positivo → inductivo)

### Parte c) Potencia aparente

$$S = V_{rms} \times I_{rms} = 84.85 \times 7.07$$

$$\boxed{|S| = 600\text{ VA}}$$

**Potencia compleja:**
$$\mathbf{S} = P + jQ = 519.6 + j300 = 600\angle 30°\text{ VA}$$

**Verificación:**
$$|S| = \sqrt{P^2 + Q^2} = \sqrt{519.6^2 + 300^2} = \sqrt{360000} = 600\text{ VA ✓}$$

### Parte d) Factor de potencia

$$FP = \cos\theta = \cos(30°) = 0.866$$

$$\boxed{FP = 0.866 \text{ en atraso}}$$

### Parte e) Corrección del factor de potencia a 0.95

**Nuevo ángulo:**
$$\theta_{nuevo} = \arccos(0.95) = 18.19°$$

**Nueva potencia reactiva:**
$$Q_{nuevo} = P \times \tan(\theta_{nuevo}) = 519.6 \times \tan(18.19°)$$
$$Q_{nuevo} = 519.6 \times 0.3287 = 170.8\text{ VAR}$$

**Potencia reactiva del capacitor:**
$$Q_C = Q - Q_{nuevo} = 300 - 170.8 = 129.2\text{ VAR}$$

El capacitor debe suministrar **potencia reactiva negativa** (capacitiva):
$$Q_C = -129.2\text{ VAR}$$

**Corriente del capacitor:**
$$I_C = \frac{Q_C}{V_{rms}} = \frac{129.2}{84.85} = 1.52\text{ A}$$

$$\boxed{I_C = 1.52\text{ A}}$$

**Reactancia capacitiva:**
$$X_C = \frac{V_{rms}^2}{Q_C} = \frac{84.85^2}{129.2} = 55.7\text{ Ω}$$

**Capacitancia necesaria:**
$$C = \frac{1}{\omega X_C} = \frac{1}{377 \times 55.7} = 47.6\text{ μF}$$

$$\boxed{C = 47.6\text{ μF}}$$

## Triángulo de Potencias

```
            │
            │ Q = 300 VAR (inductivo)
            │    ╱
            │   ╱
            │  ╱ S = 600 VA
            │ ╱  θ = 30°
            │╱_____________
                P = 519.6 W

Después de corrección (FP = 0.95):
            │
     Q' =   │    ╱
  170.8 VAR │   ╱ S' = 547 VA
            │  ╱  θ' = 18.19°
            │ ╱
            │╱_____________
                P = 519.6 W
```

## Tabla de Corrección de FP

| Parámetro | Antes | Después |
|-----------|-------|---------|
| P | 519.6 W | 519.6 W |
| Q | 300 VAR | 170.8 VAR |
| S | 600 VA | 547 VA |
| FP | 0.866 | 0.95 |
| I | 7.07 A | 6.45 A |

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| a) P | **519.6 W** |
| b) Q | **300 VAR** |
| c) S | **600 VA** |
| d) FP | **0.866 en atraso** |
| e) IC | **1.52 A** |
| e) C | **47.6 μF** |

## Simulación SPICE - Resultados Esperados
```
Sin corrección:
I = 7.07 A, θ = -30°, FP = 0.866

Con capacitor C = 47.6μF:
I = 6.45 A, θ = -18.19°, FP = 0.95
```

## Beneficios de Corrección de FP

1. **Menor corriente de línea:** De 7.07A a 6.45A (9% reducción)
2. **Menores pérdidas I²R:** Proporcionales a I²
3. **Mayor capacidad del sistema:** Libera capacidad de los conductores
4. **Mejor regulación de voltaje**
5. **Evita penalizaciones por bajo FP**

## Conceptos Aplicados
- Potencia instantánea vs promedio
- Triángulo de potencias
- Factor de potencia y su significado físico
- Corrección de FP con capacitores
- Relación entre valores pico y RMS
```
