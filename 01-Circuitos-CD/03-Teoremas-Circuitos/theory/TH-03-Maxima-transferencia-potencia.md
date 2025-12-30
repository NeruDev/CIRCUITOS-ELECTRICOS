# TH-03: Teorema de Máxima Transferencia de Potencia

## Objetivos
- Determinar la condición de máxima transferencia de potencia
- Calcular la potencia máxima transferida a una carga
- Entender el compromiso entre eficiencia y potencia máxima

## Contenido

### Planteamiento del Problema

Dado un circuito con equivalente de Thévenin (Vₜₕ, Rₜₕ) conectado a una carga RL, ¿cuál es el valor de RL que maximiza la potencia entregada a la carga?

```
     Rₜₕ
○───/\/\/───┬───○
            │
   Vₜₕ     RL
            │
○───────────┴───○
```

### Teorema

> La máxima potencia se transfiere a la carga cuando la resistencia de carga es igual a la resistencia de Thévenin del circuito fuente.

$$R_L = R_{th}$$

### Demostración

La corriente en el circuito:
$$i = \frac{V_{th}}{R_{th} + R_L}$$

Potencia en la carga:
$$P_L = i^2 R_L = \frac{V_{th}^2 \cdot R_L}{(R_{th} + R_L)^2}$$

Para encontrar el máximo, derivamos e igualamos a cero:
$$\frac{dP_L}{dR_L} = 0$$

Resolviendo:
$$R_L = R_{th}$$

### Potencia Máxima

Cuando RL = Rₜₕ:

$$P_{max} = \frac{V_{th}^2}{4R_{th}}$$

### Eficiencia en Máxima Transferencia

$$\eta = \frac{P_L}{P_{total}} = \frac{P_L}{P_L + P_{R_{th}}}$$

En máxima transferencia de potencia:
$$\eta = \frac{P_{max}}{2P_{max}} = 50\%$$

### Curva de Potencia vs Resistencia de Carga

```
P
│    ╭──╮
│   ╱    ╲
│  ╱      ╲
│ ╱        ╲
│╱          ╲
└────────────────── RL
         Rₜₕ
```

La potencia es máxima cuando RL = Rₜₕ

### Ejemplo

**Datos:**
- Vₜₕ = 12V
- Rₜₕ = 3Ω

**Solución:**
- RL óptima = 3Ω
- i = 12/(3+3) = 2A
- Pmax = (12)²/(4×3) = 144/12 = 12W

**Verificación:**
- PL = (2)² × 3 = 12W ✓

### Aplicaciones Prácticas

1. **Audio:** Impedancia de altavoces = impedancia de salida del amplificador
2. **Comunicaciones:** Adaptación de impedancias en líneas de transmisión
3. **Electrónica:** Diseño de etapas de potencia

### Consideraciones

- En sistemas de potencia, la eficiencia es más importante que la máxima transferencia
- En sistemas de señal, la máxima transferencia puede ser prioritaria
- El 50% de eficiencia significa que la fuente disipa igual potencia que la carga

## Conceptos Clave
- Condición: RL = Rₜₕ
- Pmax = Vₜₕ²/(4Rₜₕ)
- Eficiencia = 50% en máxima transferencia
