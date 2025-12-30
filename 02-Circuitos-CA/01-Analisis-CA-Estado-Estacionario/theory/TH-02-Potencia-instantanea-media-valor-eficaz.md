# TH-02: Potencia Instantánea y Media. Valor Eficaz. Factor de Potencia

## Objetivos
- Calcular potencia instantánea y promedio
- Comprender el valor eficaz (RMS)
- Definir el factor de potencia

## Contenido

### Potencia Instantánea

La potencia instantánea es el producto del voltaje y la corriente instantáneos:

$$p(t) = v(t) \cdot i(t)$$

Para:
- v(t) = Vm cos(ωt)
- i(t) = Im cos(ωt - θ)

$$p(t) = V_m I_m \cos(\omega t) \cos(\omega t - \theta)$$

Usando identidades trigonométricas:
$$p(t) = \frac{V_m I_m}{2}[\cos\theta + \cos(2\omega t - \theta)]$$

### Potencia Promedio (Media)

La potencia promedio se obtiene integrando sobre un período:

$$P = \frac{1}{T}\int_0^T p(t) \, dt = \frac{V_m I_m}{2}\cos\theta$$

En términos de valores eficaces:
$$P = V_{rms} I_{rms} \cos\theta$$

### Valor Eficaz (RMS)

El valor eficaz (Root Mean Square) de una señal periódica es:

$$V_{rms} = \sqrt{\frac{1}{T}\int_0^T v^2(t) \, dt}$$

**Para una señal senoidal:**
$$V_{rms} = \frac{V_m}{\sqrt{2}} \approx 0.707 V_m$$

$$I_{rms} = \frac{I_m}{\sqrt{2}} \approx 0.707 I_m$$

### Significado del Valor Eficaz

El valor eficaz de una señal CA produce la misma potencia en una resistencia que una señal DC del mismo valor.

**Ejemplo:** 120 V AC (eficaz) produce la misma potencia que 120 V DC.

### Factor de Potencia

El **factor de potencia (pf)** es el coseno del ángulo entre el voltaje y la corriente:

$$pf = \cos\theta$$

**Características:**
- 0 ≤ pf ≤ 1
- pf = 1: Carga puramente resistiva
- pf = 0: Carga puramente reactiva
- pf adelantado: Corriente adelanta al voltaje (carga capacitiva)
- pf atrasado: Corriente atrasa al voltaje (carga inductiva)

### Relaciones de Potencia

$$P = S \cdot pf = V_{rms} I_{rms} \cos\theta$$

Donde S = potencia aparente.

### Tabla de Valores

| Forma de onda | Vp | Vrms | Relación |
|---------------|-----|------|----------|
| Senoidal | Vm | Vm/√2 | 0.707 |
| Cuadrada | Vm | Vm | 1.0 |
| Triangular | Vm | Vm/√3 | 0.577 |

### Ejemplo

**Datos:** v(t) = 170 sin(377t) V, i(t) = 10 sin(377t - 30°) A

**Solución:**
- Vm = 170 V → Vrms = 170/√2 = 120.2 V
- Im = 10 A → Irms = 10/√2 = 7.07 A
- θ = 30°
- pf = cos(30°) = 0.866 (atrasado)
- P = 120.2 × 7.07 × 0.866 = 736 W

## Conceptos Clave
- Vrms = Vm/√2 para señales senoidales
- P = Vrms × Irms × cos(θ)
- Factor de potencia indica eficiencia de uso de potencia
