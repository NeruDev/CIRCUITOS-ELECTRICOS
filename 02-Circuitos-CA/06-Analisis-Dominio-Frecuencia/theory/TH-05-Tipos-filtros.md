# TH-05: Tipos de Filtros

## Objetivos
- Clasificar los tipos básicos de filtros
- Diseñar filtros pasivos simples
- Analizar características de filtros

## Contenido

### Clasificación de Filtros

Los filtros se clasifican según las frecuencias que permiten pasar:

| Tipo | Frecuencias que pasan | H(0) | H(∞) |
|------|----------------------|------|------|
| Pasa-bajas (LP) | Bajas | 1 | 0 |
| Pasa-altas (HP) | Altas | 0 | 1 |
| Pasa-banda (BP) | Banda central | 0 | 0 |
| Rechaza-banda (BR) | Bajas y altas | 1 | 1 |

### Filtro Pasa-Bajas (Low-Pass)

**Características:**
- Permite frecuencias < fc
- Atenúa frecuencias > fc

```
|H|
1├────╲
 │     ╲
 │      ╲
 │       ╲____
0└────────────── ω
      ωc
```

**[Circuito](../../../glossary.md#circuito) RC:**
```
    R
○──/\/\/──┬──○
          C
○─────────┴──○
```
$$H(s) = \frac{1}{1 + sRC}, \quad \omega_c = \frac{1}{RC}$$

### Filtro Pasa-Altas (High-Pass)

**Características:**
- Permite frecuencias > fc
- Atenúa frecuencias < fc

```
|H|
1│       ╱────
 │      ╱
 │     ╱
 │____╱
0└────────────── ω
      ωc
```

**Circuito RC:**
```
    C
○──||──┬──○
       R
○──────┴──○
```
$$H(s) = \frac{sRC}{1 + sRC}, \quad \omega_c = \frac{1}{RC}$$

### Filtro Pasa-Banda (Band-Pass)

**Características:**
- Permite frecuencias entre ω₁ y ω₂
- Atenúa frecuencias fuera de la banda

```
|H|
1│     ╱╲
 │    ╱  ╲
 │   ╱    ╲
 │__╱      ╲__
0└────────────── ω
   ω₁ ω₀ ω₂
```

**Circuito RLC serie ([voltaje](../../../glossary.md#voltaje) en R):**
$$H(s) = \frac{sR/L}{s^2 + sR/L + 1/LC}$$

**Parámetros:**
- Frecuencia central: ω₀ = 1/√(LC)
- Ancho de banda: BW = R/L
- Factor de calidad: Q = ω₀L/R

### Filtro Rechaza-Banda (Band-Stop/Notch)

**Características:**
- Atenúa frecuencias entre ω₁ y ω₂
- Permite frecuencias fuera de la banda

```
|H|
1├──╲    ╱──
 │   ╲  ╱
 │    ╲╱
 │    
0└────────────── ω
      ω₀
```

**Circuito RLC serie (voltaje en LC):**
$$H(s) = \frac{s^2 + 1/LC}{s^2 + sR/L + 1/LC}$$

### Comparación de Circuitos

| Circuito | Voltaje medido en | Tipo de filtro |
|----------|-------------------|----------------|
| RC | C | Pasa-bajas |
| RC | R | Pasa-altas |
| RLC serie | R | Pasa-banda |
| RLC serie | L+C | Rechaza-banda |

### Orden del Filtro

El **orden** determina qué tan rápido cae la respuesta fuera de la banda:

| Orden | Pendiente fuera de banda | Componentes típicos |
|-------|-------------------------|-------------------|
| 1 | 20 dB/década | 1 L o 1 C |
| 2 | 40 dB/década | L y C |
| n | 20n dB/década | n reactivos |

### Filtros Activos vs Pasivos

**Filtros pasivos:**
- Solo R, L, C
- No requieren alimentación
- Limitados en ganancia y selectividad

**Filtros activos:**
- Usan amplificadores operacionales
- Pueden tener ganancia > 1
- Evitan inductores (costosos y grandes)

### Especificaciones de Filtros

- **[Frecuencia](../../../glossary.md#frecuencia) de corte (fc):** Punto de -3 dB
- **Ancho de banda (BW):** Rango de frecuencias -3 dB
- **Atenuación en banda de rechazo:** dB de reducción
- **Rizado en banda de paso:** Variación permitida

### Ejemplo de Diseño

**Diseñar filtro pasa-bajas RC con fc = 1 kHz**

1. ωc = 2π × 1000 = 6283 rad/s
2. Elegir C = 0.1 μF
3. R = 1/(ωc × C) = 1/(6283 × 10⁻⁷) = 1.59 kΩ

Usar R = 1.6 kΩ (valor comercial)

## Conceptos Clave
- LP: fc = 1/RC
- BP: f₀ = 1/(2π√LC), BW = R/L
- Orden determina pendiente de atenuación
