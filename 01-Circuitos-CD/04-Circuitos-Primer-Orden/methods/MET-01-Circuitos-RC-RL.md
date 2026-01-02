# MET-01: Método de Análisis de Circuitos RC y RL de Primer Orden

## Descripción del Método

Los circuitos de primer orden contienen **un solo elemento almacenador de energía** (capacitor o inductor) y resistencias. Su comportamiento se describe mediante ecuaciones diferenciales de primer orden.

### Tipos de Respuesta
1. **Respuesta Natural:** Comportamiento del circuito sin fuentes externas (energía almacenada inicialmente)
2. **Respuesta Forzada:** Comportamiento debido a fuentes externas (estado estacionario)
3. **Respuesta Completa:** Suma de respuesta natural + respuesta forzada

---

## Constante de Tiempo (τ)

### Circuito RC
$$\tau = RC$$

### Circuito RL
$$\tau = \frac{L}{R}$$

### Significado Físico
- Tiempo para alcanzar ≈63.2% del valor final (carga)
- Tiempo para decaer a ≈36.8% del valor inicial (descarga)
- Después de 5τ, se considera que el circuito alcanzó estado estacionario (>99%)

---

## Fórmulas Generales

### Forma General de la Solución
$$x(t) = x(\infty) + [x(0) - x(\infty)]e^{-t/\tau}$$

Donde:
- $x(t)$ = variable (voltaje o corriente) en el tiempo t
- $x(0)$ = valor inicial (en t = 0⁺)
- $x(\infty)$ = valor final (estado estacionario)
- $\tau$ = constante de tiempo

---

## Parte A: Circuito RC

### Diagrama Base
```
     t=0
      ↓
●────○ ○────/\/\/────┬────●
│    SW      R       │    │
│                  ┌─┴─┐  │
│       Vs         │ C │  │
│                  │   │  │
│                  └─┬─┘  │
●────────────────────┴────●
```

### Condiciones Iniciales en Capacitor
- **Voltaje en capacitor:** Continuo (no puede cambiar instantáneamente)
$$v_C(0^+) = v_C(0^-)$$

### Respuesta Natural RC (descarga)
$$v_C(t) = V_0 e^{-t/\tau}$$

### Respuesta Completa RC (carga desde 0)
$$v_C(t) = V_s(1 - e^{-t/\tau})$$

---

## Ejemplo Clásico 1: Carga de Capacitor

### Enunciado
Un capacitor de 100 μF inicialmente descargado se conecta a través de una resistencia de 10 kΩ a una fuente de 12 V. Determine:
a) La constante de tiempo
b) El voltaje en el capacitor a t = τ, 3τ, 5τ
c) El tiempo para alcanzar 9 V

### Diagrama
```
     t=0
      ↓
●────○ ○────/\/\/────┬────●
│    SW    10kΩ      │    │
│  +                ─┴─   │
│ 12V              │100μF │
│  -               ─┬─    │
│                    │    │
●────────────────────┴────●
```

### Solución Paso a Paso

#### **a) Constante de tiempo**
$$\tau = RC = 10000 \times 100 \times 10^{-6} = 1\text{ s}$$

#### **b) Voltaje en diferentes tiempos**

Ecuación: $v_C(t) = V_s(1 - e^{-t/\tau}) = 12(1 - e^{-t/1})$

**En t = τ = 1 s:**
$$v_C(\tau) = 12(1 - e^{-1}) = 12(1 - 0.368) = 12 \times 0.632 = 7.58\text{ V}$$

**En t = 3τ = 3 s:**
$$v_C(3\tau) = 12(1 - e^{-3}) = 12(1 - 0.0498) = 12 \times 0.950 = 11.40\text{ V}$$

**En t = 5τ = 5 s:**
$$v_C(5\tau) = 12(1 - e^{-5}) = 12(1 - 0.0067) = 12 \times 0.993 = 11.92\text{ V}$$

#### **c) Tiempo para alcanzar 9 V**
$$9 = 12(1 - e^{-t/1})$$
$$\frac{9}{12} = 1 - e^{-t}$$
$$e^{-t} = 1 - 0.75 = 0.25$$
$$-t = \ln(0.25) = -1.386$$
$$t = 1.386\text{ s} = 1.386\tau$$

### Respuesta
$$\boxed{\tau = 1\text{ s}, \quad v_C(\tau) = 7.58\text{ V}, \quad v_C(3\tau) = 11.4\text{ V}, \quad t_{9V} = 1.39\text{ s}}$$

### Explicación de la Respuesta
El capacitor se carga exponencialmente hacia 12 V. En un tiempo τ (1 s), alcanza el 63.2% (7.58 V). Nunca alcanza exactamente 12 V pero se considera "completamente cargado" después de 5τ (99.3%). El tiempo para llegar a 9 V (75%) es aproximadamente 1.4τ.

---

## Ejemplo Clásico 2: Descarga de Capacitor

### Enunciado
Un capacitor de 47 μF cargado a 24 V se descarga a través de una resistencia de 22 kΩ. Calcule:
a) La constante de tiempo
b) El voltaje después de 2 s
c) La energía inicial y la energía restante después de τ

### Solución

#### **a) Constante de tiempo**
$$\tau = RC = 22000 \times 47 \times 10^{-6} = 1.034\text{ s}$$

#### **b) Voltaje en t = 2 s**
$$v_C(t) = V_0 e^{-t/\tau} = 24 e^{-2/1.034} = 24 e^{-1.934}$$
$$v_C(2) = 24 \times 0.145 = 3.47\text{ V}$$

#### **c) Energía**

**Energía inicial:**
$$W_0 = \frac{1}{2}CV_0^2 = \frac{1}{2}(47 \times 10^{-6})(24)^2 = 13.5\text{ mJ}$$

**Energía en t = τ:**
$$v_C(\tau) = 24 e^{-1} = 24 \times 0.368 = 8.83\text{ V}$$
$$W_\tau = \frac{1}{2}(47 \times 10^{-6})(8.83)^2 = 1.83\text{ mJ}$$

**Porcentaje de energía restante:**
$$\frac{W_\tau}{W_0} = e^{-2} = 0.135 = 13.5\%$$

### Respuesta
$$\boxed{\tau = 1.034\text{ s}, \quad v_C(2s) = 3.47\text{ V}, \quad W_0 = 13.5\text{ mJ}, \quad W_\tau = 1.83\text{ mJ}}$$

### Explicación de la Respuesta
La energía decae más rápido que el voltaje porque $W \propto v^2$. En un tiempo τ, el voltaje es 36.8% del inicial, pero la energía es solo (0.368)² = 13.5% de la inicial.

---

## Parte B: Circuito RL

### Diagrama Base
```
     t=0
      ↓
●────○ ○────/\/\/────ΩΩΩΩΩ────●
│    SW      R         L      │
│                             │
│            Vs               │
│                             │
●─────────────────────────────●
```

### Condiciones Iniciales en Inductor
- **Corriente en inductor:** Continua (no puede cambiar instantáneamente)
$$i_L(0^+) = i_L(0^-)$$

### Respuesta Natural RL
$$i_L(t) = I_0 e^{-t/\tau}$$

### Respuesta Completa RL
$$i_L(t) = I_f(1 - e^{-t/\tau}) + I_0 e^{-t/\tau}$$

---

## Ejemplo Clásico 3: Circuito RL con Conmutación

### Enunciado
En el circuito, el interruptor ha estado cerrado por largo tiempo y se abre en t = 0. R = 4 Ω, L = 2 H, Vs = 20 V. Encuentre i(t) para t > 0.

### Diagrama
```
     Antes (t < 0)               Después (t > 0)
●────────●────ΩΩΩΩΩ────●      ●────○ ○────ΩΩΩΩΩ────●
│        │      L      │      │    SW      L      │
│      ┌─┴─┐           │      │                   │
│ Vs   │ R │           │      │      i(t) →       │
│      └─┬─┘           │      │                   │
●────────●─────────────●      ●───────────────────●
```

### Solución Paso a Paso

#### **Paso 1: Condición inicial (t < 0)**
Con el interruptor cerrado por largo tiempo, el inductor es un cortocircuito:
$$i(0^-) = \frac{V_s}{R} = \frac{20}{4} = 5\text{ A}$$

#### **Paso 2: Continuidad de la corriente**
$$i(0^+) = i(0^-) = 5\text{ A}$$

#### **Paso 3: Valor final (t → ∞)**
Con el interruptor abierto, no hay fuente, el circuito se descarga:
$$i(\infty) = 0\text{ A}$$

#### **Paso 4: Constante de tiempo**
$$\tau = \frac{L}{R} = \frac{2}{4} = 0.5\text{ s}$$

#### **Paso 5: Ecuación de i(t)**
$$i(t) = i(\infty) + [i(0) - i(\infty)]e^{-t/\tau}$$
$$i(t) = 0 + [5 - 0]e^{-t/0.5}$$
$$i(t) = 5e^{-2t}\text{ A}$$

#### **Paso 6: Voltaje en el inductor**
$$v_L = L\frac{di}{dt} = 2 \times \frac{d}{dt}(5e^{-2t}) = 2 \times 5 \times (-2)e^{-2t}$$
$$v_L(t) = -20e^{-2t}\text{ V}$$

### Respuesta
$$\boxed{i(t) = 5e^{-2t}\text{ A para } t > 0}$$
$$\boxed{v_L(t) = -20e^{-2t}\text{ V para } t > 0}$$

### Explicación de la Respuesta
La corriente decae exponencialmente desde 5 A hasta 0 A con τ = 0.5 s. El voltaje negativo en el inductor indica que se opone al cambio de corriente (Ley de Lenz). En t = 0⁺, el inductor "ve" un voltaje de -20 V para tratar de mantener la corriente.

---

## Resumen de Fórmulas Clave

### Circuito RC

| Cantidad | Carga | Descarga |
|----------|-------|----------|
| vC(t) | Vs(1 - e^(-t/τ)) | V₀e^(-t/τ) |
| iC(t) | (Vs/R)e^(-t/τ) | -(V₀/R)e^(-t/τ) |
| τ | RC | RC |

### Circuito RL

| Cantidad | Energización | Desenergización |
|----------|--------------|-----------------|
| iL(t) | If(1 - e^(-t/τ)) | I₀e^(-t/τ) |
| vL(t) | Vse^(-t/τ) | -I₀Re^(-t/τ) |
| τ | L/R | L/R |

### Valores en Múltiplos de τ

| t | e^(-t/τ) | 1 - e^(-t/τ) |
|---|----------|--------------|
| 0 | 1.000 | 0.000 |
| τ | 0.368 | 0.632 |
| 2τ | 0.135 | 0.865 |
| 3τ | 0.050 | 0.950 |
| 4τ | 0.018 | 0.982 |
| 5τ | 0.007 | 0.993 |

---

## Errores Comunes

1. **Olvidar la continuidad:** vC y iL no pueden cambiar instantáneamente
2. **τ incorrecto:** RC para capacitor, L/R para inductor (¡no R/L!)
3. **Signo incorrecto:** El signo depende de si es carga o descarga
4. **Valor inicial vs final:** Confundir x(0) con x(∞)
5. **Unidades:** Verificar que τ tenga unidades de segundos
