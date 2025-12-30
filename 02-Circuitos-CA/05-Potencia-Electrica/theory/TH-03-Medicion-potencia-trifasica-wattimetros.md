# TH-03: Medición de Potencia en Circuitos Trifásicos. Método de los Dos Wattímetros

## Objetivos
- Comprender la medición de potencia con wattímetros
- Aplicar el método de los dos wattímetros
- Calcular potencia total y factor de potencia

## Contenido

### El Wattímetro

Un **wattímetro** mide potencia activa mediante:
- Bobina de corriente (en serie con la carga)
- Bobina de voltaje (en paralelo con la carga)

$$W = V_{rms} I_{rms} \cos\theta$$

Donde θ es el ángulo entre V e I medidos.

### Conexión de Wattímetros

```
Wattímetro:
    ○──CC──○    CC = Bobina de corriente
       │
      CV       CV = Bobina de voltaje
       │
    ○──────○
```

### Métodos de Medición Trifásica

| Método | Número de wattímetros | Aplicación |
|--------|----------------------|------------|
| Tres wattímetros | 3 | General, cualquier carga |
| Dos wattímetros | 2 | Sin neutro, 3 o 4 hilos |
| Un wattímetro | 1 | Solo cargas balanceadas |

### Método de los Dos Wattímetros

Para un sistema trifásico de 3 hilos (sin neutro):

```
    a ─────●──CC1──●────── Za
           │
          CV1  ──┐        
           │     │   Zb
    b ─────●─────┼──────── 
                 │
                CV2
                 │    Zc
    c ─────●──CC2──●──────
```

**Conexión:**
- W₁: Corriente en línea a, voltaje entre a y b
- W₂: Corriente en línea c, voltaje entre c y b

### Lecturas de los Wattímetros

$$W_1 = V_{ab} I_a \cos\angle(V_{ab}, I_a)$$
$$W_2 = V_{cb} I_c \cos\angle(V_{cb}, I_c)$$

### Potencia Total

**Para cualquier carga (balanceada o no):**
$$P_{total} = W_1 + W_2$$

Esta relación siempre es válida.

### Factor de Potencia (Carga Balanceada)

Para cargas balanceadas:

$$\tan\theta = \sqrt{3}\frac{W_1 - W_2}{W_1 + W_2}$$

$$pf = \cos\theta$$

### Casos Especiales (Carga Balanceada)

| pf | θ | W₁ | W₂ | Relación |
|----|---|-----|-----|----------|
| 1.0 | 0° | P/2 | P/2 | W₁ = W₂ |
| 0.866 | 30° | P | 0 | W₂ = 0 |
| 0.5 | 60° | P | -P/2 | W₂ negativa |
| 0 | 90° | +∞ | -∞ | Indefinido |

### Interpretación de Lecturas

- **W₁ = W₂:** pf = 1 (carga resistiva)
- **W₁ > W₂ > 0:** 0.5 < pf < 1
- **W₂ = 0:** pf = 0.5
- **W₂ < 0:** pf < 0.5 (leer invertir conexión y restar)

### Ejemplo

**Datos:** Sistema trifásico, W₁ = 5000 W, W₂ = 2000 W

**Cálculos:**
1. Potencia total: P = 5000 + 2000 = 7000 W

2. Factor de potencia:
   $$\tan\theta = \sqrt{3}\frac{5000 - 2000}{5000 + 2000} = \sqrt{3}\frac{3000}{7000} = 0.742$$
   $$\theta = \arctan(0.742) = 36.6°$$
   $$pf = \cos(36.6°) = 0.803$$

3. Potencia reactiva:
   $$Q = P\tan\theta = 7000 \times 0.742 = 5194 \text{ VAR}$$

4. Potencia aparente:
   $$S = \sqrt{P^2 + Q^2} = \sqrt{7000^2 + 5194^2} = 8718 \text{ VA}$$

### Ventajas del Método

1. Solo requiere 2 wattímetros
2. Válido para cargas balanceadas y desbalanceadas
3. No requiere acceso al neutro
4. Permite calcular P, Q y pf

## Conceptos Clave
- Ptotal = W₁ + W₂ (siempre)
- tan θ = √3(W₁-W₂)/(W₁+W₂) (balanceado)
- W₂ puede ser negativa si pf < 0.5
