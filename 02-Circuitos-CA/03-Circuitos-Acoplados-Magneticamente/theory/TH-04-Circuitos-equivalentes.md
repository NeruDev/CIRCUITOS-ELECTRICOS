# TH-04: Circuitos Equivalentes

## Objetivos
- Desarrollar circuitos equivalentes para inductores acoplados
- Aplicar el modelo T para análisis
- Eliminar el acoplamiento magnético usando circuitos equivalentes

## Contenido

### Necesidad de Circuitos Equivalentes

Los circuitos equivalentes permiten:
- Analizar inductores acoplados sin usar ecuaciones de voltaje mutuo
- Usar técnicas estándar de análisis de circuitos
- Simplificar circuitos complejos

### Circuito Equivalente T

Para dos inductores acoplados con inductancia mutua M:

**Circuito original:**
```
   •           •
   ╭───╮      ╭───╮
──┤L₁ ├──────┤L₂ ├──
   ╰───╯  M   ╰───╯
```

**Equivalente T:**
```
   L₁-M      L₂-M
──⌇⌇⌇──┬──⌇⌇⌇──
       │
       M
       │
───────┴───────
```

**Elementos del equivalente T:**
- Rama izquierda: La = L₁ - M
- Rama derecha: Lb = L₂ - M
- Rama central: Lc = M

⚠️ **Nota:** Si M > L₁ o M > L₂, alguna inductancia será negativa, lo cual es válido matemáticamente pero no físicamente realizable.

### Circuito Equivalente π

**Equivalente π:**
```
       L₃
───┬──⌇⌇⌇──┬───
   │       │
  L₁      L₂
   │       │
───┴───────┴───
```

**Relaciones:**
$$L_1' = \frac{L_1 L_2 - M^2}{L_2 - M}$$
$$L_2' = \frac{L_1 L_2 - M^2}{L_1 - M}$$
$$L_3' = \frac{L_1 L_2 - M^2}{M}$$

### Selección del Modelo

| Situación | Modelo recomendado |
|-----------|-------------------|
| Análisis general | Equivalente T |
| k ≈ 1 (alto acoplamiento) | Transformador ideal + dispersión |
| Simulación | Depende del software |

### Ejemplo: Equivalente T

**Datos:** L₁ = 5H, L₂ = 8H, M = 3H

**Equivalente T:**
- La = L₁ - M = 5 - 3 = 2H
- Lb = L₂ - M = 8 - 3 = 5H
- Lc = M = 3H

### Transformador con Inductancia de Dispersión

Para transformadores reales (k < 1), se puede modelar como:

```
    L_d1      ideal      L_d2
──⌇⌇⌇──┬──╭─────╮──┬──⌇⌇⌇──
       │  │ 1:n │  │
       │  │ideal│  │
       └──╰─────╯──┘
```

Donde:
- L_d1 = L₁(1 - k²) = inductancia de dispersión primaria
- n = relación de vueltas

### Modelo con Pérdidas

Para incluir pérdidas:
```
    R₁   L_d1     ideal     L_d2   R₂
──/\/\─⌇⌇⌇──┬──╭─────╮──┬──⌇⌇⌇─/\/\──
            │  │ 1:n │  │
           Rm  │ideal│  │
            │  ╰─────╯  │
────────────┴───────────┴────────────
```

Donde:
- R₁, R₂ = resistencias de los devanados
- Rm = resistencia de pérdidas en el núcleo

## Conceptos Clave
- Equivalente T: L₁-M, L₂-M, M
- Permite usar análisis de circuitos estándar
- Válido matemáticamente aunque aparezcan L negativas
