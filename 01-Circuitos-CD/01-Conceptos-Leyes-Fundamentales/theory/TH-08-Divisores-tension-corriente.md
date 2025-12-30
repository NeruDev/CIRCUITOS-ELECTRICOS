# TH-08: Divisores de Tensión y Corriente

## Objetivos
- Aplicar el principio del divisor de tensión
- Aplicar el principio del divisor de corriente
- Resolver problemas prácticos usando divisores

## Contenido

### Divisor de Tensión

En un circuito serie, el voltaje se divide proporcionalmente a las resistencias.

```
      R₁           R₂
+──/\/\/──┬───/\/\/──┐
│         │          │
Vs       v₁         v₂
│                    │
└────────────────────┘
```

**Fórmula general:**
$$v_k = V_s \cdot \frac{R_k}{R_1 + R_2 + ... + R_n}$$

**Para dos resistencias:**
$$v_1 = V_s \cdot \frac{R_1}{R_1 + R_2}$$
$$v_2 = V_s \cdot \frac{R_2}{R_1 + R_2}$$

**Observación:** La resistencia mayor tiene el mayor voltaje.

### Divisor de Corriente

En un circuito paralelo, la corriente se divide inversamente proporcional a las resistencias.

```
        ┌──/\/\/──┐
        │   R₁    │i₁
   Is → ├──/\/\/──┤i₂
        │   R₂    │
        └─────────┘
```

**Para dos resistencias en paralelo:**
$$i_1 = I_s \cdot \frac{R_2}{R_1 + R_2}$$
$$i_2 = I_s \cdot \frac{R_1}{R_1 + R_2}$$

**Usando conductancias:**
$$i_k = I_s \cdot \frac{G_k}{G_1 + G_2 + ... + G_n}$$

**Observación:** La resistencia menor tiene la mayor corriente.

### Ejemplos Prácticos

**Ejemplo 1: Divisor de Tensión**
- Vs = 20V, R₁ = 4kΩ, R₂ = 6kΩ
- v₁ = 20 × 4/(4+6) = 20 × 0.4 = 8V
- v₂ = 20 × 6/(4+6) = 20 × 0.6 = 12V

**Ejemplo 2: Divisor de Corriente**
- Is = 10mA, R₁ = 2kΩ, R₂ = 3kΩ
- i₁ = 10 × 3/(2+3) = 10 × 0.6 = 6mA
- i₂ = 10 × 2/(2+3) = 10 × 0.4 = 4mA

### Aplicaciones

1. **Potenciómetros**: Divisores de tensión variables
2. **Atenuadores**: Reducción controlada de señales
3. **Redes de polarización**: En circuitos con transistores
4. **Medición de voltaje**: Voltímetros con resistencia interna

### Errores Comunes
- Olvidar que el divisor de corriente es inversamente proporcional
- No considerar la carga conectada al divisor
- Aplicar las fórmulas en circuitos que no son puramente serie o paralelo

## Conceptos Clave
- Proporcionalidad directa en divisor de tensión
- Proporcionalidad inversa en divisor de corriente
- Efecto de carga en divisores
