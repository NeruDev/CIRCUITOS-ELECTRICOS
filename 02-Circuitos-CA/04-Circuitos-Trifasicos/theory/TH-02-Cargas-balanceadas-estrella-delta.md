# TH-02: Circuitos Trifásicos con Cargas Balanceadas en Estrella y Delta

## Objetivos
- Analizar conexiones estrella (Y) y delta (Δ)
- Calcular voltajes y corrientes en sistemas balanceados
- Aplicar equivalentes monofásicos

## Contenido

### Conexión Estrella (Y)

```
        a
        │
       Za
        │
n ──────┼────── neutro
        │
       Zb      Zc
        │     /
        b    c
```

**Características:**
- Punto neutro común
- Corriente de línea = corriente de fase
- Voltaje de línea = √3 × voltaje de fase

**Relaciones:**
$$I_L = I_f$$
$$V_L = \sqrt{3}V_f$$
$$\mathbf{V}_{ab} = \mathbf{V}_{an} - \mathbf{V}_{bn} = \sqrt{3}V_f\angle 30°$$

### Conexión Delta (Δ)

```
    a ────Zab──── b
     \          /
      \        /
      Zca    Zbc
        \    /
         \  /
          c
```

**Características:**
- Sin punto neutro
- Voltaje de línea = voltaje de fase
- Corriente de línea = √3 × corriente de fase

**Relaciones:**
$$V_L = V_f$$
$$I_L = \sqrt{3}I_f$$
$$\mathbf{I}_a = \mathbf{I}_{ab} - \mathbf{I}_{ca} = \sqrt{3}I_f\angle -30°$$

### Sistema Balanceado

Un sistema es **balanceado** cuando:
- Las tres impedancias de carga son iguales: Za = Zb = Zc = Z
- Los voltajes de fuente están balanceados

### Equivalente Monofásico

Para sistemas balanceados, se puede analizar solo una fase:

```
    Zlinea
○───⬚───┬───○
        │
   Vf  Zf
        │
○───────┴───○
   Neutro
```

**Procedimiento:**
1. Convertir delta a estrella si es necesario
2. Analizar una fase con el equivalente monofásico
3. Las otras fases tienen los mismos valores con ±120° de desfase

### Conversión Delta-Estrella

$$Z_Y = \frac{Z_\Delta}{3}$$

Para cargas iguales en delta, la impedancia equivalente en estrella es 1/3.

### Tabla de Relaciones (Sistema Balanceado)

| Cantidad | Estrella (Y) | Delta (Δ) |
|----------|--------------|-----------|
| VL | √3 Vf | Vf |
| IL | If | √3 If |
| Vf | VL/√3 | VL |
| If | IL | IL/√3 |

### Ejemplo: Carga Balanceada en Y

**Datos:** VL = 400V, Z = 10+j8Ω (por fase), secuencia abc

**Solución:**
1. Voltaje de fase: Vf = 400/√3 = 231V
2. Van = 231∠0° V
3. Corriente de línea: Ia = Van/Z = 231∠0°/(10+j8)
4. |Z| = √(100+64) = 12.8Ω, θ = arctan(8/10) = 38.7°
5. Ia = 231/12.8 ∠-38.7° = 18∠-38.7° A

### Ejemplo: Carga Balanceada en Δ

**Datos:** VL = 400V, ZΔ = 30∠30°Ω

**Solución:**
1. Voltaje de fase = VL = 400V
2. Corriente de fase: If = 400/30 = 13.3A
3. Corriente de línea: IL = √3 × 13.3 = 23.1A

## Conceptos Clave
- Estrella: IL = If, VL = √3Vf
- Delta: VL = Vf, IL = √3If
- Sistemas balanceados: equivalente monofásico
