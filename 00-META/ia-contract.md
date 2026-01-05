<!--
::METADATA::
type: reference
topic_id: meta-ia-contract-circuits
file_id: IA_CONTRACT_CIRCUITOS
status: active
audience: ai_context
last_updated: 2025-12-30
-->

# Contrato IA para Circuitos Eléctricos

## Propósito
Este documento establece las directrices para la generación de contenido asistido por IA en el repositorio de Circuitos Eléctricos, integrando simulación con **Proteus 8.15**.

---

## 1. Principios Didácticos

### 1.1 Estructura "Theory-First, Method-Second"

Para cada tema, el contenido debe dividirse:

1. **Fundamentos Teóricos (`theory/`)**:
    - Definiciones, leyes físicas (Ohm, Kirchhoff) y demostraciones.
    - *No incluir ejemplos numéricos complejos aquí.*
2. **Metodología (`methods/`)**:
    - "Recetas" o algoritmos paso a paso para resolver circuitos.
    - Ejemplo: "Paso 1: Identificar nodos esenciales. Paso 2: Asignar nodo de referencia..."
3. **Problemas (`problems/`)**:
    - Enunciados limpios sin pistas de solución.
    - Diagramas esquemáticos claros.
4. **Simulación (`simulation/`)**:
    - Archivos `.pdsprj` de Proteus 8.15.
    - Validación de resultados teóricos.

### 1.2 Progresión de Dificultad

Los problemas deben etiquetarse por nivel:

| Nivel | Símbolo | Descripción |
|-------|---------|-------------|
| Conceptual/Básico | ⭐ | Aplicación directa de fórmula (ej. Divisor de voltaje simple) |
| Intermedio | ⭐⭐ | Requiere sistema de ecuaciones o manipulación del circuito |
| Avanzado | ⭐⭐⭐ | Circuitos mixtos complejos, fuentes dependientes, análisis de potencia |

---

## 2. Nomenclatura de Archivos

| Prefijo | Tipo de contenido | Ubicación |
|---------|-------------------|-----------|
| `TH-XX` | Teoría | `theory/` |
| `MET-XX` | Métodos/Procedimientos | `methods/` |
| `PR-XX` | Problemas resueltos | `problems/` |
| `EJ-XX` | Ejercicios propuestos | `problems/` |
| `SIM-XX` | Simulaciones | `simulation/` |

---

## 3. Convenciones y Símbolos Estándar

### 3.1 Símbolos Eléctricos

| Símbolo | Descripción | Unidad |
|---------|-------------|--------|
| V, v | Voltaje/Tensión | Volts (V) |
| I, i | Corriente | Amperes (A) |
| R | Resistencia | Ohms (Ω) |
| L | Inductancia | Henrios (H) |
| C | Capacitancia | Faradios (F) |
| P | Potencia | Watts (W) |
| Z | Impedancia | Ohms (Ω) |
| Y | Admitancia | Siemens (S) |

### 3.2 Convenciones Generales

- Usar notación matemática estándar de ingeniería eléctrica
- Incluir diagramas de circuitos cuando sea necesario
- Mantener consistencia en símbolos y unidades (SI)
- Documentar todas las fórmulas con su derivación o referencia

---

## 4. Estándar de Simulación con Proteus 8.15

### 4.1 Reglas para Esquemáticos (ISIS)

- **Estilo Visual**:
  - Usar componentes genéricos (RES, CAP, IND) a menos que se especifique una parte real.
  - Textos y etiquetas legibles (Times New Roman o Arial, mínimo 12pt).
  - Fondo blanco para exportación de imágenes.
- **Archivos Fuente**:
  - Los archivos `.pdsprj` deben guardarse en la carpeta `simulation/` de cada módulo.
- **Instrumentación**:
  - Usar puntas de prueba (Voltage/Current Probes) en lugar de multímetros virtuales excesivos.

### 4.2 Validación de Resultados

Al resolver problemas, comparar resultados teóricos vs. simulados:

```
Calculado: 5.00V | Simulado: 4.99V (Diferencia: 0.2%)
```

---

## 5. Formato de Solución y Verificación

### 5.1 Estructura de Solución Estándar

Toda solución generada debe seguir este formato:

```markdown
**[PR-XX]** Título del Problema

## 1. Análisis Previo
- Identificación de topología (ej. 3 mallas, sin fuentes de corriente).
- Método seleccionado: Análisis de Mallas / Nodos / Thévenin, etc.

## 2. Datos del Problema
- V₁ = 12V
- R₁ = 1kΩ, R₂ = 2kΩ
- (Lista de valores conocidos)

## 3. Planteamiento
- Ecuación Malla 1: V₁ - I₁R₁ - (I₁-I₂)R₂ = 0
- Ecuación Malla 2: ...

## 4. Cálculo
- Resolución del sistema lineal.
- **Resultados:** I₁ = 2mA, I₂ = -0.5mA

## 5. Validación (Proteus 8.15)
- Archivo de simulación: `simulation/SIM-XX-nombre.pdsprj`
- Configuración: Análisis DC Operating Point
- **Comparación:**
  | Variable | Calculado | Simulado | Error |
  |----------|-----------|----------|-------|
  | I₁       | 2.00 mA   | 1.99 mA  | 0.5%  |
  | V_out    | 5.00 V    | 4.98 V   | 0.4%  |

## 6. Conclusiones
- Verificación exitosa con error < 1%
- Observaciones adicionales si aplica
```

### 5.2 Formato para Ejercicios Propuestos

```markdown
**[EJ-XX]** Título del Ejercicio

**Dificultad:** ⭐⭐ (Intermedio)

## Enunciado
Descripción clara del problema...

## Diagrama
(Incluir esquemático o descripción textual del circuito)

## Datos
- V₁ = 10V
- R₁ = 1kΩ
- ...

## Se pide
a) Calcular la corriente I₁
b) Determinar el voltaje en R₂
c) Verificar con simulación

## Respuestas (ocultas para autoevaluación)
<!-- 
a) I₁ = 5mA
b) V_R2 = 3V
-->
```

---

## 6. Formato de Netlists y Diagramas

### 6.1 Sintaxis SPICE (Compatible con Proteus)

Para descripciones textuales de circuitos:

```spice
* Circuito Divisor de Voltaje
V1 1 0 DC 12V
R1 1 2 1k
R2 2 0 2k
.OP
.END
```

### 6.2 Descripción Textual de Conexiones

Si no se puede generar imagen:
```
R1 (10kΩ) entre Vcc (nodo 1) y N1 (nodo 2)
R2 (5kΩ) entre N1 (nodo 2) y GND (nodo 0)
Vs (12V) entre Vcc (nodo 1) y GND (nodo 0)
```

---

## 7. Estructura de manifest.json

Cada módulo debe tener un `manifest.json` con:

```json
{
  "id": "cd-02-tecnicas-analisis",
  "name": "Técnicas de Análisis de Circuitos",
  "description": "Descripción del módulo",
  "topics": ["nodos", "mallas"],
  "prerequisites": ["cd-01-conceptos"],
  "status": "en_desarrollo",
  "software_requirements": ["Proteus 8.15"],
  "difficulty_levels": {
    "conceptual": "⭐",
    "intermedio": "⭐⭐",
    "avanzado": "⭐⭐⭐"
  },
  "resource_map": {
    "theory": "theory/",
    "methods": "methods/",
    "problems": "problems/",
    "simulation": "simulation/"
  },
  "theoryFiles": 3,
  "methodFiles": 0,
  "problemFiles": 0,
  "simulationFiles": 0
}
```

---

## 8. Referencias Bibliográficas

- Nilsson, J. W., & Riedel, S. A. - "Electric Circuits"
- Alexander, C. K., & Sadiku, M. N. O. - "Fundamentals of Electric Circuits"
- Hayt, W. H., Kemmerly, J. E., & Durbin, S. M. - "Engineering Circuit Analysis"
