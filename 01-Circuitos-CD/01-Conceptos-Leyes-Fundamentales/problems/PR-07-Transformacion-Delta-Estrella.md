# PR-07: Transformación Delta-Estrella ⭐⭐

## Enunciado
Un circuito contiene una configuración delta (triángulo) con Ra = 30Ω, Rb = 60Ω, Rc = 90Ω conectada a una fuente de 120V. Determine:
a) Las resistencias equivalentes en configuración estrella (Y)
b) La corriente entregada por la fuente

## Diagrama del Circuito

```
Delta (Δ):                    Estrella (Y):

       a                            a
      /\                            |
   Ra/  \Rb                        R₁
  30Ω    60Ω                        |
   /      \                     ────○────
  b───Rc───c                    |       |
     90Ω                       R₂       R₃
                               |       |
                               b       c
```

**Circuito completo:**
```
         ┌────────[Ra=30Ω]────────┐
         │                        │
       + │          a             │
      (Vs)                       │
      120V          │            │
       - │    Rb=60Ω│            │Rc=90Ω
         │          │            │
         │          │            │
         └────b─────┴─────c──────┘
```

## Netlist SPICE

```spice
* PR-07: Transformacion Delta a Estrella
* Circuito original en Delta

V1 1 0 DC 120V     ; Fuente de voltaje 120V
Ra 1 2 30          ; Ra = 30Ω entre nodos 1(a) y 2(b)
Rb 1 3 60          ; Rb = 60Ω entre nodos 1(a) y 3(c)
Rc 2 3 90          ; Rc = 90Ω entre nodos 2(b) y 3(c)
Rload 2 0 1m       ; Cortocircuito de b a tierra (para completar)
Rload2 3 0 1m      ; Cortocircuito de c a tierra

.OP
.END
```

```spice
* PR-07b: Circuito equivalente en Estrella

V1 1 0 DC 120V     ; Fuente de voltaje 120V
R1 1 4 10          ; R1 = 10Ω (estrella)
R2 4 0 15          ; R2 = 15Ω (estrella)  
R3 4 0 30          ; R3 = 30Ω (estrella, en paralelo con R2)

.OP
.END
```

## Solución

### Datos
- Ra = 30 Ω (entre a y b)
- Rb = 60 Ω (entre a y c)
- Rc = 90 Ω (entre b y c)
- Vs = 120 V

### Parte a) Transformación Δ → Y

Las fórmulas de transformación Delta a Estrella son:

$$R_1 = \frac{R_a \cdot R_b}{R_a + R_b + R_c}$$

$$R_2 = \frac{R_a \cdot R_c}{R_a + R_b + R_c}$$

$$R_3 = \frac{R_b \cdot R_c}{R_a + R_b + R_c}$$

**Denominador común:**
$$R_a + R_b + R_c = 30 + 60 + 90 = 180\text{ Ω}$$

**Cálculo de R₁ (conectada al nodo a):**
$$R_1 = \frac{R_a \cdot R_b}{180} = \frac{(30)(60)}{180} = \frac{1800}{180} = 10\text{ Ω}$$

**Cálculo de R₂ (conectada al nodo b):**
$$R_2 = \frac{R_a \cdot R_c}{180} = \frac{(30)(90)}{180} = \frac{2700}{180} = 15\text{ Ω}$$

**Cálculo de R₃ (conectada al nodo c):**
$$R_3 = \frac{R_b \cdot R_c}{180} = \frac{(60)(90)}{180} = \frac{5400}{180} = 30\text{ Ω}$$

### Parte b) Corriente de la fuente

Asumiendo que los nodos b y c están conectados a tierra (referencia):

**En configuración estrella:**
- R₂ y R₃ están en paralelo (ambas conectadas entre el centro y tierra)

$$R_{23} = \frac{R_2 \cdot R_3}{R_2 + R_3} = \frac{(15)(30)}{15 + 30} = \frac{450}{45} = 10\text{ Ω}$$

**Resistencia total:**
$$R_{total} = R_1 + R_{23} = 10 + 10 = 20\text{ Ω}$$

**Corriente de la fuente:**
$$I_s = \frac{V_s}{R_{total}} = \frac{120\text{ V}}{20\text{ Ω}} = 6\text{ A}$$

## Respuestas

| Magnitud | Valor |
|----------|-------|
| a) R₁ | **10 Ω** |
| a) R₂ | **15 Ω** |
| a) R₃ | **30 Ω** |
| b) Is | **6 A** |

## Tabla Resumen de Transformaciones

### Delta (Δ) → Estrella (Y)
$$R_1 = \frac{R_a R_b}{R_a + R_b + R_c}$$

### Estrella (Y) → Delta (Δ)
$$R_a = \frac{R_1 R_2 + R_2 R_3 + R_1 R_3}{R_3}$$

### Caso especial: Resistencias iguales
- Si $R_\Delta = R_a = R_b = R_c$, entonces $R_Y = \frac{R_\Delta}{3}$
- Si $R_Y = R_1 = R_2 = R_3$, entonces $R_\Delta = 3R_Y$

## Conceptos Aplicados
- Transformación Delta-Estrella
- Equivalencia de circuitos
- Simplificación de redes