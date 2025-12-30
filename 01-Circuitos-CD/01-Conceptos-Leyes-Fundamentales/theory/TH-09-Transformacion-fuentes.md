# TH-09: Transformación de Fuentes

## Objetivos
- Comprender la equivalencia entre fuentes de voltaje y corriente
- Realizar transformaciones de fuentes
- Simplificar circuitos usando transformaciones

## Contenido

### Principio de Equivalencia

Una fuente de voltaje Vs en serie con una resistencia Rs es equivalente a una fuente de corriente Is en paralelo con la misma resistencia Rs.

### Transformación de Fuente de Voltaje a Corriente

```
Fuente de Voltaje:           Fuente de Corriente:
    Rs                            
+──/\/\/──○ a               ┌──○ a
│                           │
Vs                    Is ↑  ═  Rs
│                           │
└─────────○ b               └──○ b
```

**Relación:**
$$I_s = \frac{V_s}{R_s}$$

La resistencia Rs permanece igual, pero cambia de serie a paralelo.

### Transformación de Fuente de Corriente a Voltaje

**Relación:**
$$V_s = I_s \cdot R_s$$

La resistencia Rs permanece igual, pero cambia de paralelo a serie.

### Condiciones para la Transformación

1. La fuente debe tener una resistencia asociada (interna)
2. Las fuentes ideales (sin resistencia) no se pueden transformar:
   - Fuente de voltaje ideal: Rs = 0
   - Fuente de corriente ideal: Rs = ∞

### Procedimiento de Simplificación

1. Identificar fuentes con resistencias asociadas
2. Transformar fuentes según convenga (todas a voltaje o todas a corriente)
3. Combinar fuentes y resistencias equivalentes
4. Resolver el circuito simplificado

### Ejemplo de Aplicación

**Circuito original:**
```
    2Ω            4Ω
+──/\/\/──┬──○──/\/\/──┐
│         │            │
12V      3A↑          RL
│         │            │
└─────────┴────────────┘
```

**Paso 1:** Transformar fuente de voltaje a corriente
- Is = 12V/2Ω = 6A

**Paso 2:** Combinar fuentes de corriente en paralelo
- I_total = 6A + 3A = 9A (si están en el mismo sentido)

**Paso 3:** Combinar resistencias en paralelo
- Req = 2Ω || 4Ω = 8/6 = 1.33Ω

### Aplicaciones

- Simplificación de circuitos complejos
- Análisis de circuitos con múltiples fuentes
- Obtención de equivalentes de Thévenin y Norton

## Conceptos Clave
- Equivalencia de fuentes
- Conservación de la potencia máxima disponible
- Limitaciones de fuentes ideales
