# TH-05: El Transformador Ideal, Marcas de Polaridad e Impedancias Reflejadas

## Objetivos
- Definir el transformador ideal
- Aplicar las relaciones de transformación
- Calcular impedancias reflejadas

## Contenido

### El Transformador Ideal

Un **transformador ideal** tiene las siguientes características:
- Coeficiente de acoplamiento k = 1
- Inductancias infinitas (L₁ = L₂ = ∞)
- Sin pérdidas (R₁ = R₂ = 0)
- Relación de vueltas definida: n = N₂/N₁

### Símbolo del Transformador

```
     •      •
   ╭───╮  ╭───╮
──┤   ├──┤   ├──
  │N₁ │||│N₂ │
──┤   ├──┤   ├──
   ╰───╯  ╰───╯
   
   n = N₂/N₁
```

### Relaciones del Transformador Ideal

**Relación de voltajes:**
$$\frac{\mathbf{V}_2}{\mathbf{V}_1} = n = \frac{N_2}{N_1}$$

**Relación de corrientes:**
$$\frac{\mathbf{I}_1}{\mathbf{I}_2} = n = \frac{N_2}{N_1}$$

**Relación de potencias:**
$$P_1 = P_2$$ (conservación de potencia)

### Marcas de Polaridad (Puntos)

Las marcas de polaridad indican las terminales correspondientes.

**Regla de signos:**
- Si V₁ es positivo en el punto del primario, V₂ es positivo en el punto del secundario
- Si I₁ entra por el punto, I₂ sale por el punto (para transferencia de potencia)

### Impedancia Reflejada

La impedancia vista desde el primario cuando hay una carga ZL en el secundario:

$$\mathbf{Z}_{reflejada} = \frac{\mathbf{Z}_L}{n^2}$$

**Demostración:**
$$\mathbf{Z}_{in} = \frac{\mathbf{V}_1}{\mathbf{I}_1} = \frac{\mathbf{V}_2/n}{\mathbf{I}_2 \cdot n} = \frac{\mathbf{V}_2}{n^2 \mathbf{I}_2} = \frac{\mathbf{Z}_L}{n^2}$$

### Transformadores Elevadores y Reductores

| Tipo | n | Voltaje | Corriente |
|------|---|---------|-----------|
| Elevador | n > 1 | V₂ > V₁ | I₂ < I₁ |
| Reductor | n < 1 | V₂ < V₁ | I₂ > I₁ |
| 1:1 (Aislamiento) | n = 1 | V₂ = V₁ | I₂ = I₁ |

### Adaptación de Impedancias

Para máxima transferencia de potencia con transformador:

$$n = \sqrt{\frac{\mathbf{Z}_L}{\mathbf{Z}_s}}$$

Donde Zs es la impedancia de la fuente.

### Ejemplo

**Circuito:**
```
       10Ω      1:5     
○──/\/\/──┬──╭───╮──┬──○
          │  │   │  │
   50∠0°  │  │   │  250Ω
     V    │  │   │  │
          │  ╰───╯  │
○─────────┴─────────┴──○
```

**Impedancia reflejada:**
$$Z_{ref} = \frac{250}{5^2} = \frac{250}{25} = 10Ω$$

**Corriente primaria:**
$$I_1 = \frac{50\angle 0°}{10 + 10} = 2.5\angle 0° \text{ A}$$

**Voltaje primario del transformador:**
$$V_1 = 50 - (2.5)(10) = 25 \text{ V}$$

**Voltaje secundario:**
$$V_2 = n \cdot V_1 = 5 \times 25 = 125 \text{ V}$$

**Corriente secundaria:**
$$I_2 = \frac{I_1}{n} = \frac{2.5}{5} = 0.5 \text{ A}$$

**Verificación de potencia:**
$$P_1 = V_1 I_1 = 25 \times 2.5 = 62.5 \text{ W}$$
$$P_2 = V_2 I_2 = 125 \times 0.5 = 62.5 \text{ W}$$ ✓

## Conceptos Clave
- V₂/V₁ = n, I₁/I₂ = n
- Z_reflejada = Z_L/n²
- Potencia se conserva: P₁ = P₂
