# ⚡ Constantes Físicas - Electricidad y Magnetismo

> 📌 **Referencia rápida** de las constantes fundamentales utilizadas en el análisis de circuitos eléctricos.

---

## 📋 Índice
- [Constantes Fundamentales](#constantes-fundamentales)
- [Constantes Electromagnéticas](#constantes-electromagnéticas)
- [Propiedades de Materiales](#propiedades-de-materiales)
- [Prefijos del SI](#prefijos-del-si)
- [Conversiones Útiles](#conversiones-útiles)

---

## Constantes Fundamentales

<a id="carga-electron"></a>
| Constante | Símbolo | Valor | Unidad | Temas Relacionados |
|-----------|---------|-------|--------|-------------------|
| **Carga del electrón** | $e$ | $1.602 \times 10^{-19}$ | C (Coulombs) | [Carga y Corriente](01-Circuitos-CD/01-Conceptos-Leyes-Fundamentales/theory/TH-03-Carga-corriente-tension-potencia.md) |
| **Masa del electrón** | $m_e$ | $9.109 \times 10^{-31}$ | kg | [Introducción](01-Circuitos-CD/01-Conceptos-Leyes-Fundamentales/theory/TH-01-Introduccion-circuitos.md) |
| **Número de Avogadro** | $N_A$ | $6.022 \times 10^{23}$ | mol⁻¹ | [Sistemas de Unidades](01-Circuitos-CD/01-Conceptos-Leyes-Fundamentales/theory/TH-02-Sistemas-unidades.md) |
| **Constante de Boltzmann** | $k_B$ | $1.381 \times 10^{-23}$ | J/K | — |

---

## Constantes Electromagnéticas

<a id="permitividad"></a>
### Permitividad y Permeabilidad

| Constante | Símbolo | Valor | Unidad | Temas Relacionados |
|-----------|---------|-------|--------|-------------------|
| **Permitividad del vacío** | $\varepsilon_0$ | $8.854 \times 10^{-12}$ | F/m | [Capacitancia](01-Circuitos-CD/04-Circuitos-Primer-Orden/theory/TH-01-Inductancia-capacitancia-combinaciones.md) |
| **Permeabilidad del vacío** | $\mu_0$ | $4\pi \times 10^{-7}$ | H/m | [Inductancia](01-Circuitos-CD/04-Circuitos-Primer-Orden/theory/TH-01-Inductancia-capacitancia-combinaciones.md), [Acoplamiento Magnético](02-Circuitos-CA/03-Circuitos-Acoplados-Magneticamente/theory/TH-01-Fenomeno-induccion.md) |
| **Velocidad de la luz** | $c$ | $2.998 \times 10^{8}$ | m/s | [Frecuencia](02-Circuitos-CA/06-Analisis-Dominio-Frecuencia/theory/TH-01-Introduccion-respuesta-frecuencia.md) |
| **Impedancia del vacío** | $Z_0$ | $376.73$ | Ω | [Impedancia](02-Circuitos-CA/01-Analisis-CA-Estado-Estacionario/theory/TH-04-Notacion-fasorial-impedancia-admitancia.md) |

> 💡 **Relación fundamental:** $c = \frac{1}{\sqrt{\varepsilon_0 \mu_0}}$

<a id="resistividad"></a>
### Resistividad de Conductores Comunes (a 20°C)

| Material | Símbolo | Resistividad $\rho$ (Ω·m) | Conductividad $\sigma$ (S/m) | Aplicación |
|----------|---------|---------------------------|------------------------------|------------|
| **Plata** | Ag | $1.59 \times 10^{-8}$ | $6.29 \times 10^{7}$ | Contactos de alta calidad |
| **Cobre** | Cu | $1.68 \times 10^{-8}$ | $5.96 \times 10^{7}$ | Cables, PCBs |
| **Oro** | Au | $2.44 \times 10^{-8}$ | $4.10 \times 10^{7}$ | Conectores |
| **Aluminio** | Al | $2.65 \times 10^{-8}$ | $3.77 \times 10^{7}$ | Líneas de transmisión |
| **Tungsteno** | W | $5.60 \times 10^{-8}$ | $1.79 \times 10^{7}$ | Filamentos |

> 📚 **Relacionado:** [Ley de Ohm](01-Circuitos-CD/01-Conceptos-Leyes-Fundamentales/theory/TH-05-Ley-Ohm-Leyes-Kirchhoff.md) | [Resistencia](glossary.md#resistencia)

---

## Propiedades de Materiales

<a id="dielectricos"></a>
### Constantes Dieléctricas Relativas ($\varepsilon_r$)

| Material | $\varepsilon_r$ | Aplicación | Tema Relacionado |
|----------|-----------------|------------|------------------|
| **Vacío** | 1.0 (exacto) | Referencia | — |
| **Aire** | 1.0006 | Capacitores variables | [Capacitancia](01-Circuitos-CD/04-Circuitos-Primer-Orden/theory/TH-01-Inductancia-capacitancia-combinaciones.md) |
| **Teflón (PTFE)** | 2.1 | Cables coaxiales | — |
| **Polietileno** | 2.3 | Aislamiento | — |
| **Papel** | 3.5 | Capacitores antiguos | — |
| **Vidrio** | 4-10 | Aisladores | — |
| **Mica** | 5.4 | Capacitores precisión | — |
| **Cerámica (BaTiO₃)** | 1200-10000 | Capacitores MLCC | — |

> 📐 **Fórmula:** $C = \varepsilon_0 \varepsilon_r \frac{A}{d}$

<a id="permeabilidad-magnetica"></a>
### Permeabilidad Magnética Relativa ($\mu_r$)

| Material | $\mu_r$ | Tipo | Tema Relacionado |
|----------|---------|------|------------------|
| **Vacío/Aire** | 1.0 | Referencia | — |
| **Aluminio** | 1.000022 | Paramagnético | — |
| **Cobre** | 0.999994 | Diamagnético | — |
| **Hierro puro** | ~5000 | Ferromagnético | [Inductores Acoplados](02-Circuitos-CA/03-Circuitos-Acoplados-Magneticamente/theory/TH-02-Autoinduccion-induccion-mutua.md) |
| **Ferrita** | 100-3000 | Ferrimagnético | [Transformadores](02-Circuitos-CA/03-Circuitos-Acoplados-Magneticamente/theory/TH-05-Transformador-ideal-polaridad-impedancias.md) |
| **Mu-metal** | ~100,000 | Ferromagnético | Blindaje |

> 📐 **Fórmula:** $L = \mu_0 \mu_r \frac{N^2 A}{\ell}$

---

## Prefijos del SI

<a id="prefijos"></a>
| Prefijo | Símbolo | Factor | Ejemplo en Circuitos |
|---------|---------|--------|---------------------|
| **tera** | T | $10^{12}$ | THz (frecuencias ópticas) |
| **giga** | G | $10^{9}$ | GHz (RF, microondas) |
| **mega** | M | $10^{6}$ | MΩ (resistencias altas), MHz |
| **kilo** | k | $10^{3}$ | kΩ, kHz, kW |
| — | — | $10^{0}$ | V, A, Ω, Hz, W |
| **mili** | m | $10^{-3}$ | mA, mV, mH |
| **micro** | μ | $10^{-6}$ | μF, μH, μA |
| **nano** | n | $10^{-9}$ | nF, ns |
| **pico** | p | $10^{-12}$ | pF (capacitores pequeños) |
| **femto** | f | $10^{-15}$ | fF (capacitancias parásitas) |

> 📚 **Relacionado:** [Sistemas de Unidades](01-Circuitos-CD/01-Conceptos-Leyes-Fundamentales/theory/TH-02-Sistemas-unidades.md)

---

## Conversiones Útiles

<a id="conversiones"></a>
### Energía y Potencia

| Conversión | Equivalencia | Tema Relacionado |
|------------|--------------|------------------|
| 1 kWh | 3.6 MJ = $3.6 \times 10^6$ J | [Potencia](02-Circuitos-CA/05-Potencia-Electrica/theory/TH-01-Potencia-real-reactiva-aparente-compleja.md) |
| 1 HP (caballo de fuerza) | 746 W | — |
| 1 BTU | 1055 J | — |
| 1 eV | $1.602 \times 10^{-19}$ J | — |

### Frecuencia y Período

| Relación | Fórmula | Tema Relacionado |
|----------|---------|------------------|
| Frecuencia angular | $\omega = 2\pi f$ | [Ondas Senoidales](02-Circuitos-CA/01-Analisis-CA-Estado-Estacionario/theory/TH-01-Onda-senoidal-caracteristicas.md) |
| Período | $T = \frac{1}{f}$ | [Análisis CA](02-Circuitos-CA/01-Analisis-CA-Estado-Estacionario/00-Intro.md) |
| Frecuencia de red (México/USA) | 60 Hz → $\omega = 377$ rad/s | [Sistemas Trifásicos](02-Circuitos-CA/04-Circuitos-Trifasicos/theory/TH-01-Generacion-CA-trifasica.md) |
| Frecuencia de red (Europa) | 50 Hz → $\omega = 314$ rad/s | — |

### Constantes de Tiempo

| Circuito | Constante de Tiempo | Tema Relacionado |
|----------|---------------------|------------------|
| **RC** | $\tau = RC$ | [Circuito RC](01-Circuitos-CD/04-Circuitos-Primer-Orden/theory/TH-03-Circuito-RC-sin-fuente.md) |
| **RL** | $\tau = \frac{L}{R}$ | [Circuito RL](01-Circuitos-CD/04-Circuitos-Primer-Orden/theory/TH-02-Circuito-RL-sin-fuente.md) |
| **RLC (factor de amortiguamiento)** | $\alpha = \frac{R}{2L}$ | [Circuitos Segundo Orden](01-Circuitos-CD/05-Circuitos-Segundo-Orden/theory/TH-01-Circuitos-segundo-orden-sin-fuentes.md) |
| **RLC (frecuencia natural)** | $\omega_0 = \frac{1}{\sqrt{LC}}$ | [Resonancia](02-Circuitos-CA/06-Analisis-Dominio-Frecuencia/theory/TH-03-Circuitos-resonantes-serie-paralelo.md) |

---

## 📊 Valores Típicos en Circuitos

<a id="valores-tipicos"></a>
### Componentes Comerciales

| Componente | Rango Típico | Series Estándar |
|------------|--------------|-----------------|
| **Resistores** | 1Ω - 10MΩ | E12, E24, E96 |
| **Capacitores cerámicos** | 1pF - 100μF | — |
| **Capacitores electrolíticos** | 1μF - 10,000μF | — |
| **Inductores SMD** | 1nH - 10mH | — |

### Voltajes Estándar

| Aplicación | Voltaje | Tema Relacionado |
|------------|---------|------------------|
| Baterías AA/AAA | 1.5V DC | [Circuitos CD](01-Circuitos-CD/00-Index.md) |
| USB | 5V DC | — |
| Automotive | 12V DC | — |
| Residencial (México/USA) | 120V RMS, 60Hz | [Valor Eficaz](02-Circuitos-CA/01-Analisis-CA-Estado-Estacionario/theory/TH-02-Potencia-instantanea-media-valor-eficaz.md) |
| Industrial (trifásico) | 480V RMS | [Trifásico](02-Circuitos-CA/04-Circuitos-Trifasicos/00-Intro.md) |

---

## 🔗 Referencias Cruzadas

| Constante | Ver también en Glosario |
|-----------|------------------------|
| Resistencia | [glossary.md#resistencia](glossary.md#resistencia) |
| Impedancia | [glossary.md#impedancia](glossary.md#impedancia) |
| Capacitancia | [glossary.md#capacitancia](glossary.md#capacitancia) |
| Inductancia | [glossary.md#inductancia](glossary.md#inductancia) |
| Frecuencia | [glossary.md#frecuencia](glossary.md#frecuencia) |
| Potencia | [glossary.md#potencia-activa](glossary.md#potencia-activa) |

---

> 📖 **Fuentes:** NIST CODATA, IEC 60027, IEEE Std 315
