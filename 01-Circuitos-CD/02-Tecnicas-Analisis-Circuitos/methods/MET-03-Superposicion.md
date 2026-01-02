# MET-03: Método de Superposición

## Descripción del Método

El **Principio de Superposición** establece que en un circuito lineal con múltiples fuentes independientes, la respuesta (voltaje o corriente) en cualquier elemento es la suma algebraica de las respuestas causadas por cada fuente actuando sola.

### Requisitos
- El circuito debe ser **lineal** (componentes lineales: R, L, C)
- Solo aplica a **fuentes independientes**
- Las fuentes dependientes permanecen activas

### Concepto Clave
$$\text{Respuesta Total} = \sum_{i=1}^{n} \text{Respuesta debido a fuente } i$$

---

## Pasos del Método

### Paso 1: Contar las Fuentes Independientes
- Identificar todas las fuentes de voltaje independientes
- Identificar todas las fuentes de corriente independientes

### Paso 2: Analizar con Una Fuente a la Vez
Para cada fuente:
- **Desactivar** las demás fuentes:
  - Fuente de voltaje → Cortocircuito (V = 0)
  - Fuente de corriente → Circuito abierto (I = 0)
- Calcular la respuesta parcial

### Paso 3: Sumar las Contribuciones
$$V_{total} = V_1 + V_2 + V_3 + \cdots$$
$$I_{total} = I_1 + I_2 + I_3 + \cdots$$

**Nota:** Los signos dependen de la dirección de cada contribución.

---

## Visualización del Método

```
Circuito Original          Contribución Fuente 1    Contribución Fuente 2
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│  Vs₁    R    Vs₂│       │  Vs₁    R   ─●─ │       │  ─●─    R    Vs₂│
│   ○─────/\/\/─○ │   =   │   ○─────/\/\/─○ │   +   │   ○─────/\/\/─○ │
│   │           │ │       │   │           │ │       │   │           │ │
│  ─┴─    Is   ─┴─│       │  ─┴─    ○    ─┴─│       │  ─┴─    ○    ─┴─│
│  GND         GND│       │  GND    ↑    GND│       │  GND    ↑    GND│
└─────────────────┘       └──── abierto ────┘       └──── abierto ────┘

Desactivar:
- Fuente de voltaje → Cortocircuito (cable)
- Fuente de corriente → Circuito abierto (eliminar)
```

---

## Ejemplo Clásico 1: Dos Fuentes de Voltaje

### Enunciado
Usando superposición, encuentre la corriente I a través de R₂.

### Diagrama Original
```
         R₁=4Ω            R₃=3Ω
    ●────/\/\/────●────/\/\/────●
    │             │             │
  + │           ┌─┴─┐           │ +
 12V│           │R₂ │           │6V
    │           │6Ω │           │
  - │        I↓ └─┬─┘           │ -
    │             │             │
    └─────────────●─────────────┘
                 GND
```

### Solución Paso a Paso

#### **Contribución de la Fuente de 12V (desactivar 6V)**

```
         R₁=4Ω            R₃=3Ω
    ●────/\/\/────●────/\/\/────●
    │             │             │
  + │           ┌─┴─┐           │
 12V│           │R₂ │           ●─── Cortocircuito
    │           │6Ω │           │
  - │       I₁↓ └─┬─┘           │
    │             │             │
    └─────────────●─────────────┘
```

**Análisis:**
R₂ y R₃ están en paralelo:
$$R_{23} = \frac{R_2 \times R_3}{R_2 + R_3} = \frac{6 \times 3}{6 + 3} = \frac{18}{9} = 2\text{ Ω}$$

Corriente total desde la fuente:
$$I_T = \frac{12}{R_1 + R_{23}} = \frac{12}{4 + 2} = 2\text{ A}$$

Usando divisor de corriente para I₁:
$$I_1 = I_T \times \frac{R_3}{R_2 + R_3} = 2 \times \frac{3}{6 + 3} = 2 \times \frac{1}{3} = 0.667\text{ A}$$

Dirección: hacia abajo (↓)

#### **Contribución de la Fuente de 6V (desactivar 12V)**

```
         R₁=4Ω            R₃=3Ω
    ●────/\/\/────●────/\/\/────●
    │             │             │
    │           ┌─┴─┐           │ +
●───●           │R₂ │           │6V
Cortocircuito   │6Ω │           │
    │       I₂↑ └─┬─┘           │ -
    │             │             │
    └─────────────●─────────────┘
```

**Análisis:**
R₁ y R₂ están en paralelo (vistos desde la fuente de 6V):
$$R_{12} = \frac{R_1 \times R_2}{R_1 + R_2} = \frac{4 \times 6}{4 + 6} = \frac{24}{10} = 2.4\text{ Ω}$$

Corriente total desde la fuente de 6V:
$$I_T = \frac{6}{R_3 + R_{12}} = \frac{6}{3 + 2.4} = \frac{6}{5.4} = 1.111\text{ A}$$

Usando divisor de corriente para I₂:
$$I_2 = I_T \times \frac{R_1}{R_1 + R_2} = 1.111 \times \frac{4}{4 + 6} = 1.111 \times 0.4 = 0.444\text{ A}$$

Dirección: hacia arriba (↑), opuesta a I₁

#### **Suma de Contribuciones**

$$I_{total} = I_1 - I_2 = 0.667 - 0.444 = 0.223\text{ A}$$

(Restamos porque van en direcciones opuestas)

### Respuesta
$$\boxed{I = 0.223\text{ A} \text{ (hacia abajo)}}$$

### Explicación de la Respuesta
La corriente resultante (0.223 A hacia abajo) es menor que cada contribución individual porque las fuentes "compiten" por establecer corriente en R₂. La fuente de 12V domina ligeramente, resultando en corriente neta hacia abajo. Este es el poder de la superposición: permite analizar el efecto de cada fuente por separado.

---

## Ejemplo Clásico 2: Fuente de Voltaje y Fuente de Corriente

### Enunciado
Calcule Vₓ usando superposición.

### Diagrama Original
```
         R₁=2kΩ           R₂=4kΩ
    ●────/\/\/────●───────/\/\/────●
    │             │                │
  + │           ┌─┴─┐              │
 10V│      Vₓ   │R₃ │            ┌─┴─┐
    │    +  -   │2kΩ│            │Is │
  - │           └─┬─┘            │3mA│
    │             │              └─┬─┘
    └─────────────●────────────────┘
                 GND
```

### Solución

#### **Contribución de la Fuente de 10V (Is = 0, abierto)**

```
         R₁=2kΩ           R₂=4kΩ
    ●────/\/\/────●───────/\/\/────●
    │             │                │
  + │           ┌─┴─┐              │
 10V│    Vₓ₁    │R₃ │              ○ Circuito abierto
    │           │2kΩ│              
  - │           └─┬─┘              
    │             │                
    └─────────────●────────────────┘
```

R₂ no conduce corriente (circuito abierto), así que es un divisor simple:
$$V_{x1} = 10 \times \frac{R_3}{R_1 + R_3} = 10 \times \frac{2k}{2k + 2k} = 10 \times \frac{1}{2} = 5\text{ V}$$

#### **Contribución de la Fuente de 3mA (10V cortocircuito)**

```
         R₁=2kΩ           R₂=4kΩ
    ●────/\/\/────●───────/\/\/────●
    │             │                │
    ●─────────────│              ┌─┴─┐
 Cortocircuito    │ Vₓ₂          │Is │
                ┌─┴─┐            │3mA│
                │R₃ │            └─┬─┘
                │2kΩ│              │
                └─┬─┘              │
                  │                │
    ●─────────────●────────────────┘
```

Ahora R₁ está en paralelo con R₃ (ambos conectados entre el mismo nodo y tierra):
$$R_{13} = \frac{R_1 \times R_3}{R_1 + R_3} = \frac{2k \times 2k}{2k + 2k} = \frac{4M}{4k} = 1\text{ kΩ}$$

La fuente de corriente ve R₁₃ en serie con R₂:
$$R_{eq} = R_{13} + R_2 = 1k + 4k = 5\text{ kΩ}$$

Pero queremos Vₓ₂ a través de R₃ (o R₁₃):

Voltaje en el nodo:
$$V_{nodo} = I_s \times R_{13} = 3\text{mA} \times 1\text{kΩ} = 3\text{ V}$$

Por tanto:
$$V_{x2} = 3\text{ V}$$

Pero verificamos la dirección: la corriente de 3mA fluye hacia el nodo, creando voltaje + arriba.

#### **Suma de Contribuciones**

Ambas contribuciones tienen la misma polaridad (+ arriba):
$$V_x = V_{x1} + V_{x2} = 5 + 3 = 8\text{ V}$$

### Respuesta
$$\boxed{V_x = 8\text{ V}}$$

### Explicación de la Respuesta
Ambas fuentes contribuyen positivamente al voltaje Vₓ. La fuente de 10V aporta 5V a través del divisor de voltaje. La fuente de 3mA aporta 3V adicionales al inyectar corriente en el nodo. Las contribuciones se suman porque ambas "empujan" en la misma dirección.

---

## Ejemplo Clásico 3: Tres Fuentes

### Enunciado
Encuentre la corriente I usando superposición.

### Diagrama
```
         R₁=6Ω       R₂=3Ω
    ●────/\/\/───●───/\/\/───●
    │            │           │
  + │          ┌─┴─┐       + │
 18V│     I    │R₃ │        │9V
    │    ↓     │6Ω │         │
  - │          └─┬─┘       - │
    │            ├───────────┘
    │          ┌─┴─┐
    │          │Is │
    │          │2A │
    │          └─┬─┘
    └────────────┘
```

### Solución

#### **Contribución de 18V (Is=0, 9V cortocircuito)**

R₃ en paralelo con R₂:
$$R_{23} = \frac{6 \times 3}{6 + 3} = 2\text{ Ω}$$

$$I_T = \frac{18}{6 + 2} = 2.25\text{ A}$$

Corriente por R₃ (divisor):
$$I_1 = 2.25 \times \frac{3}{6+3} = 0.75\text{ A (abajo)}$$

#### **Contribución de 9V (Is=0, 18V cortocircuito)**

R₃ en paralelo con R₁:
$$R_{13} = \frac{6 \times 6}{6 + 6} = 3\text{ Ω}$$

$$I_T = \frac{9}{3 + 3} = 1.5\text{ A}$$

Corriente por R₃:
$$I_2 = 1.5 \times \frac{6}{6+6} = 0.75\text{ A (arriba)}$$

#### **Contribución de 2A (18V y 9V cortocircuito)**

R₁ en paralelo con R₂: $R_{12} = \frac{6 \times 3}{9} = 2$ Ω

Esta combinación en paralelo con R₃ = 6Ω:
$$R_{eq} = \frac{2 \times 6}{2 + 6} = 1.5\text{ Ω}$$

Corriente por R₃ (divisor de corriente):
$$I_3 = 2 \times \frac{R_{12}}{R_{12} + R_3} = 2 \times \frac{2}{2+6} = 0.5\text{ A (arriba)}$$

#### **Suma Total**

$$I = I_1 - I_2 - I_3 = 0.75 - 0.75 - 0.5 = -0.5\text{ A}$$

### Respuesta
$$\boxed{I = 0.5\text{ A (hacia arriba)}}$$

### Explicación de la Respuesta
El signo negativo indica que la corriente fluye hacia arriba, opuesto a la referencia original. Las fuentes de 9V y 2A combinadas dominan sobre la fuente de 18V para determinar la dirección final de la corriente.

---

## Resumen del Método

| Fuente | Para desactivar |
|--------|-----------------|
| Voltaje independiente | Cortocircuito (V = 0) |
| Corriente independiente | Circuito abierto (I = 0) |
| Fuente dependiente | **NO desactivar** (permanece activa) |

## Ventajas y Desventajas

| Ventajas | Desventajas |
|----------|-------------|
| Conceptualmente simple | Más cálculos si hay muchas fuentes |
| Útil para análisis de sensibilidad | Solo para circuitos lineales |
| Permite entender contribuciones | No funciona para potencia (P ≠ P₁ + P₂) |

## Errores Comunes
1. Desactivar fuentes dependientes (¡NO se desactivan!)
2. Olvidar que cortocircuito ≠ eliminar el elemento
3. Sumar contribuciones con signos incorrectos
4. Aplicar a circuitos no lineales (diodos, transistores)
