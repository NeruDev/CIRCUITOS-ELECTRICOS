# PR-01: Inductores Acoplados - Coeficiente de Acoplamiento ⭐⭐

## Enunciado
Dos bobinas con L₁ = 100mH y L₂ = 400mH tienen un coeficiente de acoplamiento k = 0.6. Se conectan en serie con acoplamiento aditivo. Determine:
a) La [inductancia](../../../glossary.md#inductancia) mutua M
b) La inductancia total equivalente Leq
c) La inductancia total si se conectan con acoplamiento sustractivo
d) El rango de Leq para 0 ≤ k ≤ 1

Datos: L₁ = 100mH, L₂ = 400mH, k = 0.6

## Diagrama del Circuito

### Acoplamiento Aditivo (puntos del mismo lado)
```
    •──────────────•──────────────•
    │      L₁      │      L₂      │
   ┌┴┐    ●       ┌┴┐    ●       │
   │ │   100mH    │ │   400mH    │
   │ │←───M───→  │ │            │
   └┬┘            └┬┘            │
    •──────────────•──────────────•
    
    ● = punto de polaridad (marcas de punto)
    M = inductancia mutua
    k = 0.6
```

### Acoplamiento Sustractivo (puntos en lados opuestos)
```
    •──────────────•──────────────•
    │      L₁      │      L₂      │
   ┌┴┐    ●       ┌┴┐            │
   │ │   100mH    │ │   400mH ●  │
   │ │←───M───→  │ │            │
   └┬┘            └┬┘            │
    •──────────────•──────────────•
```

## Netlist SPICE

```spice
* PR-01: Inductores Acoplados en Serie

* Acoplamiento aditivo
L1 1 2 100mH        ; L1 = 100mH
L2 2 3 400mH        ; L2 = 400mH
K1 L1 L2 0.6        ; Coeficiente de acoplamiento k = 0.6

V1 1 0 AC 1 0
R1 3 0 1            ; Resistencia pequeña para cerrar circuito

.AC LIN 1 1k 1k
.PRINT AC IM(V1) VM(1)
* Z = V/I = jωLeq → Leq = Z/(jω)
.END
```

## Solución

### Datos
- L₁ = 100 mH = 0.1 H
- L₂ = 400 mH = 0.4 H
- k = 0.6

### Parte a) Inductancia mutua M

La inductancia mutua se relaciona con el coeficiente de acoplamiento:
$$k = \frac{M}{\sqrt{L_1 L_2}}$$

Despejando M:
$$M = k\sqrt{L_1 L_2} = 0.6\sqrt{(0.1)(0.4)}$$

$$M = 0.6\sqrt{0.04} = 0.6 \times 0.2 = 0.12\text{ H}$$

$$\boxed{M = 120\text{ mH}}$$

### Parte b) Inductancia equivalente - Acoplamiento aditivo

Para dos inductores en serie con **acoplamiento aditivo** (flujos se suman):
$$L_{eq(+)} = L_1 + L_2 + 2M$$

$$L_{eq(+)} = 100 + 400 + 2(120) = 100 + 400 + 240$$

$$\boxed{L_{eq(+)} = 740\text{ mH}}$$

### Parte c) Inductancia equivalente - Acoplamiento sustractivo

Para dos inductores en serie con **acoplamiento sustractivo** (flujos se oponen):
$$L_{eq(-)} = L_1 + L_2 - 2M$$

$$L_{eq(-)} = 100 + 400 - 2(120) = 100 + 400 - 240$$

$$\boxed{L_{eq(-)} = 260\text{ mH}}$$

### Parte d) Rango de Leq para 0 ≤ k ≤ 1

**Caso k = 0 (sin acoplamiento):**
$$M = 0$$
$$L_{eq} = L_1 + L_2 = 100 + 400 = 500\text{ mH}$$

**Caso k = 1 (acoplamiento perfecto):**
$$M_{max} = \sqrt{L_1 L_2} = \sqrt{(100)(400)} = 200\text{ mH}$$

- Aditivo: $L_{eq(+)} = 500 + 2(200) = 900$ mH
- Sustractivo: $L_{eq(-)} = 500 - 2(200) = 100$ mH

**Rango completo:**
$$\boxed{100\text{ mH} \leq L_{eq} \leq 900\text{ mH}}$$

### Tabla de Leq vs k

| k | M (mH) | Leq aditivo | Leq sustractivo |
|---|--------|-------------|-----------------|
| 0 | 0 | 500 mH | 500 mH |
| 0.2 | 40 | 580 mH | 420 mH |
| 0.4 | 80 | 660 mH | 340 mH |
| 0.6 | 120 | 740 mH | 260 mH |
| 0.8 | 160 | 820 mH | 180 mH |
| 1.0 | 200 | 900 mH | 100 mH |

## Gráfica

```
Leq (mH)
    │
900 ├────────────────────────● Aditivo (k=1)
    │                    ╱
800 │                ╱
    │            ╱
700 │        ╱
    │    ╱
600 │╱
    │
500 ├●──────────────────────── k=0
    │╲
400 │    ╲
    │        ╲
300 │            ╲
    │                ╲
200 │                    ╲
    │                        ╲
100 ├────────────────────────● Sustractivo (k=1)
    └─┴───┴───┴───┴───┴───┴──► k
      0  0.2 0.4 0.6 0.8 1.0
```

## Conceptos Físicos

**Regla del punto:** Los puntos indican los terminales con la misma polaridad de [voltaje](../../../glossary.md#voltaje) inducido.
- Si la [corriente](../../../glossary.md#corriente) **entra** por el terminal con punto en ambas bobinas → acoplamiento aditivo
- Si la corriente entra por el punto en una y sale por el punto en otra → acoplamiento sustractivo

**Coeficiente de acoplamiento:**
- k = 0: Sin acoplamiento (bobinas muy separadas)
- k = 1: Acoplamiento perfecto (todo el flujo de L₁ enlaza L₂)
- 0 < k < 1: Acoplamiento parcial (caso típico)

## Respuestas

| Parámetro | Valor |
|-----------|-------|
| a) M | **120 mH** |
| b) Leq aditivo | **740 mH** |
| c) Leq sustractivo | **260 mH** |
| d) Rango Leq | **100 mH a 900 mH** |

## Verificación SPICE

```spice
* Simulación para verificar Leq
* A 1kHz: XL = ωL = 2π(1000)L

* Con L1=100mH, L2=400mH, k=0.6
* Leq_aditivo = 740mH → XL = 4649Ω
* Leq_sustractivo = 260mH → XL = 1634Ω

* SPICE calcula automáticamente considerando M
```

## Conceptos Aplicados
- Inductancia mutua: M = k√(L₁L₂)
- Coeficiente de acoplamiento: 0 ≤ k ≤ 1
- Acoplamiento aditivo y sustractivo
- Convención de puntos
- Inductancia equivalente en serie