# TH-06: Teorema de Superposición en CA

## Objetivos
- Aplicar superposición a circuitos CA
- Manejar fuentes de diferente frecuencia
- Sumar respuestas en el dominio del tiempo

## Contenido

### Principio de Superposición en CA

En un circuito lineal con múltiples fuentes CA, la respuesta total es la suma de las respuestas debidas a cada fuente actuando sola.

### Procedimiento (Fuentes de Misma Frecuencia)

1. **Desactivar** todas las fuentes excepto una
2. **Calcular** la respuesta fasorial debida a esa fuente
3. **Repetir** para cada fuente
4. **Sumar** las respuestas fasoriales

$$\mathbf{V}_{total} = \mathbf{V}_1 + \mathbf{V}_2 + ... + \mathbf{V}_n$$

### Procedimiento (Fuentes de Diferente Frecuencia)

⚠️ **No se pueden sumar fasores de diferente frecuencia.**

1. Para cada frecuencia, resolver el circuito separadamente
2. Obtener la respuesta en el dominio del tiempo para cada frecuencia
3. Sumar las respuestas en el dominio del tiempo

$$v(t) = v_1(t) + v_2(t) + ... + v_n(t)$$

### Desactivar Fuentes

**Fuente de voltaje AC:** Reemplazar por cortocircuito
**Fuente de corriente AC:** Reemplazar por circuito abierto
**Fuente DC:** Se trata como CA con ω = 0

### Ejemplo: Misma Frecuencia

```
       Z=10Ω
    ○───/\/\/───○
    │           │
Vs₁=20∠0°   Vs₂=10∠90°
    │           │
    ○───────────○
```

**Con solo Vs₁:**
$$\mathbf{I}_1 = \frac{20\angle 0° - 10\angle 90°}{10} = \frac{20 - j10}{10}$$

Pero aquí tenemos un error de planteamiento. Mejor ejemplo:

```
       Z₁=10Ω     Z₂=j10Ω
    ○───/\/\/───┬───⌇⌇⌇───○
    │           │         │
Vs₁=20∠0°      │     Vs₂=10∠90°
    │          Z₃=5Ω      │
    │           │         │
    ○───────────┴─────────○
```

**Paso 1: Solo Vs₁ (Vs₂ = 0)**
Calcular V₃' en Z₃

**Paso 2: Solo Vs₂ (Vs₁ = 0)**
Calcular V₃'' en Z₃

**Paso 3: Sumar**
$$\mathbf{V}_3 = \mathbf{V}_3' + \mathbf{V}_3''$$

### Ejemplo: Diferente Frecuencia

Circuito con:
- Vs₁ = 10 cos(100t) V
- Vs₂ = 5 cos(200t) V

**No se pueden sumar fasores porque ω₁ ≠ ω₂**

**Solución:**
1. Resolver para ω = 100 rad/s → v₁(t)
2. Resolver para ω = 200 rad/s → v₂(t)
3. v(t) = v₁(t) + v₂(t) (suma en dominio del tiempo)

### Caso Especial: CA + DC

Si hay fuentes DC y AC:
1. Para DC (ω = 0): C = abierto, L = corto
2. Para AC: análisis fasorial normal
3. Sumar en el dominio del tiempo

### Potencia con Superposición

⚠️ **La potencia NO se calcula por superposición directa.**

Para calcular potencia total:
1. Encontrar v(t) e i(t) totales
2. Calcular P = (1/T)∫v(t)·i(t)dt

## Conceptos Clave
- Misma frecuencia: sumar fasores
- Diferente frecuencia: sumar en tiempo
- Potencia no se superpone
