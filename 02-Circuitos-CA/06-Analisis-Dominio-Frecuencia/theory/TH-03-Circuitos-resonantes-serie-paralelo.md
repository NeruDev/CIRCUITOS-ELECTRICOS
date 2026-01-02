# TH-03: Circuitos Resonantes Serie y Paralelo

## Objetivos
- Definir [resonancia](../../../glossary.md#resonancia) en circuitos RLC
- Calcular [frecuencia](../../../glossary.md#frecuencia) de resonancia y factor de calidad
- Analizar circuitos resonantes serie y paralelo

## Contenido

### Concepto de Resonancia

La **resonancia** ocurre cuando la [reactancia](../../../glossary.md#reactancia) inductiva iguala a la reactancia capacitiva:

$$X_L = X_C$$
$$\omega L = \frac{1}{\omega C}$$

### Frecuencia de Resonancia

$$\omega_0 = \frac{1}{\sqrt{LC}}$$
$$f_0 = \frac{1}{2\pi\sqrt{LC}}$$

A esta frecuencia, el [circuito](../../../glossary.md#circuito) es puramente resistivo.

### Circuito RLC Serie Resonante

```
    R       L       C
○──/\/\/──⌇⌇⌇──||──○
```

**[Impedancia](../../../glossary.md#impedancia):**
$$Z = R + j\omega L + \frac{1}{j\omega C} = R + j\left(\omega L - \frac{1}{\omega C}\right)$$

**En resonancia (ω = ω₀):**
- Z = R (mínima)
- Corriente máxima: I = V/R
- VL y VC pueden ser >> V (amplificación)

### Circuito RLC Paralelo Resonante

```
○──┬──┬──┬──○
   R  L  C
○──┴──┴──┴──○
```

**Admitancia:**
$$Y = \frac{1}{R} + \frac{1}{j\omega L} + j\omega C = \frac{1}{R} + j\left(\omega C - \frac{1}{\omega L}\right)$$

**En resonancia (ω = ω₀):**
- Y = 1/R (mínima)
- Z = R (máxima)
- [Corriente](../../../glossary.md#corriente) de entrada mínima

### Factor de Calidad (Q)

El **factor de calidad** Q indica la "selectividad" del circuito:

**Serie:**
$$Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 RC} = \frac{1}{R}\sqrt{\frac{L}{C}}$$

**Paralelo:**
$$Q = R\omega_0 C = \frac{R}{\omega_0 L} = R\sqrt{\frac{C}{L}}$$

### Significado del Factor Q

- Q alto: Resonancia aguda (selectiva)
- Q bajo: Resonancia amplia (poco selectiva)

**Relación con amplificación:**
- En serie: VL/V = VC/V = Q (en resonancia)
- En paralelo: IL/I = IC/I = Q (en resonancia)

### Ancho de Banda

El ancho de banda está relacionado con Q:

$$BW = \frac{\omega_0}{Q} = \frac{f_0}{Q}$$

**Frecuencias de corte (-3 dB):**
$$\omega_1 = \omega_0\left(\sqrt{1 + \frac{1}{4Q^2}} - \frac{1}{2Q}\right)$$
$$\omega_2 = \omega_0\left(\sqrt{1 + \frac{1}{4Q^2}} + \frac{1}{2Q}\right)$$

Para Q alto: ω₁ ≈ ω₀ - BW/2, ω₂ ≈ ω₀ + BW/2

### Curva de Resonancia

```
|H|
│     ╱╲
│    ╱  ╲   Q alto
│   ╱    ╲
│──╱──────╲── Q bajo
│ ╱        ╲
└──────────────── ω
       ω₀
```

### Aplicaciones de Resonancia

1. **Sintonización de radio:** Selección de frecuencias
2. **Filtros:** Banda pasante estrecha
3. **Osciladores:** Generación de frecuencias
4. **Antenas:** Adaptación de impedancia

### Ejemplo

**Datos:** R = 10Ω, L = 1mH, C = 10nF

**Cálculos:**
1. ω₀ = 1/√(10⁻³ × 10⁻⁸) = 10⁵ rad/s
2. f₀ = 10⁵/(2π) = 15.9 kHz
3. Q = (10⁵ × 10⁻³)/10 = 10
4. BW = 10⁵/10 = 10⁴ rad/s = 1.59 kHz

## Conceptos Clave
- ω₀ = 1/√(LC)
- Q = ω₀L/R (serie) o Q = R/(ω₀L) (paralelo)
- BW = ω₀/Q
