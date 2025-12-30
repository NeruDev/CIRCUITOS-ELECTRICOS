# TH-02: Corrección del Factor de Potencia

## Objetivos
- Comprender la importancia del factor de potencia
- Calcular capacitores para corrección
- Analizar beneficios económicos de la corrección

## Contenido

### Importancia del Factor de Potencia

Un factor de potencia bajo significa:
- Mayor corriente para la misma potencia útil
- Mayores pérdidas en líneas de transmisión
- Mayor capacidad requerida de generadores y transformadores
- Penalizaciones tarifarias de las compañías eléctricas

### Ejemplo del Problema

Para entregar P = 1000 W con V = 120 V:

| pf | I = P/(V·pf) | S = VI |
|-----|-------------|--------|
| 1.0 | 8.33 A | 1000 VA |
| 0.8 | 10.4 A | 1250 VA |
| 0.6 | 13.9 A | 1667 VA |

### Método de Corrección

Se agregan **capacitores en paralelo** con la carga para reducir la potencia reactiva.

```
        ┌──────┐
    ○───┤Carga ├───○
    │   │  ZL  │   │
    │   └──────┘   │
    │    ┌──┐      │
    └────┤C ├──────┘
         └──┘
```

### Cálculo del Capacitor

**Antes de la corrección:**
- P = potencia activa (no cambia)
- Q₁ = P tan(θ₁)
- pf₁ = cos(θ₁)

**Después de la corrección:**
- P = potencia activa (igual)
- Q₂ = P tan(θ₂)
- pf₂ = cos(θ₂) (nuevo, mejorado)

**Potencia reactiva del capacitor:**
$$Q_C = Q_1 - Q_2 = P(\tan\theta_1 - \tan\theta_2)$$

**Capacitancia requerida:**
$$C = \frac{Q_C}{\omega V_{rms}^2} = \frac{P(\tan\theta_1 - \tan\theta_2)}{\omega V_{rms}^2}$$

### Diagrama de Potencias

```
Antes:          Después:
    ╱│              │
  S₁╱ │Q₁          S₂│Q₂
  ╱   │            │
╱─────┘          ──┘
   P               P
```

El capacitor reduce Q sin cambiar P.

### Ejemplo de Cálculo

**Datos:**
- Carga: P = 10 kW, pf₁ = 0.7 atrasado
- Se desea: pf₂ = 0.95 atrasado
- V = 220 V, f = 60 Hz

**Solución:**

1. Ángulos:
   - θ₁ = arccos(0.7) = 45.6°
   - θ₂ = arccos(0.95) = 18.2°

2. Potencias reactivas:
   - Q₁ = 10000 × tan(45.6°) = 10,200 VAR
   - Q₂ = 10000 × tan(18.2°) = 3,290 VAR

3. QC del capacitor:
   - QC = 10,200 - 3,290 = 6,910 VAR

4. Capacitancia:
   - ω = 2π(60) = 377 rad/s
   - C = 6910 / (377 × 220²) = 379 μF

### Beneficios de la Corrección

1. **Reducción de corriente:** Menor I para misma P
2. **Reducción de pérdidas:** Pérdidas ∝ I² (menores pérdidas I²R)
3. **Liberación de capacidad:** Generadores y transformadores pueden entregar más potencia activa
4. **Ahorro económico:** Evita penalizaciones tarifarias

### Consideraciones Prácticas

- Se usan bancos de capacitores (varios capacitores)
- Pueden ser fijos o automáticos (conmutados)
- Ubicación: en la carga, en subestación, o centralizado
- Evitar sobrecorrección (pf adelantado)

### Corrección a pf = 1

$$Q_C = Q_1 = P \tan\theta_1$$

La potencia reactiva del capacitor debe igualar toda la Q de la carga.

## Conceptos Clave
- Capacitores en paralelo para corregir pf
- QC = P(tan θ₁ - tan θ₂)
- C = QC/(ωV²)
