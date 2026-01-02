# MET-01: Método del Equivalente de Thévenin

## Descripción del Método

El **[Teorema de](../../../glossary.md#norton) [Thévenin](../../../glossary.md#thevenin)** establece que cualquier [circuito](../../../glossary.md#circuito) lineal de dos terminales puede ser reemplazado por un circuito equivalente que consiste en:
- Una **fuente de [voltaje](../../../glossary.md#voltaje)** Vth (voltaje de Thévenin)
- Una **[resistencia](../../../glossary.md#resistencia) en serie** Rth (resistencia de Thévenin)

### Utilidad
- Simplifica el análisis cuando se cambia la [carga](../../../glossary.md#carga)
- Facilita cálculos de máxima transferencia de potencia
- Permite caracterizar circuitos complejos con solo dos parámetros

---

## Fórmulas Fundamentales

$$V_{th} = V_{ab} \text{ (circuito abierto)}$$

$$R_{th} = \frac{V_{th}}{I_{sc}} \text{ (donde } I_{sc} \text{ es la corriente de cortocircuito)}$$

**O equivalentemente (si no hay fuentes dependientes):**
$$R_{th} = R_{eq} \text{ (desactivando todas las fuentes independientes)}$$

---

## Pasos del Método

### Paso 1: Identificar los Terminales
- Seleccionar los dos terminales (a, b) donde se conectará la carga
- Remover la carga del circuito

### Paso 2: Calcular Vth (Voltaje de Thévenin)
- Dejar los terminales en **circuito abierto**
- Calcular el voltaje entre a y b: $V_{th} = V_{ab}$

### Paso 3: Calcular Rth (Resistencia de Thévenin)
**Método A (sin fuentes dependientes):**
- Desactivar todas las fuentes independientes
- Calcular la resistencia equivalente vista desde a-b

**Método B (con fuentes dependientes o cualquier caso):**
- Calcular la corriente de cortocircuito Isc
- $R_{th} = V_{th} / I_{sc}$

### Paso 4: Dibujar el Circuito Equivalente
```
        Rth
    a●───/\/\/───┬───●
                 │
              +  │
             Vth ─┴─
              -  │
                 │
    b●───────────┴───●
```

### Paso 5: Reconectar la Carga
- Conectar RL entre los terminales a-b
- Analizar el circuito simplificado

---

## Ejemplo Clásico 1: Circuito con Fuentes de Voltaje

### Enunciado
Encuentre el equivalente de Thévenin visto desde los terminales a-b.

### Diagrama Original
```
            R₁=4Ω           R₂=12Ω
    ●────────/\/\/────●────/\/\/────●a
    │                 │              
  + │               ┌─┴─┐            
 32V│               │R₃ │            
    │               │6Ω │            
  - │               └─┬─┘            
    │                 │              
    └─────────────────●─────────────●b
```

### Solución Paso a Paso

#### **Paso 1: Identificar terminales**
- Terminal a: extremo derecho superior
- Terminal b: extremo derecho inferior (tierra)

#### **Paso 2: Calcular Vth (circuito abierto)**

Con terminales abiertos, no hay corriente por R₂:
$$I_{R2} = 0 \Rightarrow V_{R2} = 0$$

El voltaje Vth = voltaje en R₃

[Corriente](../../../glossary.md#corriente) por R₁ y R₃ (en serie):
$$I = \frac{32}{R_1 + R_3} = \frac{32}{4 + 6} = \frac{32}{10} = 3.2\text{ A}$$

Voltaje en R₃:
$$V_{th} = I \times R_3 = 3.2 \times 6 = 19.2\text{ V}$$

#### **Paso 3: Calcular Rth (desactivar fuentes)**

Desactivar la fuente de 32V (cortocircuito):
```
            R₁=4Ω           R₂=12Ω
    ●────────/\/\/────●────/\/\/────●a
    │                 │              
    │               ┌─┴─┐            
●───●               │R₃ │       Rth  
Cortocircuito       │6Ω │       ←    
    │               └─┬─┘            
    │                 │              
    └─────────────────●─────────────●b
```

Visto desde a-b:
- R₁ y R₃ están en paralelo: $R_{13} = \frac{4 \times 6}{4 + 6} = 2.4$ Ω
- R₁₃ está en serie con R₂: $R_{th} = R_{13} + R_2 = 2.4 + 12 = 14.4$ Ω

#### **Paso 4: Circuito Equivalente de Thévenin**

```
       Rth=14.4Ω
    a●───/\/\/───┬───●
                 │
              +  │
           19.2V ─┴─
              -  │
                 │
    b●───────────┴───●
```

### Respuesta
$$\boxed{V_{th} = 19.2\text{ V}, \quad R_{th} = 14.4\text{ Ω}}$$

### Explicación de la Respuesta
El circuito original complejo se reduce a una fuente de 19.2V en serie con 14.4Ω. Esto significa que si conectamos cualquier carga RL, la corriente será:
$$I_L = \frac{19.2}{14.4 + R_L}$$

Por ejemplo, con RL = 10Ω:
$$I_L = \frac{19.2}{14.4 + 10} = \frac{19.2}{24.4} = 0.787\text{ A}$$

---

## Ejemplo Clásico 2: Circuito con Fuente de Corriente

### Enunciado
Determine el equivalente de Thévenin.

### Diagrama
```
                R₁=6Ω           R₂=3Ω
    ●────────────/\/\/────●────/\/\/────●a
    │                     │              
  ┌─┴─┐                 ┌─┴─┐            
  │Is │                 │R₃ │            
  │4A │                 │6Ω │            
  └─┬─┘                 └─┬─┘            
    │                     │              
    └─────────────────────●─────────────●b
```

### Solución

#### **Vth (circuito abierto)**

La fuente de corriente de 4A se divide entre R₁ y (R₂ + R₃):
Pero con a-b abierto, R₂ está en serie con circuito abierto → I_R2 = 0

Toda la corriente 4A pasa por R₁:
$$V_{R1} = 4 \times 6 = 24\text{ V}$$

Voltaje del [nodo](../../../glossary.md#nodo) intermedio respecto a b:
$$V_{nodo} = 24\text{ V}$$

Voltaje en R₃ (con I = 0 en R₂):
$$V_{th} = V_{nodo} = 24\text{ V}$$

¡Espera! Revisemos: El nodo comparte R₃, y con circuito abierto en a-b:
La corriente de 4A fluye por R₁. El nodo tiene 24V.
R₃ está entre este nodo y b (tierra), así que:
$$I_{R3} = \frac{24}{6} = 4\text{ A}$$

Pero esto implica que toda la corriente va por R₃, no por R₂ (correcto, ya que a-b está abierto).

$$V_{th} = V_a - V_b = V_{nodo} - I_{R2} \times R_2 = 24 - 0 \times 3 = 24\text{ V}$$

Hmm, reconsideremos la topología. Con a-b abierto:
- El nodo tiene potencial V_n
- $I_{R1} + I_{R3} = 4A$ ([LCK](../../../glossary.md#lck))
- $I_{R1} = V_n/R_1$... 

Revisión: La fuente de corriente tiene su terminal + arriba.
$$I_s = I_{R1} = 4\text{ A (toda por R1 si R3 está en la malla)}$$

$$V_n = I_s \times R_1 = 4 \times 6 = 24\text{ V}$$

Pero R₃ también está conectado:
$$V_n = I_{R1} \times R_1 = I_{R3} \times R_3$$

Esto no es posible a menos que estén en paralelo...

**Reinterpretación del circuito:**
```
    ●───────●─────/\/\/─────●───/\/\/───●a
    │       │      R₁=6Ω    │    R₂=3Ω   
  ┌─┴─┐     │             ┌─┴─┐          
  │Is │     │             │R₃ │          
  │4A │     │             │6Ω │          
  └─┬─┘     │             └─┬─┘          
    │       │               │            
    └───────●───────────────●───────────●b
```

En esta configuración, R₁ está entre la fuente y el nodo central:
$$V_{nodo} = 4 \times (R_1 \| R_3) = 4 \times \frac{6 \times 6}{12} = 4 \times 3 = 12\text{ V}$$

Con circuito abierto:
$$V_{th} = V_{nodo} = 12\text{ V}$$

#### **Rth (desactivar Is)**
Fuente de corriente → circuito abierto

$$R_{th} = (R_1 \| R_3) + R_2 = 3 + 3 = 6\text{ Ω}$$

### Respuesta
$$\boxed{V_{th} = 12\text{ V}, \quad R_{th} = 6\text{ Ω}}$$

---

## Ejemplo Clásico 3: Usando Corriente de Cortocircuito

### Enunciado
Calcule Vth y Rth usando el método de cortocircuito.

### Diagrama
```
            R₁=2Ω           R₂=4Ω
    ●────────/\/\/────●────/\/\/────●a
    │                 │              
  + │               ┌─┴─┐            
 12V│               │R₃ │     Isc→   
    │               │4Ω │            
  - │               └─┬─┘            
    │                 │              
    └─────────────────●─────────────●b
```

### Solución

#### **Paso 1: Vth (circuito abierto)**
Sin corriente en R₂:
$$I = \frac{12}{R_1 + R_3} = \frac{12}{2 + 4} = 2\text{ A}$$
$$V_{th} = I \times R_3 = 2 \times 4 = 8\text{ V}$$

#### **Paso 2: Isc (cortocircuito a-b)**
```
            R₁=2Ω           R₂=4Ω
    ●────────/\/\/────●────/\/\/────●a
    │                 │              │
  + │               ┌─┴─┐            │
 12V│               │R₃ │     Isc→   │
    │               │4Ω │            │
  - │               └─┬─┘            │
    │                 │              │
    └─────────────────●──────────────●b
                          Cortocircuito
```

R₂ y R₃ están en paralelo:
$$R_{23} = \frac{4 \times 4}{4 + 4} = 2\text{ Ω}$$

Corriente total:
$$I_T = \frac{12}{R_1 + R_{23}} = \frac{12}{2 + 2} = 3\text{ A}$$

Corriente de cortocircuito (por R₂):
$$I_{sc} = I_T \times \frac{R_3}{R_2 + R_3} = 3 \times \frac{4}{8} = 1.5\text{ A}$$

#### **Paso 3: Rth**
$$R_{th} = \frac{V_{th}}{I_{sc}} = \frac{8}{1.5} = 5.33\text{ Ω}$$

#### **Verificación (desactivando fuentes)**
$$R_{th} = R_2 + (R_1 \| R_3) = 4 + \frac{2 \times 4}{6} = 4 + 1.33 = 5.33\text{ Ω}$$ ✓

### Respuesta
$$\boxed{V_{th} = 8\text{ V}, \quad R_{th} = 5.33\text{ Ω}}$$

### Explicación de la Respuesta
El método de cortocircuito es especialmente útil cuando hay fuentes dependientes (donde no podemos simplemente desactivar fuentes). Siempre se cumple que $R_{th} = V_{th}/I_{sc}$.

---

## Aplicación: Cálculo con Carga

Una vez obtenido el equivalente de Thévenin:

$$I_L = \frac{V_{th}}{R_{th} + R_L}$$

$$V_L = I_L \times R_L = V_{th} \times \frac{R_L}{R_{th} + R_L}$$

$$P_L = I_L^2 \times R_L = \frac{V_{th}^2 \times R_L}{(R_{th} + R_L)^2}$$

### Máxima Transferencia de Potencia
Ocurre cuando: $R_L = R_{th}$
$$P_{max} = \frac{V_{th}^2}{4R_{th}}$$

---

## Resumen: Cuándo Usar Cada Método

| Método para Rth | Cuándo usar |
|-----------------|-------------|
| Desactivar fuentes | Solo fuentes independientes |
| Vth/Isc | Siempre funciona, especialmente con fuentes dependientes |
| Fuente de prueba | Alternativa con fuentes dependientes |

## Errores Comunes
1. Olvidar que Vth es con circuito ABIERTO
2. Confundir cortocircuito con circuito abierto
3. No desactivar correctamente las fuentes
4. Calcular Rth incluyendo la carga
