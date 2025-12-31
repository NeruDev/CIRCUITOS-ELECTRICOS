# Modelos SPICE Comunes

Esta carpeta contiene modelos SPICE comunes utilizados en las simulaciones de Proteus 8.15.

## Estructura

```
spice-models/
├── README.md           # Este archivo
├── passive/            # Modelos de componentes pasivos
├── diodes/             # Modelos de diodos
├── transistors/        # Modelos de transistores
└── opamps/             # Modelos de amplificadores operacionales
```

## Uso en Proteus

1. Los modelos pueden importarse directamente en Proteus 8.15
2. Usar la opción "Edit Component" > "Make Device" para componentes personalizados
3. Consultar la documentación de Proteus para sintaxis específica

## Formato de Modelos

### Diodo Genérico (1N4148)
```spice
.MODEL D1N4148 D (
+ IS=2.52E-9
+ RS=0.568
+ N=1.752
+ BV=100
+ IBV=100E-6
+ CJO=4E-12
+ VJ=0.5
+ M=0.4
+ TT=6E-9
)
```

### Transistor BJT (2N2222)
```spice
.MODEL Q2N2222 NPN (
+ IS=14.34E-15
+ BF=255.9
+ VAF=74.03
+ IKF=0.2847
+ NE=1.307
+ BR=6.092
+ RC=1
+ CJC=7.306E-12
+ CJE=22.01E-12
+ TF=411.1E-12
)
```

## Notas

- Los modelos básicos de Proteus son suficientes para la mayoría de ejercicios del repositorio
- Para componentes específicos, consultar datasheet del fabricante
- El motor de simulación de Proteus está basado en SPICE 3F5

## Referencias

- [SPICE Model Handbook](https://www.analog.com/en/technical-articles/introduction-to-spice-modeling.html)
- [Proteus Design Suite Documentation](https://www.labcenter.com/documentation/)
