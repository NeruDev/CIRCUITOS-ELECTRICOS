# PR-02: Sistema Trifásico Y-Δ ⭐⭐⭐

## Enunciado
Una fuente trifásica balanceada en Y con [voltaje](../../../glossary.md#voltaje) de línea VL = 440V alimenta una [carga](../../../glossary.md#carga) balanceada conectada en [delta](../../../glossary.md#delta) (Δ) con ZΔ = 45∠30° Ω por fase. Determine:
a) Los voltajes de fase de la fuente y de la carga
b) Las corrientes de fase en la carga
c) Las corrientes de línea
d) La potencia total consumida por la carga

## Diagrama del Circuito

```
    Fuente Y                            Carga Δ
    
         Van                         a' ●───────●
    ●─────────● a ──────────────────●   │ ZΔ    │
    │                               │   │       │
    │    Vbn                        │  ┌┴┐     ┌┴┐
    ●─────────● b ──────────────────●──┤ZΔ├─────┤ZΔ├──●
    │                               │  └┬┘     └┬┘   │
    │    Vcn                        │   │       │    │
    ●─────────● c ──────────────────●───┴───────┴────●
    │                               │
    └─────────● n                   │  ZΔ = 45∠30° Ω
                                    │
                                    c'
    VL = 440V
```

### Detalle de la Carga Delta

```
                a' (línea a)
                ●
               /│\
              / │ \
         Zab /  │  \ Zca
            /   │   \
           /    │    \
    b' ●───────●───────● c'
     (línea b)  Zbc  (línea c)
    
    Zab = Zbc = Zca = ZΔ = 45∠30° Ω
```

## Netlist SPICE

```spice
* PR-02: Sistema Trifásico Y-Δ
* Fuente Y con VL = 440V, Carga Delta

* Voltaje de fase fuente: Vf = VL/√3 = 440/1.732 = 254.0V
Va 1 0 AC 254.0 0        ; Van = 254∠0° V
Vb 2 0 AC 254.0 -120     ; Vbn = 254∠-120° V
Vc 3 0 AC 254.0 120      ; Vcn = 254∠120° V

* Carga Delta: ZΔ = 45∠30° = 38.97 + j22.5 Ω
* R = 38.97Ω, XL = 22.5Ω
* XL = ωL → L = XL/(2πf) = 22.5/(2π×60) = 59.7mH

* Impedancia entre líneas (delta)
Rab 1 2 38.97
Lab 1 2 59.7m

Rbc 2 3 38.97
Lbc 2 3 59.7m

Rca 3 1 38.97
Lca 3 1 59.7m

.AC LIN 1 60 60
.PRINT AC IM(Rab) IP(Rab) IM(Va) IP(Va)
.END
```

## Solución

### Datos
- VL = 440 V (voltaje de línea)
- ZΔ = 45∠30° Ω ([impedancia](../../../glossary.md#impedancia) de carga por fase delta)

### Parte a) Voltajes

**Voltaje de fase de la fuente (Y):**
$$V_f = \frac{V_L}{\sqrt{3}} = \frac{440}{1.732} = 254.0\text{ V}$$

$$\boxed{V_{an} = 254.0\angle 0° \text{ V}}$$
$$\boxed{V_{bn} = 254.0\angle -120° \text{ V}}$$
$$\boxed{V_{cn} = 254.0\angle 120° \text{ V}}$$

**Voltaje de fase de la carga (Δ):**
En conexión delta, el voltaje de fase de la carga es igual al voltaje de línea:
$$V_{Δ} = V_L = 440\text{ V}$$

Los voltajes de línea (fase-fase):
$$V_{ab} = V_{an} - V_{bn} = V_L\angle 30°$$

$$\boxed{V_{ab} = 440\angle 30° \text{ V}}$$
$$\boxed{V_{bc} = 440\angle -90° \text{ V}}$$
$$\boxed{V_{ca} = 440\angle 150° \text{ V}}$$

### Parte b) Corrientes de fase en la carga

Las corrientes de fase en la carga delta:
$$I_{ab} = \frac{V_{ab}}{Z_Δ} = \frac{440\angle 30°}{45\angle 30°}$$

$$\boxed{I_{ab} = 9.78\angle 0° \text{ A}}$$

$$I_{bc} = \frac{V_{bc}}{Z_Δ} = \frac{440\angle -90°}{45\angle 30°}$$

$$\boxed{I_{bc} = 9.78\angle -120° \text{ A}}$$

$$I_{ca} = \frac{V_{ca}}{Z_Δ} = \frac{440\angle 150°}{45\angle 30°}$$

$$\boxed{I_{ca} = 9.78\angle 120° \text{ A}}$$

**Magnitud de corriente de fase:**
$$I_Δ = I_f = 9.78\text{ A}$$

### Parte c) Corrientes de línea

En conexión delta, la [corriente](../../../glossary.md#corriente) de línea es √3 veces la corriente de fase:
$$I_L = \sqrt{3} \times I_Δ = \sqrt{3} \times 9.78 = 16.94\text{ A}$$

Por LCK en cada nodo de la delta:

**Nodo a':**
$$I_a = I_{ab} - I_{ca} = 9.78\angle 0° - 9.78\angle 120°$$

Convertimos a rectangular:
- $I_{ab} = 9.78\angle 0° = 9.78 + j0$
- $I_{ca} = 9.78\angle 120° = -4.89 + j8.47$

$$I_a = (9.78 + 4.89) + j(0 - 8.47) = 14.67 - j8.47$$
$$I_a = 16.94\angle -30°\text{ A}$$

$$\boxed{I_a = 16.94\angle -30° \text{ A}}$$
$$\boxed{I_b = 16.94\angle -150° \text{ A}}$$
$$\boxed{I_c = 16.94\angle 90° \text{ A}}$$

### Parte d) Potencia total

**Potencia compleja por fase:**
$$S_{fase} = V_{ab} \times I_{ab}^* = 440\angle 30° \times 9.78\angle 0°$$
$$S_{fase} = 4303.2\angle 30°\text{ VA}$$

**Potencia total (3 fases):**
$$S_{total} = 3 \times S_{fase} = 3 \times 4303.2\angle 30°$$
$$S_{total} = 12909.6\angle 30°\text{ VA}$$

**Componentes:**
$$\boxed{P = |S|\cos(30°) = 12909.6 \times 0.866 = 11180\text{ W} = 11.18\text{ kW}}$$
$$\boxed{Q = |S|\sin(30°) = 12909.6 \times 0.5 = 6454.8\text{ VAR} = 6.45\text{ kVAR}}$$
$$\boxed{|S| = 12.91\text{ kVA}}$$

**Verificación con fórmula de línea:**
$$P = \sqrt{3} \times V_L \times I_L \times \cos\theta$$
$$P = \sqrt{3} \times 440 \times 16.94 \times \cos(30°)$$
$$P = 1.732 \times 440 \times 16.94 \times 0.866 = 11180\text{ W ✓}$$

## Resumen de Relaciones Y-Δ

| Parámetro | Conexión Y | Conexión Δ |
|-----------|------------|------------|
| V línea | VL = √3 × Vf | VL = VΔ |
| I línea | IL = If | IL = √3 × IΔ |
| V fase carga | Vf = VL/√3 | VΔ = VL |
| I fase carga | If = IL | IΔ = IL/√3 |

## Diagrama Fasorial

```
              Ic = 16.94∠90°
                   │
                   │
                   │
    ───────────────●───────────────
                  /│\
           Iab   / │ \ Vab
          9.78∠0° │   440∠30°
                 / │   \
                /  │    \
     ●─────────    │     ─────────●
   Ia = 16.94∠-30° │      Ib = 16.94∠-150°
```

## Tabla Resumen

| Parámetro | Valor |
|-----------|-------|
| Vf fuente (Y) | 254 V |
| VΔ carga (Δ) | 440 V |
| IΔ (fase delta) | 9.78 A |
| IL (línea) | 16.94 A |
| P total | 11.18 kW |
| Q total | 6.45 kVAR |
| S total | 12.91 kVA |
| FP | 0.866 en atraso |

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| a) Vf fuente | **254∠0°, 254∠-120°, 254∠120° V** |
| a) VΔ carga | **440∠30°, 440∠-90°, 440∠150° V** |
| b) Iab | **9.78∠0° A** |
| b) Ibc | **9.78∠-120° A** |
| b) Ica | **9.78∠120° A** |
| c) Ia | **16.94∠-30° A** |
| c) Ib | **16.94∠-150° A** |
| c) Ic | **16.94∠90° A** |
| d) P | **11.18 kW** |
| d) Q | **6.45 kVAR** |

## Conceptos Aplicados
- Conversión Y a Δ
- Relación voltaje línea-fase en Δ: VL = VΔ
- Relación corriente línea-fase en Δ: IL = √3 × IΔ
- Desfase 30° entre corriente de línea y de fase
- Potencia trifásica