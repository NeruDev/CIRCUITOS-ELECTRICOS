# MET-01: Método de Análisis de Circuitos Acoplados Magnéticamente

## Descripción del Método

Los **circuitos acoplados magnéticamente** contienen inductores que comparten flujo magnético, creando [inductancia](../../../glossary.md#inductancia) mutua. El análisis requiere considerar tanto la auto-inductancia como la inductancia mutua.

---

## Conceptos Fundamentales

### Inductancia Mutua
$$M = k\sqrt{L_1 L_2}$$

Donde:
- $M$ = inductancia mutua (H)
- $k$ = coeficiente de acoplamiento (0 ≤ k ≤ 1)
- $L_1, L_2$ = auto-inductancias

### Coeficiente de Acoplamiento
- k = 0: Sin acoplamiento
- k = 1: Acoplamiento perfecto (transformador ideal)
- 0 < k < 1: Acoplamiento parcial

---

## Ecuaciones de Voltaje

### Convención del Punto
El **punto** (•) indica la polaridad del acoplamiento:
- Corrientes que entran por puntos: voltajes mutuos del mismo signo
- Corrientes entrando/saliendo: voltajes mutuos de signo opuesto

### Ecuaciones Generales
$$v_1 = L_1\frac{di_1}{dt} \pm M\frac{di_2}{dt}$$
$$v_2 = \pm M\frac{di_1}{dt} + L_2\frac{di_2}{dt}$$

**Signo + si ambas corrientes entran (o salen) por los puntos**
**Signo - si una entra y otra sale por los puntos**

### En Dominio Fasorial
$$\mathbf{V}_1 = j\omega L_1 \mathbf{I}_1 \pm j\omega M \mathbf{I}_2$$
$$\mathbf{V}_2 = \pm j\omega M \mathbf{I}_1 + j\omega L_2 \mathbf{I}_2$$

---

## Pasos del Método

### Paso 1: Identificar Polaridades (Puntos)
- Marcar los puntos en ambas bobinas
- Determinar la dirección de las corrientes respecto a los puntos

### Paso 2: Escribir Ecuaciones de Malla/Nodo
- Incluir términos de auto-inductancia
- Incluir términos de inductancia mutua con signo correcto

### Paso 3: Convertir a Dominio Fasorial
- Reemplazar d/dt por jω
- Usar impedancias

### Paso 4: Resolver el Sistema de Ecuaciones

### Paso 5: Interpretar Resultados

---

## Ejemplo Clásico 1: Dos Bobinas Acopladas

### Enunciado
Dos bobinas acopladas tienen L₁ = 0.5 H, L₂ = 2 H, M = 0.8 H. Una fuente v₁(t) = 100cos(100t) V se conecta a la bobina 1. La bobina 2 está cortocircuitada. Encuentre i₁(t) e i₂(t).

### Diagrama
```
    +  • i₁→            • +
   ┌───┬──ΩΩΩΩ──┐   ┌──ΩΩΩΩ──┬───┐
   │   │  L₁    │ M │  L₂    │   │
 + │   │  0.5H  │   │  2H    │   │
v₁ │   └────────┘   └────────┘   │ (corto)
 - │                             │
   └─────────────────────────────┘
```

Las corrientes entran por los puntos: **signo positivo** en M.

### Solución

#### **Paso 1: Ecuaciones de malla**

**Malla 1:**
$$v_1 = L_1\frac{di_1}{dt} + M\frac{di_2}{dt}$$

**[Malla](../../../glossary.md#malla) 2 (cortocircuito):**
$$0 = M\frac{di_1}{dt} + L_2\frac{di_2}{dt}$$

#### **Paso 2: Dominio fasorial**
$$\omega = 100\text{ rad/s}$$
$$\mathbf{V}_1 = 100\angle 0°\text{ V}$$

Impedancias:
$$j\omega L_1 = j(100)(0.5) = j50\text{ Ω}$$
$$j\omega L_2 = j(100)(2) = j200\text{ Ω}$$
$$j\omega M = j(100)(0.8) = j80\text{ Ω}$$

#### **Paso 3: Sistema de ecuaciones**
$$100 = j50\mathbf{I}_1 + j80\mathbf{I}_2$$ ... (1)
$$0 = j80\mathbf{I}_1 + j200\mathbf{I}_2$$ ... (2)

De (2):
$$\mathbf{I}_2 = -\frac{j80}{j200}\mathbf{I}_1 = -0.4\mathbf{I}_1$$

Sustituyendo en (1):
$$100 = j50\mathbf{I}_1 + j80(-0.4\mathbf{I}_1)$$
$$100 = j50\mathbf{I}_1 - j32\mathbf{I}_1$$
$$100 = j18\mathbf{I}_1$$
$$\mathbf{I}_1 = \frac{100}{j18} = \frac{100}{18}\angle -90° = 5.56\angle -90°\text{ A}$$

$$\mathbf{I}_2 = -0.4 \times 5.56\angle -90° = 2.22\angle 90°\text{ A}$$

#### **Paso 4: Dominio del tiempo**
$$i_1(t) = 5.56\cos(100t - 90°) = 5.56\sin(100t)\text{ A}$$
$$i_2(t) = 2.22\cos(100t + 90°) = -2.22\sin(100t)\text{ A}$$

### Respuesta
$$\boxed{i_1(t) = 5.56\sin(100t)\text{ A}}$$
$$\boxed{i_2(t) = -2.22\sin(100t)\text{ A}}$$

### Explicación
La [corriente](../../../glossary.md#corriente) i₂ fluye en dirección opuesta a i₁ debido a la [ley de](../../../glossary.md#ley-ohm) Lenz: el campo magnético inducido se opone al cambio del campo original. El acoplamiento magnético permite transferir energía sin conexión eléctrica directa.

---

## Ejemplo Clásico 2: Transformador con Carga

### Enunciado
Un [transformador](../../../glossary.md#transformador) tiene L₁ = 10 mH, L₂ = 40 mH, k = 0.9. La [frecuencia](../../../glossary.md#frecuencia) es 1000 rad/s. El primario se conecta a 50∠0° V y el secundario a una [carga](../../../glossary.md#carga) de 100 Ω. Encuentre las corrientes y el [voltaje](../../../glossary.md#voltaje) en la carga.

### Diagrama
```
         R₁=0         R₂=0
    +  •  i₁→           •  i₂→   +
   ┌───┬──ΩΩΩΩ──┐   ┌──ΩΩΩΩ──┬───/\/\/───┐
   │   │  L₁    │ M │  L₂    │   100Ω    │
 + │   │ 10mH   │   │ 40mH   │          ─┴─
Vs │   └────────┘   └────────┘           ─
 - │                                      │
   └──────────────────────────────────────┘
```

### Solución

#### **Paso 1: Calcular M**
$$M = k\sqrt{L_1 L_2} = 0.9\sqrt{(0.01)(0.04)} = 0.9 \times 0.02 = 0.018\text{ H}$$

#### **Paso 2: Impedancias**
$$j\omega L_1 = j(1000)(0.01) = j10\text{ Ω}$$
$$j\omega L_2 = j(1000)(0.04) = j40\text{ Ω}$$
$$j\omega M = j(1000)(0.018) = j18\text{ Ω}$$
$$Z_L = 100\text{ Ω}$$

#### **Paso 3: Ecuaciones de malla**

Asumiendo que ambas corrientes entran por los puntos:

**Malla 1:**
$$\mathbf{V}_s = j\omega L_1 \mathbf{I}_1 + j\omega M \mathbf{I}_2$$
$$50 = j10\mathbf{I}_1 + j18\mathbf{I}_2$$ ... (1)

**Malla 2:**
$$0 = j\omega M \mathbf{I}_1 + (j\omega L_2 + Z_L)\mathbf{I}_2$$
$$0 = j18\mathbf{I}_1 + (j40 + 100)\mathbf{I}_2$$ ... (2)

#### **Paso 4: Resolver**
De (2):
$$\mathbf{I}_1 = -\frac{(j40 + 100)}{j18}\mathbf{I}_2 = -\frac{100 + j40}{j18}\mathbf{I}_2$$

$$\mathbf{I}_1 = -\frac{107.7\angle 21.8°}{18\angle 90°}\mathbf{I}_2 = -5.98\angle -68.2°\mathbf{I}_2$$

Sustituyendo en (1):
$$50 = j10(-5.98\angle -68.2°)\mathbf{I}_2 + j18\mathbf{I}_2$$
$$50 = -59.8\angle 21.8°\mathbf{I}_2 + j18\mathbf{I}_2$$
$$50 = (-55.5 - j22.2)\mathbf{I}_2 + j18\mathbf{I}_2$$
$$50 = (-55.5 - j4.2)\mathbf{I}_2$$
$$50 = 55.66\angle -175.7°\mathbf{I}_2$$
$$\mathbf{I}_2 = \frac{50}{55.66\angle -175.7°} = 0.898\angle 175.7°\text{ A}$$

$$\mathbf{I}_1 = -5.98\angle -68.2° \times 0.898\angle 175.7°$$
$$\mathbf{I}_1 = 5.37\angle 107.5°\text{ A}$$

#### **Paso 5: Voltaje en la carga**
$$\mathbf{V}_L = \mathbf{I}_2 \times Z_L = 0.898\angle 175.7° \times 100 = 89.8\angle 175.7°\text{ V}$$

### Respuesta
$$\boxed{\mathbf{I}_1 = 5.37\angle 107.5°\text{ A}}$$
$$\boxed{\mathbf{I}_2 = 0.898\angle 175.7°\text{ A}}$$
$$\boxed{\mathbf{V}_L = 89.8\angle 175.7°\text{ V}}$$

---

## Ejemplo Clásico 3: Circuito Equivalente T

### Enunciado
Derive el circuito equivalente T para dos bobinas acopladas con L₁ = 5 H, L₂ = 8 H, M = 4 H.

### Circuito Original
```
    • i₁→        M=4H      • i₂→
   ┬──ΩΩΩΩ──┐       ┌──ΩΩΩΩ──┬
   │  L₁=5H │       │  L₂=8H │
   └────────┘       └────────┘
```

### Circuito Equivalente T
```
       L₁-M           L₂-M
    ●───ΩΩΩΩ────┬────ΩΩΩΩ───●
    i₁→         │         ←i₂
              ┌─┴─┐
              │ M │
              │ 4H│
              └─┬─┘
    ●───────────┴───────────●
```

### Solución

#### **Valores del equivalente T**
$$L_a = L_1 - M = 5 - 4 = 1\text{ H}$$
$$L_b = L_2 - M = 8 - 4 = 4\text{ H}$$
$$L_c = M = 4\text{ H}$$

### Verificación
**Con el [circuito](../../../glossary.md#circuito) original:**
$$V_1 = j\omega L_1 I_1 + j\omega M I_2 = j\omega(5I_1 + 4I_2)$$
$$V_2 = j\omega M I_1 + j\omega L_2 I_2 = j\omega(4I_1 + 8I_2)$$

**Con el equivalente T:**
$$V_1 = j\omega(L_1-M)I_1 + j\omega M(I_1 + I_2) = j\omega(I_1 - 4I_1 + 4I_1 + 4I_2)$$
Reorganizando:
$$V_1 = j\omega[(L_1-M)I_1 + M(I_1+I_2)] = j\omega[L_1 I_1 - MI_1 + MI_1 + MI_2]$$
$$V_1 = j\omega(L_1 I_1 + MI_2)$$ ✓

### Respuesta
$$\boxed{L_a = 1\text{ H}, \quad L_b = 4\text{ H}, \quad L_c = 4\text{ H}}$$

### Explicación
El circuito equivalente T elimina el acoplamiento magnético, permitiendo usar técnicas estándar de análisis. Solo es válido cuando M < L₁ y M < L₂ (de lo contrario, aparecen inductancias negativas).

---

## Transformador Ideal

### Relaciones
$$\frac{V_1}{V_2} = \frac{N_1}{N_2} = n$$ (relación de vueltas)
$$\frac{I_1}{I_2} = \frac{N_2}{N_1} = \frac{1}{n}$$

### Impedancia Reflejada
$$Z_{in} = n^2 Z_L$$

Una impedancia $Z_L$ en el secundario aparece como $n^2 Z_L$ vista desde el primario.

---

## Resumen de Fórmulas

| Concepto | Fórmula |
|----------|---------|
| Inductancia mutua | $M = k\sqrt{L_1 L_2}$ |
| Coeficiente de acoplamiento | $k = M/\sqrt{L_1 L_2}$ |
| Equivalente T (serie) | $L_a = L_1 - M$, $L_b = L_2 - M$, $L_c = M$ |
| Equivalente π (paralelo) | $L_A = L_1 L_2/M - L_1$, etc. |
| Impedancia reflejada | $Z_{ref} = n^2 Z_L$ |

## Errores Comunes
1. No considerar la convención del punto
2. Usar signo incorrecto en el término de inductancia mutua
3. Olvidar que el equivalente T puede tener inductancias negativas
4. Confundir la relación de vueltas con la relación de impedancias
