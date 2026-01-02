# TH-01: El Fenómeno de la Inducción

## Objetivos
- Comprender la [ley de](../../../glossary.md#ley-ohm) Faraday
- Relacionar flujo magnético con [voltaje](../../../glossary.md#voltaje) inducido
- Establecer las bases del acoplamiento magnético

## Contenido

### Ley de Faraday

La ley de inducción electromagnética de Faraday establece:

$$e = -N\frac{d\Phi}{dt}$$

Donde:
- e = voltaje inducido (fem)
- N = número de espiras
- Φ = flujo magnético (Weber)
- dΦ/dt = tasa de cambio del flujo

### Flujo Magnético

El flujo magnético a través de una superficie:

$$\Phi = \int_S \mathbf{B} \cdot d\mathbf{A}$$

Para campo uniforme y perpendicular:
$$\Phi = BA$$

### Ley de Lenz

El voltaje inducido tiene una polaridad tal que se opone al cambio de flujo que lo produce. Esto explica el signo negativo en la ley de Faraday.

### Inductancia Propia

Cuando una corriente i fluye por un inductor, crea un flujo magnético proporcional:

$$\Phi = Li$$

Por la ley de Faraday:
$$v = L\frac{di}{dt}$$

### Inducción Mutua

Cuando dos inductores están cerca, el flujo de uno puede enlazar al otro:

```
    Bobina 1         Bobina 2
    ╭─────╮         ╭─────╮
    │     │ ═══════>│     │
    │ L₁  │   Φ₁₂   │ L₂  │
    │     │         │     │
    ╰─────╯         ╰─────╯
```

El flujo Φ₁₂ de la bobina 1 que enlaza la bobina 2 induce un voltaje en la bobina 2.

### Aplicaciones de la Inducción

1. **Transformadores:** Transferencia de energía por acoplamiento magnético
2. **Generadores:** Conversión de energía mecánica a eléctrica
3. **Motores:** Conversión de energía eléctrica a mecánica
4. **Sensores inductivos:** Detección de posición y velocidad

### Energía en Campo Magnético

$$W = \frac{1}{2}Li^2 = \frac{1}{2}\frac{\Phi^2}{L}$$

## Conceptos Clave
- Fem inducida proporcional a dΦ/dt
- Ley de Lenz: oposición al cambio
- Base del [transformador](../../../glossary.md#transformador) y acoplamiento
