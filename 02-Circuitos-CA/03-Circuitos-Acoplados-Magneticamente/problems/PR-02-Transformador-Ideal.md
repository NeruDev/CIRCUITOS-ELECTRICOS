```markdown
# PR-02: Transformador Ideal - Relación de Transformación ⭐⭐

## Enunciado
Un transformador ideal tiene N₁ = 500 vueltas en el primario y N₂ = 100 vueltas en el secundario. Se conecta una carga ZL = 8Ω en el secundario y una fuente Vs = 120∠0° V en el primario. Determine:
a) La relación de transformación n
b) El voltaje en el secundario V₂
c) Las corrientes I₁ e I₂
d) La impedancia vista desde el primario Zin
e) La potencia entregada a la carga

## Diagrama del Circuito

```
    Primario          Transformador         Secundario
                         Ideal
       I₁ →           N₁ : N₂            ← I₂
    ●────────┐      ┌───┬───┐      ┌────────●
    │        │      │   │   │      │        │
  + │       ┌┴┐    ╔╧═══╧═══╧╗    ┌┴┐     + │
Vs (─)      │ │    ║   ●●    ║    │ │    V₂│
120V│       │N₁│   ║ ┃    ┃  ║   │N₂│      │
  - │       │500   ║ ┃    ┃  ║   │100│     - │
    │       └┬┘    ╚═══════════╝    └┬┘      │
    │        │      └───────┘      │     ┌──┴──┐
    ●────────┴─────────────────────┴─────┤ ZL  │
                                         │  8Ω │
                                         └──┬──┘
                                            │
                                           ─┴─
```

## Netlist SPICE

```spice
* PR-02: Transformador Ideal
* Usando acoplamiento k ≈ 1 con inductancias grandes

* Modelo aproximado de transformador ideal:
* L1 y L2 muy grandes con k ≈ 1
* n = N1/N2 = sqrt(L1/L2) → L1/L2 = n²

V1 1 0 AC 120 0       ; Fuente 120V∠0°
L1 1 0 25             ; L1 grande (elegimos L1 = 25H)
L2 2 0 1              ; L2 = L1/n² = 25/25 = 1H para n=5
K1 L1 L2 0.9999       ; k ≈ 1 (ideal)
RL 2 0 8              ; Carga ZL = 8Ω

.AC LIN 1 60 60       ; Análisis a 60 Hz
.PRINT AC VM(2) IM(L1) IM(L2) 
.END
```

## Solución

### Datos
- N₁ = 500 vueltas
- N₂ = 100 vueltas
- Vs = V₁ = 120∠0° V
- ZL = 8 Ω

### Propiedades del Transformador Ideal

1. **Relación de voltajes:** $\frac{V_1}{V_2} = \frac{N_1}{N_2} = n$
2. **Relación de corrientes:** $\frac{I_1}{I_2} = \frac{N_2}{N_1} = \frac{1}{n}$
3. **Conservación de potencia:** $V_1 I_1^* = V_2 I_2^*$ (potencia compleja se conserva)

### Parte a) Relación de transformación

$$n = \frac{N_1}{N_2} = \frac{500}{100} = 5$$

$$\boxed{n = 5:1 \text{ (reductor de voltaje)}}$$

### Parte b) Voltaje en el secundario

$$V_2 = \frac{V_1}{n} = \frac{120\angle 0°}{5}$$

$$\boxed{V_2 = 24\angle 0° \text{ V}}$$

En el dominio del tiempo:
$$v_2(t) = 24\cos(\omega t)\text{ V}$$

### Parte c) Corrientes I₁ e I₂

**Corriente en el secundario:**
$$I_2 = \frac{V_2}{Z_L} = \frac{24\angle 0°}{8\angle 0°}$$

$$\boxed{I_2 = 3\angle 0° \text{ A}}$$

**Corriente en el primario:**
$$I_1 = \frac{I_2}{n} = \frac{3\angle 0°}{5}$$

$$\boxed{I_1 = 0.6\angle 0° \text{ A}}$$

**Verificación de potencia:**
$$S_1 = V_1 I_1^* = (120)(0.6) = 72\text{ VA}$$
$$S_2 = V_2 I_2^* = (24)(3) = 72\text{ VA ✓}$$

### Parte d) Impedancia vista desde el primario

La impedancia reflejada al primario:
$$Z_{in} = n^2 \times Z_L = (5)^2 \times 8 = 25 \times 8$$

$$\boxed{Z_{in} = 200\text{ Ω}}$$

**Verificación:**
$$Z_{in} = \frac{V_1}{I_1} = \frac{120}{0.6} = 200\text{ Ω ✓}$$

### Parte e) Potencia entregada a la carga

$$P_L = |I_2|^2 \times R_L = (3)^2 \times 8 = 9 \times 8$$

$$\boxed{P_L = 72\text{ W}}$$

**Verificación desde el primario:**
$$P_{in} = |I_1|^2 \times Z_{in} = (0.6)^2 \times 200 = 0.36 \times 200 = 72\text{ W ✓}$$

En un transformador ideal, toda la potencia de entrada se transfiere a la carga (eficiencia = 100%).

## Reflexión de Impedancias

```
Vista desde          Transformador         Vista desde
el primario            Ideal               el secundario
    
    ┌───────┐        n : 1                 ┌───────┐
    │       │     ┌───┬───┐               │       │
  ──┤ Zin   ├──   │   │   │   ──────────┤  ZL   ├──
    │ n²ZL  │     │   │   │               │       │
    └───────┘     └───┴───┘               └───────┘
    
    200Ω           5 : 1                    8Ω
```

## Tabla Resumen

| Parámetro | Primario | Secundario |
|-----------|----------|------------|
| Vueltas | N₁ = 500 | N₂ = 100 |
| Voltaje | V₁ = 120V | V₂ = 24V |
| Corriente | I₁ = 0.6A | I₂ = 3A |
| Impedancia | Zin = 200Ω | ZL = 8Ω |
| Potencia | Pin = 72W | PL = 72W |

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| a) n | **5:1 (reductor)** |
| b) V₂ | **24∠0° V** |
| c) I₂ | **3∠0° A** |
| c) I₁ | **0.6∠0° A** |
| d) Zin | **200 Ω** |
| e) PL | **72 W** |

## Aplicaciones del Transformador

1. **Adaptación de impedancias:** Hacer que ZL "parezca" n²ZL
2. **Elevación/reducción de voltaje:** Distribución de energía eléctrica
3. **Aislamiento galvánico:** Separar circuitos eléctricamente

## Simulación SPICE - Resultados Esperados
```
A f = 60 Hz:
VM(2) = 24V (voltaje secundario)
IM(L1) = 0.6A (corriente primario)
IM(L2) = 3A (corriente secundario)
Potencia = V2 × I2 = 72W
```

## Conceptos Aplicados
- Relación de transformación: n = N₁/N₂
- Transformación de voltaje: V₂ = V₁/n
- Transformación de corriente: I₁ = I₂/n
- Reflexión de impedancia: Zin = n²ZL
- Conservación de potencia en transformador ideal
```
