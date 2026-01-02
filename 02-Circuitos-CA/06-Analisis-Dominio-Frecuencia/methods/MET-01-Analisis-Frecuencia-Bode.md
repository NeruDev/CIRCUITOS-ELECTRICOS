# MET-01: Método de Análisis en el Dominio de la Frecuencia

## Descripción del Método

El análisis en el dominio de la [frecuencia](../../../glossary.md#frecuencia) estudia el comportamiento de circuitos cuando la frecuencia de la fuente varía. Es fundamental para diseño de filtros, análisis de respuesta en frecuencia y caracterización de sistemas.

---

## Función de Transferencia

### Definición
$$\mathbf{H}(\omega) = \frac{\mathbf{V}_{salida}}{\mathbf{V}_{entrada}} = \frac{\mathbf{Y}(\omega)}{\mathbf{X}(\omega)}$$

### Forma General
$$\mathbf{H}(j\omega) = |\mathbf{H}(\omega)| \angle \phi(\omega)$$

Donde:
- $|\mathbf{H}(\omega)|$ = ganancia (magnitud)
- $\phi(\omega)$ = fase

---

## Función de Transferencia con s = jω

### Variable Compleja
$$s = \sigma + j\omega$$

Para análisis de frecuencia en estado estable:
$$s = j\omega$$

### Impedancias en Términos de s
- [Resistor](../../../glossary.md#resistencia): $Z_R = R$
- [Inductor](../../../glossary.md#inductancia): $Z_L = sL$
- [Capacitor](../../../glossary.md#capacitancia): $Z_C = \frac{1}{sC}$

---

## Diagramas de Bode

### Ganancia en Decibeles
$$|H|_{dB} = 20\log_{10}|H|$$

### Escala Logarítmica de Frecuencia
Se usa escala logarítmica para ω, permitiendo ver varias décadas de frecuencia.

### Componentes del Diagrama de Bode
1. **Diagrama de Magnitud**: |H| en dB vs log(ω)
2. **Diagrama de Fase**: φ vs log(ω)

---

## Pasos del Método

### Paso 1: Obtener H(s) o H(jω)
- Aplicar divisor de voltaje, análisis nodal, etc.
- Expresar en forma de cociente de polinomios

### Paso 2: Identificar Polos y Ceros
- Ceros: valores de s donde H(s) = 0
- Polos: valores de s donde H(s) → ∞

### Paso 3: Forma Estándar para Bode
$$H(s) = K \frac{(1 + s/z_1)(1 + s/z_2)...}{(1 + s/p_1)(1 + s/p_2)...}$$

### Paso 4: Trazar Aproximaciones Asintóticas
- Por cada polo simple: -20 dB/década después de ω = p
- Por cada cero simple: +20 dB/década después de ω = z
- Polos/ceros en el origen: pendiente desde ω = 0

### Paso 5: Calcular Puntos Críticos
- Frecuencias de corte (-3 dB)
- Frecuencia de [resonancia](../../../glossary.md#resonancia) (si aplica)

---

## Filtros Básicos

### Filtro Paso Bajo (RC)
```
        R
●───────/\/\/───┬───● Vout
│               │
+             ┌─┴─┐
Vin           │ C │
-             └─┬─┘
│               │
●───────────────┴───●
```

$$H(s) = \frac{1}{1 + sRC}$$

Frecuencia de corte:
$$\omega_c = \frac{1}{RC}, \quad f_c = \frac{1}{2\pi RC}$$

### Filtro Paso Alto (RC)
```
        C
●───────┤├──────┬───● Vout
│               │
+             ┌─┴─┐
Vin           │ R │
-             └─┬─┘
│               │
●───────────────┴───●
```

$$H(s) = \frac{sRC}{1 + sRC}$$

### Filtro Paso Banda (RLC)
$$H(s) = \frac{s/RC}{s^2 + s/RC + 1/LC}$$

### Filtro Rechaza Banda (Notch)
$$H(s) = \frac{s^2 + 1/LC}{s^2 + s/RC + 1/LC}$$

---

## Ejemplo Clásico 1: Análisis de Filtro Paso Bajo RC

### Enunciado
Un filtro RC tiene R = 10 kΩ y C = 0.01 μF. Determine:
a) Función de transferencia
b) Frecuencia de corte
c) Magnitud y fase a f = 1 kHz y f = 10 kHz

### Diagrama
```
        10kΩ
●───────/\/\/───┬───● Vout
│               │
+             ┌─┴─┐
Vin           │0.01│
-             │ μF │
│             └─┬─┘
●───────────────┴───●
```

### Solución

#### **Paso 1: Función de transferencia**
Por divisor de voltaje:
$$H(s) = \frac{Z_C}{Z_R + Z_C} = \frac{1/sC}{R + 1/sC}$$

Multiplicando por sC:
$$H(s) = \frac{1}{1 + sRC}$$

#### **Paso 2: Frecuencia de corte**
$$\omega_c = \frac{1}{RC} = \frac{1}{(10 \times 10^3)(0.01 \times 10^{-6})}$$
$$\omega_c = \frac{1}{10^{-4}} = 10,000\text{ rad/s}$$

$$f_c = \frac{\omega_c}{2\pi} = \frac{10,000}{2\pi} = 1,592\text{ Hz}$$

#### **Paso 3: Respuesta a f = 1 kHz**
$$\omega = 2\pi(1000) = 6,283\text{ rad/s}$$

$$H(j\omega) = \frac{1}{1 + j\omega RC} = \frac{1}{1 + j(6283)(10^{-4})}$$
$$H(j\omega) = \frac{1}{1 + j0.628}$$

**Magnitud:**
$$|H| = \frac{1}{\sqrt{1^2 + 0.628^2}} = \frac{1}{1.181} = 0.847$$
$$|H|_{dB} = 20\log(0.847) = -1.44\text{ dB}$$

**Fase:**
$$\phi = -\arctan(0.628) = -32.1°$$

#### **Paso 4: Respuesta a f = 10 kHz**
$$\omega = 2\pi(10,000) = 62,832\text{ rad/s}$$

$$H(j\omega) = \frac{1}{1 + j(62832)(10^{-4})} = \frac{1}{1 + j6.28}$$

**Magnitud:**
$$|H| = \frac{1}{\sqrt{1 + 39.4}} = \frac{1}{6.36} = 0.157$$
$$|H|_{dB} = 20\log(0.157) = -16.1\text{ dB}$$

**Fase:**
$$\phi = -\arctan(6.28) = -80.9°$$

### Respuesta
$$\boxed{f_c = 1,592\text{ Hz}}$$
$$\boxed{f = 1\text{ kHz}: |H| = 0.847 = -1.44\text{ dB}, \phi = -32.1°}$$
$$\boxed{f = 10\text{ kHz}: |H| = 0.157 = -16.1\text{ dB}, \phi = -80.9°}$$

### Explicación
A 1 kHz (por debajo de fc), el filtro atenúa poco la señal. A 10 kHz (por encima de fc), la atenuación es significativa (~16 dB). La fase varía de 0° (bajas frecuencias) a -90° (altas frecuencias).

---

## Ejemplo Clásico 2: Resonancia en Circuito RLC Serie

### Enunciado
Un [circuito](../../../glossary.md#circuito) RLC serie tiene R = 10 Ω, L = 100 mH, C = 10 μF. Calcule:
a) Frecuencia de resonancia
b) Factor de calidad Q
c) Ancho de banda
d) [Impedancia](../../../glossary.md#impedancia) a resonancia

### Solución

#### **Paso 1: Frecuencia de resonancia**
A resonancia, XL = XC:
$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{(0.1)(10 \times 10^{-6})}}$$
$$\omega_0 = \frac{1}{\sqrt{10^{-6}}} = \frac{1}{10^{-3}} = 1000\text{ rad/s}$$

$$f_0 = \frac{\omega_0}{2\pi} = \frac{1000}{2\pi} = 159.2\text{ Hz}$$

#### **Paso 2: Factor de calidad**
$$Q = \frac{\omega_0 L}{R} = \frac{1000 \times 0.1}{10} = 10$$

O equivalentemente:
$$Q = \frac{1}{\omega_0 RC} = \frac{1}{1000 \times 10 \times 10^{-5}} = 10$$

#### **Paso 3: Ancho de banda**
$$BW = \frac{\omega_0}{Q} = \frac{1000}{10} = 100\text{ rad/s}$$

$$BW_f = \frac{f_0}{Q} = \frac{159.2}{10} = 15.92\text{ Hz}$$

Frecuencias de media potencia:
$$\omega_1 = \omega_0 - \frac{BW}{2} = 950\text{ rad/s}$$
$$\omega_2 = \omega_0 + \frac{BW}{2} = 1050\text{ rad/s}$$

#### **Paso 4: Impedancia a resonancia**
A resonancia:
$$Z = R + j(\omega_0 L - \frac{1}{\omega_0 C}) = R + j(100 - 100) = R = 10\text{ Ω}$$

La impedancia es mínima y puramente resistiva.

### Respuesta
$$\boxed{f_0 = 159.2\text{ Hz}, \quad Q = 10, \quad BW = 15.92\text{ Hz}, \quad Z_0 = 10\text{ Ω}}$$

### Explicación
El factor Q = 10 indica un circuito selectivo: amplifica señales cerca de f₀ y atenúa las demás. A resonancia, las reactancias se cancelan y solo queda la resistencia.

---

## Ejemplo Clásico 3: Diagrama de Bode de un Sistema de Segundo Orden

### Enunciado
Trace el diagrama de Bode asintótico para:
$$H(s) = \frac{100}{s^2 + 10s + 100}$$

### Solución

#### **Paso 1: Identificar parámetros**
Forma estándar de segundo orden:
$$H(s) = \frac{\omega_0^2}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$$

Comparando:
$$\omega_0^2 = 100 \Rightarrow \omega_0 = 10\text{ rad/s}$$
$$2\zeta\omega_0 = 10 \Rightarrow \zeta = \frac{10}{2(10)} = 0.5$$

#### **Paso 2: Ganancia DC**
$$H(0) = \frac{100}{100} = 1 = 0\text{ dB}$$

#### **Paso 3: Frecuencia de resonancia**
$$\omega_r = \omega_0\sqrt{1 - 2\zeta^2} = 10\sqrt{1 - 0.5} = 10\sqrt{0.5} = 7.07\text{ rad/s}$$

#### **Paso 4: Pico de resonancia**
$$M_p = \frac{1}{2\zeta\sqrt{1-\zeta^2}} = \frac{1}{2(0.5)\sqrt{0.75}} = \frac{1}{0.866} = 1.155$$
$$M_{p,dB} = 20\log(1.155) = 1.25\text{ dB}$$

#### **Paso 5: Asíntotas**
- ω << ω₀: |H| ≈ 1 (0 dB), φ ≈ 0°
- ω >> ω₀: |H| ∝ 1/ω², pendiente -40 dB/década, φ → -180°
- ω = ω₀: φ = -90°

#### **Diagrama de Magnitud (Aproximado)**
```
|H| (dB)
    │
  0 ┼───────────────────●
    │                    ╲
    │                     ╲  -40 dB/dec
-20 ┼                      ╲
    │                       ╲
-40 ┼                        ╲
    │
    ┼────┬────┬────┬────┬────┬───→ ω (rad/s)
        1    10   100  1k   10k
              ω₀
```

#### **Diagrama de Fase (Aproximado)**
```
φ (grados)
  0 ┼────────────╲
    │             ╲
-45 ┼              ╲
    │               ╲
-90 ┼                ●
    │                 ╲
-135┼                  ╲
    │                   ╲
-180┼────────────────────────
    ┼────┬────┬────┬────┬────→ ω (rad/s)
        1    10   100  1k
              ω₀
```

### Respuesta
$$\boxed{\omega_0 = 10\text{ rad/s}, \quad \zeta = 0.5, \quad M_p = 1.25\text{ dB a } \omega_r = 7.07\text{ rad/s}}$$

---

## Resumen de Fórmulas de Resonancia

### RLC Serie
| Parámetro | Fórmula |
|-----------|---------|
| Frecuencia resonancia | $\omega_0 = 1/\sqrt{LC}$ |
| Factor Q | $Q = \omega_0 L/R = 1/(\omega_0 RC)$ |
| Ancho de banda | $BW = \omega_0/Q = R/L$ |
| Impedancia | $Z_{min} = R$ |

### RLC Paralelo
| Parámetro | Fórmula |
|-----------|---------|
| Frecuencia resonancia | $\omega_0 = 1/\sqrt{LC}$ |
| Factor Q | $Q = R/(\omega_0 L) = \omega_0 RC$ |
| Ancho de banda | $BW = \omega_0/Q = 1/(RC)$ |
| Impedancia | $Z_{max} = R$ |

## Tipos de Filtros

| Filtro | Comportamiento |
|--------|----------------|
| Paso bajo | Pasa bajas frecuencias, atenúa altas |
| Paso alto | Pasa altas frecuencias, atenúa bajas |
| Paso banda | Pasa banda de frecuencias, atenúa resto |
| Rechaza banda | Atenúa banda específica, pasa resto |

## Errores Comunes
1. Confundir ω (rad/s) con f (Hz)
2. Olvidar el factor 20 al convertir a dB (no 10)
3. No considerar el desfase en la función de transferencia
4. Confundir Q en serie vs paralelo
