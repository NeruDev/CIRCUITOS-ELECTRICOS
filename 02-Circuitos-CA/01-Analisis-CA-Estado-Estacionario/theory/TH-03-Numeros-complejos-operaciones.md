# TH-03: Representación y Operaciones con Números Complejos

## Objetivos
- Representar números complejos en diferentes formas
- Realizar operaciones aritméticas con complejos
- Aplicar números complejos al análisis de CA

## Contenido

### Definición

Un número complejo tiene la forma:
$$z = a + jb$$

Donde:
- a = parte real: Re{z}
- b = parte imaginaria: Im{z}
- j = √(-1) (unidad imaginaria, en ingeniería)

### Formas de Representación

**Forma rectangular:**
$$z = a + jb$$

**Forma polar:**
$$z = r\angle\theta = r e^{j\theta}$$

Donde:
- r = |z| = √(a² + b²) = magnitud o módulo
- θ = arctan(b/a) = argumento o ángulo

**Forma exponencial (Euler):**
$$z = r e^{j\theta}$$

$$e^{j\theta} = \cos\theta + j\sin\theta$$

### Conversión entre Formas

**Rectangular a Polar:**
$$r = \sqrt{a^2 + b^2}$$
$$\theta = \arctan\left(\frac{b}{a}\right)$$

**Polar a Rectangular:**
$$a = r\cos\theta$$
$$b = r\sin\theta$$

### Operaciones Básicas

**Conjugado:**
$$z^* = a - jb = r\angle(-\theta)$$

**Suma/Resta (mejor en rectangular):**
$$(a_1 + jb_1) + (a_2 + jb_2) = (a_1 + a_2) + j(b_1 + b_2)$$

**Multiplicación (mejor en polar):**
$$(r_1\angle\theta_1) \cdot (r_2\angle\theta_2) = r_1 r_2 \angle(\theta_1 + \theta_2)$$

**División (mejor en polar):**
$$\frac{r_1\angle\theta_1}{r_2\angle\theta_2} = \frac{r_1}{r_2} \angle(\theta_1 - \theta_2)$$

### Plano Complejo

```
      Im
       │
       │    •z = a + jb
     b ├────╱
       │   ╱ θ
───────┼──╱──────── Re
       │  a
       │
```

### Propiedades Útiles

$$j^2 = -1$$
$$j^3 = -j$$
$$j^4 = 1$$

$$\frac{1}{j} = -j$$

$$e^{j90°} = j$$
$$e^{-j90°} = -j$$

### Ejemplos

**Ejemplo 1:** Convertir z = 3 + j4 a polar
- r = √(9 + 16) = 5
- θ = arctan(4/3) = 53.13°
- z = 5∠53.13°

**Ejemplo 2:** Multiplicar (3∠30°)(4∠45°)
- z = 12∠75°

**Ejemplo 3:** Dividir (10∠60°)/(2∠15°)
- z = 5∠45°

### Aplicación en CA

Las señales senoidales se representan como:
$$v(t) = V_m \cos(\omega t + \phi) \leftrightarrow \mathbf{V} = V_m\angle\phi$$

Esto permite usar álgebra compleja en lugar de ecuaciones diferenciales.

## Conceptos Clave
- Suma/resta: usar forma rectangular
- Multiplicación/división: usar forma polar
- j² = -1 es fundamental
