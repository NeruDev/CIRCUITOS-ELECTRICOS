# Resumen de Fórmulas - Circuitos Trifásicos

## Voltajes Trifásicos (Secuencia abc)

$$\mathbf{V}_a = V_p\angle 0°$$
$$\mathbf{V}_b = V_p\angle -120°$$
$$\mathbf{V}_c = V_p\angle 120°$$

**Propiedad:** $\mathbf{V}_a + \mathbf{V}_b + \mathbf{V}_c = 0$

## Relaciones de Voltaje y Corriente

### Conexión Estrella (Y)
$$V_L = \sqrt{3}V_f$$
$$I_L = I_f$$
$$\mathbf{V}_{ab} = \sqrt{3}V_f\angle 30°$$

### Conexión Delta (Δ)
$$V_L = V_f$$
$$I_L = \sqrt{3}I_f$$
$$\mathbf{I}_a = \sqrt{3}I_f\angle -30°$$

## Conversión Δ-Y

$$Z_Y = \frac{Z_\Delta}{3}$$
$$Z_\Delta = 3Z_Y$$

## Potencia Trifásica (Balanceada)

**Potencia activa:**
$$P = 3V_f I_f \cos\theta = \sqrt{3}V_L I_L \cos\theta$$

**Potencia reactiva:**
$$Q = 3V_f I_f \sin\theta = \sqrt{3}V_L I_L \sin\theta$$

**Potencia aparente:**
$$S = 3V_f I_f = \sqrt{3}V_L I_L$$

## Carga Y sin Neutro (Desbalanceada)

**Voltaje del punto flotante:**
$$\mathbf{V}_{n'n} = \frac{\mathbf{V}_{an}Y_a + \mathbf{V}_{bn}Y_b + \mathbf{V}_{cn}Y_c}{Y_a + Y_b + Y_c}$$

## Carga Δ (Corrientes de Línea)

$$\mathbf{I}_a = \mathbf{I}_{ab} - \mathbf{I}_{ca}$$
$$\mathbf{I}_b = \mathbf{I}_{bc} - \mathbf{I}_{ab}$$
$$\mathbf{I}_c = \mathbf{I}_{ca} - \mathbf{I}_{bc}$$

## Corriente de Neutro

$$\mathbf{I}_n = \mathbf{I}_a + \mathbf{I}_b + \mathbf{I}_c$$

(= 0 para sistemas balanceados)

## Tabla Rápida

| Conexión | VL | IL |
|----------|-----|-----|
| Y | √3 Vf | If |
| Δ | Vf | √3 If |
