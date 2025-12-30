# TH-07: Análisis de Circuitos RL y RC con Fuentes Constantes

## Objetivos
- Aplicar un método general para circuitos de primer orden
- Resolver circuitos RL y RC con cualquier condición inicial
- Analizar circuitos con conmutación

## Contenido

### Método General de Solución

Para cualquier circuito de primer orden con fuente constante:

$$x(t) = x(\infty) + [x(0^+) - x(\infty)]e^{-t/\tau}$$

Donde x puede ser voltaje o corriente.

### Pasos del Método

**Paso 1:** Determinar x(0⁺)
- Para capacitor: v_C(0⁺) = v_C(0⁻)
- Para inductor: i_L(0⁺) = i_L(0⁻)

**Paso 2:** Determinar x(∞)
- Analizar circuito en estado estable
- C → circuito abierto
- L → cortocircuito

**Paso 3:** Calcular τ
- τ = R_eq·C (circuito RC)
- τ = L/R_eq (circuito RL)
- R_eq: resistencia vista por L o C

**Paso 4:** Aplicar la fórmula general

### Circuito RC con Fuente Constante

```
    t=0
Vs──/──R──┬──○
          │
          C  v_C
          │
──────────┴──○
```

$$v_C(t) = V_s + [v_C(0^+) - V_s]e^{-t/RC}$$

**Si v_C(0⁻) = 0:**
$$v_C(t) = V_s(1 - e^{-t/RC})$$

### Circuito RL con Fuente Constante

```
    t=0
Vs──/──R──┬──○
          │
          L  i_L
          │
──────────┴──○
```

$$i_L(t) = \frac{V_s}{R} + [i_L(0^+) - \frac{V_s}{R}]e^{-Rt/L}$$

**Si i_L(0⁻) = 0:**
$$i_L(t) = \frac{V_s}{R}(1 - e^{-t/\tau})$$

### Circuitos con Conmutación

Cuando hay cambio de estado en t = t₀:

$$x(t) = x(\infty) + [x(t_0^+) - x(\infty)]e^{-(t-t_0)/\tau}$$

### Ejemplo Completo

**Circuito:**
```
    t=0         4Ω
12V──/──┬──/\/\/──┐
        │         │
      0.5F       6Ω
        │         │
────────┴─────────┘
```
v_C(0⁻) = 6V

**Solución:**

1. **v_C(0⁺)** = v_C(0⁻) = 6V

2. **v_C(∞):** Divisor de voltaje
   - v_C(∞) = 12 × 6/(4+6) = 7.2V

3. **τ:** R_eq vista por C
   - R_eq = 4||6 = 2.4Ω
   - τ = 2.4 × 0.5 = 1.2s

4. **Respuesta:**
$$v_C(t) = 7.2 + (6 - 7.2)e^{-t/1.2}$$
$$v_C(t) = 7.2 - 1.2e^{-t/1.2} \text{ V}$$

### Resumen de Fórmulas por Tipo

| Circuito | τ | x(∞) |
|----------|---|------|
| RC serie | RC | Divisor/circuito DC |
| RL serie | L/R | Divisor/circuito DC |

## Conceptos Clave
- Método de tres pasos: x(0⁺), x(∞), τ
- R_eq vista desde L o C
- Continuidad de variables de estado
