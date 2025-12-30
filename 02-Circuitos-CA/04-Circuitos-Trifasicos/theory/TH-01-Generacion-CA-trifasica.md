# TH-01: Generación de CA Trifásica

## Objetivos
- Comprender la generación de voltajes trifásicos
- Identificar secuencias de fase
- Representar voltajes trifásicos como fasores

## Contenido

### Sistema Trifásico

Un **sistema trifásico** consiste en tres voltajes senoidales de igual magnitud y frecuencia, desfasados 120° entre sí.

### Generación de Voltajes Trifásicos

Un generador trifásico tiene tres devanados separados 120° mecánicamente:

```
      a
     /|\
    / | \
   /  |  \
  c───┼───b
      │
   (Rotor)
```

### Voltajes de Fase

**Secuencia positiva (abc):**
$$v_a(t) = V_m \cos(\omega t)$$
$$v_b(t) = V_m \cos(\omega t - 120°)$$
$$v_c(t) = V_m \cos(\omega t - 240°) = V_m \cos(\omega t + 120°)$$

**En forma fasorial:**
$$\mathbf{V}_a = V_p\angle 0°$$
$$\mathbf{V}_b = V_p\angle -120°$$
$$\mathbf{V}_c = V_p\angle 120°$$

### Secuencia de Fase

**Secuencia positiva (abc):** a adelanta a b, b adelanta a c
**Secuencia negativa (acb):** a adelanta a c, c adelanta a b

### Diagrama Fasorial

```
            Va
             │
             │
    Vc ──────┼────── Vb
            120°
```

Las tres fases están separadas 120°.

### Propiedad Fundamental

La suma de los tres voltajes de fase es cero:
$$\mathbf{V}_a + \mathbf{V}_b + \mathbf{V}_c = 0$$

Esto es fundamental para sistemas balanceados.

### Ventajas del Sistema Trifásico

1. **Transmisión eficiente:** Menos conductores que tres sistemas monofásicos
2. **Potencia constante:** La potencia instantánea total es constante
3. **Motores:** Los motores trifásicos son más simples y eficientes
4. **Generación:** Fácil de generar con alternadores

### Notación de Voltajes

| Notación | Significado |
|----------|-------------|
| Vp o Vf | Voltaje de fase |
| VL | Voltaje de línea |
| Vab, Vbc, Vca | Voltajes línea-línea |
| Van, Vbn, Vcn | Voltajes fase-neutro |

### Frecuencias Comunes

| Región | Frecuencia |
|--------|------------|
| América (60 Hz) | ω = 377 rad/s |
| Europa (50 Hz) | ω = 314 rad/s |

## Conceptos Clave
- Tres voltajes iguales desfasados 120°
- Va + Vb + Vc = 0
- Secuencia positiva: abc
