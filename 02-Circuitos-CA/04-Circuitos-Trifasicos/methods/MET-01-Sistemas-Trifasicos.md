# MET-01: Método de Análisis de Circuitos Trifásicos

## Descripción del Método

Los sistemas trifásicos son la forma estándar de generación, transmisión y distribución de energía eléctrica. Este método cubre el análisis de sistemas **balanceados** y las principales configuraciones: Y-Y, Y-Δ, Δ-Y y Δ-Δ.

---

## Sistema Trifásico Balanceado

### Voltajes de Fase (Secuencia ABC positiva)
$$\mathbf{V}_{an} = V_p \angle 0°$$
$$\mathbf{V}_{bn} = V_p \angle -120°$$
$$\mathbf{V}_{cn} = V_p \angle -240° = V_p \angle 120°$$

Donde $V_p$ = voltaje de fase (línea a neutro)

### Voltajes de Línea
$$\mathbf{V}_{ab} = \mathbf{V}_{an} - \mathbf{V}_{bn}$$

Relación magnitud:
$$V_L = \sqrt{3} V_p$$

Relación fasorial:
$$\mathbf{V}_{ab} = \sqrt{3} V_p \angle 30°$$

---

## Configuraciones

### Conexión Estrella (Y)
```
        a ●
          │
        ┌─┴─┐
        │Za │
        └─┬─┘
          │
    n ●───┼───● n
          │
        ┌─┴─┐
        │Zb │
        └─┬─┘
          │
        b ●
```

### Conexión Delta (Δ)
```
    a ●───────/\/\/───────● b
      │         Zab       │
      │                   │
    ┌─┴─┐               ┌─┴─┐
    │Zca│               │Zbc│
    └─┬─┘               └─┬─┘
      │                   │
      └─────────●─────────┘
                c
```

---

## Conversión Y-Δ

### De Y a Δ
$$Z_{ab} = \frac{Z_a Z_b + Z_b Z_c + Z_c Z_a}{Z_c}$$

Para carga balanceada ($Z_a = Z_b = Z_c = Z_Y$):
$$Z_\Delta = 3Z_Y$$

### De Δ a Y
$$Z_a = \frac{Z_{ab} Z_{ca}}{Z_{ab} + Z_{bc} + Z_{ca}}$$

Para carga balanceada:
$$Z_Y = \frac{Z_\Delta}{3}$$

---

## Método del Circuito Equivalente por Fase

### Pasos del Método (Sistema Balanceado)

#### Paso 1: Convertir todo a Y
- Si la fuente está en Δ, convertir a Y
- Si la [carga](../../../glossary.md#carga) está en Δ, convertir a Y
- $Z_Y = Z_\[Delta](../../../glossary.md#delta) / 3$

#### Paso 2: Dibujar Circuito Monofásico
- Una fase de la fuente
- [Impedancia](../../../glossary.md#impedancia) de línea (si existe)
- Impedancia de carga por fase
- Retorno por neutro (impedancia = 0 si balanceado)

#### Paso 3: Analizar el Circuito Monofásico
$$\mathbf{I}_a = \frac{\mathbf{V}_{an}}{Z_{total}}$$

#### Paso 4: Calcular las Otras Fases
$$\mathbf{I}_b = \mathbf{I}_a \angle -120°$$
$$\mathbf{I}_c = \mathbf{I}_a \angle +120°$$

#### Paso 5: Calcular Potencia Total
$$S_{3\phi} = 3 \times S_{1\phi}$$

---

## Relaciones de Corriente

### Sistema Y
- [Corriente](../../../glossary.md#corriente) de línea = Corriente de fase
$$I_L = I_p$$

### Sistema Δ
- Corriente de línea ≠ Corriente de fase
$$I_L = \sqrt{3} I_p$$

---

## Ejemplo Clásico 1: Sistema Y-Y Balanceado

### Enunciado
Una fuente trifásica balanceada en Y de 208 V línea-línea alimenta una carga balanceada en Y de 10∠30° Ω por fase. Calcule las corrientes de línea y la potencia consumida.

### Diagrama
```
    FUENTE Y              CARGA Y
      a ●────────────────────●
        │       Ia →         │
      ┌─┴─┐                ┌─┴─┐
     Va   │               │10∠30°│
      └─┬─┘                └─┬─┘
        │                    │
    n ●─┼────────────────────┼─● n'
        │                    │
      ┌─┴─┐                ┌─┴─┐
     Vb   │               │10∠30°│
      └─┬─┘                └─┬─┘
        │       Ib →         │
      b ●────────────────────●
```

### Solución

#### **Paso 1: Voltaje de fase**
$$V_L = 208\text{ V}$$
$$V_p = \frac{V_L}{\sqrt{3}} = \frac{208}{\sqrt{3}} = 120\text{ V}$$

Fasores de [voltaje](../../../glossary.md#voltaje):
$$\mathbf{V}_{an} = 120\angle 0°\text{ V}$$
$$\mathbf{V}_{bn} = 120\angle -120°\text{ V}$$
$$\mathbf{V}_{cn} = 120\angle 120°\text{ V}$$

#### **Paso 2: Corriente de línea (fase a)**
$$\mathbf{I}_a = \frac{\mathbf{V}_{an}}{Z_Y} = \frac{120\angle 0°}{10\angle 30°}$$
$$\mathbf{I}_a = 12\angle -30°\text{ A}$$

#### **Paso 3: Las otras corrientes**
$$\mathbf{I}_b = 12\angle(-30° - 120°) = 12\angle -150°\text{ A}$$
$$\mathbf{I}_c = 12\angle(-30° + 120°) = 12\angle 90°\text{ A}$$

#### **Paso 4: Potencia**
Potencia por fase:
$$S_{1\phi} = \mathbf{V}_{an} \mathbf{I}_a^* = (120\angle 0°)(12\angle 30°)$$
$$S_{1\phi} = 1440\angle 30° = 1247.1 + j720\text{ VA}$$
$$P_{1\phi} = 1247.1\text{ W}, \quad Q_{1\phi} = 720\text{ VAR}$$

Potencia total:
$$P_{3\phi} = 3 \times 1247.1 = 3741.3\text{ W}$$
$$Q_{3\phi} = 3 \times 720 = 2160\text{ VAR}$$
$$S_{3\phi} = 3 \times 1440 = 4320\text{ VA}$$

#### **Verificación con fórmulas directas**
$$P_{3\phi} = \sqrt{3} V_L I_L \cos\theta = \sqrt{3}(208)(12)\cos 30° = 3741\text{ W}$$ ✓

### Respuesta
$$\boxed{\mathbf{I}_a = 12\angle -30°\text{ A}, \quad P_{3\phi} = 3.74\text{ kW}, \quad Q_{3\phi} = 2.16\text{ kVAR}}$$

### Explicación
En un sistema Y-Y balanceado, el neutro no lleva corriente (las tres corrientes suman cero). La potencia total es tres veces la potencia de una fase, o puede calcularse con la fórmula $P = \sqrt{3} V_L I_L \cos\theta$.

---

## Ejemplo Clásico 2: Sistema Y-Δ

### Enunciado
Una fuente trifásica balanceada en Y de 400 V de línea alimenta una carga balanceada en Δ de 30∠45° Ω por fase. Calcule las corrientes de línea y de fase de la carga.

### Solución

#### **Método 1: Convertir Δ a Y**

$$Z_Y = \frac{Z_\Delta}{3} = \frac{30\angle 45°}{3} = 10\angle 45°\text{ Ω}$$

$$V_p = \frac{400}{\sqrt{3}} = 231\text{ V}$$

Corriente de línea:
$$\mathbf{I}_a = \frac{231\angle 0°}{10\angle 45°} = 23.1\angle -45°\text{ A}$$

#### **Método 2: Análisis directo**

Voltaje de línea = Voltaje aplicado a cada impedancia Δ:
$$\mathbf{V}_{ab} = 400\angle 30°\text{ V}$$

Corriente de fase en la carga (Δ):
$$\mathbf{I}_{AB} = \frac{\mathbf{V}_{ab}}{Z_\Delta} = \frac{400\angle 30°}{30\angle 45°} = 13.33\angle -15°\text{ A}$$

Corriente de línea:
$$I_L = \sqrt{3} I_{fase} = \sqrt{3} \times 13.33 = 23.1\text{ A}$$

La corriente de línea adelanta 30° a la corriente de fase:
$$\mathbf{I}_a = 23.1\angle(-15° - 30°) = 23.1\angle -45°\text{ A}$$

### Respuesta
$$\boxed{I_L = 23.1\text{ A}, \quad I_{fase} = 13.33\text{ A}}$$
$$\boxed{\mathbf{I}_a = 23.1\angle -45°\text{ A}}$$

---

## Ejemplo Clásico 3: Potencia en Sistema Desbalanceado (Introducción)

### Enunciado
Una fuente Y de 240 V línea alimenta cargas en Y: Za = 10 Ω, Zb = 15 Ω, Zc = 20 Ω. Asumiendo neutros conectados, encuentre las corrientes.

### Nota
En sistemas desbalanceados, no se puede usar el método de [circuito](../../../glossary.md#circuito) equivalente por fase. Se debe analizar el circuito completo.

### Solución (con neutros conectados)

$$V_p = \frac{240}{\sqrt{3}} = 138.6\text{ V}$$

$$\mathbf{I}_a = \frac{138.6\angle 0°}{10} = 13.86\angle 0°\text{ A}$$
$$\mathbf{I}_b = \frac{138.6\angle -120°}{15} = 9.24\angle -120°\text{ A}$$
$$\mathbf{I}_c = \frac{138.6\angle 120°}{20} = 6.93\angle 120°\text{ A}$$

Corriente de neutro:
$$\mathbf{I}_n = \mathbf{I}_a + \mathbf{I}_b + \mathbf{I}_c$$
$$\mathbf{I}_n = 13.86 + 9.24\angle -120° + 6.93\angle 120°$$
$$\mathbf{I}_n = 13.86 + (-4.62 - j8) + (-3.47 + j6)$$
$$\mathbf{I}_n = 5.77 - j2$$
$$\mathbf{I}_n = 6.1\angle -19.1°\text{ A}$$

### Respuesta
$$\boxed{I_a = 13.86\text{ A}, \quad I_b = 9.24\text{ A}, \quad I_c = 6.93\text{ A}, \quad I_n = 6.1\text{ A}}$$

### Explicación
En sistemas desbalanceados, las corrientes no suman cero, por lo que fluye corriente por el neutro. Sin conexión de neutro, el análisis es más complejo (requiere resolver el sistema completo).

---

## Fórmulas de Potencia Trifásica

### Potencia Activa
$$P_{3\phi} = \sqrt{3} V_L I_L \cos\theta = 3 V_p I_p \cos\theta$$

### Potencia Reactiva
$$Q_{3\phi} = \sqrt{3} V_L I_L \sin\theta = 3 V_p I_p \sin\theta$$

### Potencia Aparente
$$S_{3\phi} = \sqrt{3} V_L I_L = 3 V_p I_p$$

### Relación
$$S_{3\phi} = \sqrt{P_{3\phi}^2 + Q_{3\phi}^2}$$

---

## Tabla de Conversiones

| Parámetro | Y | Δ |
|-----------|---|---|
| Voltaje de línea | $V_L = \sqrt{3}V_p$ | $V_L = V_{fase}$ |
| Corriente de línea | $I_L = I_{fase}$ | $I_L = \sqrt{3}I_{fase}$ |
| Impedancia | $Z_Y$ | $Z_\Delta = 3Z_Y$ |

## Errores Comunes
1. Confundir voltaje de línea con voltaje de fase
2. No aplicar el factor √3 correctamente
3. Olvidar el desfase de 30° entre voltajes de línea y fase
4. Usar método por fase en sistemas desbalanceados
