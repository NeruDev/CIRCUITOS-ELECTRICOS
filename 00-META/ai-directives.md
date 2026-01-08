<!--
::METADATA::
type: reference
topic_id: meta-ai-directives
file_id: ai-directives
status: active
audience: ai_context
last_updated: 2026-01-08
-->

# 🤖 Directivas Técnicas para IA — Circuitos Eléctricos

> **Complementa a:** [Contrato IA Principal](ia-contract.md)
>
> Este documento contiene directivas técnicas específicas para asistentes de IA.

---

## 1. Jerarquía de Documentos

```
Prioridad de lectura para IA:
1. ia-contract.md         ← LEY SUPREMA
2. ai-directives.md       ← Este documento (reglas técnicas)
3. _directives.md         ← Reglas del subtema actual
4. manifest.json          ← Mapa de recursos del subtema
```

---

## 2. Comportamiento por Tipo de Solicitud

### 2.1 Solicitudes de Explicación Teórica

```yaml
acción: Consultar theory/ del subtema
formato: Markdown con ecuaciones LaTeX
incluir:
  - Definición formal
  - Analogía intuitiva (si existe)
  - Enlace al glosario
  - Referencia bibliográfica
```

### 2.2 Solicitudes de Resolución de Problemas

```yaml
acción: Seguir formato de ia-contract.md sección 5
pasos:
  1. Análisis previo
  2. Datos del problema
  3. Planteamiento de ecuaciones
  4. Resolución paso a paso
  5. Verificación con simulación (si disponible)
  6. Conclusiones
```

### 2.3 Solicitudes de Generación de Ejercicios

```yaml
acción: Usar plantilla de EJ-XX
incluir:
  - Nivel de dificultad (⭐, ⭐⭐, ⭐⭐⭐)
  - Diagrama o descripción del circuito
  - Datos claramente listados
  - Múltiples incisos (a, b, c...)
  - Respuestas ocultas en comentarios
```

---

## 3. Patrones de Reconocimiento

### 3.1 Detección de Carpeta Notas/

```
Si ruta contiene: */Notas/*
  → Desactivar TODAS las validaciones
  → Leer contenido completo si se solicita
  → NO sugerir correcciones de formato
```

### 3.2 Detección de Tipo de Archivo por Prefijo

| Prefijo | Tipo | Ubicación esperada |
|---------|------|-------------------|
| `TH-XX` | Teoría | `theory/` |
| `MET-XX` | Método | `methods/` |
| `PR-XX` | Problema resuelto | `problems/` |
| `EJ-XX` | Ejercicio propuesto | `problems/` |
| `SIM-XX` | Simulación | `simulation/` |

---

## 4. Validación de Contenido

### 4.1 Verificar contra Bibliografía

Antes de generar contenido teórico, consultar:
- `00-META/bibliografia-general.md`
- Referencias del `manifest.json` del subtema

### 4.2 Consistencia de Símbolos

Usar notación definida en:
- `00-META/notation-cheatsheet.md`

### 4.3 Términos del Glosario

Al mencionar un término técnico por primera vez:
- Verificar si existe en `glossary.md`
- Crear enlace: `[término](../../glossary.md#termino)`

---

## 5. Formatos de Salida

### 5.1 Ecuaciones

```latex
% Inline
$V = IR$

% Block
$$
V_{out} = V_{in} \cdot \frac{R_2}{R_1 + R_2}
$$
```

### 5.2 Circuitos en Texto (SPICE)

```spice
* Nombre del circuito
V1 1 0 DC 12V
R1 1 2 1k
R2 2 0 2k
.OP
.END
```

### 5.3 Tablas de Resultados

```markdown
| Variable | Calculado | Simulado | Error |
|----------|-----------|----------|-------|
| I₁       | 2.00 mA   | 1.99 mA  | 0.5%  |
```

---

## 6. Restricciones

### ❌ NO hacer:

- Inventar valores de componentes no especificados
- Omitir unidades en resultados
- Usar notación inconsistente con `notation-cheatsheet.md`
- Modificar archivos en carpeta `Notas/` sin solicitud explícita

### ✅ SIEMPRE hacer:

- Mostrar trabajo paso a paso
- Incluir unidades en todos los valores
- Referenciar fuentes cuando sea apropiado
- Usar el sistema de niveles de dificultad

---

## 7. Plantillas Rápidas

### Plantilla de Respuesta Corta

```markdown
**Respuesta:** [valor con unidades]

**Desarrollo breve:**
1. [Paso 1]
2. [Paso 2]
3. [Resultado]
```

### Plantilla de Respuesta Completa

Ver: [plantilla-respuestas.md](plantilla-respuestas.md)

---

## 8. Actualización

Este documento se actualiza cuando:
- Cambian las convenciones del repositorio
- Se añaden nuevos tipos de contenido
- Se modifican los scripts de validación

**Última revisión:** 2026-01-08
