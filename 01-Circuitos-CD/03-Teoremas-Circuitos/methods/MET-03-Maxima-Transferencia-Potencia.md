# MET-03: Método de Máxima Transferencia de Potencia

## Descripción del Método

El **[Teorema de](../../../glossary.md#norton) Máxima Transferencia de Potencia** establece que una [carga](../../../glossary.md#carga) recibe máxima potencia de una fuente cuando la [resistencia](../../../glossary.md#resistencia) de carga iguala a la resistencia interna de la fuente (resistencia de [Thévenin](../../../glossary.md#thevenin)).

$$R_L = R_{th} \Rightarrow P_{max}$$

### Contexto
Este teorema es fundamental en:
- Diseño de sistemas de comunicaciones
- Adaptación de impedancias (matching)
- Diseño de amplificadores de audio
- Transferencia de energía en RF

---

## Fórmulas Fundamentales

### Condición de Máxima Transferencia
$$\boxed{R_L = R_{th}}$$

### Potencia Máxima
$$\boxed{P_{max} = \frac{V_{th}^2}{4R_{th}}}$$

### Eficiencia en Máxima Transferencia
$$\eta = \frac{P_L}{P_{total}} = \frac{P_L}{P_L + P_{Rth}} = 50\%$$

---

## Demostración Matemática

### Potencia en la Carga
Dado el [circuito](../../../glossary.md#circuito) de Thévenin con carga RL:

$$I = \frac{V_{th}}{R_{th} + R_L}$$

$$P_L = I^2 R_L = \frac{V_{th}^2 \cdot R_L}{(R_{th} + R_L)^2}$$

### Encontrar el Máximo
Derivar PL respecto a RL e igualar a cero:

$$\frac{dP_L}{dR_L} = V_{th}^2 \cdot \frac{(R_{th} + R_L)^2 - R_L \cdot 2(R_{th} + R_L)}{(R_{th} + R_L)^4} = 0$$

$$\frac{(R_{th} + R_L) - 2R_L}{(R_{th} + R_L)^3} = 0$$

$$R_{th} + R_L - 2R_L = 0$$

$$\boxed{R_L = R_{th}}$$

### Potencia Máxima
Sustituyendo RL = Rth:

$$P_{max} = \frac{V_{th}^2 \cdot R_{th}}{(R_{th} + R_{th})^2} = \frac{V_{th}^2 \cdot R_{th}}{4R_{th}^2} = \frac{V_{th}^2}{4R_{th}}$$

---

## Pasos del Método

### Paso 1: Obtener el Equivalente de Thévenin
- Calcular Vth (voltaje en circuito abierto)
- Calcular Rth (resistencia equivalente)

### Paso 2: Determinar RL para Máxima Potencia
$$R_L = R_{th}$$

### Paso 3: Calcular la Potencia Máxima
$$P_{max} = \frac{V_{th}^2}{4R_{th}}$$

### Paso 4: Calcular Corriente y Voltaje en la Carga
$$I_{max} = \frac{V_{th}}{2R_{th}}$$
$$V_{L,max} = \frac{V_{th}}{2}$$

---

## Ejemplo Clásico 1: Circuito Básico

### Enunciado
Determine el valor de RL para máxima transferencia de potencia y calcule dicha potencia máxima.

### Diagrama
```
            R₁=8Ω           R₂=4Ω
    ●────────/\/\/────●────/\/\/────●
    │                 │             │
  + │               ┌─┴─┐         ┌─┴─┐
 48V│               │R₃ │         │RL │
    │               │8Ω │         │ ? │
  - │               └─┬─┘         └─┬─┘
    │                 │             │
    └─────────────────●─────────────┘
```

### Solución Paso a Paso

#### **Paso 1: Calcular Vth (circuito abierto, sin RL)**

Sin RL, no hay corriente por R₂:
$$I = \frac{48}{R_1 + R_3} = \frac{48}{8 + 8} = 3\text{ A}$$

$$V_{th} = I \times R_3 = 3 \times 8 = 24\text{ V}$$

#### **Paso 2: Calcular Rth (desactivar fuente)**

```
            R₁=8Ω           R₂=4Ω
    ●────────/\/\/────●────/\/\/────●
    │                 │             │
    │               ┌─┴─┐           │
●───●               │R₃ │        Rth│
Cortocircuito       │8Ω │        ←  │
    │               └─┬─┘           │
    │                 │             │
    └─────────────────●─────────────┘
```

$$R_{13} = R_1 \| R_3 = \frac{8 \times 8}{8 + 8} = 4\text{ Ω}$$

$$R_{th} = R_{13} + R_2 = 4 + 4 = 8\text{ Ω}$$

#### **Paso 3: RL para máxima potencia**
$$R_L = R_{th} = 8\text{ Ω}$$

#### **Paso 4: Potencia máxima**
$$P_{max} = \frac{V_{th}^2}{4R_{th}} = \frac{24^2}{4 \times 8} = \frac{576}{32} = 18\text{ W}$$

#### **Verificación**
$$I = \frac{V_{th}}{R_{th} + R_L} = \frac{24}{8 + 8} = 1.5\text{ A}$$
$$P_L = I^2 R_L = (1.5)^2 \times 8 = 2.25 \times 8 = 18\text{ W}$$ ✓

### Respuesta
$$\boxed{R_L = 8\text{ Ω}, \quad P_{max} = 18\text{ W}}$$

### Explicación de la Respuesta
Con RL = 8 Ω (igual a Rth), la carga recibe exactamente la mitad del [voltaje](../../../glossary.md#voltaje) de la fuente de Thévenin (12 V de 24 V). La potencia de 18 W es el máximo posible; cualquier otro valor de RL resultaría en menor potencia transferida. La eficiencia es del 50% porque la otra mitad de la potencia (18 W) se disipa en Rth.

---

## Ejemplo Clásico 2: Análisis de Potencia vs RL

### Enunciado
Para el circuito con Vth = 20 V y Rth = 5 Ω, calcule y grafique la potencia en la carga para RL = 1, 2, 5, 10 y 20 Ω.

### Solución

| RL (Ω) | I (A) | PL (W) | % de Pmax |
|--------|-------|--------|-----------|
| 1 | 20/(5+1) = 3.33 | 3.33² × 1 = 11.1 | 55.5% |
| 2 | 20/(5+2) = 2.86 | 2.86² × 2 = 16.3 | 81.5% |
| 5 | 20/(5+5) = 2.00 | 2.00² × 5 = 20.0 | 100% ✓ |
| 10 | 20/(5+10) = 1.33 | 1.33² × 10 = 17.8 | 89% |
| 20 | 20/(5+20) = 0.80 | 0.80² × 20 = 12.8 | 64% |

### Gráfica de Potencia vs RL

```
P (W)
  │
20├─────────────●─────────── Máximo en RL = Rth
  │           ╱   ╲
18├─────────╱───────╲────────
  │       ╱           ╲
16├─────●───────────────●────
  │   ╱                   ╲
14├─╱───────────────────────╲
  │╱                          ╲
12├●────────────────────────────●
  │
10├
  └──┬───┬───┬───┬───┬───┬───┬──► RL (Ω)
     1   2   5   10  15  20
              ↑
           RL = Rth
```

### Respuesta
$$\boxed{P_{max} = 20\text{ W cuando } R_L = R_{th} = 5\text{ Ω}}$$

### Explicación de la Respuesta
La gráfica muestra una curva con un pico claro en RL = Rth = 5 Ω. A medida que RL se aleja de 5 Ω (ya sea hacia arriba o hacia abajo), la potencia disminuye. Este comportamiento es fundamental en diseño de sistemas donde se busca maximizar la potencia entregada a una carga.

---

## Ejemplo Clásico 3: Eficiencia vs Máxima Potencia

### Enunciado
Un sistema tiene Vth = 100 V y Rth = 50 Ω. Compare:
a) Potencia y eficiencia cuando RL = 50 Ω (máxima potencia)
b) Potencia y eficiencia cuando RL = 200 Ω (alta eficiencia)

### Solución

#### **Caso a: RL = 50 Ω (Máxima potencia)**

$$I = \frac{100}{50 + 50} = 1\text{ A}$$

$$P_L = I^2 R_L = 1^2 \times 50 = 50\text{ W}$$

$$P_{Rth} = I^2 R_{th} = 1^2 \times 50 = 50\text{ W}$$

$$P_{total} = P_L + P_{Rth} = 100\text{ W}$$

$$\eta = \frac{P_L}{P_{total}} = \frac{50}{100} = 50\%$$

#### **Caso b: RL = 200 Ω (Alta eficiencia)**

$$I = \frac{100}{50 + 200} = 0.4\text{ A}$$

$$P_L = 0.4^2 \times 200 = 32\text{ W}$$

$$P_{Rth} = 0.4^2 \times 50 = 8\text{ W}$$

$$P_{total} = 32 + 8 = 40\text{ W}$$

$$\eta = \frac{32}{40} = 80\%$$

### Tabla Comparativa

| Parámetro | RL = 50 Ω | RL = 200 Ω |
|-----------|-----------|------------|
| Corriente | 1 A | 0.4 A |
| Potencia en carga | 50 W | 32 W |
| Potencia en Rth | 50 W | 8 W |
| Eficiencia | 50% | 80% |

### Respuesta
$$\boxed{\text{Máxima potencia: } P_L = 50\text{ W, } \eta = 50\%}$$
$$\boxed{\text{Alta eficiencia: } P_L = 32\text{ W, } \eta = 80\%}$$

### Explicación de la Respuesta
Existe un **trade-off** fundamental entre máxima potencia y máxima eficiencia:
- Para **máxima potencia** (RL = Rth): Eficiencia = 50% solamente
- Para **alta eficiencia** (RL >> Rth): Potencia transferida disminuye

En aplicaciones de:
- **Comunicaciones/Audio:** Se prioriza máxima potencia (matching de impedancia)
- **Transmisión de energía:** Se prioriza eficiencia (RL >> Rth)

---

## Fórmula General de Eficiencia

$$\eta = \frac{R_L}{R_{th} + R_L} = \frac{1}{1 + \frac{R_{th}}{R_L}}$$

| RL/Rth | Eficiencia | Potencia relativa |
|--------|------------|------------------|
| 0.5 | 33% | 89% de Pmax |
| 1.0 | 50% | 100% de Pmax |
| 2.0 | 67% | 89% de Pmax |
| 4.0 | 80% | 64% de Pmax |
| 10 | 91% | 33% de Pmax |

---

## Aplicaciones Prácticas

### 1. Sistemas de Audio
- Amplificadores diseñados para Zout = Zaltavoz
- Típicamente 4 Ω u 8 Ω

### 2. Comunicaciones RF
- Líneas de transmisión de 50 Ω o 75 Ω
- Antenas adaptadas a la [impedancia](../../../glossary.md#impedancia) del transmisor

### 3. Circuitos de Medición
- No siempre se busca máxima potencia
- Se prefiere alta impedancia de entrada (mínima carga)

### 4. Fuentes de Alimentación
- Se diseña Rth << RL para máxima eficiencia
- Regulación: V constante ante variaciones de carga

---

## Resumen

| Concepto | Fórmula |
|----------|---------|
| Condición máxima potencia | RL = Rth |
| Potencia máxima | Pmax = Vth²/(4Rth) |
| Corriente en máx. potencia | I = Vth/(2Rth) |
| Voltaje en carga | VL = Vth/2 |
| Eficiencia en máx. potencia | η = 50% |

## Errores Comunes
1. Confundir máxima potencia con máxima eficiencia
2. Olvidar que la condición RL = Rth solo maximiza potencia en RL
3. Aplicar el teorema a circuitos no lineales
4. No considerar que Rth puede incluir pérdidas internas
