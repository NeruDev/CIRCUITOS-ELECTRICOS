# TH-04: Gráficas de Polos y Ceros en el Plano s

## Objetivos
- Definir polos y ceros de una función de transferencia
- Representar polos y ceros en el plano s
- Relacionar ubicación de polos con comportamiento del sistema

## Contenido

### Función de Transferencia Racional

Una función de transferencia típica tiene la forma:

$$H(s) = K\frac{(s - z_1)(s - z_2)...(s - z_m)}{(s - p_1)(s - p_2)...(s - p_n)}$$

### Definiciones

**Ceros:** Valores de s donde H(s) = 0
- Son las raíces del numerador
- Se representan con ○ en el plano s

**Polos:** Valores de s donde H(s) → ∞
- Son las raíces del denominador
- Se representan con × en el plano s

### El Plano s

El plano s es el plano complejo donde:
- Eje horizontal: parte real (σ)
- Eje vertical: parte imaginaria (jω)

```
    jω
     │
     │    ○ (cero)
     │
─────┼───────── σ
     │
     │    × (polo)
     │
```

### Relación con Respuesta en Frecuencia

La respuesta en frecuencia H(jω) se obtiene evaluando H(s) en s = jω, es decir, sobre el eje imaginario.

### Estabilidad

**Sistema estable:** Todos los polos tienen parte real negativa (están en el semiplano izquierdo).

**Sistema inestable:** Al menos un polo tiene parte real positiva o cero.

### Tipos de Polos

| Tipo | Ubicación | Respuesta temporal |
|------|-----------|-------------------|
| Real negativo | σ < 0, ω = 0 | Exponencial decreciente |
| Real positivo | σ > 0, ω = 0 | Exponencial creciente |
| Complejo conjugado (σ < 0) | Semiplano izquierdo | Sinusoide amortiguada |
| Imaginario puro | σ = 0 | Sinusoide sostenida |

### Ejemplo: Filtro RC Pasa-Bajas

$$H(s) = \frac{1}{1 + sRC} = \frac{1/RC}{s + 1/RC}$$

- **Ceros:** Ninguno (o uno en s = -∞)
- **Polos:** s = -1/RC

```
    jω
     │
     │
─────×─────────── σ
   -1/RC
```

### Ejemplo: Circuito RLC Subamortiguado

$$H(s) = \frac{\omega_0^2}{s^2 + 2\alpha s + \omega_0^2}$$

Para α < ω₀ (subamortiguado):
- Polos complejos conjugados: s = -α ± jωd
- donde ωd = √(ω₀² - α²)

```
    jω
     │     × (p₁ = -α + jωd)
   ωd├───×
     │   │
─────┼───┼────── σ
     │  -α
     │
  -ωd├───× (p₂ = -α - jωd)
```

### Efecto de la Ubicación de Polos

| Característica | Efecto |
|----------------|--------|
| Polo más cerca del eje jω | Respuesta más lenta (menor frecuencia de corte) |
| Polos más alejados del eje real | Mayor factor Q, resonancia más pronunciada |
| Polo dominante | Determina principalmente la dinámica |

### Diagrama de Bode desde Polos y Ceros

- **Por cada polo real en s = -a:** -20 dB/década después de ω = a
- **Por cada cero real en s = -a:** +20 dB/década después de ω = a
- **Polos complejos:** Pico cerca de ω₀, pendiente -40 dB/década

### Factorización Típica

$$H(s) = K\frac{\prod(1 + s/z_i)}{\prod(1 + s/p_i)}$$

Esta forma facilita el trazado de diagramas de Bode.

## Conceptos Clave
- Polos: raíces del denominador (×)
- Ceros: raíces del numerador (○)
- Estabilidad: polos en semiplano izquierdo
