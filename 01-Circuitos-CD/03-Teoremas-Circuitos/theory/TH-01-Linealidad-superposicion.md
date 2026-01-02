# TH-01: Linealidad y Superposición

## Objetivos
- Comprender el concepto de linealidad en circuitos
- Aplicar el principio de [superposición](../../../glossary.md#superposicion)
- Identificar las limitaciones del principio

## Contenido

### Linealidad

Un [circuito](../../../glossary.md#circuito) es **lineal** si cumple dos propiedades:

**1. Homogeneidad (escalamiento):**
Si una entrada x produce una respuesta y, entonces una entrada kx produce una respuesta ky.
$$f(kx) = k \cdot f(x)$$

**2. Aditividad:**
Si x₁ produce y₁ y x₂ produce y₂, entonces x₁ + x₂ produce y₁ + y₂.
$$f(x_1 + x_2) = f(x_1) + f(x_2)$$

### Elementos Lineales
- Resistores (R constante)
- Capacitores (C constante)
- Inductores (L constante)
- Fuentes dependientes lineales

### Principio de Superposición

> En un circuito lineal con múltiples fuentes independientes, la respuesta en cualquier elemento es la suma algebraica de las respuestas causadas por cada fuente actuando sola.

### Procedimiento

1. **Desactivar** todas las fuentes excepto una:
   - Fuente de [voltaje](../../../glossary.md#voltaje): reemplazar por cortocircuito
   - Fuente de [corriente](../../../glossary.md#corriente): reemplazar por circuito abierto
   
2. **Calcular** la respuesta debida a esa fuente

3. **Repetir** para cada fuente independiente

4. **Sumar** todas las respuestas parciales

### Ejemplo

```
    R₁=2Ω      R₂=4Ω
 ○──/\/\/──○──/\/\/──○
 │                   │
10V                 2A↓
 │                   │
 ○───────────────────○
```

**Paso 1: Solo fuente de 10V (I₂=0)**
- Circuito abierto donde estaba I₂
- i'ᵣ₁ = 10/(2+4) = 1.67A

**Paso 2: Solo fuente de 2A (V₁=0)**
- Cortocircuito donde estaba V₁
- i''ᵣ₁ = 2 × 4/(2+4) = 1.33A ([divisor de corriente](../../../glossary.md#divisor-corriente))

**Paso 3: Sumar**
- iᵣ₁ = i'ᵣ₁ + i''ᵣ₁ = 1.67 + 1.33 = 3A

### Limitaciones

- **No aplica a potencia:** P ≠ P₁ + P₂ (porque P = I²R)
- **Solo para respuestas lineales:** voltaje, corriente
- **Solo fuentes independientes:** las dependientes permanecen activas

## Conceptos Clave
- Linealidad = homogeneidad + aditividad
- Desactivar vs eliminar fuentes
- No usar superposición para potencia
