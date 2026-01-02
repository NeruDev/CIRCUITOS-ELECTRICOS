# MET-02: Método de Respuesta al Escalón en Circuitos de Segundo Orden

## Descripción del Método

La **respuesta al escalón** es la respuesta de un [circuito](../../../glossary.md#circuito) RLC cuando se aplica una fuente de [voltaje](../../../glossary.md#voltaje) o [corriente](../../../glossary.md#corriente) constante (escalón unitario). La respuesta completa incluye la **respuesta natural** (transitoria) y la **respuesta forzada** (estado estable).

---

## Respuesta Completa

$$x(t) = x_{forzada}(t) + x_{natural}(t) = x_f + x_n(t)$$

Para t → ∞, la respuesta natural se desvanece y queda solo la respuesta forzada.

### Estado Estable DC
- **Capacitor**: Circuito abierto (i = 0)
- **Inductor**: Cortocircuito (v = 0)

---

## Pasos del Método

### Paso 1: Encontrar Condiciones Iniciales
- $x(0^+)$ - valor inicial
- $\frac{dx}{dt}\bigg|_{0^+}$ - derivada inicial

### Paso 2: Encontrar Respuesta en Estado Estable
- Analizar circuito con C → abierto, L → corto
- $x(\infty) = x_f$

### Paso 3: Calcular α y ω₀
- Serie: $\alpha = R/(2L)$, $\omega_0 = 1/\sqrt{LC}$
- Paralelo: $\alpha = 1/(2RC)$, $\omega_0 = 1/\sqrt{LC}$

### Paso 4: Determinar Tipo de Amortiguamiento
- Comparar α² con ω₀²

### Paso 5: Escribir Solución General
- Forma: $x(t) = x_f + x_n(t)$

### Paso 6: Aplicar Condiciones Iniciales
- Encontrar constantes A₁, A₂

---

## Formas de la Respuesta Según Amortiguamiento

### Sobreamortiguado (α > ω₀)
$$x(t) = x_f + A_1 e^{s_1 t} + A_2 e^{s_2 t}$$

### Críticamente Amortiguado (α = ω₀)
$$x(t) = x_f + (A_1 + A_2 t)e^{-\alpha t}$$

### Subamortiguado (α < ω₀)
$$x(t) = x_f + e^{-\alpha t}(A_1 \cos\omega_d t + A_2 \sin\omega_d t)$$

donde $\omega_d = \sqrt{\omega_0^2 - \alpha^2}$

---

## Ejemplo Clásico 1: Respuesta al Escalón en RLC Serie

### Enunciado
Un circuito RLC serie con R = 5 Ω, L = 1 H, C = 0.04 F tiene condiciones iniciales nulas. En t = 0 se aplica una fuente de 24 V. Determine i(t).

### Diagrama
```
     t=0
      ↓
●────○ ○───────┬────/\/\/────ΩΩΩΩΩ────┬────●
      │        │      5Ω       1H     │    │
    ┌─┴─┐      │                    ┌─┴─┐  │
    │24V│      │                    │0.04│ │
    │ + │      │                    │ F  │ │
    └─┬─┘      │                    └─┬─┘  │
●─────┴────────┴──────────────────────┴────●
```

### Solución

#### **Paso 1: Condiciones Iniciales**
- $i_L(0^-) = 0$ A → $i_L(0^+) = 0$ A (corriente en [inductor](../../../glossary.md#inductancia) continua)
- $v_C(0^-) = 0$ V → $v_C(0^+) = 0$ V (voltaje en [capacitor](../../../glossary.md#capacitancia) continuo)

Para la derivada, aplicamos [LVK](../../../glossary.md#lvk) en t = 0⁺:
$$V_s = v_R + v_L + v_C$$
$$24 = R i(0^+) + L\frac{di}{dt}\bigg|_{0^+} + v_C(0^+)$$
$$24 = 5(0) + 1 \cdot \frac{di}{dt}\bigg|_{0^+} + 0$$
$$\frac{di}{dt}\bigg|_{0^+} = 24\text{ A/s}$$

#### **Paso 2: Respuesta en Estado Estable**
En DC (t → ∞):
- Capacitor → circuito abierto
- Corriente en serie = 0

$$i_f = i(\infty) = 0\text{ A}$$

#### **Paso 3: Calcular α y ω₀**
$$\alpha = \frac{R}{2L} = \frac{5}{2(1)} = 2.5\text{ Np/s}$$
$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{1 \times 0.04}} = \frac{1}{0.2} = 5\text{ rad/s}$$

#### **Paso 4: Tipo de amortiguamiento**
$$\alpha^2 = 6.25, \quad \omega_0^2 = 25$$
$$\alpha < \omega_0 \Rightarrow \textbf{Subamortiguado}$$

$$\omega_d = \sqrt{25 - 6.25} = \sqrt{18.75} = 4.33\text{ rad/s}$$

#### **Paso 5: Solución general**
$$i(t) = 0 + e^{-2.5t}(A_1 \cos 4.33t + A_2 \sin 4.33t)$$
$$i(t) = e^{-2.5t}(A_1 \cos 4.33t + A_2 \sin 4.33t)$$

#### **Paso 6: Aplicar condiciones iniciales**

**i(0) = 0:**
$$i(0) = A_1 = 0$$

**di/dt|₀ = 24:**
$$\frac{di}{dt} = -2.5 e^{-2.5t}(A_1 \cos 4.33t + A_2 \sin 4.33t) + e^{-2.5t}(-4.33 A_1 \sin 4.33t + 4.33 A_2 \cos 4.33t)$$

En t = 0:
$$\frac{di}{dt}\bigg|_0 = -2.5 A_1 + 4.33 A_2 = 24$$

Con A₁ = 0:
$$4.33 A_2 = 24$$
$$A_2 = 5.54$$

### Respuesta
$$\boxed{i(t) = 5.54 e^{-2.5t} \sin(4.33t)\text{ A}}$$

### Explicación
La corriente parte de cero (condición inicial), aumenta inicialmente debido al voltaje aplicado, y luego oscila con amplitud decreciente hasta estabilizarse en cero (estado estable en DC con capacitor).

---

## Ejemplo Clásico 2: Respuesta Críticamente Amortiguada

### Enunciado
Un circuito RLC serie tiene L = 1 H, C = 0.25 F. Determine R para respuesta críticamente amortiguada. Si se aplica un escalón de 20 V con condiciones iniciales nulas, encuentre v_C(t).

### Solución

#### **Paso 1: Encontrar R para amortiguamiento crítico**
Condición: $\alpha = \omega_0$

$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{1 \times 0.25}} = \frac{1}{0.5} = 2\text{ rad/s}$$

$$\alpha = \frac{R}{2L} = 2$$
$$R = 4L = 4(1) = 4\text{ Ω}$$

#### **Paso 2: Condiciones iniciales**
- $v_C(0^+) = 0$ V
- $i(0^+) = 0$ A

Para $\frac{dv_C}{dt}\bigg|_{0^+}$:
$$i_C = C\frac{dv_C}{dt}$$
$$\frac{dv_C}{dt}\bigg|_{0^+} = \frac{i_C(0^+)}{C} = \frac{0}{0.25} = 0\text{ V/s}$$

#### **Paso 3: Estado estable**
En DC, el capacitor está completamente cargado:
$$v_C(\infty) = 20\text{ V}$$

#### **Paso 4: Solución general (crítico)**
$$v_C(t) = v_f + (A_1 + A_2 t)e^{-\alpha t}$$
$$v_C(t) = 20 + (A_1 + A_2 t)e^{-2t}$$

#### **Paso 5: Aplicar condiciones iniciales**

**v_C(0) = 0:**
$$0 = 20 + A_1$$
$$A_1 = -20$$

**dv_C/dt|₀ = 0:**
$$\frac{dv_C}{dt} = A_2 e^{-2t} - 2(A_1 + A_2 t)e^{-2t}$$

En t = 0:
$$0 = A_2 - 2A_1 = A_2 - 2(-20) = A_2 + 40$$
$$A_2 = -40$$

### Respuesta
$$\boxed{v_C(t) = 20 - (20 + 40t)e^{-2t}\text{ V}}$$

### Verificación
- t = 0: $v_C(0) = 20 - 20 = 0$ ✓
- t → ∞: $v_C(\infty) = 20 - 0 = 20$ V ✓

### Explicación
El voltaje alcanza el valor final de 20 V lo más rápido posible sin sobrepasar (sin oscilación). Este es el comportamiento óptimo para sistemas donde se desea respuesta rápida sin overshoot.

---

## Ejemplo Clásico 3: Respuesta Sobreamortiguada con Condiciones Iniciales No Nulas

### Enunciado
En un circuito RLC paralelo, R = 1 Ω, L = 2 H, C = 2 F. En t = 0, se conecta una fuente de corriente de 12 A. Las condiciones iniciales son v(0) = 0 V e i_L(0) = 0 A. Determine v(t).

### Solución

#### **Paso 1: Calcular α y ω₀ (paralelo)**
$$\alpha = \frac{1}{2RC} = \frac{1}{2(1)(2)} = 0.25\text{ Np/s}$$
$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{2 \times 2}} = \frac{1}{2} = 0.5\text{ rad/s}$$

#### **Paso 2: Tipo de amortiguamiento**
$$\alpha^2 = 0.0625, \quad \omega_0^2 = 0.25$$
$$\alpha < \omega_0 \Rightarrow \textbf{Subamortiguado}$$

$$\omega_d = \sqrt{0.25 - 0.0625} = \sqrt{0.1875} = 0.433\text{ rad/s}$$

#### **Paso 3: Estado estable**
En DC, C → abierto, L → corto:
$$v(\infty) = I_s \times R = 12 \times 1 = 12\text{ V}$$

#### **Paso 4: Condiciones iniciales**
- $v(0^+) = 0$ V
- $i_L(0^+) = 0$ A, $i_C(0^+) = ?$

Por [LCK](../../../glossary.md#lck): $I_s = i_R + i_L + i_C$
$$12 = \frac{v(0)}{R} + i_L(0) + i_C(0^+)$$
$$12 = 0 + 0 + i_C(0^+)$$
$$i_C(0^+) = 12\text{ A}$$

$$\frac{dv}{dt}\bigg|_{0^+} = \frac{i_C(0^+)}{C} = \frac{12}{2} = 6\text{ V/s}$$

#### **Paso 5: Solución general**
$$v(t) = 12 + e^{-0.25t}(A_1 \cos 0.433t + A_2 \sin 0.433t)$$

#### **Paso 6: Aplicar condiciones iniciales**

**v(0) = 0:**
$$0 = 12 + A_1$$
$$A_1 = -12$$

**dv/dt|₀ = 6:**
$$\frac{dv}{dt}\bigg|_0 = -0.25 A_1 + 0.433 A_2$$
$$6 = -0.25(-12) + 0.433 A_2$$
$$6 = 3 + 0.433 A_2$$
$$A_2 = \frac{3}{0.433} = 6.93$$

### Respuesta
$$\boxed{v(t) = 12 + e^{-0.25t}(-12\cos 0.433t + 6.93\sin 0.433t)\text{ V}}$$

O en forma polar:
$$v(t) = 12 - 13.86 e^{-0.25t}\cos(0.433t + 30°)\text{ V}$$

### Explicación
El voltaje oscila alrededor del valor final de 12 V debido al comportamiento subamortiguado. La constante de tiempo del decaimiento es 1/α = 4 s, mientras que el período de oscilación es T = 2π/ωd ≈ 14.5 s.

---

## Características de la Respuesta

### Tiempo de Subida (Rise Time)
Tiempo para que la respuesta suba del 10% al 90% del valor final.

### Tiempo de Pico (Peak Time)
$$t_p = \frac{\pi}{\omega_d}$$ (solo subamortiguado)

### Sobreimpulso (Overshoot)
$$\%OS = 100 e^{-\pi\zeta/\sqrt{1-\zeta^2}}$$ donde $\zeta = \alpha/\omega_0$

### Tiempo de Establecimiento (Settling Time)
- 2% criterio: $t_s \approx \frac{4}{\alpha}$
- 5% criterio: $t_s \approx \frac{3}{\alpha}$

---

## Resumen de Fórmulas

| Característica | Fórmula |
|----------------|---------|
| Frecuencia amortiguada | $\omega_d = \sqrt{\omega_0^2 - \alpha^2}$ |
| Factor de amortiguamiento | $\zeta = \alpha/\omega_0$ |
| Período de oscilación | $T = 2\pi/\omega_d$ |
| Constante de decaimiento | $\tau = 1/\alpha$ |
| Tiempo de pico | $t_p = \pi/\omega_d$ |

## Errores Comunes
1. Olvidar sumar la respuesta forzada xf
2. Usar condiciones iniciales en t = 0⁻ en lugar de t = 0⁺
3. Calcular mal dv/dt o di/dt usando relaciones incorrectas
4. Confundir ω₀ con ωd
