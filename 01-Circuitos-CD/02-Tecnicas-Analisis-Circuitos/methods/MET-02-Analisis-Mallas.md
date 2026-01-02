# MET-02: Método de Análisis de Mallas

## Descripción del Método

El **Análisis de Mallas** es una técnica sistemática que aplica la Ley de Voltajes de Kirchhoff (LVK) para encontrar las corrientes de malla en un circuito planar. Es el dual del análisis nodal.

### Conceptos Clave
- **Malla:** Lazo cerrado que no contiene otros lazos en su interior
- **Corriente de malla:** Corriente hipotética que circula alrededor de una malla
- **Supermalla:** Región formada cuando una fuente de corriente está entre dos mallas

### Ventajas
- Ideal para circuitos con muchos elementos en serie
- Funciona bien con fuentes de voltaje
- Número reducido de ecuaciones para circuitos planares

---

## Pasos del Método

### Paso 1: Verificar que el Circuito sea Planar
- El circuito debe poder dibujarse sin cruces de cables

### Paso 2: Identificar y Numerar las Mallas
- Asignar una corriente de malla a cada "ventana"
- Por convención, todas en sentido horario (o todas antihorario)

### Paso 3: Aplicar LVK a Cada Malla
- Recorrer cada malla en el sentido de su corriente
- Sumar voltajes: $\sum V = 0$
- Usar $V = IR$ para cada resistencia

### Paso 4: Manejar Fuentes de Corriente
- **Fuente en el perímetro:** La corriente de malla es igual a la fuente
- **Fuente entre mallas:** Formar supermalla

### Paso 5: Resolver el Sistema de Ecuaciones

---

## Convención de Signos

```
Recorriendo la Malla 1 (horario):

    ┌────/\/\/─────────────┐
    │  +  R   -            │
    │                      │
  + │                      │ +
   ─┴─   ↻ i₁          R₂ ─┴─
   Vs                      
   ─┬─                    ─┬─
  - │                      │ -
    │                      │
    └──────────────────────┘

LVK: +Vs - i₁R - i₁R₂ = 0 (si i₂ no afecta)

Si hay malla adyacente con i₂:
- Resistencia compartida: V = (i₁ - i₂)R
```

---

## Ejemplo Clásico 1: Dos Mallas Independientes

### Enunciado
Usando análisis de mallas, encuentre las corrientes i₁ e i₂.

### Diagrama
```
         R₁=4Ω           R₂=2Ω
    ●────/\/\/────●────/\/\/────●
    │             │             │
  + │           ┌─┴─┐           │ +
 12V│           │R₃ │           │6V
    │           │6Ω │           │
  - │           └─┬─┘           │ -
    │             │             │
    └──────●──────┴──────●──────┘
           
    Malla 1 ↻i₁    Malla 2 ↻i₂
```

### Solución Paso a Paso

**Paso 1: Identificar mallas**
- Malla 1: Izquierda con fuente de 12V
- Malla 2: Derecha con fuente de 6V
- R₃ es compartida por ambas mallas

**Paso 2: LVK en Malla 1 (recorrido horario)**
$$+12 - i_1 R_1 - (i_1 - i_2)R_3 = 0$$
$$12 - 4i_1 - 6(i_1 - i_2) = 0$$
$$12 - 4i_1 - 6i_1 + 6i_2 = 0$$
$$12 - 10i_1 + 6i_2 = 0$$
$$10i_1 - 6i_2 = 12 \quad \text{...(Ec. 1)}$$

**Paso 3: LVK en Malla 2 (recorrido horario)**
$$-(i_2 - i_1)R_3 - i_2 R_2 - 6 = 0$$
$$-6(i_2 - i_1) - 2i_2 - 6 = 0$$
$$-6i_2 + 6i_1 - 2i_2 - 6 = 0$$
$$6i_1 - 8i_2 = 6$$
$$3i_1 - 4i_2 = 3 \quad \text{...(Ec. 2)}$$

**Paso 4: Resolver el sistema**
De Ec. 2: $i_1 = (3 + 4i_2)/3$

Sustituyendo en Ec. 1:
$$10 \cdot \frac{3 + 4i_2}{3} - 6i_2 = 12$$
$$\frac{30 + 40i_2}{3} - 6i_2 = 12$$
$$30 + 40i_2 - 18i_2 = 36$$
$$22i_2 = 6$$
$$i_2 = \frac{6}{22} = \frac{3}{11} \approx 0.273\text{ A}$$

$$i_1 = \frac{3 + 4(3/11)}{3} = \frac{3 + 12/11}{3} = \frac{33/11 + 12/11}{3} = \frac{45/11}{3} = \frac{45}{33} = \frac{15}{11} \approx 1.364\text{ A}$$

**Paso 5: Verificación**
Corriente en R₃: $i_{R3} = i_1 - i_2 = 15/11 - 3/11 = 12/11 = 1.09$ A

LVK Malla 1: $12 - (15/11)(4) - (12/11)(6) = 12 - 60/11 - 72/11 = 12 - 132/11 = 12 - 12 = 0$ ✓

### Respuesta
$$\boxed{i_1 = 1.364\text{ A}, \quad i_2 = 0.273\text{ A}}$$

### Explicación de la Respuesta
Ambas corrientes son positivas, lo que significa que fluyen en el sentido horario asumido. i₁ es mayor porque su fuente (12V) es más grande. La corriente real por R₃ es la diferencia (i₁ - i₂) = 1.09 A, fluyendo hacia abajo (de malla 1 a malla 2).

---

## Ejemplo Clásico 2: Análisis de Mallas con Supermalla

### Enunciado
Encuentre las corrientes de malla usando el método de supermalla.

### Diagrama
```
            R₁=1Ω           R₂=2Ω
    ●────────/\/\/────●────/\/\/────●
    │                 │             │
  + │               ┌─┴─┐           │
 10V│               │4A │ Is        │
    │               └─┬─┘           │
  - │                 │             │
    │        R₃=3Ω    │    R₄=4Ω    │
    └────────/\/\/────●────/\/\/────┘
    
    Malla 1 ↻i₁         Malla 2 ↻i₂
    
    ╔═══════════════════════════════╗
    ║        SUPERMALLA             ║
    ╚═══════════════════════════════╝
```

### Solución Paso a Paso

**Paso 1: Identificar la fuente de corriente**
- Is = 4A está entre Malla 1 y Malla 2
- Debemos formar una supermalla

**Paso 2: Ecuación de restricción (por la fuente de corriente)**
La corriente de 4A fluye de Malla 1 a Malla 2:
$$i_2 - i_1 = 4 \quad \text{...(Ec. 1)}$$

**Paso 3: LVK en la Supermalla**
Recorremos el perímetro exterior evitando la fuente de corriente:
$$+10 - i_1 R_1 - i_2 R_2 - i_2 R_4 - i_1 R_3 = 0$$
$$10 - i_1(1) - i_2(2) - i_2(4) - i_1(3) = 0$$
$$10 - i_1 - 2i_2 - 4i_2 - 3i_1 = 0$$
$$10 - 4i_1 - 6i_2 = 0$$
$$4i_1 + 6i_2 = 10$$
$$2i_1 + 3i_2 = 5 \quad \text{...(Ec. 2)}$$

**Paso 4: Resolver el sistema**
De Ec. 1: $i_1 = i_2 - 4$

Sustituyendo en Ec. 2:
$$2(i_2 - 4) + 3i_2 = 5$$
$$2i_2 - 8 + 3i_2 = 5$$
$$5i_2 = 13$$
$$i_2 = \frac{13}{5} = 2.6\text{ A}$$

$$i_1 = i_2 - 4 = 2.6 - 4 = -1.4\text{ A}$$

**Paso 5: Interpretar resultados**
- i₂ = 2.6 A (sentido horario) ✓
- i₁ = -1.4 A (sentido ANTIHORARIO, opuesto al asumido)

**Verificación:**
Corriente por la fuente: $i_2 - i_1 = 2.6 - (-1.4) = 4$ A ✓

### Respuesta
$$\boxed{i_1 = -1.4\text{ A (antihorario)}, \quad i_2 = 2.6\text{ A (horario)}}$$

### Explicación de la Respuesta
La corriente i₁ negativa indica que fluye en sentido opuesto al asumido (antihorario). Esto tiene sentido porque la fuente de corriente de 4A "empuja" corriente desde la malla 1 hacia la malla 2, dominando sobre la fuente de voltaje de 10V. La supermalla permite escribir una ecuación LVK sin incluir la fuente de corriente (cuyo voltaje es desconocido).

---

## Ejemplo Clásico 3: Tres Mallas

### Enunciado
Determine las tres corrientes de malla.

### Diagrama
```
            R₁=2Ω           R₂=4Ω
    ●────────/\/\/────●────/\/\/────●────●
    │                 │             │    │
  + │               ┌─┴─┐         ┌─┴─┐  │
 24V│               │R₃ │         │R₅ │  │
    │               │2Ω │         │2Ω │  │
  - │               └─┬─┘         └─┬─┘  │
    │                 │             │    │
    │        R₄=4Ω    │    R₆=4Ω    │  + │
    └────────/\/\/────●────/\/\/────┘ 12V│
                                      -  │
    Malla 1 ↻i₁    Malla 2 ↻i₂    Malla 3 ↻i₃
```

### Solución

**LVK Malla 1:**
$$24 - 2i_1 - 2(i_1 - i_2) - 4i_1 = 0$$
$$24 - 2i_1 - 2i_1 + 2i_2 - 4i_1 = 0$$
$$24 - 8i_1 + 2i_2 = 0$$
$$8i_1 - 2i_2 = 24$$
$$4i_1 - i_2 = 12 \quad \text{...(Ec. 1)}$$

**LVK Malla 2:**
$$-2(i_2 - i_1) - 4i_2 - 4(i_2 - i_3) - 2(i_2 - i_3) = 0$$
$$-2i_2 + 2i_1 - 4i_2 - 4i_2 + 4i_3 - 2i_2 + 2i_3 = 0$$
$$2i_1 - 12i_2 + 6i_3 = 0$$
$$i_1 - 6i_2 + 3i_3 = 0 \quad \text{...(Ec. 2)}$$

**LVK Malla 3:**
$$-4(i_3 - i_2) - 2(i_3 - i_2) - 12 = 0$$
$$-4i_3 + 4i_2 - 2i_3 + 2i_2 - 12 = 0$$
$$6i_2 - 6i_3 = 12$$
$$i_2 - i_3 = 2 \quad \text{...(Ec. 3)}$$

**Resolver sistema:**
De Ec. 3: $i_2 = i_3 + 2$

Sustituyendo en Ec. 2:
$$i_1 - 6(i_3 + 2) + 3i_3 = 0$$
$$i_1 - 6i_3 - 12 + 3i_3 = 0$$
$$i_1 = 3i_3 + 12 \quad \text{...(Ec. 4)}$$

Sustituyendo Ec. 3 y Ec. 4 en Ec. 1:
$$4(3i_3 + 12) - (i_3 + 2) = 12$$
$$12i_3 + 48 - i_3 - 2 = 12$$
$$11i_3 = -34$$
$$i_3 = -\frac{34}{11} \approx -3.09\text{ A}$$

$$i_2 = -\frac{34}{11} + 2 = \frac{-34 + 22}{11} = -\frac{12}{11} \approx -1.09\text{ A}$$

$$i_1 = 3(-\frac{34}{11}) + 12 = \frac{-102 + 132}{11} = \frac{30}{11} \approx 2.73\text{ A}$$

### Respuesta
$$\boxed{i_1 = 2.73\text{ A}, \quad i_2 = -1.09\text{ A}, \quad i_3 = -3.09\text{ A}}$$

### Explicación de la Respuesta
Solo i₁ es positiva (fluye en sentido horario). i₂ e i₃ son negativas, indicando que fluyen en sentido antihorario. La fuente de 24V domina en la malla 1, mientras que la fuente de 12V en la malla 3 tiene polaridad opuesta al sentido de i₃ asumido, causando el flujo inverso.

---

## Forma Matricial del Análisis de Mallas

Para circuitos con solo fuentes de voltaje independientes:

$$\mathbf{R} \cdot \mathbf{I} = \mathbf{V}$$

$$\begin{bmatrix} R_{11} & -R_{12} & -R_{13} \\ -R_{21} & R_{22} & -R_{23} \\ -R_{31} & -R_{32} & R_{33} \end{bmatrix} \begin{bmatrix} i_1 \\ i_2 \\ i_3 \end{bmatrix} = \begin{bmatrix} V_1 \\ V_2 \\ V_3 \end{bmatrix}$$

Donde:
- $R_{ii}$ = Suma de resistencias en la malla i
- $R_{ij}$ = Resistencia compartida entre mallas i y j (signo negativo)
- $V_i$ = Suma algebraica de fuentes de voltaje en malla i

---

## Comparación: Nodal vs Mallas

| Aspecto | Análisis Nodal | Análisis de Mallas |
|---------|---------------|-------------------|
| Variable | Voltajes (V) | Corrientes (A) |
| Ecuaciones | n - 1 | m (número de mallas) |
| Mejor para | Fuentes de corriente | Fuentes de voltaje |
| Circuitos ideales | Paralelo dominante | Serie dominante |
| Caso especial | Supernodo | Supermalla |

## Errores Comunes
1. Sentido inconsistente de las corrientes de malla
2. Olvidar que la resistencia compartida usa (i₁ - i₂)
3. Signos incorrectos en las fuentes de voltaje
4. No identificar correctamente las fuentes de corriente para supermallas
