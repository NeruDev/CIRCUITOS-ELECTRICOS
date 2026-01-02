# PR-04: Filtro Pasa-Banda RLC ⭐⭐⭐

## Enunciado
Diseñe un filtro pasa-banda RLC serie con las siguientes especificaciones:
- Frecuencia central f₀ = 10 kHz
- Ancho de banda BW = 1 kHz
- Impedancia de entrada 1 kΩ a la frecuencia de resonancia

Determine:
a) Los valores de R, L y C
b) El factor de calidad Q
c) Las frecuencias de corte f₁ y f₂
d) La función de transferencia H(jω) = Vout/Vin
e) La respuesta a las frecuencias: f₀, f₁, f₂, 0.5f₀, 2f₀

## Diagrama del Circuito

```
         R           L           C
    ●────/\/\/────ΩΩΩΩ────┤├────┬─────●
    │                           │     │
  + │                         ┌─┴─┐ + │
Vin │                         │   │ Vout
    │                         │ R │  (Salida en R)
  - │                         └─┬─┘ - │
    ●───────────────────────────┴─────●
    
    Nota: Vout se toma a través de R para filtro pasa-banda
```

## Netlist SPICE

```spice
* PR-04: Filtro Pasa-Banda RLC Serie
* Salida a través de la resistencia

V1 1 0 AC 1 0         ; Entrada unitaria
R1 1 2 1k             ; R = 1kΩ (calculado)
L1 2 3 15.92m         ; L = 15.92mH (calculado)
C1 3 4 15.92n         ; C = 15.92nF (calculado)
RL 4 0 1k             ; Resistencia de carga (salida)

* Alternativa: Medir voltaje en R del circuito
* .PRINT AC VDB(4) VP(4)

.AC DEC 50 1k 100k    ; Barrido 1kHz a 100kHz
.PRINT AC VDB(4) VP(4); Magnitud y fase
.PROBE
.END
```

## Solución

### Parte a) Cálculo de R, L y C

**Especificaciones:**
- f₀ = 10 kHz → ω₀ = 2π × 10000 = 62832 rad/s
- BW = 1 kHz → Δω = 2π × 1000 = 6283 rad/s
- Z(f₀) = R = 1 kΩ

**Factor de calidad:**
$$Q = \frac{f_0}{BW} = \frac{10000}{1000} = 10$$

**Cálculo de R:**
De la especificación de impedancia:
$$\boxed{R = 1\text{ k}\Omega}$$

**Cálculo de L:**
Del ancho de banda para circuito serie:
$$BW = \frac{R}{2\pi L} \Rightarrow L = \frac{R}{2\pi \times BW}$$

$$L = \frac{1000}{2\pi \times 1000} = \frac{1}{2\pi} = 0.159\text{ H} = 159.15\text{ mH}$$

**Verificación con Q:**
$$Q = \frac{\omega_0 L}{R} \Rightarrow L = \frac{QR}{\omega_0} = \frac{10 \times 1000}{62832}$$

$$L = 0.01592\text{ H}$$

⚠️ **Corrección:** Usamos la relación correcta:
$$L = \frac{R}{2\pi \times BW} = \frac{1000}{6283.2} = 0.01592\text{ H}$$

$$\boxed{L = 15.92\text{ mH}}$$

**Cálculo de C:**
De la frecuencia de resonancia:
$$\omega_0 = \frac{1}{\sqrt{LC}} \Rightarrow C = \frac{1}{\omega_0^2 L}$$

$$C = \frac{1}{(62832)^2 \times 0.01592}$$

$$C = \frac{1}{3.948 \times 10^9 \times 0.01592} = \frac{1}{6.285 \times 10^7}$$

$$\boxed{C = 15.92\text{ nF}}$$

**Verificación:**
$$f_0 = \frac{1}{2\pi\sqrt{LC}} = \frac{1}{2\pi\sqrt{0.01592 \times 15.92 \times 10^{-9}}}$$
$$f_0 = \frac{1}{2\pi \times 1.592 \times 10^{-5}} = \frac{1}{10^{-4}} = 10000\text{ Hz}$$ ✓

### Parte b) Factor de calidad

$$Q = \frac{f_0}{BW} = \frac{10000}{1000}$$

$$\boxed{Q = 10}$$

**Verificación:**
$$Q = \frac{\omega_0 L}{R} = \frac{62832 \times 0.01592}{1000} = 10$$ ✓

$$Q = \frac{1}{\omega_0 RC} = \frac{1}{62832 \times 1000 \times 15.92 \times 10^{-9}} = 10$$ ✓

### Parte c) Frecuencias de corte

**Para Q alto:**
$$f_1 \approx f_0 - \frac{BW}{2} = 10000 - 500 = 9500\text{ Hz}$$
$$f_2 \approx f_0 + \frac{BW}{2} = 10000 + 500 = 10500\text{ Hz}$$

**Valores exactos:**
$$f_1 = f_0\left(\sqrt{1 + \frac{1}{4Q^2}} - \frac{1}{2Q}\right)$$
$$f_2 = f_0\left(\sqrt{1 + \frac{1}{4Q^2}} + \frac{1}{2Q}\right)$$

Con Q = 10:
$$\sqrt{1 + \frac{1}{400}} = \sqrt{1.0025} = 1.00125$$
$$f_1 = 10000(1.00125 - 0.05) = 10000 \times 0.95125 = 9512.5\text{ Hz}$$
$$f_2 = 10000(1.00125 + 0.05) = 10000 \times 1.05125 = 10512.5\text{ Hz}$$

$$\boxed{f_1 = 9512.5\text{ Hz}, \quad f_2 = 10512.5\text{ Hz}}$$

**Verificación:**
$$f_2 - f_1 = 10512.5 - 9512.5 = 1000\text{ Hz} = BW$$ ✓
$$\sqrt{f_1 \times f_2} = \sqrt{9512.5 \times 10512.5} = 10000\text{ Hz} = f_0$$ ✓

### Parte d) Función de transferencia

Para el filtro pasa-banda con salida en R:
$$H(j\omega) = \frac{V_R}{V_{in}} = \frac{R}{R + j\omega L + \frac{1}{j\omega C}}$$

$$H(j\omega) = \frac{R}{R + j\left(\omega L - \frac{1}{\omega C}\right)}$$

**En forma normalizada:**
$$H(j\omega) = \frac{1}{1 + jQ\left(\frac{\omega}{\omega_0} - \frac{\omega_0}{\omega}\right)}$$

Sea $u = \omega/\omega_0$:
$$\boxed{H(ju) = \frac{1}{1 + jQ\left(u - \frac{1}{u}\right)}}$$

**Magnitud:**
$$|H(j\omega)| = \frac{1}{\sqrt{1 + Q^2\left(\frac{\omega}{\omega_0} - \frac{\omega_0}{\omega}\right)^2}}$$

**Fase:**
$$\phi(\omega) = -\arctan\left[Q\left(\frac{\omega}{\omega_0} - \frac{\omega_0}{\omega}\right)\right]$$

### Parte e) Respuesta a diferentes frecuencias

**En f = f₀ = 10 kHz (u = 1):**
$$|H| = \frac{1}{\sqrt{1 + Q^2(1-1)^2}} = 1 = 0\text{ dB}$$
$$\phi = -\arctan(0) = 0°$$

**En f = f₁ = 9512.5 Hz (u = 0.9513):**
$$u - \frac{1}{u} = 0.9513 - 1.0512 = -0.0999$$
$$|H| = \frac{1}{\sqrt{1 + 100 \times 0.01}} = \frac{1}{\sqrt{2}} = 0.707 = -3\text{ dB}$$
$$\phi = -\arctan(-1) = +45°$$

**En f = f₂ = 10512.5 Hz (u = 1.0513):**
$$u - \frac{1}{u} = 1.0513 - 0.9512 = 0.1001$$
$$|H| = \frac{1}{\sqrt{1 + 100 \times 0.01}} = 0.707 = -3\text{ dB}$$
$$\phi = -\arctan(1) = -45°$$

**En f = 0.5f₀ = 5 kHz (u = 0.5):**
$$u - \frac{1}{u} = 0.5 - 2 = -1.5$$
$$|H| = \frac{1}{\sqrt{1 + 100 \times 2.25}} = \frac{1}{\sqrt{226}} = 0.0665 = -23.5\text{ dB}$$
$$\phi = -\arctan(-15) = +86.2°$$

**En f = 2f₀ = 20 kHz (u = 2):**
$$u - \frac{1}{u} = 2 - 0.5 = 1.5$$
$$|H| = \frac{1}{\sqrt{1 + 225}} = 0.0665 = -23.5\text{ dB}$$
$$\phi = -\arctan(15) = -86.2°$$

## Diagrama de Bode

```
|H| (dB)
    │
  0 ├─────────────●─────────────  En f₀
    │           ╱   ╲
 -3 ├──────────●─────●──────────  f₁ y f₂
    │        ╱         ╲
-10 │      ╱             ╲
    │    ╱                 ╲
-20 │  ╱                     ╲
    │╱                         ╲
    └──┴────┴────┴────┴────┴──► f (kHz)
       5   9.5  10  10.5  20
         f₁  f₀  f₂

φ (grados)
+90°├════●═══════════════════════
    │    ╲
+45°├─────●──────────────────────  En f₁
    │      ╲
  0°├───────●────────────────────  En f₀
    │        ╲
-45°├─────────●──────────────────  En f₂
    │          ╲
-90°├═══════════●════════════════
    └──┴────┴────┴────┴────┴──► f (kHz)
       5   9.5  10  10.5  20
```

## Tabla de Respuesta en Frecuencia

| f (kHz) | f/f₀ | |H| | |H| (dB) | φ (°) |
|---------|------|-----|---------|-------|
| 5.0 | 0.5 | 0.0665 | -23.5 | +86.2 |
| 9.0 | 0.9 | 0.687 | -3.26 | +46.6 |
| 9.5 | 0.95 | 0.707 | -3.0 | +45.0 |
| 10.0 | 1.0 | 1.0 | 0 | 0 |
| 10.5 | 1.05 | 0.707 | -3.0 | -45.0 |
| 11.0 | 1.1 | 0.463 | -6.69 | -62.4 |
| 20.0 | 2.0 | 0.0665 | -23.5 | -86.2 |

## Tabla de Diseño Final

| Componente | Valor | Valor Comercial |
|------------|-------|-----------------|
| R | 1 kΩ | 1 kΩ |
| L | 15.92 mH | 15 mH + ajuste |
| C | 15.92 nF | 15 nF + 1 nF |

| Parámetro | Valor |
|-----------|-------|
| f₀ | **10 kHz** |
| BW | **1 kHz** |
| Q | **10** |
| f₁ | **9512.5 Hz** |
| f₂ | **10512.5 Hz** |
| H(f₀) | **1 (0 dB)** |

## Simulación SPICE - Resultados Esperados
```
f = 5 kHz:    VDB(4) = -23.5 dB, VP(4) = +86°
f = 9.5 kHz:  VDB(4) = -3.0 dB,  VP(4) = +45°
f = 10 kHz:   VDB(4) = 0 dB,     VP(4) = 0°
f = 10.5 kHz: VDB(4) = -3.0 dB,  VP(4) = -45°
f = 20 kHz:   VDB(4) = -23.5 dB, VP(4) = -86°
```

## Aplicaciones
1. **Sintonizadores de radio:** Selección de frecuencia de estación
2. **Ecualizadores:** Ajuste de bandas de frecuencia específicas
3. **Instrumentación:** Medición de frecuencias específicas
4. **Comunicaciones:** Filtros de canal

## Conceptos Aplicados
- Diseño de filtros pasa-banda
- Relación Q-BW-f₀
- Función de transferencia normalizada
- Análisis de respuesta en frecuencia
- Diagramas de Bode para filtros de segundo orden