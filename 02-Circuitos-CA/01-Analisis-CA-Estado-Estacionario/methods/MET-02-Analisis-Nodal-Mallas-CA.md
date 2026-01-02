# MET-02: Análisis Nodal y de Mallas en Circuitos CA

## Descripción del Método

Los métodos de análisis nodal y de mallas se aplican a circuitos CA de la misma manera que en CD, pero usando **fasores** e **impedancias** en lugar de voltajes/corrientes DC y resistencias.

---

## Análisis Nodal en CA

### Ecuación Fundamental
Por LCK en cada nodo:
$$\sum \mathbf{I} = 0$$

Usando admitancias:
$$\mathbf{I} = \mathbf{Y} \cdot \mathbf{V}$$

### Forma Matricial
$$[\mathbf{Y}][\mathbf{V}] = [\mathbf{I}_s]$$

Donde:
- $[\mathbf{Y}]$ = matriz de admitancias (complejas)
- $[\mathbf{V}]$ = vector de voltajes nodales (fasores)
- $[\mathbf{I}_s]$ = vector de corrientes de fuente

---

## Análisis de Mallas en CA

### Ecuación Fundamental
Por LVK en cada malla:
$$\sum \mathbf{V} = 0$$

Usando impedancias:
$$\mathbf{V} = \mathbf{Z} \cdot \mathbf{I}$$

### Forma Matricial
$$[\mathbf{Z}][\mathbf{I}] = [\mathbf{V}_s]$$

Donde:
- $[\mathbf{Z}]$ = matriz de impedancias (complejas)
- $[\mathbf{I}]$ = vector de corrientes de malla (fasores)
- $[\mathbf{V}_s]$ = vector de voltajes de fuente

---

## Pasos del Método Nodal

### Paso 1: Convertir a Dominio Fasorial
- Fuentes → Fasores
- Elementos → Admitancias

### Paso 2: Seleccionar Nodo de Referencia

### Paso 3: Asignar Variables de Voltaje
- Una variable por cada nodo no referencia

### Paso 4: Aplicar LCK en Cada Nodo
- Corrientes salientes = corrientes entrantes
- Expresar en términos de admitancias

### Paso 5: Resolver Sistema de Ecuaciones

### Paso 6: Convertir a Dominio del Tiempo

---

## Pasos del Método de Mallas

### Paso 1: Convertir a Dominio Fasorial
- Fuentes → Fasores
- Elementos → Impedancias

### Paso 2: Asignar Corrientes de Malla
- Sentido horario (convención)

### Paso 3: Aplicar LVK en Cada Malla
- Suma de caídas de voltaje = 0

### Paso 4: Resolver Sistema de Ecuaciones

### Paso 5: Convertir a Dominio del Tiempo

---

## Ejemplo Clásico 1: Análisis Nodal con 2 Fuentes

### Enunciado
Determine V₁ y V₂ en el siguiente circuito donde ω = 4 rad/s.

### Diagrama
```
        10Ω              j8Ω
●───────/\/\/\/──┬───────ΩΩΩΩ───────┬───●
│                │                  │   │
+              ┌─┴─┐              ┌─┴─┐ +
20∠0°V         │-j5│              │10Ω│ 4∠0°A
-              │ Ω │              └─┬─┘ ↓
│              └─┬─┘                │   │
●────────────────┴──────────────────┴───●
                 ⏊ (ref)
```

**Datos:**
- Fuente de voltaje: $\mathbf{V}_s = 20\angle 0°$ V
- Fuente de corriente: $\mathbf{I}_s = 4\angle 0°$ A
- R₁ = 10 Ω, R₂ = 10 Ω
- X_L = 8 Ω (inductor)
- X_C = 5 Ω (capacitor)

### Solución

#### **Paso 1: Admitancias**
$$\mathbf{Y}_{10\Omega} = \frac{1}{10} = 0.1\text{ S}$$
$$\mathbf{Y}_{j8} = \frac{1}{j8} = -j0.125\text{ S}$$
$$\mathbf{Y}_{-j5} = \frac{1}{-j5} = j0.2\text{ S}$$

#### **Paso 2: Ecuaciones nodales**

**Nodo V₁:**
$$\frac{\mathbf{V}_1 - 20\angle 0°}{10} + \frac{\mathbf{V}_1}{-j5} + \frac{\mathbf{V}_1 - \mathbf{V}_2}{j8} = 0$$

Multiplicando:
$$0.1(\mathbf{V}_1 - 20) + j0.2\mathbf{V}_1 + (-j0.125)(\mathbf{V}_1 - \mathbf{V}_2) = 0$$
$$(0.1 + j0.2 - j0.125)\mathbf{V}_1 + j0.125\mathbf{V}_2 = 2$$
$$(0.1 + j0.075)\mathbf{V}_1 + j0.125\mathbf{V}_2 = 2$$ ... (1)

**Nodo V₂:**
$$\frac{\mathbf{V}_2 - \mathbf{V}_1}{j8} + \frac{\mathbf{V}_2}{10} = 4\angle 0°$$
$$(-j0.125)(\mathbf{V}_2 - \mathbf{V}_1) + 0.1\mathbf{V}_2 = 4$$
$$j0.125\mathbf{V}_1 + (0.1 - j0.125)\mathbf{V}_2 = 4$$ ... (2)

#### **Paso 3: Resolver el sistema**

En forma matricial:
$$\begin{bmatrix} 0.1+j0.075 & j0.125 \\ j0.125 & 0.1-j0.125 \end{bmatrix} \begin{bmatrix} \mathbf{V}_1 \\ \mathbf{V}_2 \end{bmatrix} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$$

**Determinante:**
$$\Delta = (0.1+j0.075)(0.1-j0.125) - (j0.125)(j0.125)$$
$$\Delta = 0.01 - j0.0125 + j0.0075 + 0.009375 + 0.015625$$
$$\Delta = 0.035 - j0.005 = 0.0354\angle -8.13°$$

**Solución por Cramer:**
$$\mathbf{V}_1 = \frac{\begin{vmatrix} 2 & j0.125 \\ 4 & 0.1-j0.125 \end{vmatrix}}{\Delta}$$
$$\mathbf{V}_1 = \frac{2(0.1-j0.125) - 4(j0.125)}{\Delta} = \frac{0.2 - j0.25 - j0.5}{\Delta}$$
$$\mathbf{V}_1 = \frac{0.2 - j0.75}{0.0354\angle -8.13°} = \frac{0.776\angle -75°}{0.0354\angle -8.13°}$$
$$\mathbf{V}_1 = 21.92\angle -66.87°\text{ V}$$

$$\mathbf{V}_2 = \frac{\begin{vmatrix} 0.1+j0.075 & 2 \\ j0.125 & 4 \end{vmatrix}}{\Delta}$$
$$\mathbf{V}_2 = \frac{4(0.1+j0.075) - 2(j0.125)}{\Delta} = \frac{0.4 + j0.3 - j0.25}{\Delta}$$
$$\mathbf{V}_2 = \frac{0.4 + j0.05}{0.0354\angle -8.13°} = \frac{0.403\angle 7.13°}{0.0354\angle -8.13°}$$
$$\mathbf{V}_2 = 11.38\angle 15.26°\text{ V}$$

### Respuesta
$$\boxed{\mathbf{V}_1 = 21.92\angle -66.87°\text{ V}}$$
$$\boxed{\mathbf{V}_2 = 11.38\angle 15.26°\text{ V}}$$

### Dominio del tiempo (ω = 4 rad/s)
$$v_1(t) = 21.92\cos(4t - 66.87°)\text{ V}$$
$$v_2(t) = 11.38\cos(4t + 15.26°)\text{ V}$$

---

## Ejemplo Clásico 2: Análisis de Mallas con 2 Mallas

### Enunciado
Encuentre las corrientes de malla I₁ e I₂ donde ω = 10 rad/s.

### Diagrama
```
        4Ω        j3Ω
●───────/\/\/───ΩΩΩΩ───┬─────────●
│                      │         │
+      →I₁           ┌─┴─┐      +
50∠0°V               │-j2│      30∠45°V
-                    │ Ω │      -
│                    └─┬─┘       │
●──────────2Ω─────────┴──────────●
           ←I₂
```

### Solución

#### **Paso 1: Impedancias**
- $\mathbf{Z}_1 = 4$ Ω (resistor)
- $\mathbf{Z}_L = j3$ Ω (inductor)
- $\mathbf{Z}_C = -j2$ Ω (capacitor)
- $\mathbf{Z}_2 = 2$ Ω (resistor)

#### **Paso 2: Ecuaciones de malla**

**Malla 1 (horario):**
$$50\angle 0° = \mathbf{I}_1(4 + j3) + (\mathbf{I}_1 - \mathbf{I}_2)(-j2)$$
$$50 = \mathbf{I}_1(4 + j3 - j2) - \mathbf{I}_2(-j2)$$
$$50 = (4 + j)\mathbf{I}_1 + j2\mathbf{I}_2$$ ... (1)

**Malla 2 (horario):**
$$(\mathbf{I}_2 - \mathbf{I}_1)(-j2) + \mathbf{I}_2(2) + 30\angle 45° = 0$$
$$-j2\mathbf{I}_2 + j2\mathbf{I}_1 + 2\mathbf{I}_2 = -30\angle 45°$$
$$j2\mathbf{I}_1 + (2 - j2)\mathbf{I}_2 = -21.21 - j21.21$$ ... (2)

#### **Paso 3: Resolver el sistema**

$$\begin{bmatrix} 4+j & j2 \\ j2 & 2-j2 \end{bmatrix} \begin{bmatrix} \mathbf{I}_1 \\ \mathbf{I}_2 \end{bmatrix} = \begin{bmatrix} 50 \\ -21.21-j21.21 \end{bmatrix}$$

**Determinante:**
$$\Delta = (4+j)(2-j2) - (j2)(j2)$$
$$\Delta = 8 - j8 + j2 + 2 + 4 = 14 - j6$$
$$\Delta = 15.23\angle -23.2°$$

**I₁:**
$$\mathbf{I}_1 = \frac{50(2-j2) - j2(-21.21-j21.21)}{\Delta}$$
$$= \frac{100 - j100 + j42.42 - 42.42}{15.23\angle -23.2°}$$
$$= \frac{57.58 - j57.58}{15.23\angle -23.2°} = \frac{81.43\angle -45°}{15.23\angle -23.2°}$$
$$\mathbf{I}_1 = 5.35\angle -21.8°\text{ A}$$

**I₂:**
$$\mathbf{I}_2 = \frac{(4+j)(50) - j2(-21.21-j21.21)}{\Delta}$$
$$= \frac{-50(4+j) - j2(-21.21-j21.21)}{\Delta}$$

Recalculando:
$$\mathbf{I}_2 = \frac{(4+j)(-21.21-j21.21) - j2(50)}{\Delta}$$
$$= \frac{-84.84 - j84.84 - j21.21 + 21.21 - j100}{15.23\angle -23.2°}$$
$$= \frac{-63.63 - j206.05}{15.23\angle -23.2°} = \frac{215.66\angle -107.2°}{15.23\angle -23.2°}$$
$$\mathbf{I}_2 = 14.16\angle -84°\text{ A}$$

### Respuesta
$$\boxed{\mathbf{I}_1 = 5.35\angle -21.8°\text{ A}}$$
$$\boxed{\mathbf{I}_2 = 14.16\angle -84°\text{ A}}$$

---

## Ejemplo Clásico 3: Supernodo en CA

### Enunciado
Encuentre el voltaje V₁ usando el método del supernodo.

### Diagrama
```
        R=4Ω           
●───────/\/\/───┬───────────●
│               │           │
+             ┌─┴─┐      ┌──┴──┐
12∠0°V        │-j2│    + │6∠0°V│ -
-             │ Ω │      └──┬──┘
│             └─┬─┘         │
│               │  Supernodo│
●───────────────┴───────────●
        ⏊ (ref)
```

El supernodo encierra la fuente de voltaje de 6∠0° V.

### Solución

#### **Paso 1: Relación del supernodo**
Sea V₁ el voltaje a la izquierda de la fuente de 6V, y V₂ a la derecha.
$$\mathbf{V}_2 - \mathbf{V}_1 = 6\angle 0°$$
$$\mathbf{V}_2 = \mathbf{V}_1 + 6$$ ... (1)

#### **Paso 2: LCK en el supernodo**
$$\frac{12 - \mathbf{V}_1}{4} = \frac{\mathbf{V}_1}{-j2} + \frac{\mathbf{V}_2}{0}$$

Note que V₂ está conectado directamente a la referencia a través de nada (cortocircuito implícito), pero en este caso V₂ = V₁ + 6.

Replanteando el circuito:
$$\frac{12 - \mathbf{V}_1}{4} = \frac{\mathbf{V}_1 - 0}{-j2}$$

$$\frac{12 - \mathbf{V}_1}{4} = \frac{\mathbf{V}_1}{-j2}$$

$$3 - 0.25\mathbf{V}_1 = j0.5\mathbf{V}_1$$

$$3 = \mathbf{V}_1(0.25 + j0.5)$$

$$\mathbf{V}_1 = \frac{3}{0.25 + j0.5} = \frac{3}{0.559\angle 63.43°}$$

$$\mathbf{V}_1 = 5.37\angle -63.43°\text{ V}$$

### Respuesta
$$\boxed{\mathbf{V}_1 = 5.37\angle -63.43°\text{ V}}$$

---

## Resumen de Fórmulas

### Matriz de Admitancias
$$Y_{ii} = \text{suma de admitancias conectadas al nodo } i$$
$$Y_{ij} = -(\text{admitancia entre nodos } i \text{ y } j)$$

### Matriz de Impedancias
$$Z_{ii} = \text{suma de impedancias en la malla } i$$
$$Z_{ij} = -(\text{impedancia compartida entre mallas } i \text{ y } j)$$

### Admitancia vs Impedancia
$$\mathbf{Y} = \frac{1}{\mathbf{Z}}$$

## Errores Comunes
1. Olvidar el signo negativo en elementos fuera de la diagonal
2. No convertir correctamente entre rectangular y polar
3. Confundir las convenciones de corriente en supermallas
4. No considerar que las fuentes de corriente crean supernodos
