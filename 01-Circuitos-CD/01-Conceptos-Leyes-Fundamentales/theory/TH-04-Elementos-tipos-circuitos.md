# TH-04: Elementos de un Circuito y Tipos de Circuitos

## Objetivos
- Clasificar los elementos de un [circuito](../../../glossary.md#circuito)
- Identificar fuentes independientes y dependientes
- Distinguir entre diferentes tipos de circuitos

## Contenido

### Clasificación de Elementos

#### Elementos Activos
Pueden suministrar energía al circuito:
- Fuentes de [voltaje](../../../glossary.md#voltaje)
- Fuentes de [corriente](../../../glossary.md#corriente)

#### Elementos Pasivos
Absorben o almacenan energía:
- **[Resistor](../../../glossary.md#resistencia) (R)**: Disipa energía en forma de calor
- **[Capacitor](../../../glossary.md#capacitancia) (C)**: Almacena energía en campo eléctrico
- **[Inductor](../../../glossary.md#inductancia) (L)**: Almacena energía en campo magnético

### Fuentes Independientes

**Fuente de voltaje ideal**: Mantiene un voltaje constante independientemente de la corriente.

**Fuente de corriente ideal**: Mantiene una corriente constante independientemente del voltaje.

### Fuentes Dependientes (Controladas)

| Tipo | Símbolo | Descripción |
|------|---------|-------------|
| VCVS | Fuente de voltaje controlada por voltaje | v = μ·vₓ |
| VCCS | Fuente de corriente controlada por voltaje | i = g·vₓ |
| CCVS | Fuente de voltaje controlada por corriente | v = r·iₓ |
| CCCS | Fuente de corriente controlada por corriente | i = β·iₓ |

### Tipos de Circuitos

#### Por conexión
- **Circuito serie**: Los elementos comparten la misma corriente
- **Circuito paralelo**: Los elementos comparten el mismo voltaje
- **Circuito mixto**: Combinación de serie y paralelo

#### Por tipo de señal
- **Circuito de CD**: Opera con [corriente directa](../../../glossary.md#corriente-directa)
- **Circuito de CA**: Opera con corriente alterna

#### Por comportamiento
- **Circuito lineal**: La respuesta es proporcional a la excitación
- **Circuito no lineal**: Contiene elementos no lineales

### Símbolos de Elementos

```
Resistor:     ─/\/\/\/─   o   ─▭─
Capacitor:    ─||─  o  ─|├─
Inductor:     ─⌇⌇⌇⌇─
Fuente V:     (+─)  o  (círculo con + -)
Fuente I:     (→)   o  (círculo con flecha)
```

## Conceptos Clave
- Elementos activos vs pasivos
- Fuentes independientes vs dependientes
- Circuitos lineales y no lineales
