# Resumen de Fórmulas - Análisis en el Dominio de la Frecuencia

## Función de Transferencia

$$H(j\omega) = |H(j\omega)| \angle\phi(\omega)$$

**Magnitud en dB:**
$$|H|_{dB} = 20\log_{10}|H|$$

## Filtro RC Pasa-Bajas

$$H(j\omega) = \frac{1}{1 + j\omega RC}$$
$$\omega_c = \frac{1}{RC}$$
$$|H| = \frac{1}{\sqrt{1 + (\omega/\omega_c)^2}}$$

## Filtro RC Pasa-Altas

$$H(j\omega) = \frac{j\omega RC}{1 + j\omega RC}$$
$$|H| = \frac{\omega/\omega_c}{\sqrt{1 + (\omega/\omega_c)^2}}$$

## Resonancia

**Frecuencia de resonancia:**
$$\omega_0 = \frac{1}{\sqrt{LC}}$$
$$f_0 = \frac{1}{2\pi\sqrt{LC}}$$

## Factor de Calidad

**Serie:**
$$Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 RC}$$

**Paralelo:**
$$Q = R\omega_0 C = \frac{R}{\omega_0 L}$$

## Ancho de Banda

$$BW = \frac{\omega_0}{Q} = \frac{f_0}{Q}$$

## Frecuencias de Corte (-3 dB)

$$\omega_{1,2} = \omega_0\left(\sqrt{1 + \frac{1}{4Q^2}} \mp \frac{1}{2Q}\right)$$

Para Q alto:
$$\omega_1 \approx \omega_0 - \frac{BW}{2}$$
$$\omega_2 \approx \omega_0 + \frac{BW}{2}$$

## Polos y Ceros

**Polo:** Raíz del denominador (×)
**Cero:** Raíz del numerador (○)

**Estabilidad:** Todos los polos en semiplano izquierdo (σ < 0)

## Pendientes en Diagrama de Bode

| Elemento | Pendiente |
|----------|-----------|
| Polo simple | -20 dB/década |
| Cero simple | +20 dB/década |
| Polo doble | -40 dB/década |

## Tipos de Filtros

| Tipo | fc o f₀ |
|------|---------|
| LP (RC) | 1/(2πRC) |
| HP (RC) | 1/(2πRC) |
| BP (RLC) | 1/(2π√LC) |
| BR (RLC) | 1/(2π√LC) |
