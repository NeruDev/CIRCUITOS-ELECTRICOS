# TH-01: Potencia Real, Reactiva, Aparente y Compleja. Triángulo de Potencias

## Objetivos
- Definir los diferentes tipos de potencia en CA
- Calcular potencia compleja
- Interpretar el triángulo de potencias

## Contenido

### Potencia Instantánea

Para v(t) = Vm cos(ωt + θv) e i(t) = Im cos(ωt + θi):

$$p(t) = v(t) \cdot i(t) = \frac{V_m I_m}{2}[\cos(\theta_v - \theta_i) + \cos(2\omega t + \theta_v + \theta_i)]$$

### Potencia Real (Activa) - P

La **potencia real** es el promedio de la potencia instantánea:

$$P = V_{rms} I_{rms} \cos\theta$$

Donde θ = θv - θi es el ángulo de desfase entre voltaje y corriente.

- **Unidad:** Watts (W)
- Representa la potencia que realiza trabajo útil
- Es la única potencia que se convierte en otras formas de energía

### Potencia Reactiva - Q

La **potencia reactiva** se asocia con elementos reactivos (L y C):

$$Q = V_{rms} I_{rms} \sin\theta$$

- **Unidad:** Volt-Ampere Reactivo (VAR)
- Q > 0: Carga inductiva (corriente atrasada)
- Q < 0: Carga capacitiva (corriente adelantada)
- No realiza trabajo útil; oscila entre fuente y carga

### Potencia Aparente - S

La **potencia aparente** es el producto de los valores RMS:

$$S = V_{rms} I_{rms}$$

- **Unidad:** Volt-Ampere (VA)
- Representa la capacidad de la fuente/línea
- S = √(P² + Q²)

### Potencia Compleja - S

La **potencia compleja** combina P y Q:

$$\mathbf{S} = P + jQ = V_{rms} I_{rms} \angle\theta$$

O en forma fasorial:
$$\mathbf{S} = \mathbf{V} \cdot \mathbf{I}^*$$

Donde I* es el conjugado de I.

### Triángulo de Potencias

```
        ╱│
      ╱  │
   S╱    │Q
  ╱ θ    │
╱────────┘
     P
```

**Relaciones:**
$$S^2 = P^2 + Q^2$$
$$\tan\theta = \frac{Q}{P}$$
$$\cos\theta = \frac{P}{S}$$ (factor de potencia)

### Factor de Potencia

$$pf = \cos\theta = \frac{P}{S}$$

| Tipo de carga | θ | Q | pf |
|---------------|---|---|-----|
| Resistiva pura | 0° | 0 | 1 |
| Inductiva | +θ | + | atrasado |
| Capacitiva | -θ | - | adelantado |

### Potencia en Elementos

| Elemento | P | Q |
|----------|---|---|
| Resistor | I²R = V²/R | 0 |
| Inductor | 0 | I²XL = V²/XL |
| Capacitor | 0 | -I²XC = -V²/XC |

### Conservación de Potencia Compleja

La potencia compleja se conserva:
$$\mathbf{S}_{total} = \mathbf{S}_1 + \mathbf{S}_2 + ... + \mathbf{S}_n$$

### Ejemplo

**Datos:** V = 120∠0° V, I = 5∠-30° A

**Cálculos:**
- S = VI* = (120∠0°)(5∠30°) = 600∠30° VA
- P = 600 cos(30°) = 520 W
- Q = 600 sin(30°) = 300 VAR (inductivo)
- pf = cos(30°) = 0.866 atrasado

## Conceptos Clave
- S = P + jQ = VI*
- S² = P² + Q²
- pf = cos(θ) = P/S
