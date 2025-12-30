# TH-03: Análisis de Circuitos con Acoplamiento Magnético

## Objetivos
- Escribir las ecuaciones de malla para circuitos acoplados
- Aplicar métodos de análisis a transformadores
- Resolver circuitos con múltiples acoplamientos

## Contenido

### Procedimiento de Análisis

1. **Identificar** todas las inductancias y acoplamientos
2. **Determinar** la polaridad usando la convención del punto
3. **Escribir** las ecuaciones de malla o nodos
4. **Resolver** el sistema de ecuaciones

### Ecuaciones de Malla con Acoplamiento

Para un circuito con dos mallas acopladas:

```
      R₁        •          R₂
○──/\/\/──┬───╭───╮───┬──/\/\/──○
          │   │ L₁│   │
    Vs    │   ╰───╯   │    ZL
          │     M     │
          │   ╭───╮   │
          │   │ L₂│   │
          └───╰───╯───┘
                •
```

**Malla 1:**
$$\mathbf{V}_s = (R_1 + j\omega L_1)\mathbf{I}_1 + j\omega M \mathbf{I}_2$$

**Malla 2:**
$$0 = j\omega M \mathbf{I}_1 + (R_2 + j\omega L_2 + \mathbf{Z}_L)\mathbf{I}_2$$

### Determinación del Signo de M

**Paso 1:** Asignar direcciones de corriente de malla

**Paso 2:** Verificar la dirección de cada corriente respecto a los puntos:
- Si ambas entran (o salen) por los puntos: +M
- Si una entra y otra sale: -M

### Ejemplo de Análisis

**Circuito:**
```
      4Ω         •
○──/\/\/──┬──╭───╮──┐
          │  │ 2H│  │
   10∠0°  │  ╰───╯  │
    V     │   M=1H  │
          │  ╭───╮  │
          │  │ 4H│  │    8Ω
          └──╰───╯──┴──/\/\/──○
               •
ω = 2 rad/s
```

**Impedancias:**
- ZL1 = jωL₁ = j(2)(2) = j4Ω
- ZL2 = jωL₂ = j(2)(4) = j8Ω
- ZM = jωM = j(2)(1) = j2Ω

**Ecuaciones de malla:**
- Malla 1: $10 = (4 + j4)I_1 + j2 I_2$
- Malla 2: $0 = j2 I_1 + (8 + j8)I_2$

**Solución:**
De la malla 2: $I_1 = -\frac{(8 + j8)}{j2}I_2 = (4 - j4)I_2$

Sustituyendo en malla 1:
$10 = (4 + j4)(4 - j4)I_2 + j2 I_2$
$10 = (32)I_2 + j2 I_2$
$10 = (32 + j2)I_2$

$I_2 = \frac{10}{32 + j2} = 0.312\angle{-3.6°}$ A

### Circuitos con Múltiples Acoplamientos

Para tres o más bobinas acopladas, se extiende el método:

$$v_k = L_k\frac{di_k}{dt} + \sum_{j \neq k} M_{kj}\frac{di_j}{dt}$$

### Verificación del Análisis

- Verificar LCK en cada nodo
- Verificar LVK en cada malla
- Comprobar que las potencias se balancean

## Conceptos Clave
- Incluir voltajes mutuos en cada ecuación de malla
- El signo depende de direcciones de corriente y puntos
- Método sistemático para múltiples acoplamientos
