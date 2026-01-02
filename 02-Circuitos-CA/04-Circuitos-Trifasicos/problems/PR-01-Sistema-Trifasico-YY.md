# PR-01: Sistema Trifásico Balanceado Y-Y ⭐⭐

## Enunciado
Un sistema [trifásico](../../../glossary.md#trifasico) balanceado tiene una fuente en [estrella](../../../glossary.md#estrella) (Y) con [voltaje](../../../glossary.md#voltaje) de línea VL = 380V conectada a una [carga](../../../glossary.md#carga) balanceada también en Y con ZY = 30 + j40 Ω por fase. Determine:
a) Los voltajes de fase de la fuente
b) Las corrientes de línea
c) La [potencia activa](../../../glossary.md#potencia-activa), reactiva y aparente total
d) El [factor de potencia](../../../glossary.md#factor-potencia)

Secuencia de fases: positiva (abc)

## Diagrama del Circuito

```
    Fuente Y (balanceada)              Carga Y (balanceada)
    
         Van                              ZY = 30+j40 Ω
    ●─────────● a ─────────────────────● a' ─────●
    │                                            │
    │    Vbn                              ZY    │
    ●─────────● b ─────────────────────● b' ─────●
    │                                            │
    │    Vcn                              ZY    │
    ●─────────● c ─────────────────────● c' ─────●
    │                                            │
    └─────────● n ─────────────────────● n' ─────┘
           (neutro fuente)           (neutro carga)
    
    VL = 380V (línea a línea)
    Secuencia: abc (positiva)
```

## Diagrama Fasorial

```
              Vcn
               │
               │ 120°
         ─────●─────
        /     │     \
       /      │      \
      /       │       \
Van ●─────────┼─────────● Vbn
              │
              │
              
    Secuencia positiva: Van adelanta a Vbn en 120°
                        Vbn adelanta a Vcn en 120°
```

## Netlist SPICE

```spice
* PR-01: Sistema Trifásico Y-Y Balanceado
* Fuente Y con VL = 380V

* Voltaje de fase Vf = VL/√3 = 380/1.732 = 219.4V
Va 1 0 AC 219.4 0        ; Van = 219.4∠0° V
Vb 2 0 AC 219.4 -120     ; Vbn = 219.4∠-120° V
Vc 3 0 AC 219.4 120      ; Vcn = 219.4∠120° V

* Impedancias de carga Y
* ZY = 30 + j40 Ω → R = 30Ω, XL = 40Ω
* XL = ωL → L = XL/(2πf) = 40/(2π×60) = 106mH (a 60Hz)

Ra 1 0 30
La 1 0 106m

Rb 2 0 30
Lb 2 0 106m

Rc 3 0 30
Lc 3 0 106m

.AC LIN 1 60 60          ; Análisis a 60 Hz
.PRINT AC IM(Ra) IP(Ra) VM(1) VP(1)
.END
```

## Solución

### Datos
- VL = 380 V (voltaje de línea)
- ZY = 30 + j40 Ω ([impedancia](../../../glossary.md#impedancia) de carga por fase)
- Secuencia: positiva (abc)

### Parte a) Voltajes de fase de la fuente

En un sistema Y balanceado, el voltaje de fase se relaciona con el de línea:
$$V_f = \frac{V_L}{\sqrt{3}} = \frac{380}{\sqrt{3}} = \frac{380}{1.732}$$

$$V_f = 219.4\text{ V (magnitud)}$$

**Fasores de voltaje (secuencia positiva):**
$$\boxed{V_{an} = 219.4\angle 0° \text{ V}}$$
$$\boxed{V_{bn} = 219.4\angle -120° \text{ V}}$$
$$\boxed{V_{cn} = 219.4\angle 120° \text{ V}}$$

### Parte b) Corrientes de línea

**Impedancia de carga en forma polar:**
$$Z_Y = 30 + j40 = \sqrt{30^2 + 40^2}\angle\arctan\left(\frac{40}{30}\right)$$
$$Z_Y = 50\angle 53.13° \text{ Ω}$$

**Corrientes de fase (= corrientes de línea en conexión Y):**
$$I_a = \frac{V_{an}}{Z_Y} = \frac{219.4\angle 0°}{50\angle 53.13°}$$
$$\boxed{I_a = 4.39\angle -53.13° \text{ A}}$$

$$I_b = \frac{V_{bn}}{Z_Y} = \frac{219.4\angle -120°}{50\angle 53.13°}$$
$$\boxed{I_b = 4.39\angle -173.13° \text{ A}}$$

$$I_c = \frac{V_{cn}}{Z_Y} = \frac{219.4\angle 120°}{50\angle 53.13°}$$
$$\boxed{I_c = 4.39\angle 66.87° \text{ A}}$$

**Magnitud de corriente de línea:**
$$I_L = 4.39\text{ A}$$

### Parte c) Potencias

**Potencia compleja por fase:**
$$S_{fase} = V_f \times I^* = 219.4\angle 0° \times 4.39\angle 53.13°$$
$$S_{fase} = 963.2\angle 53.13°\text{ VA}$$
$$S_{fase} = 578.4 + j769.8\text{ VA}$$

**Potencia total (3 fases):**
$$S_{total} = 3 \times S_{fase} = 3 \times 963.2\angle 53.13°$$
$$S_{total} = 2889.6\angle 53.13°\text{ VA}$$

**Componentes:**
$$\boxed{P = 3 \times 578.4 = 1735.2\text{ W}}$$
$$\boxed{Q = 3 \times 769.8 = 2309.4\text{ VAR}}$$
$$\boxed{|S| = 2889.6\text{ VA}}$$

**Fórmulas alternativas:**
$$P = \sqrt{3} \times V_L \times I_L \times \cos\theta = \sqrt{3} \times 380 \times 4.39 \times 0.6 = 1733.5\text{ W ✓}$$
$$Q = \sqrt{3} \times V_L \times I_L \times \sin\theta = \sqrt{3} \times 380 \times 4.39 \times 0.8 = 2311.3\text{ VAR ✓}$$

### Parte d) Factor de potencia

$$FP = \cos\theta = \cos(53.13°) = 0.6$$

$$\boxed{FP = 0.6 \text{ en atraso (inductivo)}}$$

El factor de potencia está en atraso porque la carga es inductiva (parte imaginaria positiva).

## Verificación: Corriente de neutro

En sistema balanceado, la [corriente](../../../glossary.md#corriente) de neutro debe ser cero:
$$I_n = I_a + I_b + I_c$$

En forma rectangular:
- $I_a = 4.39\angle -53.13° = 2.634 - j3.512$
- $I_b = 4.39\angle -173.13° = -4.359 - j0.526$
- $I_c = 4.39\angle 66.87° = 1.725 + j4.038$

$$I_n = (2.634 - 4.359 + 1.725) + j(-3.512 - 0.526 + 4.038)$$
$$I_n = 0 + j0 = 0 \checkmark$$

## Tabla Resumen

| Parámetro | Fase a | Fase b | Fase c |
|-----------|--------|--------|--------|
| Vf | 219.4∠0° V | 219.4∠-120° V | 219.4∠120° V |
| IL | 4.39∠-53.13° A | 4.39∠-173.13° A | 4.39∠66.87° A |
| Sf | 963.2∠53.13° VA | 963.2∠53.13° VA | 963.2∠53.13° VA |

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| a) Van | **219.4∠0° V** |
| a) Vbn | **219.4∠-120° V** |
| a) Vcn | **219.4∠120° V** |
| b) Ia | **4.39∠-53.13° A** |
| b) Ib | **4.39∠-173.13° A** |
| b) Ic | **4.39∠66.87° A** |
| c) P total | **1735.2 W** |
| c) Q total | **2309.4 VAR** |
| c) S total | **2889.6 VA** |
| d) FP | **0.6 en atraso** |

## Relaciones Importantes Y-Y

| Conexión Y | Relación |
|------------|----------|
| VL = √3 × Vf | Voltaje línea vs fase |
| IL = If | Corriente línea = fase |
| P = √3 × VL × IL × cosθ | Potencia activa |
| Q = √3 × VL × IL × sinθ | Potencia reactiva |
| S = √3 × VL × IL | Potencia aparente |

## Conceptos Aplicados
- Sistema trifásico balanceado
- Conexión estrella (Y)
- Secuencia de fases positiva
- Relación VL/Vf en conexión Y
- Potencias trifásicas
- Factor de potencia