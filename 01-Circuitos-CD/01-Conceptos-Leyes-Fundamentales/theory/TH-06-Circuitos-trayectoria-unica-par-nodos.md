# TH-06: Análisis de Circuitos de Una Sola Trayectoria y de Un Par de Nodos

## Objetivos
- Analizar circuitos con una sola trayectoria (serie)
- Analizar circuitos con un par de nodos (paralelo)
- Aplicar [LCK](../../../glossary.md#lck) y [LVK](../../../glossary.md#lvk) en configuraciones básicas

## Contenido

### Circuito de Una Sola Trayectoria (Serie)

En un [circuito](../../../glossary.md#circuito) serie, todos los elementos comparten la **misma [corriente](../../../glossary.md#corriente)**.

```
    R₁        R₂        R₃
+──/\/\/──┬──/\/\/──┬──/\/\/──┐
│         │         │         │
Vs        v₁        v₂        v₃
│                             │
└─────────────────────────────┘
```

**Características:**
- La corriente es igual en todos los elementos: i = i₁ = i₂ = i₃
- Los voltajes se suman: Vs = v₁ + v₂ + v₃

**[Resistencia](../../../glossary.md#resistencia) equivalente en serie:**
$$R_{eq} = R_1 + R_2 + R_3 + ... + R_n$$

**Corriente en el circuito:**
$$i = \frac{V_s}{R_{eq}} = \frac{V_s}{R_1 + R_2 + ... + R_n}$$

### Circuito de Un Par de Nodos (Paralelo)

En un circuito paralelo, todos los elementos comparten el **mismo [voltaje](../../../glossary.md#voltaje)**.

```
        ┌──/\/\/──┐
        │   R₁    │
        ├──/\/\/──┤
+  Is → │   R₂    │ v
        ├──/\/\/──┤
        │   R₃    │
        └─────────┘
```

**Características:**
- El voltaje es igual en todos los elementos: v = v₁ = v₂ = v₃
- Las corrientes se suman: Is = i₁ + i₂ + i₃

**Resistencia equivalente en paralelo:**
$$\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + ... + \frac{1}{R_n}$$

**Para dos resistencias en paralelo:**
$$R_{eq} = \frac{R_1 \cdot R_2}{R_1 + R_2}$$

**Conductancia equivalente:**
$$G_{eq} = G_1 + G_2 + G_3 + ... + G_n$$

donde G = 1/R (Siemens)

### Ejemplos

**Ejemplo 1: Circuito Serie**
- Vs = 12V, R₁ = 2Ω, R₂ = 4Ω
- Req = 2 + 4 = 6Ω
- i = 12/6 = 2A
- v₁ = 2×2 = 4V, v₂ = 2×4 = 8V

**Ejemplo 2: Circuito Paralelo**
- Is = 6A, R₁ = 3Ω, R₂ = 6Ω
- 1/Req = 1/3 + 1/6 = 3/6 = 1/2 → Req = 2Ω
- v = 6×2 = 12V
- i₁ = 12/3 = 4A, i₂ = 12/6 = 2A

## Conceptos Clave
- Corriente común en serie
- Voltaje común en paralelo
- Resistencia/conductancia equivalente
