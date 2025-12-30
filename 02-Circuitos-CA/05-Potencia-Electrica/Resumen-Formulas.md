# Resumen de Fórmulas - Potencia Eléctrica

## Tipos de Potencia

| Tipo | Fórmula | Unidad |
|------|---------|--------|
| Real (P) | Vrms Irms cos θ | W |
| Reactiva (Q) | Vrms Irms sin θ | VAR |
| Aparente (S) | Vrms Irms | VA |
| Compleja (S) | P + jQ | VA |

## Relaciones

$$S = \sqrt{P^2 + Q^2}$$
$$\tan\theta = \frac{Q}{P}$$
$$pf = \cos\theta = \frac{P}{S}$$

## Potencia Compleja

$$\mathbf{S} = \mathbf{V}\mathbf{I}^* = P + jQ$$

## Triángulo de Potencias

```
        ╱│
      ╱  │
   S╱    │Q
  ╱ θ    │
╱────────┘
     P
```

## Factor de Potencia

$$pf = \cos\theta = \frac{P}{S}$$

- pf adelantado: carga capacitiva (Q < 0)
- pf atrasado: carga inductiva (Q > 0)

## Corrección del Factor de Potencia

**Capacitancia requerida:**
$$Q_C = P(\tan\theta_1 - \tan\theta_2)$$
$$C = \frac{Q_C}{\omega V^2}$$

## Potencia Trifásica (Balanceada)

$$P = 3V_f I_f \cos\theta = \sqrt{3}V_L I_L \cos\theta$$
$$Q = 3V_f I_f \sin\theta = \sqrt{3}V_L I_L \sin\theta$$
$$S = 3V_f I_f = \sqrt{3}V_L I_L$$

## Método de los Dos Wattímetros

**Potencia total:**
$$P = W_1 + W_2$$

**Factor de potencia (balanceado):**
$$\tan\theta = \sqrt{3}\frac{W_1 - W_2}{W_1 + W_2}$$

## Potencia en Elementos

| Elemento | P | Q |
|----------|---|---|
| R | I²R | 0 |
| L | 0 | I²XL |
| C | 0 | -I²XC |
