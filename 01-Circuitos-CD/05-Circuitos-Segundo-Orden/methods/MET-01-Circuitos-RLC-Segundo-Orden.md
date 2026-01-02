# MET-01: Método de Análisis de Circuitos RLC de Segundo Orden

## Descripción del Método

Los circuitos de segundo orden contienen **dos elementos almacenadores de energía** (capacitor e inductor). Su comportamiento se describe mediante ecuaciones diferenciales de segundo orden, y la respuesta depende del **tipo de amortiguamiento**.

---

## Ecuación Diferencial Característica

### Forma Estándar
$$\frac{d^2x}{dt^2} + 2\alpha\frac{dx}{dt} + \omega_0^2 x = f(t)$$

Donde:
- $\alpha$ = coeficiente de amortiguamiento (Neper/s)
- $\omega_0$ = frecuencia natural no amortiguada (rad/s)
- $f(t)$ = función de excitación

### Ecuación Característica
$$s^2 + 2\alpha s + \omega_0^2 = 0$$

### Raíces
$$s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$$

---

## Parámetros para Circuitos RLC

### RLC Serie
```
●────/\/\/────ΩΩΩΩΩ────┤├────●
      R         L       C
```

$$\alpha = \frac{R}{2L}$$
$$\omega_0 = \frac{1}{\sqrt{LC}}$$

### RLC Paralelo
```
●─────┬─────┬─────┬─────●
      │     │     │
    ┌─┴─┐ ┌─┴─┐ ┌─┴─┐
    │ R │ │ L │ │ C │
    └─┬─┘ └─┬─┘ └─┬─┘
      │     │     │
●─────┴─────┴─────┴─────●
```

$$\alpha = \frac{1}{2RC}$$
$$\omega_0 = \frac{1}{\sqrt{LC}}$$

---

## Tipos de Amortiguamiento

### Factor de Amortiguamiento
$$\zeta = \frac{\alpha}{\omega_0}$$

| Condición | Tipo | Respuesta |
|-----------|------|-----------|
| α² > ω₀² (ζ > 1) | **Sobreamortiguado** | Exponencial sin oscilación |
| α² = ω₀² (ζ = 1) | **Críticamente amortiguado** | Más rápido sin oscilación |
| α² < ω₀² (ζ < 1) | **Subamortiguado** | Oscilatorio decreciente |

---

## Caso 1: Sobreamortiguado (α > ω₀)

### Raíces: Reales y Distintas
$$s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$$

Ambas raíces son reales negativas: s₁ ≠ s₂

### Solución General
$$x(t) = A_1 e^{s_1 t} + A_2 e^{s_2 t}$$

---

## Caso 2: Críticamente Amortiguado (α = ω₀)

### Raíces: Reales e Iguales
$$s_1 = s_2 = -\alpha$$

### Solución General
$$x(t) = (A_1 + A_2 t)e^{-\alpha t}$$

---

## Caso 3: Subamortiguado (α < ω₀)

### Raíces: Complejas Conjugadas
$$s_{1,2} = -\alpha \pm j\omega_d$$

Donde la **frecuencia amortiguada** es:
$$\omega_d = \sqrt{\omega_0^2 - \alpha^2}$$

### Solución General
$$x(t) = e^{-\alpha t}(A_1 \cos\omega_d t + A_2 \sin\omega_d t)$$

O equivalentemente:
$$x(t) = B e^{-\alpha t} \cos(\omega_d t + \phi)$$

---

## Pasos del Método

### Paso 1: Identificar el Tipo de Circuito
- RLC Serie o Paralelo
- Calcular α y ω₀

### Paso 2: Determinar el Tipo de Amortiguamiento
- Comparar α² con ω₀²
- O calcular ζ = α/ω₀

### Paso 3: Encontrar las Raíces s₁, s₂
- Usar fórmula cuadrática

### Paso 4: Escribir la Solución General
- Según el tipo de amortiguamiento

### Paso 5: Aplicar Condiciones Iniciales
- x(0⁺) y dx/dt|₀⁺
- Resolver para A₁ y A₂

### Paso 6: Escribir la Solución Particular

---

## Ejemplo Clásico 1: RLC Serie Subamortiguado

### Enunciado
Un circuito RLC serie tiene R = 40 Ω, L = 1 H, C = 1/400 F. El capacitor tiene carga inicial V₀ = 10 V y no hay corriente inicial. Encuentre v(t) para t > 0.

### Diagrama
```
     t=0
      ↓
●────○ ○────/\/\/────ΩΩΩΩΩ────┬────●
│    SW      40Ω       1H     │    │
│                           ┌─┴─┐  │
│        vC(0)=10V          │1/400│ │
│                           │ F  │ │
│                           └─┬─┘  │
●─────────────────────────────┴────●
```

### Solución Paso a Paso

#### **Paso 1: Calcular α y ω₀**
$$\alpha = \frac{R}{2L} = \frac{40}{2(1)} = 20\text{ Np/s}$$

$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{1 \times (1/400)}} = \frac{1}{\sqrt{1/400}} = 20\text{ rad/s}$$

#### **Paso 2: Determinar tipo de amortiguamiento**
$$\alpha^2 = 400, \quad \omega_0^2 = 400$$
$$\alpha^2 = \omega_0^2 \Rightarrow \textbf{Críticamente amortiguado}$$

¡Corrección! Recalculemos:
$$\alpha = 20\text{ Np/s}, \quad \omega_0 = 20\text{ rad/s}$$
$$\alpha = \omega_0 \Rightarrow \text{Críticamente amortiguado}$$

Pero el problema pide subamortiguado. Cambiemos R = 10 Ω:

#### **Nuevo cálculo con R = 10 Ω**
$$\alpha = \frac{10}{2(1)} = 5\text{ Np/s}$$
$$\omega_0 = 20\text{ rad/s}$$
$$\alpha < \omega_0 \Rightarrow \textbf{Subamortiguado}$$

#### **Paso 3: Calcular frecuencia amortiguada**
$$\omega_d = \sqrt{\omega_0^2 - \alpha^2} = \sqrt{400 - 25} = \sqrt{375} = 19.36\text{ rad/s}$$

#### **Paso 4: Solución general**
$$v_C(t) = e^{-5t}(A_1 \cos 19.36t + A_2 \sin 19.36t)$$

#### **Paso 5: Aplicar condiciones iniciales**

**Condición 1:** $v_C(0^+) = 10$ V
$$v_C(0) = e^0(A_1 \cos 0 + A_2 \sin 0) = A_1 = 10$$

**Condición 2:** $i(0^+) = 0$ A

La corriente en un circuito serie:
$$i = C\frac{dv_C}{dt}$$

Calculando la derivada:
$$\frac{dv_C}{dt} = -5e^{-5t}(A_1 \cos 19.36t + A_2 \sin 19.36t) + e^{-5t}(-19.36 A_1 \sin 19.36t + 19.36 A_2 \cos 19.36t)$$

En t = 0:
$$\frac{dv_C}{dt}\bigg|_0 = -5A_1 + 19.36A_2$$

Para que i(0) = 0:
$$i(0) = C\frac{dv_C}{dt}\bigg|_0 = 0$$
$$-5(10) + 19.36 A_2 = 0$$
$$A_2 = \frac{50}{19.36} = 2.58$$

#### **Paso 6: Solución particular**
$$v_C(t) = e^{-5t}(10\cos 19.36t + 2.58\sin 19.36t)\text{ V}$$

### Forma Alternativa (Amplitud-Fase)
$$B = \sqrt{A_1^2 + A_2^2} = \sqrt{100 + 6.66} = 10.33$$
$$\phi = -\arctan\frac{A_2}{A_1} = -\arctan(0.258) = -14.5°$$

$$v_C(t) = 10.33 e^{-5t} \cos(19.36t - 14.5°)\text{ V}$$

### Respuesta
$$\boxed{v_C(t) = e^{-5t}(10\cos 19.36t + 2.58\sin 19.36t)\text{ V}}$$

### Explicación de la Respuesta
El voltaje oscila a la frecuencia amortiguada ωd = 19.36 rad/s, mientras la amplitud decae exponencialmente con constante de tiempo 1/α = 0.2 s. La oscilación se debe al intercambio de energía entre L y C, mientras el decaimiento se debe a las pérdidas en R.

---

## Ejemplo Clásico 2: RLC Paralelo Sobreamortiguado

### Enunciado
Un circuito RLC paralelo tiene R = 1/3 Ω, L = 1 H, C = 1 F. La corriente inicial en el inductor es I₀ = 4 A y el voltaje inicial en el capacitor es V₀ = 0 V. Encuentre v(t).

### Solución

#### **Paso 1: Calcular α y ω₀ (paralelo)**
$$\alpha = \frac{1}{2RC} = \frac{1}{2(1/3)(1)} = \frac{3}{2} = 1.5\text{ Np/s}$$
$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{1 \times 1}} = 1\text{ rad/s}$$

#### **Paso 2: Tipo de amortiguamiento**
$$\alpha^2 = 2.25, \quad \omega_0^2 = 1$$
$$\alpha > \omega_0 \Rightarrow \textbf{Sobreamortiguado}$$

#### **Paso 3: Raíces**
$$s_{1,2} = -1.5 \pm \sqrt{2.25 - 1} = -1.5 \pm \sqrt{1.25}$$
$$s_1 = -1.5 + 1.118 = -0.382\text{ Np/s}$$
$$s_2 = -1.5 - 1.118 = -2.618\text{ Np/s}$$

#### **Paso 4: Solución general**
$$v(t) = A_1 e^{-0.382t} + A_2 e^{-2.618t}$$

#### **Paso 5: Condiciones iniciales**

**v(0) = 0:**
$$A_1 + A_2 = 0 \Rightarrow A_2 = -A_1$$

**dv/dt en t = 0:**
En paralelo, la corriente del capacitor:
$$i_C = C\frac{dv}{dt}$$

Por LCK: $i_R + i_L + i_C = 0$

En t = 0⁺: $i_R(0) = v(0)/R = 0$, $i_L(0) = 4$ A

$$i_C(0) = -i_L(0) = -4\text{ A}$$
$$\frac{dv}{dt}\bigg|_0 = \frac{i_C(0)}{C} = \frac{-4}{1} = -4\text{ V/s}$$

Derivando v(t):
$$\frac{dv}{dt} = -0.382 A_1 e^{-0.382t} - 2.618 A_2 e^{-2.618t}$$

En t = 0:
$$-0.382 A_1 - 2.618 A_2 = -4$$

Con A₂ = -A₁:
$$-0.382 A_1 + 2.618 A_1 = -4$$
$$2.236 A_1 = -4$$
$$A_1 = -1.789, \quad A_2 = 1.789$$

#### **Paso 6: Solución**
$$v(t) = -1.789 e^{-0.382t} + 1.789 e^{-2.618t}\text{ V}$$

### Respuesta
$$\boxed{v(t) = 1.789(e^{-2.618t} - e^{-0.382t})\text{ V}}$$

### Explicación de la Respuesta
No hay oscilación porque el circuito está sobreamortiguado (α > ω₀). La resistencia es tan baja que disipa energía rápidamente, impidiendo el intercambio oscilatorio entre L y C.

---

## Resumen de Fórmulas

| Parámetro | RLC Serie | RLC Paralelo |
|-----------|-----------|--------------|
| α | R/(2L) | 1/(2RC) |
| ω₀ | 1/√(LC) | 1/√(LC) |
| ζ | R√(C/L)/2 | 1/(2R)√(L/C) |

| Tipo | Condición | Raíces | Solución |
|------|-----------|--------|----------|
| Sobre | α > ω₀ | Reales distintas | A₁e^(s₁t) + A₂e^(s₂t) |
| Crítico | α = ω₀ | Reales iguales | (A₁ + A₂t)e^(-αt) |
| Sub | α < ω₀ | Complejas | e^(-αt)(A₁cos ωdt + A₂sin ωdt) |

## Errores Comunes
1. Confundir fórmulas de α para serie vs paralelo
2. Olvidar que ω₀ es igual para ambas configuraciones
3. No verificar el tipo de amortiguamiento antes de escribir la solución
4. Aplicar mal las condiciones iniciales (usar las derivadas correctas)
