# MET-01: Método de Aplicación de la Ley de Ohm

## Descripción del Método

La **Ley de Ohm** establece la relación fundamental entre voltaje (V), corriente (I) y resistencia (R) en un elemento resistivo. Es la base para el análisis de cualquier circuito eléctrico.

$$V = I \cdot R$$

## Fórmulas Fundamentales

| Para encontrar | Fórmula | Unidades |
|----------------|---------|----------|
| Voltaje | $V = I \cdot R$ | Volts (V) |
| Corriente | $I = \frac{V}{R}$ | Amperes (A) |
| Resistencia | $R = \frac{V}{I}$ | Ohms (Ω) |

## Pasos del Método

### Paso 1: Identificar las Variables Conocidas
- Identificar qué valores están dados en el problema
- Verificar las unidades (convertir si es necesario a V, A, Ω)

### Paso 2: Determinar la Variable Desconocida
- ¿Qué se pide calcular?
- Seleccionar la fórmula apropiada

### Paso 3: Aplicar la Ley de Ohm
- Sustituir valores conocidos
- Resolver algebraicamente

### Paso 4: Verificar el Resultado
- Comprobar que las unidades sean correctas
- Verificar que el resultado sea físicamente razonable

## Triángulo de Ohm (Ayuda Visual)

```
        ┌───────┐
        │   V   │
        ├───┬───┤
        │ I │ R │
        └───┴───┘
        
Para encontrar V: cubrir V → queda I×R
Para encontrar I: cubrir I → queda V/R  
Para encontrar R: cubrir R → queda V/I
```

---

## Ejemplo Clásico 1: Calcular Corriente

### Enunciado
Una resistencia de 470 Ω está conectada a una fuente de 12 V. Calcule la corriente que circula por la resistencia.

### Diagrama
```
    +  12V  -
    ●──────●
    │      │
    │    ┌─┴─┐
    │    │470│
    │    │ Ω │
    │    └─┬─┘
    │  I↓  │
    ●──────●
```

### Solución Paso a Paso

**Paso 1: Identificar variables conocidas**
- V = 12 V
- R = 470 Ω

**Paso 2: Variable desconocida**
- I = ? (corriente)
- Fórmula: $I = \frac{V}{R}$

**Paso 3: Aplicar Ley de Ohm**
$$I = \frac{V}{R} = \frac{12\text{ V}}{470\text{ Ω}}$$

$$I = 0.02553\text{ A} = 25.53\text{ mA}$$

**Paso 4: Verificación**
- Unidades: V/Ω = A ✓
- Comprobación: $V = I \times R = 0.02553 \times 470 = 12\text{ V}$ ✓

### Respuesta
$$\boxed{I = 25.53\text{ mA}}$$

### Explicación de la Respuesta
La corriente de 25.53 mA es relativamente pequeña debido a que la resistencia de 470 Ω limita significativamente el flujo de corriente. Este valor es típico en circuitos electrónicos de señal. Si la resistencia fuera menor, la corriente sería mayor (relación inversamente proporcional).

---

## Ejemplo Clásico 2: Calcular Resistencia

### Enunciado
Un LED requiere una corriente de 20 mA para operar correctamente. Si se conecta a una fuente de 5 V y la caída de voltaje en el LED es 2 V, ¿qué resistencia limitadora se necesita?

### Diagrama
```
    ●────────┬────────●
    │   +5V  │        │
    │      ┌─┴─┐      │
    │      │ R │ ← Calcular
    │      │ ? │      │
    │      └─┬─┘      │
    │    VR  │        │
    │      ┌─┴─┐      │
    │      │LED│ VLED=2V
    │      └─┬─┘      │
    │   I=20mA↓       │
    ●────────┴────────●
           GND
```

### Solución Paso a Paso

**Paso 1: Identificar variables conocidas**
- V_fuente = 5 V
- V_LED = 2 V
- I = 20 mA = 0.020 A

**Paso 2: Calcular voltaje en R**
$$V_R = V_{fuente} - V_{LED} = 5 - 2 = 3\text{ V}$$

**Paso 3: Aplicar Ley de Ohm**
$$R = \frac{V_R}{I} = \frac{3\text{ V}}{0.020\text{ A}}$$

$$R = 150\text{ Ω}$$

**Paso 4: Verificación**
$$I = \frac{V_R}{R} = \frac{3}{150} = 0.020\text{ A} = 20\text{ mA}$$ ✓

### Respuesta
$$\boxed{R = 150\text{ Ω}}$$

### Explicación de la Respuesta
La resistencia de 150 Ω absorbe los 3 V excedentes (5V - 2V del LED) y limita la corriente a exactamente 20 mA. Esta es una aplicación muy común de la Ley de Ohm: calcular resistencias limitadoras de corriente para proteger componentes sensibles como LEDs. En la práctica, se usaría una resistencia comercial de 150 Ω o el valor estándar más cercano (como 180 Ω para mayor seguridad).

---

## Ejemplo Clásico 3: Calcular Voltaje

### Enunciado
Por una resistencia de 2.2 kΩ circula una corriente de 5 mA. ¿Cuál es la caída de voltaje en la resistencia?

### Diagrama
```
        I = 5mA
    ●────→────┐
    │         │
  + │       ┌─┴─┐
  V │       │2.2│
  ? │       │kΩ │
  - │       └─┬─┘
    │         │
    ●─────────┘
```

### Solución Paso a Paso

**Paso 1: Identificar variables conocidas**
- R = 2.2 kΩ = 2200 Ω
- I = 5 mA = 0.005 A

**Paso 2: Variable desconocida**
- V = ? (voltaje)
- Fórmula: $V = I \times R$

**Paso 3: Aplicar Ley de Ohm**
$$V = I \times R = 0.005\text{ A} \times 2200\text{ Ω}$$

$$V = 11\text{ V}$$

**Paso 4: Verificación**
$$I = \frac{V}{R} = \frac{11}{2200} = 0.005\text{ A} = 5\text{ mA}$$ ✓

### Respuesta
$$\boxed{V = 11\text{ V}}$$

### Explicación de la Respuesta
Una corriente de 5 mA a través de 2.2 kΩ produce una caída de voltaje de 11 V. Este tipo de cálculo es fundamental para diseñar divisores de voltaje y determinar los niveles de señal en diferentes puntos de un circuito. La relación es directamente proporcional: duplicar la corriente duplicaría el voltaje.

---

## Potencia y Ley de Ohm

La Ley de Ohm se combina frecuentemente con las fórmulas de potencia:

$$P = V \cdot I = I^2 R = \frac{V^2}{R}$$

### Ejemplo de Potencia

**Problema:** Calcular la potencia disipada por una resistencia de 100 Ω con 12 V aplicados.

**Solución:**
$$P = \frac{V^2}{R} = \frac{(12)^2}{100} = \frac{144}{100} = 1.44\text{ W}$$

**Respuesta:** La resistencia disipa **1.44 W**. Se necesitaría una resistencia de al menos 2 W de potencia nominal para evitar sobrecalentamiento.

---

## Errores Comunes a Evitar

1. **Unidades incorrectas:** Siempre convertir kΩ a Ω, mA a A antes de calcular
2. **Confundir voltaje con corriente:** V siempre es la diferencia de potencial entre dos puntos
3. **Ignorar la polaridad:** El sentido de la corriente determina el signo del voltaje
4. **Olvidar verificar:** Siempre comprobar el resultado sustituyendo en la ecuación original

## Casos Especiales

| Caso | R | V | I | Resultado |
|------|---|---|---|-----------|
| Cortocircuito | 0 Ω | 0 V | Máxima (limitada por fuente) | Peligroso |
| Circuito abierto | ∞ Ω | V_fuente | 0 A | Sin corriente |
| Carga nominal | R > 0 | V = IR | I = V/R | Operación normal |

## Conceptos Relacionados
- Divisor de voltaje
- Divisor de corriente
- Potencia eléctrica
- Leyes de Kirchhoff
