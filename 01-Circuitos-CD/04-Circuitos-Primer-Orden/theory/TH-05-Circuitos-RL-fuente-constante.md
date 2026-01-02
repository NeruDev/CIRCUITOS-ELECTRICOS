# TH-05: Análisis de Circuitos RL con Fuente Constante

## Objetivos
- Analizar circuitos RL con fuente de [voltaje](../../../glossary.md#voltaje) DC
- Calcular la respuesta completa
- Determinar condiciones iniciales y finales

## Contenido

### Circuito RL con Fuente DC

```
    t=0
  ○──/──┬──/\/\/──○
  │     │    R    │
  V     │         │
  │     L         │
  ○─────┴─────────○
```

En t = 0, se conecta una fuente V al [circuito](../../../glossary.md#circuito) RL.

### Ecuación Diferencial

$$V = L\frac{di}{dt} + Ri$$

Ecuación diferencial de primer orden no homogénea.

### Solución General

$$i(t) = i_f + (i_0 - i_f)e^{-t/\tau}$$

Donde:
- i₀ = [corriente](../../../glossary.md#corriente) inicial (t = 0⁻)
- i_f = corriente final (t → ∞)
- τ = L/R

### Valores Inicial y Final

**Valor inicial i(0⁺):**
- La corriente en el [inductor](../../../glossary.md#inductancia) no puede cambiar instantáneamente
- i(0⁺) = i(0⁻)

**Valor final i(∞):**
- En estado estable, el inductor es un cortocircuito
- i(∞) = V/R

### Respuesta para i(0⁻) = 0

$$i(t) = \frac{V}{R}(1 - e^{-t/\tau})$$

### Voltaje en el Inductor

$$v_L(t) = L\frac{di}{dt} = Ve^{-t/\tau}$$

### Voltaje en el Resistor

$$v_R(t) = Ri(t) = V(1 - e^{-t/\tau})$$

### Gráficas

```
i(t)                          v_L(t)
│      ___________            │
│    ╱                        V├──╮
│  ╱                          │   ╲
V/R├                           │     ╲___
│                             │          ──
0└────────────── t            0└────────────── t
     τ    2τ                       τ    2τ
```

### Procedimiento de Análisis

1. Encontrar i(0⁺) = i(0⁻) (continuidad)
2. Encontrar i(∞) (análisis DC, L = corto)
3. Calcular τ = L/R_eq
4. Aplicar: i(t) = i(∞) + [i(0⁺) - i(∞)]e^(-t/τ)

### Ejemplo

**Datos:** V = 12V, R = 4Ω, L = 2H, i(0⁻) = 0

**Solución:**
- i(0⁺) = 0
- i(∞) = 12/4 = 3A
- τ = 2/4 = 0.5s
- i(t) = 3(1 - e^(-2t)) A

## Conceptos Clave
- Continuidad de corriente en L
- En DC estable: L = cortocircuito
- Forma general de la respuesta
