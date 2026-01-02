# MET-01: Método de Análisis de Potencia en Circuitos CA

## Descripción del Método

La potencia en circuitos CA tiene varias componentes: [potencia activa](../../../glossary.md#potencia-activa) (real), [potencia reactiva](../../../glossary.md#potencia-reactiva) y [potencia aparente](../../../glossary.md#potencia-aparente). El análisis correcto de potencia es fundamental para el diseño eficiente de sistemas eléctricos.

---

## Tipos de Potencia

### Potencia Instantánea
$$p(t) = v(t) \cdot i(t)$$

Para señales sinusoidales:
$$p(t) = \frac{V_m I_m}{2}[\cos\theta + \cos(2\omega t + \theta)]$$

Donde θ = ángulo de [impedancia](../../../glossary.md#impedancia) (diferencia de fase entre v e i)

### Potencia Activa (Real)
$$P = \frac{V_m I_m}{2}\cos\theta = V_{rms} I_{rms} \cos\theta$$

- Unidades: Watts (W)
- Representa energía disipada (calor, trabajo)

### Potencia Reactiva
$$Q = \frac{V_m I_m}{2}\sin\theta = V_{rms} I_{rms} \sin\theta$$

- Unidades: VAR (Volt-Ampere Reactivo)
- Representa energía intercambiada con elementos reactivos
- Q > 0: [carga](../../../glossary.md#carga) inductiva (consume VARs)
- Q < 0: carga capacitiva (genera VARs)

### Potencia Aparente
$$S = V_{rms} I_{rms}$$

- Unidades: VA (Volt-Ampere)
- Representa la capacidad del sistema

### Potencia Compleja
$$\mathbf{S} = P + jQ = \mathbf{V}\mathbf{I}^*$$

Donde $\mathbf{I}^*$ es el conjugado de la [corriente](../../../glossary.md#corriente).

---

## Triángulo de Potencias

```
            |\
            | \
            |  \  S (VA)
      Q     |   \
    (VAR)   |θ   \
            |_____\
              P (W)
```

$$S = \sqrt{P^2 + Q^2}$$
$$\cos\theta = \frac{P}{S}$$ (factor de potencia)
$$\tan\theta = \frac{Q}{P}$$

---

## Factor de Potencia

$$fp = \cos\theta = \frac{P}{S}$$

### Clasificación
- **fp = 1**: Carga puramente resistiva (ideal)
- **fp adelantado**: Carga capacitiva (I adelanta a V)
- **fp atrasado**: Carga inductiva (I atrasa a V)

---

## Pasos del Método

### Paso 1: Identificar Voltaje y Corriente
- Determinar V e I (valores [RMS](../../../glossary.md#valor-eficaz) o pico)
- Identificar el ángulo de fase de cada uno

### Paso 2: Calcular el Ángulo de Potencia
$$\theta = \theta_V - \theta_I$$

### Paso 3: Calcular las Potencias
$$P = VI\cos\theta$$
$$Q = VI\sin\theta$$
$$S = VI$$

### Paso 4: Verificar
$$S^2 = P^2 + Q^2$$

---

## Ejemplo Clásico 1: Análisis de Potencia Básico

### Enunciado
Un circuito tiene voltaje v(t) = 170cos(377t + 20°) V y corriente i(t) = 8cos(377t - 10°) A. Calcule todas las potencias y el factor de potencia.

### Solución

#### **Paso 1: Valores RMS**
$$V_{rms} = \frac{V_m}{\sqrt{2}} = \frac{170}{\sqrt{2}} = 120.2\text{ V}$$
$$I_{rms} = \frac{I_m}{\sqrt{2}} = \frac{8}{\sqrt{2}} = 5.66\text{ A}$$

#### **Paso 2: Ángulo de potencia**
$$\theta = \theta_V - \theta_I = 20° - (-10°) = 30°$$

El [voltaje](../../../glossary.md#voltaje) adelanta a la corriente → **carga inductiva** → fp atrasado

#### **Paso 3: Potencias**
$$P = V_{rms}I_{rms}\cos\theta = (120.2)(5.66)\cos 30°$$
$$P = (120.2)(5.66)(0.866) = 589\text{ W}$$

$$Q = V_{rms}I_{rms}\sin\theta = (120.2)(5.66)\sin 30°$$
$$Q = (120.2)(5.66)(0.5) = 340\text{ VAR}$$

$$S = V_{rms}I_{rms} = (120.2)(5.66) = 680\text{ VA}$$

#### **Paso 4: Factor de potencia**
$$fp = \cos 30° = 0.866\text{ (atrasado)}$$

#### **Verificación**
$$S = \sqrt{P^2 + Q^2} = \sqrt{589^2 + 340^2} = 680\text{ VA}$$ ✓

### Respuesta
$$\boxed{P = 589\text{ W}, \quad Q = 340\text{ VAR}, \quad S = 680\text{ VA}, \quad fp = 0.866\text{ atrasado}}$$

### Explicación
El ángulo positivo de θ indica que la corriente atrasa al voltaje (carga inductiva). El [factor de potencia](../../../glossary.md#factor-potencia) de 0.866 significa que solo el 86.6% de la potencia aparente se convierte en trabajo útil.

---

## Ejemplo Clásico 2: Corrección del Factor de Potencia

### Enunciado
Una carga de 50 kW opera con factor de potencia de 0.7 atrasado desde una línea de 480 V. Determine el [capacitor](../../../glossary.md#capacitancia) necesario para corregir el factor de potencia a 0.95 atrasado.

### Diagrama
```
      ┌────────────────────────────────┐
      │                                │
    ──┴──                            ┌─┴─┐
    ─────  C                         │Carga│
    ──┬──  (a agregar)               │ L │
      │                              └─┬─┘
      └────────────────────────────────┘
          │←─────── 480V ──────────→│
```

### Solución

#### **Paso 1: Potencias originales**
$$P = 50\text{ kW}$$
$$fp_1 = 0.7 \Rightarrow \theta_1 = \arccos(0.7) = 45.57°$$

$$S_1 = \frac{P}{fp_1} = \frac{50}{0.7} = 71.43\text{ kVA}$$
$$Q_1 = S_1 \sin\theta_1 = 71.43 \times \sin 45.57° = 51\text{ kVAR}$$

O usando: $Q_1 = P\tan\theta_1 = 50 \times \tan 45.57° = 51\text{ kVAR}$

#### **Paso 2: Potencia reactiva final**
$$fp_2 = 0.95 \Rightarrow \theta_2 = \arccos(0.95) = 18.19°$$
$$Q_2 = P\tan\theta_2 = 50 \times \tan 18.19° = 16.43\text{ kVAR}$$

#### **Paso 3: Reactivos del capacitor**
$$Q_C = Q_1 - Q_2 = 51 - 16.43 = 34.57\text{ kVAR}$$

El capacitor debe suministrar 34.57 kVAR (potencia reactiva negativa).

#### **Paso 4: Valor del capacitor**
$$Q_C = \frac{V^2}{X_C} = V^2 \omega C$$

Asumiendo f = 60 Hz:
$$\omega = 2\pi(60) = 377\text{ rad/s}$$

$$C = \frac{Q_C}{\omega V^2} = \frac{34570}{377 \times 480^2}$$
$$C = \frac{34570}{86,860,800} = 398\text{ μF}$$

#### **Verificación**
Nueva potencia aparente:
$$S_2 = \frac{P}{fp_2} = \frac{50}{0.95} = 52.6\text{ kVA}$$

Reducción de corriente:
$$I_1 = \frac{S_1}{V} = \frac{71,430}{480} = 148.8\text{ A}$$
$$I_2 = \frac{S_2}{V} = \frac{52,630}{480} = 109.6\text{ A}$$

Reducción: $\frac{148.8 - 109.6}{148.8} \times 100\% = 26.3\%$

### Respuesta
$$\boxed{C = 398\text{ μF}, \quad Q_C = 34.57\text{ kVAR}}$$

### Explicación
La corrección del factor de potencia reduce la corriente de línea sin cambiar la potencia activa. Esto disminuye las pérdidas I²R en los conductores y permite usar conductores más pequeños o alimentar más carga con la misma infraestructura.

---

## Ejemplo Clásico 3: Potencia en Circuito con Múltiples Cargas

### Enunciado
Tres cargas conectadas en paralelo a una fuente de 240 V, 60 Hz:
- Carga 1: 10 kW, fp = 0.8 atrasado
- Carga 2: 8 kVA, fp = 0.6 atrasado
- Carga 3: 5 kW, fp = 1.0

Encuentre la potencia total, el factor de potencia total, y la corriente de la fuente.

### Solución

#### **Paso 1: Analizar cada carga**

**Carga 1:** P₁ = 10 kW, fp = 0.8
$$\theta_1 = \arccos(0.8) = 36.87°$$
$$Q_1 = P_1 \tan\theta_1 = 10 \times 0.75 = 7.5\text{ kVAR}$$
$$S_1 = \frac{P_1}{fp_1} = \frac{10}{0.8} = 12.5\text{ kVA}$$

**Carga 2:** S₂ = 8 kVA, fp = 0.6
$$P_2 = S_2 \times fp_2 = 8 \times 0.6 = 4.8\text{ kW}$$
$$\theta_2 = \arccos(0.6) = 53.13°$$
$$Q_2 = S_2 \sin\theta_2 = 8 \times 0.8 = 6.4\text{ kVAR}$$

**Carga 3:** P₃ = 5 kW, fp = 1.0
$$Q_3 = 0\text{ kVAR}$$ (puramente resistiva)
$$S_3 = 5\text{ kVA}$$

#### **Paso 2: Potencias totales**
$$P_T = P_1 + P_2 + P_3 = 10 + 4.8 + 5 = 19.8\text{ kW}$$
$$Q_T = Q_1 + Q_2 + Q_3 = 7.5 + 6.4 + 0 = 13.9\text{ kVAR}$$
$$S_T = \sqrt{P_T^2 + Q_T^2} = \sqrt{19.8^2 + 13.9^2} = 24.2\text{ kVA}$$

#### **Paso 3: Factor de potencia total**
$$fp_T = \frac{P_T}{S_T} = \frac{19.8}{24.2} = 0.818\text{ atrasado}$$

O: $\theta_T = \arctan\frac{Q_T}{P_T} = \arctan\frac{13.9}{19.8} = 35.1°$
$fp_T = \cos 35.1° = 0.818$

#### **Paso 4: Corriente de la fuente**
$$I = \frac{S_T}{V} = \frac{24,200}{240} = 100.8\text{ A}$$

### Respuesta
$$\boxed{P_T = 19.8\text{ kW}, \quad Q_T = 13.9\text{ kVAR}, \quad S_T = 24.2\text{ kVA}}$$
$$\boxed{fp_T = 0.818\text{ atrasado}, \quad I = 100.8\text{ A}}$$

---

## Máxima Transferencia de Potencia en CA

### Condición
Para máxima transferencia de potencia, la impedancia de carga debe ser el **conjugado complejo** de la impedancia de la fuente:

$$Z_L = Z_s^*$$

Si $Z_s = R_s + jX_s$, entonces $Z_L = R_s - jX_s$

### Potencia Máxima
$$P_{max} = \frac{|V_s|^2}{4R_s}$$

---

## Resumen de Fórmulas

| Potencia | Fórmula | Unidades |
|----------|---------|----------|
| Activa | $P = VI\cos\theta$ | W |
| Reactiva | $Q = VI\sin\theta$ | VAR |
| Aparente | $S = VI$ | VA |
| Compleja | $\mathbf{S} = \mathbf{V}\mathbf{I}^*$ | VA |

| Factor de Potencia | Fórmula |
|--------------------|---------|
| Definición | $fp = \cos\theta = P/S$ |
| Corrección | $Q_C = P(\tan\theta_1 - \tan\theta_2)$ |

## Errores Comunes
1. Confundir valores pico con valores RMS
2. No considerar el signo de Q (inductivo vs capacitivo)
3. Olvidar que el conjugado de I se usa para calcular S
4. Sumar potencias aparentes directamente (se deben sumar P y Q por separado)
