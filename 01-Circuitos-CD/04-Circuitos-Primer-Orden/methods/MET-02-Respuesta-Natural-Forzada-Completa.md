# MET-02: Método de Respuesta Natural, Forzada y Completa

## Descripción del Método

La **respuesta completa** de un circuito de primer orden es la suma de:
1. **Respuesta Natural (xn):** Comportamiento del circuito debido a la energía almacenada inicialmente
2. **Respuesta Forzada (xf):** Comportamiento debido a la excitación externa (fuente)

$$x(t) = x_n(t) + x_f(t)$$

---

## Respuesta Natural

### Definición
Es la respuesta del circuito cuando **no hay fuentes activas** pero existe energía almacenada inicialmente en el capacitor o inductor.

### Característica
- Decae exponencialmente a cero
- Depende solo de las condiciones iniciales
- Forma: $x_n(t) = Ae^{-t/\tau}$

### Para Circuito RC (sin fuente)
$$v_C(t) = V_0 e^{-t/RC}$$

### Para Circuito RL (sin fuente)
$$i_L(t) = I_0 e^{-Rt/L}$$

---

## Respuesta Forzada (Estado Estacionario)

### Definición
Es la respuesta del circuito después de que los transitorios han desaparecido, determinada únicamente por las fuentes.

### Característica
- Tiene la misma forma que la excitación
- Para DC: constante
- Para AC: senoidal con la misma frecuencia

### Para Fuente DC
- Capacitor → Circuito abierto (iC = 0)
- Inductor → Cortocircuito (vL = 0)

---

## Respuesta Completa

### Fórmula General
$$x(t) = x_f + (x_0 - x_f)e^{-t/\tau}$$

Donde:
- $x_f$ = valor final (forzado) = $x(\infty)$
- $x_0$ = valor inicial = $x(0^+)$
- $\tau$ = constante de tiempo

### Pasos del Método

#### Paso 1: Encontrar x(0⁺) - Condición Inicial
- Para capacitor: $v_C(0^+) = v_C(0^-)$ (continuidad del voltaje)
- Para inductor: $i_L(0^+) = i_L(0^-)$ (continuidad de la corriente)

#### Paso 2: Encontrar x(∞) - Valor Final
- Analizar el circuito en estado estacionario (t → ∞)
- Capacitor = circuito abierto
- Inductor = cortocircuito

#### Paso 3: Calcular τ - Constante de Tiempo
- Encontrar la resistencia equivalente vista por C o L
- $\tau = R_{eq}C$ o $\tau = L/R_{eq}$

#### Paso 4: Escribir la Solución
$$x(t) = x(\infty) + [x(0^+) - x(\infty)]e^{-t/\tau}$$

---

## Ejemplo Clásico 1: Respuesta Completa RC con Fuente DC

### Enunciado
El capacitor tiene una carga inicial de 4 V. En t = 0, el interruptor se cierra. Encuentre vC(t) para t ≥ 0.

### Diagrama
```
     t=0
      ↓
●────○ ○────/\/\/────┬────●
│    SW    R=5kΩ     │    │
│  +               ┌─┴─┐  │
│ 12V              │ C │ vC(0⁻)=4V
│  -               │2μF│  │
│                  └─┬─┘  │
●────────────────────┴────●
```

### Solución Paso a Paso

#### **Paso 1: Condición inicial vC(0⁺)**
$$v_C(0^+) = v_C(0^-) = 4\text{ V}$$

#### **Paso 2: Valor final vC(∞)**
En estado estacionario, iC = 0, el capacitor es circuito abierto:
$$v_C(\infty) = 12\text{ V}$$ (todo el voltaje de la fuente)

#### **Paso 3: Constante de tiempo τ**
$$\tau = RC = 5000 \times 2 \times 10^{-6} = 0.01\text{ s} = 10\text{ ms}$$

#### **Paso 4: Escribir la solución**
$$v_C(t) = v_C(\infty) + [v_C(0^+) - v_C(\infty)]e^{-t/\tau}$$
$$v_C(t) = 12 + (4 - 12)e^{-t/0.01}$$
$$v_C(t) = 12 - 8e^{-100t}\text{ V}$$

#### **Verificación**
- En t = 0: $v_C(0) = 12 - 8e^0 = 12 - 8 = 4$ V ✓
- En t = ∞: $v_C(\infty) = 12 - 8(0) = 12$ V ✓

### Desglose de la Respuesta

**Respuesta Forzada:**
$$v_{Cf}(t) = 12\text{ V}$$

**Respuesta Natural:**
$$v_{Cn}(t) = -8e^{-100t}\text{ V}$$

**Respuesta Completa:**
$$v_C(t) = v_{Cf} + v_{Cn} = 12 - 8e^{-100t}\text{ V}$$

### Respuesta
$$\boxed{v_C(t) = 12 - 8e^{-100t}\text{ V para } t \geq 0}$$

### Explicación de la Respuesta
El capacitor comienza en 4 V (carga parcial) y se carga hacia 12 V. La respuesta natural (-8e^(-100t)) representa la "corrección" desde el valor inicial hasta el final. A medida que t → ∞, la exponencial → 0 y el capacitor alcanza 12 V.

---

## Ejemplo Clásico 2: Circuito RL con Conmutación

### Enunciado
El interruptor ha estado en posición 1 por largo tiempo y cambia a posición 2 en t = 0. Encuentre i(t) e v(t) para t > 0.

### Diagrama
```
       Posición 1      Posición 2
            │              │
            ▼              ▼
●───────○ 1 ○───/\/\/─────○ 2 ○───●
│            │   2Ω               │
│  +       ┌─┴─┐              ┌─┴─┐
│ 40V      │6Ω │              │4Ω │
│  -       └─┬─┘              └─┬─┘
│            │      ┌────ΩΩΩΩ──┤
│            │      │   3H     │
│            │    i(t)→        │
●────────────●──────┴──────────●
```

### Solución Paso a Paso

#### **Paso 1: Condición inicial i(0⁺)**

**Para t < 0 (posición 1, estado estacionario):**
El inductor es cortocircuito. El circuito tiene 40V con resistencias 2Ω y 6Ω en paralelo + ruta por inductor.

Simplificando: Con el inductor en cortocircuito, 6Ω está en paralelo con el inductor.
$$R_{eq} = 2 + (6 \| 0) = 2 + 0 = 2\text{ Ω}$$

Toda la corriente pasa por el inductor (menor resistencia):
$$i(0^-) = \frac{40}{2} = 20\text{ A}$$

Por continuidad:
$$i(0^+) = 20\text{ A}$$

#### **Paso 2: Valor final i(∞)**

**Para t > 0 (posición 2):**
En estado estacionario, el inductor es cortocircuito.
No hay fuente conectada en posición 2, solo resistencia de 4Ω.
$$i(\infty) = 0\text{ A}$$

#### **Paso 3: Constante de tiempo τ**
Resistencia vista por el inductor en posición 2:
$$R_{eq} = 4\text{ Ω}$$
$$\tau = \frac{L}{R_{eq}} = \frac{3}{4} = 0.75\text{ s}$$

#### **Paso 4: Escribir la solución**
$$i(t) = i(\infty) + [i(0^+) - i(\infty)]e^{-t/\tau}$$
$$i(t) = 0 + (20 - 0)e^{-t/0.75}$$
$$i(t) = 20e^{-4t/3}\text{ A}$$

#### **Paso 5: Calcular v(t) en el inductor**
$$v(t) = L\frac{di}{dt} = 3 \times 20 \times \left(-\frac{4}{3}\right)e^{-4t/3}$$
$$v(t) = -80e^{-4t/3}\text{ V}$$

### Respuesta
$$\boxed{i(t) = 20e^{-4t/3}\text{ A para } t > 0}$$
$$\boxed{v(t) = -80e^{-4t/3}\text{ V para } t > 0}$$

### Explicación de la Respuesta
Cuando el interruptor cambia, el inductor mantiene su corriente de 20 A instantáneamente. Luego, la energía almacenada se disipa en la resistencia de 4 Ω. El voltaje negativo indica que el inductor actúa como fuente, tratando de mantener la corriente. En t = 0⁺, |v| = 80 V es muy alto porque el inductor "empuja" toda la corriente a través de 4 Ω.

---

## Ejemplo Clásico 3: Circuito con Resistencias Múltiples

### Enunciado
Determine v(t) para t > 0 si el capacitor inicialmente está descargado.

### Diagrama
```
     t=0
      ↓           R₁=6Ω
●────○ ○──────────/\/\/────┬────●
│    SW                    │    │
│  +                     ┌─┴─┐  │
│ 30V        R₂=3Ω       │ C │  │
│  -        ───/\/\/───  │4μF│  │
│           │         │  └─┬─┘  │
●───────────┴─────────┴────┴────●
```

### Solución

#### **Condiciones Iniciales**
$$v_C(0^+) = v_C(0^-) = 0\text{ V}$$

#### **Valor Final**
En estado estacionario, iC = 0, C es circuito abierto.
R₂ no tiene corriente (está en serie con C abierto):
$$v_C(\infty) = V_s \times \frac{R_2}{R_1 + R_2} = 30 \times \frac{3}{6+3} = 10\text{ V}$$

¡Espera! Si R₂ está en paralelo con C:
$$v_C(\infty) = 30 \times \frac{R_2 \| \infty}{R_1 + (R_2 \| \infty)} = 30 \times \frac{3}{6+3} = 10\text{ V}$$

Pero si no hay corriente por R₂ (C abierto), todo el voltaje cae en R₁... Revisemos la topología.

Con C = circuito abierto, la corriente fluye solo por R₁, pero R₂ está en paralelo con C, así que:
$$v_C(\infty) = V_s - I \times R_1$$

Con C abierto, no hay corriente: I = 0? No, porque R₂ está en paralelo:
$$I = \frac{30}{R_1 + R_2} = \frac{30}{6+3} = 3.33\text{ A}$$ (si R₂ y R₁ en serie)

La corriente va por R₁ → R₂ → regresa. Entonces:
$$v_C(\infty) = I \times R_2 = 3.33 \times 3 = 10\text{ V}$$

#### **Constante de Tiempo**
Resistencia equivalente vista por C (fuente desactivada):
$$R_{eq} = R_1 \| R_2 = \frac{6 \times 3}{6 + 3} = 2\text{ Ω}$$

$$\tau = R_{eq} \times C = 2 \times 4 \times 10^{-6} = 8\text{ μs}$$

#### **Solución**
$$v_C(t) = 10(1 - e^{-t/8\mu s})\text{ V}$$
$$v_C(t) = 10(1 - e^{-125000t})\text{ V}$$

### Respuesta
$$\boxed{v_C(t) = 10(1 - e^{-125000t})\text{ V para } t > 0}$$

---

## Tabla de Referencia Rápida

| Paso | Acción |
|------|--------|
| 1 | Encontrar x(0⁺) por continuidad |
| 2 | Encontrar x(∞) analizando DC: C=abierto, L=corto |
| 3 | Calcular τ = RC o L/R con Req vista por C o L |
| 4 | x(t) = x(∞) + [x(0⁺) - x(∞)]e^(-t/τ) |

## Casos Especiales

| Caso | x(0⁺) | x(∞) | Solución |
|------|-------|------|----------|
| Carga desde 0 | 0 | xf | xf(1 - e^(-t/τ)) |
| Descarga completa | x₀ | 0 | x₀e^(-t/τ) |
| Entre dos valores | x₀ | xf | xf + (x₀-xf)e^(-t/τ) |

## Errores Comunes
1. Usar mal la continuidad: es vC o iL, no cualquier variable
2. Calcular τ con R incorrecta (debe ser la vista por C o L)
3. Confundir respuesta natural con respuesta forzada
4. No verificar los casos límite t = 0 y t = ∞
