<!--
::METADATA::
type: reference
topic_id: meta-templates
file_id: plantilla-respuestas
status: active
audience: both
last_updated: 2026-01-08
-->

# 📝 Plantilla para Respuestas y Soluciones

> Formato estándar para documentar soluciones de problemas de circuitos eléctricos.

---

## Plantilla Completa — Problema Resuelto

```markdown
<!--
::METADATA::
type: solution
topic_id: [id-del-subtema]
file_id: PR-XX-[nombre]
status: stable
audience: student
last_updated: YYYY-MM-DD
-->

# [PR-XX] Título del Problema

**Dificultad:** ⭐⭐ (Intermedio)  
**Tema:** [Nombre del tema]  
**Método:** [Análisis de mallas / nodos / Thévenin / etc.]

---

## 1. Enunciado

[Descripción clara del problema]

### Diagrama del Circuito

[Imagen o descripción textual del circuito]

### Datos

| Variable | Valor |
|----------|-------|
| V₁ | 12 V |
| R₁ | 1 kΩ |
| R₂ | 2 kΩ |

### Se pide

a) [Primera pregunta]  
b) [Segunda pregunta]  
c) [Tercera pregunta]

---

## 2. Análisis Previo

- **Topología:** [Descripción: N nodos, M mallas, etc.]
- **Método seleccionado:** [Justificación del método elegido]
- **Simplificaciones posibles:** [Si aplica]

---

## 3. Desarrollo

### Paso 1: [Título del paso]

[Explicación del paso]

$$
[Ecuación principal]
$$

### Paso 2: [Título del paso]

[Explicación del paso]

$$
[Ecuación o sistema]
$$

### Paso 3: Resolución

[Desarrollo algebraico]

---

## 4. Resultados

| Variable | Valor | Unidad |
|----------|-------|--------|
| I₁ | 2.00 | mA |
| V_out | 5.00 | V |
| P_total | 24 | mW |

---

## 5. Verificación

### 5.1 Verificación Analítica

[Aplicar método alternativo o verificar conservación de energía]

### 5.2 Comparación con Simulación

**Archivo:** `simulation/SIM-XX-nombre.pdsprj`

| Variable | Calculado | Simulado | Error |
|----------|-----------|----------|-------|
| I₁ | 2.00 mA | 1.99 mA | 0.5% |
| V_out | 5.00 V | 4.98 V | 0.4% |

✅ Verificación exitosa (error < 1%)

---

## 6. Conclusiones

- [Observación principal del resultado]
- [Aplicación práctica o insight]
- [Consideraciones adicionales]

---

## Referencias

- [Enlace a teoría relacionada](../theory/TH-XX.md)
- [Enlace al método usado](../methods/MET-XX.md)
```

---

## Plantilla Corta — Solo Respuesta

```markdown
# [PR-XX] Título

**Respuestas:**

a) I₁ = **2.00 mA**  
b) V_out = **5.00 V**  
c) P_total = **24 mW**

---

**Desarrollo breve:**

1. Aplicar [método/ley]
2. Plantear ecuación: $V = IR$
3. Resolver: $I = V/R = 12V/6kΩ = 2mA$
```

---

## Plantilla — Ejercicio Propuesto

```markdown
<!--
::METADATA::
type: problem
topic_id: [id-del-subtema]
file_id: EJ-XX-[nombre]
status: stable
audience: student
-->

# [EJ-XX] Título del Ejercicio

**Dificultad:** ⭐⭐ (Intermedio)  
**Tema:** [Nombre del tema]

---

## Enunciado

[Descripción del problema]

### Diagrama

[Imagen o descripción]

### Datos

- V₁ = 10 V
- R₁ = 1 kΩ
- R₂ = 2 kΩ

### Se pide

a) Calcular la corriente I₁  
b) Determinar el voltaje en R₂  
c) Calcular la potencia total

---

## Pistas (opcional)

<details>
<summary>💡 Pista 1</summary>
Considera usar el divisor de voltaje.
</details>

<details>
<summary>💡 Pista 2</summary>
Las resistencias están en serie.
</details>

---

## Respuestas

<!-- Ocultas para autoevaluación -->
<!--
a) I₁ = 3.33 mA
b) V_R2 = 6.67 V
c) P_total = 33.3 mW
-->

<details>
<summary>📝 Ver respuestas</summary>

a) I₁ = 3.33 mA  
b) V_R2 = 6.67 V  
c) P_total = 33.3 mW

</details>
```

---

## Convenciones de Formato

### Ecuaciones

```latex
% Inline
La ley de Ohm establece que $V = IR$.

% Block
$$
V_{out} = V_{in} \cdot \frac{R_2}{R_1 + R_2}
$$
```

### Tablas de Datos

```markdown
| Variable | Valor | Unidad |
|----------|-------|--------|
| V_in | 12 | V |
| R_eq | 4.7 | kΩ |
```

### Código SPICE

```spice
* Título del circuito
V1 1 0 DC 12V
R1 1 2 1k
R2 2 0 2k
.OP
.END
```

---

## Niveles de Dificultad

| Nivel | Símbolo | Descripción |
|-------|---------|-------------|
| Básico | ⭐ | Aplicación directa de fórmula |
| Intermedio | ⭐⭐ | Requiere sistema de ecuaciones |
| Avanzado | ⭐⭐⭐ | Circuitos complejos, fuentes dependientes |

---

## Checklist de Calidad

- [ ] Enunciado claro y completo
- [ ] Diagrama o descripción del circuito
- [ ] Todos los datos necesarios incluidos
- [ ] Desarrollo paso a paso
- [ ] Unidades en todos los valores
- [ ] Verificación incluida
- [ ] Formato Markdown correcto
