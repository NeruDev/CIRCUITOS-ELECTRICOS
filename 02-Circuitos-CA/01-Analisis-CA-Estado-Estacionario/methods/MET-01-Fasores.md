# MET-01: Método de Fasores para Análisis de Circuitos CA

## Descripción del Método

Los **fasores** son números complejos que representan señales sinusoidales en estado estable. Transforman ecuaciones diferenciales en ecuaciones algebraicas, simplificando enormemente el análisis de circuitos CA.

---

## Representación Fasorial

### Señal Sinusoidal
$$v(t) = V_m \cos(\omega t + \phi)$$

### Fasor Correspondiente
$$\mathbf{V} = V_m \angle \phi = V_m e^{j\phi} = V_m(\cos\phi + j\sin\phi)$$

Donde:
- $V_m$ = amplitud (valor pico)
- $\phi$ = ángulo de fase
- $\omega$ = [frecuencia](../../../glossary.md#frecuencia) angular (rad/s)

---

## Formas de Representación

### Forma Rectangular
$$\mathbf{V} = a + jb$$

donde:
- $a = V_m \cos\phi$ (parte real)
- $b = V_m \sin\phi$ (parte imaginaria)

### Forma Polar
$$\mathbf{V} = V_m \angle \phi$$

### Conversiones
$$V_m = \sqrt{a^2 + b^2}$$
$$\phi = \arctan\frac{b}{a}$$ (considerar cuadrante)

---

## Impedancia de Elementos

### Resistor
$$\mathbf{Z}_R = R \angle 0° = R$$

Voltaje y corriente **en fase**

### Inductor
$$\mathbf{Z}_L = j\omega L = \omega L \angle 90°$$

[Voltaje](../../../glossary.md#voltaje) **adelanta** 90° a la [corriente](../../../glossary.md#corriente)

### Capacitor
$$\mathbf{Z}_C = \frac{1}{j\omega C} = -\frac{j}{\omega C} = \frac{1}{\omega C} \angle -90°$$

Voltaje **atrasa** 90° a la corriente

---

## Pasos del Método

### Paso 1: Identificar la Frecuencia
$$\omega = 2\pi f$$

### Paso 2: Convertir Fuentes a Fasores
$$v(t) = V_m \cos(\omega t + \phi) \rightarrow \mathbf{V} = V_m \angle \phi$$

### Paso 3: Calcular Impedancias
- $\mathbf{Z}_R = R$
- $\mathbf{Z}_L = j\omega L$
- $\mathbf{Z}_C = 1/(j\omega C)$

### Paso 4: Analizar el Circuito
- Aplicar Ley de Ohm: $\mathbf{V} = \mathbf{Z}\mathbf{I}$
- Aplicar LCK y LVK en forma fasorial

### Paso 5: Convertir a Dominio del Tiempo
$$\mathbf{V} = V_m \angle \phi \rightarrow v(t) = V_m \cos(\omega t + \phi)$$

---

## Operaciones con Fasores

### Suma/Resta
Usar forma rectangular:
$$\mathbf{V}_1 + \mathbf{V}_2 = (a_1 + a_2) + j(b_1 + b_2)$$

### Multiplicación/División
Usar forma polar:
$$\mathbf{V}_1 \times \mathbf{V}_2 = V_{m1}V_{m2} \angle (\phi_1 + \phi_2)$$
$$\frac{\mathbf{V}_1}{\mathbf{V}_2} = \frac{V_{m1}}{V_{m2}} \angle (\phi_1 - \phi_2)$$

---

## Ejemplo Clásico 1: Circuito RC Serie

### Enunciado
Un circuito RC serie tiene R = 100 Ω y C = 10 μF. La fuente es v(t) = 50cos(1000t + 30°) V. Encuentre la corriente i(t) y el voltaje en el capacitor v_C(t).

### Diagrama
```
         R=100Ω        C=10μF
●───────/\/\/\/───────┤├───────●
│                              │
+                              +
v(t)=50cos(1000t+30°)V        vC
-                              -
│                              │
●──────────────────────────────●
```

### Solución

#### **Paso 1: Identificar ω**
$$\omega = 1000\text{ rad/s}$$

#### **Paso 2: Convertir fuente a fasor**
$$v(t) = 50\cos(1000t + 30°) \rightarrow \mathbf{V}_s = 50 \angle 30°\text{ V}$$

#### **Paso 3: Calcular impedancias**
$$\mathbf{Z}_R = 100\text{ Ω}$$
$$\mathbf{Z}_C = \frac{1}{j\omega C} = \frac{1}{j(1000)(10 \times 10^{-6})} = \frac{1}{j0.01} = -j100\text{ Ω} = 100 \angle -90°\text{ Ω}$$

#### **Paso 4: Impedancia total**
$$\mathbf{Z}_{total} = \mathbf{Z}_R + \mathbf{Z}_C = 100 - j100\text{ Ω}$$

Convertir a polar:
$$|\mathbf{Z}| = \sqrt{100^2 + 100^2} = 141.42\text{ Ω}$$
$$\theta_Z = \arctan\frac{-100}{100} = -45°$$
$$\mathbf{Z}_{total} = 141.42 \angle -45°\text{ Ω}$$

#### **Paso 5: Calcular corriente**
$$\mathbf{I} = \frac{\mathbf{V}_s}{\mathbf{Z}_{total}} = \frac{50 \angle 30°}{141.42 \angle -45°}$$
$$\mathbf{I} = \frac{50}{141.42} \angle (30° - (-45°)) = 0.354 \angle 75°\text{ A}$$

#### **Paso 6: Voltaje en el capacitor**
$$\mathbf{V}_C = \mathbf{I} \times \mathbf{Z}_C = (0.354 \angle 75°)(100 \angle -90°)$$
$$\mathbf{V}_C = 35.4 \angle -15°\text{ V}$$

#### **Paso 7: Convertir a dominio del tiempo**
$$i(t) = 0.354\cos(1000t + 75°)\text{ A} = 354\cos(1000t + 75°)\text{ mA}$$
$$v_C(t) = 35.4\cos(1000t - 15°)\text{ V}$$

### Respuesta
$$\boxed{i(t) = 354\cos(1000t + 75°)\text{ mA}}$$
$$\boxed{v_C(t) = 35.4\cos(1000t - 15°)\text{ V}}$$

### Explicación
La corriente adelanta al voltaje de la fuente por 45° debido a la naturaleza capacitiva del circuito (φ = -45° de la impedancia total). El voltaje en el capacitor atrasa 90° respecto a la corriente, resultando en un ángulo de fase de -15°.

---

## Ejemplo Clásico 2: Circuito RLC Serie

### Enunciado
Un circuito serie tiene R = 30 Ω, L = 50 mH, C = 200 μF. La fuente es v(t) = 100cos(500t) V. Determine la corriente y el voltaje en cada elemento.

### Solución

#### **Paso 1: Frecuencia**
$$\omega = 500\text{ rad/s}$$

#### **Paso 2: Fasor de la fuente**
$$\mathbf{V}_s = 100 \angle 0°\text{ V}$$

#### **Paso 3: Impedancias**
$$\mathbf{Z}_R = 30\text{ Ω}$$
$$\mathbf{Z}_L = j\omega L = j(500)(0.05) = j25\text{ Ω}$$
$$\mathbf{Z}_C = \frac{1}{j\omega C} = \frac{1}{j(500)(200 \times 10^{-6})} = \frac{1}{j0.1} = -j10\text{ Ω}$$

#### **Paso 4: Impedancia total**
$$\mathbf{Z}_{total} = 30 + j25 - j10 = 30 + j15\text{ Ω}$$
$$|\mathbf{Z}| = \sqrt{30^2 + 15^2} = 33.54\text{ Ω}$$
$$\theta_Z = \arctan\frac{15}{30} = 26.57°$$
$$\mathbf{Z}_{total} = 33.54 \angle 26.57°\text{ Ω}$$

#### **Paso 5: Corriente**
$$\mathbf{I} = \frac{100 \angle 0°}{33.54 \angle 26.57°} = 2.98 \angle -26.57°\text{ A}$$

#### **Paso 6: Voltajes en cada elemento**
$$\mathbf{V}_R = \mathbf{I} \times \mathbf{Z}_R = (2.98 \angle -26.57°)(30) = 89.4 \angle -26.57°\text{ V}$$
$$\mathbf{V}_L = \mathbf{I} \times \mathbf{Z}_L = (2.98 \angle -26.57°)(25 \angle 90°) = 74.5 \angle 63.43°\text{ V}$$
$$\mathbf{V}_C = \mathbf{I} \times \mathbf{Z}_C = (2.98 \angle -26.57°)(10 \angle -90°) = 29.8 \angle -116.57°\text{ V}$$

#### **Paso 7: Dominio del tiempo**
$$i(t) = 2.98\cos(500t - 26.57°)\text{ A}$$
$$v_R(t) = 89.4\cos(500t - 26.57°)\text{ V}$$
$$v_L(t) = 74.5\cos(500t + 63.43°)\text{ V}$$
$$v_C(t) = 29.8\cos(500t - 116.57°)\text{ V}$$

### Verificación con LVK
$$\mathbf{V}_R + \mathbf{V}_L + \mathbf{V}_C = \mathbf{V}_s$$

Convertir a rectangular:
- $\mathbf{V}_R = 80 - j40$ V
- $\mathbf{V}_L = 33.3 + j66.6$ V
- $\mathbf{V}_C = -13.3 - j26.6$ V

Suma: $(80 + 33.3 - 13.3) + j(-40 + 66.6 - 26.6) = 100 + j0$ V ✓

### Respuesta
$$\boxed{i(t) = 2.98\cos(500t - 26.57°)\text{ A}}$$

### Explicación
El [circuito](../../../glossary.md#circuito) es inductivo (XL > XC), por lo que la corriente atrasa al voltaje de la fuente. La [reactancia](../../../glossary.md#reactancia) neta es XL - XC = 25 - 10 = 15 Ω inductiva.

---

## Ejemplo Clásico 3: Circuito Paralelo RL

### Enunciado
Un circuito paralelo tiene una [resistencia](../../../glossary.md#resistencia) de 60 Ω y una [inductancia](../../../glossary.md#inductancia) de 0.1 H conectados a una fuente v(t) = 120cos(200t + 45°) V. Calcule la corriente total de la fuente.

### Diagrama
```
     ●───────────┬──────────┬───────────●
     │           │          │           │
     +         ┌─┴─┐      ┌─┴─┐         │
  v(t)         │60Ω│      │0.1H│        │
     -         └─┬─┘      └─┬─┘         │
     │           │          │           │
     ●───────────┴──────────┴───────────●
```

### Solución

#### **Paso 1: Frecuencia y fasor**
$$\omega = 200\text{ rad/s}$$
$$\mathbf{V} = 120 \angle 45°\text{ V}$$

#### **Paso 2: Impedancias**
$$\mathbf{Z}_R = 60\text{ Ω}$$
$$\mathbf{Z}_L = j\omega L = j(200)(0.1) = j20\text{ Ω}$$

#### **Paso 3: Admitancias**
$$\mathbf{Y}_R = \frac{1}{\mathbf{Z}_R} = \frac{1}{60} = 0.0167\text{ S}$$
$$\mathbf{Y}_L = \frac{1}{\mathbf{Z}_L} = \frac{1}{j20} = -j0.05\text{ S}$$

#### **Paso 4: Admitancia total**
$$\mathbf{Y}_{total} = \mathbf{Y}_R + \mathbf{Y}_L = 0.0167 - j0.05\text{ S}$$
$$|\mathbf{Y}| = \sqrt{0.0167^2 + 0.05^2} = 0.0527\text{ S}$$
$$\theta_Y = \arctan\frac{-0.05}{0.0167} = -71.57°$$

#### **Paso 5: Corriente total**
$$\mathbf{I}_s = \mathbf{V} \times \mathbf{Y}_{total} = (120 \angle 45°)(0.0527 \angle -71.57°)$$
$$\mathbf{I}_s = 6.32 \angle -26.57°\text{ A}$$

#### **Paso 6: Corrientes individuales**
$$\mathbf{I}_R = \frac{\mathbf{V}}{\mathbf{Z}_R} = \frac{120 \angle 45°}{60} = 2 \angle 45°\text{ A}$$
$$\mathbf{I}_L = \frac{\mathbf{V}}{\mathbf{Z}_L} = \frac{120 \angle 45°}{20 \angle 90°} = 6 \angle -45°\text{ A}$$

#### **Verificación con LCK**
$$\mathbf{I}_s = \mathbf{I}_R + \mathbf{I}_L$$
- $\mathbf{I}_R = 2\angle 45° = 1.414 + j1.414$ A
- $\mathbf{I}_L = 6\angle -45° = 4.243 - j4.243$ A
- Suma: $5.657 - j2.829 = 6.32\angle -26.57°$ A ✓

### Respuesta
$$\boxed{i_s(t) = 6.32\cos(200t - 26.57°)\text{ A}}$$

### Explicación
La corriente total atrasa al voltaje porque el circuito es más inductivo (la corriente del inductor es mayor que la de la resistencia). En circuitos paralelos, es más conveniente usar admitancias.

---

## Tabla de Impedancias

| Elemento | Impedancia | Ángulo | V adelanta/atrasa I |
|----------|------------|--------|---------------------|
| R | R | 0° | En fase |
| L | jωL | +90° | Adelanta 90° |
| C | 1/(jωC) | -90° | Atrasa 90° |

## Conversión Importante
$$j = 1\angle 90° = e^{j90°}$$
$$\frac{1}{j} = -j = 1\angle -90°$$

## Errores Comunes
1. Olvidar convertir de forma polar a rectangular para suma
2. Confundir adelanto y atraso de fase
3. No considerar el cuadrante correcto al calcular arctan
4. Usar amplitudes RMS cuando se dieron valores pico (o viceversa)
