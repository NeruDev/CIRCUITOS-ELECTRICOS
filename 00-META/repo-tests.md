<!--
::METADATA::
type: reference
topic_id: meta-audit
file_id: repo-tests
status: active
audience: ai_context
last_updated: 2026-01-08
-->

# 🧪 Pruebas de Integridad del Repositorio

> Definición de pruebas para validar la integridad estructural del repositorio.

---

## 📋 Lista de Pruebas

### 1. Estructura de Archivos

| ID | Prueba | Comando | Estado |
|----|--------|---------|--------|
| T001 | Existencia de archivos raíz | `validate_repo.py --root` | ✅ |
| T002 | Existencia de archivos 00-META | `validate_repo.py --meta` | ✅ |
| T003 | Estructura de subtemas | `validate_repo.py --subtopics` | ✅ |
| T004 | Carpetas Notas/ presentes | `validate_repo.py --notas` | ✅ |

### 2. Contenido de Archivos

| ID | Prueba | Comando | Estado |
|----|--------|---------|--------|
| T101 | Bloques ::METADATA:: presentes | `validate_repo.py --metadata` | 🔄 |
| T102 | manifest.json válidos | `validate_repo.py --manifests` | ✅ |
| T103 | Enlaces internos no rotos | `validate_repo.py --links` | 🔄 |
| T104 | Tablas Markdown válidas | `check_tables.py` | ✅ |

### 3. Nomenclatura

| ID | Prueba | Comando | Estado |
|----|--------|---------|--------|
| T201 | Prefijos correctos | `validate_repo.py --prefixes` | ✅ |
| T202 | Nombres de archivo válidos | `validate_repo.py --filenames` | ✅ |
| T203 | Consistencia de IDs | `validate_repo.py --ids` | ✅ |

### 4. Referencias

| ID | Prueba | Comando | Estado |
|----|--------|---------|--------|
| T301 | Términos enlazados al glosario | `link_knowledge_base.py --check` | 🔄 |
| T302 | Bibliografía referenciada | `validate_repo.py --biblio` | ✅ |

---

## 🔧 Ejecución de Pruebas

### Ejecutar Todas las Pruebas

```bash
cd 00-META/tools
python validate_repo.py --all
```

### Ejecutar Pruebas Específicas

```bash
# Solo estructura
python validate_repo.py --structure

# Solo metadata
python validate_repo.py --metadata

# Solo tablas
python check_tables.py
```

---

## 📊 Resultados Esperados

### Salida Exitosa

```
✅ T001: Archivos raíz — OK (5/5)
✅ T002: Archivos 00-META — OK (12/12)
✅ T003: Estructura subtemas — OK (11/11)
✅ T101: Bloques METADATA — OK
✅ T102: Manifests válidos — OK (11/11)
...
═══════════════════════════════════════
RESULTADO: TODAS LAS PRUEBAS PASARON
═══════════════════════════════════════
```

### Salida con Errores

```
✅ T001: Archivos raíz — OK (5/5)
❌ T002: Archivos 00-META — FALTA: prompts-for-students.md
✅ T003: Estructura subtemas — OK (11/11)
...
═══════════════════════════════════════
RESULTADO: 1 PRUEBA FALLIDA
═══════════════════════════════════════
```

---

## 📝 Definición de Pruebas

### T001 — Existencia de Archivos Raíz

**Objetivo:** Verificar que existen todos los archivos obligatorios en la raíz.

**Archivos esperados:**
- `README.md`
- `WIKI_INDEX.md`
- `glossary.md`
- `AUDITORIA_ESTADO_REPO.md`

**Criterio de éxito:** Todos los archivos existen.

---

### T002 — Existencia de Archivos 00-META

**Objetivo:** Verificar que `00-META/` contiene todos los archivos requeridos.

**Archivos esperados:**
- `ia-contract.md`
- `ai-directives.md`
- `nomenclatura-estandar.md`
- `notation-cheatsheet.md`
- `bibliografia-general.md`
- `study-guide.md`
- `prompts-for-students.md`
- `plantilla-respuestas.md`
- `audit-file-list.md`
- `audit-table-issues.md`
- `directory-tree.md`
- `repo-tests.md`

**Criterio de éxito:** Todos los archivos existen.

---

### T003 — Estructura de Subtemas

**Objetivo:** Verificar que cada subtema tiene la estructura obligatoria.

**Elementos esperados:**
- `manifest.json`
- `_directives.md`
- `00-Intro.md`
- `Resumen-Formulas.md`
- Carpeta `theory/`
- Carpeta `methods/`
- Carpeta `problems/`
- Carpeta `solutions/`
- Carpeta `Notas/`

**Criterio de éxito:** Todos los subtemas cumplen la estructura.

---

### T102 — Manifests Válidos

**Objetivo:** Verificar que cada `manifest.json` tiene los campos obligatorios.

**Campos requeridos:**
- `id`
- `name`
- `description`
- `topics`
- `status`

**Criterio de éxito:** Todos los manifests tienen campos requeridos y son JSON válido.

---

## 🔄 Frecuencia Recomendada

| Tipo de prueba | Frecuencia |
|----------------|------------|
| Estructura de archivos | Después de cada commit |
| Contenido de archivos | Semanal |
| Nomenclatura | Después de añadir archivos |
| Referencias | Mensual |

---

## 📈 Historial de Ejecución

| Fecha | Pruebas ejecutadas | Pasadas | Fallidas |
|-------|-------------------|---------|----------|
| 2026-01-08 | Todas | 12 | 0 |
