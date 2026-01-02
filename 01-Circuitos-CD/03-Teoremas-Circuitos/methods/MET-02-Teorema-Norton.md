# MET-02: Método del Equivalente de Norton

## Descripción del Método

El **[Teorema de](../../../glossary.md#norton) Norton** establece que cualquier [circuito](../../../glossary.md#circuito) lineal de dos terminales puede ser reemplazado por un circuito equivalente que consiste en:
- Una **fuente de [corriente](../../../glossary.md#corriente)** In (corriente de Norton)
- Una **[resistencia](../../../glossary.md#resistencia) en paralelo** Rn (resistencia de Norton)

### Relación con Thévenin
Los equivalentes de [Thévenin](../../../glossary.md#thevenin) y Norton son **duales**:
$$I_n = \frac{V_{th}}{R_{th}}$$
$$R_n = R_{th}$$

```
  Thévenin              Norton
     Rth                 
a●───/\/\/───┬      a●───┬───●
             │           │
          +  │         ┌─┴─┐
         Vth ─┴─       │In │ Rn
          -  │         └─┬─┘
             │           │
b●───────────┘      b●───┴───●
```

---

## Fórmulas Fundamentales

$$I_n = I_{sc} \text{ (corriente de cortocircuito entre a-b)}$$

$$R_n = R_{th} = \frac{V_{oc}}{I_{sc}}$$

---

## Pasos del Método

### Paso 1: Identificar los Terminales
- Seleccionar los dos terminales (a, b)
- Remover la [carga](../../../glossary.md#carga)

### Paso 2: Calcular In (Corriente de Norton)
- **Cortocircuitar** los terminales a-b
- Calcular la corriente que fluye de a hacia b: $I_n = I_{sc}$

### Paso 3: Calcular Rn (Resistencia de Norton)
**Método A:** Desactivar todas las fuentes independientes y calcular Req desde a-b

**Método B:** $R_n = V_{oc} / I_{sc}$ (donde Voc es el [voltaje](../../../glossary.md#voltaje) en circuito abierto)

### Paso 4: Dibujar el Circuito Equivalente

```
    a●───────┬───────●
             │
           ┌─┴─┐
           │In │  Rn
           │ ↑ ├──/\/\/──┐
           └─┬─┘         │
             │           │
    b●───────┴───────────┘
```

---

## Ejemplo Clásico 1: Circuito con Fuente de Voltaje

### Enunciado
Encuentre el equivalente de Norton visto desde los terminales a-b.

### Diagrama
```
            R₁=6Ω           R₂=12Ω
    ●────────/\/\/────●────/\/\/────●a
    │                 │              
  + │               ┌─┴─┐            
 24V│               │R₃ │            
    │               │4Ω │            
  - │               └─┬─┘            
    │                 │              
    └─────────────────●─────────────●b
```

### Solución Paso a Paso

#### **Paso 1: Calcular In (cortocircuito a-b)**

```
            R₁=6Ω           R₂=12Ω
    ●────────/\/\/────●────/\/\/────●a
    │                 │              │
  + │               ┌─┴─┐            │
 24V│               │R₃ │     In →   │
    │               │4Ω │            │
  - │               └─┬─┘            │
    │                 │              │
    └─────────────────●──────────────●b
                          Cortocircuito
```

Con a-b cortocircuitado, R₂ y R₃ están en paralelo:
$$R_{23} = \frac{12 \times 4}{12 + 4} = \frac{48}{16} = 3\text{ Ω}$$

Corriente total de la fuente:
$$I_T = \frac{24}{R_1 + R_{23}} = \frac{24}{6 + 3} = \frac{24}{9} = 2.667\text{ A}$$

Corriente de Norton (por R₂, usando [divisor de corriente](../../../glossary.md#divisor-corriente)):
$$I_n = I_T \times \frac{R_3}{R_2 + R_3} = 2.667 \times \frac{4}{12 + 4} = 2.667 \times \frac{4}{16}$$
$$I_n = 2.667 \times 0.25 = 0.667\text{ A}$$

#### **Paso 2: Calcular Rn (desactivar fuente de 24V)**

```
            R₁=6Ω           R₂=12Ω
    ●────────/\/\/────●────/\/\/────●a
    │                 │              
    │               ┌─┴─┐        Rn  
●───●               │R₃ │        ←   
Cortocircuito       │4Ω │            
    │               └─┬─┘            
    │                 │              
    └─────────────────●─────────────●b
```

Desde a-b:
- R₁ y R₃ están en paralelo: $R_{13} = \frac{6 \times 4}{6 + 4} = 2.4$ Ω
- En serie con R₂: $R_n = R_{13} + R_2 = 2.4 + 12 = 14.4$ Ω

#### **Paso 3: Verificación con Vth**

Calculemos Vth para verificar:
$$V_{th} = I_n \times R_n = 0.667 \times 14.4 = 9.6\text{ V}$$

Verificación directa (circuito abierto):
$$I = \frac{24}{6 + 4} = 2.4\text{ A}$$
$$V_{th} = I \times R_3 = 2.4 \times 4 = 9.6\text{ V}$$ ✓

#### **Paso 4: Circuito Equivalente de Norton**

```
    a●───────┬────────────●
             │
           ┌─┴─┐    Rn=14.4Ω
           │In │    
           │0.667A├──/\/\/──┐
           │ ↑  │           │
           └─┬─┘            │
             │              │
    b●───────┴──────────────┘
```

### Respuesta
$$\boxed{I_n = 0.667\text{ A} = \frac{2}{3}\text{ A}, \quad R_n = 14.4\text{ Ω}}$$

### Explicación de la Respuesta
El equivalente de Norton representa el circuito como una fuente de corriente de 0.667 A con una resistencia de 14.4 Ω en paralelo. Cualquier carga conectada entre a-b "compartirá" esta corriente con Rn según el divisor de corriente.

---

## Ejemplo Clásico 2: Conversión Thévenin-Norton

### Enunciado
Dado el circuito de Thévenin, encuentre su equivalente de Norton.

### Diagrama Thévenin
```
       Rth=10Ω
    a●───/\/\/───┬───●
                 │
              +  │
             20V ─┴─
              -  │
                 │
    b●───────────┴───●
```

### Solución

#### **Corriente de Norton**
$$I_n = \frac{V_{th}}{R_{th}} = \frac{20}{10} = 2\text{ A}$$

#### **Resistencia de Norton**
$$R_n = R_{th} = 10\text{ Ω}$$

#### **Circuito Equivalente de Norton**
```
    a●───────┬──────────●
             │
           ┌─┴─┐   Rn=10Ω
           │In │    
           │2A ├──/\/\/──┐
           │ ↑ │         │
           └─┬─┘         │
             │           │
    b●───────┴───────────┘
```

### Respuesta
$$\boxed{I_n = 2\text{ A}, \quad R_n = 10\text{ Ω}}$$

### Explicación de la Respuesta
La conversión es directa: dividir Vth entre Rth da In. La resistencia se mantiene igual pero pasa de estar en serie (Thévenin) a estar en paralelo (Norton). Ambos equivalentes producen exactamente la misma corriente y voltaje en cualquier carga.

---

## Ejemplo Clásico 3: Circuito con Fuente de Corriente

### Enunciado
Determine el equivalente de Norton.

### Diagrama
```
                  R₁=4Ω      
    ●──────●──────/\/\/──────●a
    │      │                  
  ┌─┴─┐  ┌─┴─┐               
  │Is │  │R₂ │               
  │6A │  │12Ω│               
  └─┬─┘  └─┬─┘               
    │      │                  
    └──────●─────────────────●b
```

### Solución

#### **In (cortocircuito a-b)**

Con a-b cortocircuitado, R₁ está en cortocircuito → V = 0 en R₁

```
                  R₁=4Ω      
    ●──────●──────/\/\/──────●a
    │      │                 │
  ┌─┴─┐  ┌─┴─┐               │
  │Is │  │R₂ │      In →     │
  │6A │  │12Ω│               │
  └─┬─┘  └─┬─┘               │
    │      │                 │
    └──────●─────────────────●b
                 Cortocircuito
```

La corriente de 6A se divide entre R₂ y el cortocircuito (R₁ en serie con cortocircuito = R₁):
$$I_n = 6 \times \frac{R_2}{R_1 + R_2} = 6 \times \frac{12}{4 + 12} = 6 \times \frac{12}{16} = 4.5\text{ A}$$

#### **Rn (desactivar Is)**

Fuente de corriente → circuito abierto:
```
                  R₁=4Ω      
    ●──────●──────/\/\/──────●a
    │      │                  
    ○    ┌─┴─┐          Rn   
 Abierto │R₂ │          ←    
         │12Ω│               
         └─┬─┘               
           │                  
    ●──────●─────────────────●b
```

$$R_n = R_1 + R_2 = 4 + 12 = 16\text{ Ω}$$

#### **Verificación**
$$V_{th} = I_n \times R_n = 4.5 \times 16 = 72\text{ V}$$

Comprobación directa (circuito abierto):
Los 6A pasan todos por R₂:
$$V_{th} = 6 \times R_2 = 6 \times 12 = 72\text{ V}$$ ✓

### Respuesta
$$\boxed{I_n = 4.5\text{ A}, \quad R_n = 16\text{ Ω}}$$

---

## Análisis con Carga Usando Norton

Una vez obtenido el equivalente:

$$I_L = I_n \times \frac{R_n}{R_n + R_L}$$ (divisor de corriente)

$$V_L = I_L \times R_L = I_n \times \frac{R_n \times R_L}{R_n + R_L}$$

### Ejemplo de Aplicación

Dado In = 4.5 A y Rn = 16 Ω, calcular IL para RL = 8 Ω:

$$I_L = 4.5 \times \frac{16}{16 + 8} = 4.5 \times \frac{16}{24} = 4.5 \times \frac{2}{3} = 3\text{ A}$$

$$V_L = 3 \times 8 = 24\text{ V}$$

---

## Comparación: Thévenin vs Norton

| Característica | Thévenin | Norton |
|---------------|----------|--------|
| Fuente | Voltaje (Vth) | Corriente (In) |
| Resistencia | En serie (Rth) | En paralelo (Rn) |
| Ideal para | Cargas en serie | Cargas en paralelo |
| Comportamiento límite | RL→∞: VL = Vth | RL→0: IL = In |

### Cuándo Usar Cada Uno

| Situación | Mejor opción |
|-----------|--------------|
| Carga variable en serie | Thévenin |
| Carga variable en paralelo | Norton |
| Análisis de corriente | Norton |
| Análisis de voltaje | Thévenin |
| Fuentes de corriente dominantes | Norton |
| Fuentes de voltaje dominantes | Thévenin |

---

## Resumen de Conversiones

### Thévenin → Norton
$$I_n = \frac{V_{th}}{R_{th}}$$
$$R_n = R_{th}$$

### Norton → Thévenin
$$V_{th} = I_n \times R_n$$
$$R_{th} = R_n$$

## Errores Comunes
1. Confundir el sentido de la corriente In
2. Olvidar que In es la corriente de CORTOCIRCUITO
3. Colocar Rn en serie en lugar de paralelo
4. No verificar la relación Vth = In × Rn
