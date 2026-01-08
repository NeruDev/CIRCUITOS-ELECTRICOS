<!--
::METADATA::
type: reference
topic_id: meta-audit
file_id: audit-file-list
status: active
audience: ai_context
last_updated: 2026-01-08
-->

# 📋 Lista de Archivos Obligatorios

> Checklist para validar la integridad del repositorio según la [Plantilla de Arquitectura Modular Universal](../Plantilla%20de%20Arquitectura%20Modular%20Universal.md).

---

## Nivel 0 — Raíz

| Archivo | Obligatorio | Descripción |
|---------|-------------|-------------|
| `README.md` | ✅ Sí | Portada del proyecto |
| `WIKI_INDEX.md` | ✅ Sí | Tabla de contenidos maestra |
| `glossary.md` | ✅ Sí | Diccionario de términos |
| `AUDITORIA_ESTADO_REPO.md` | ✅ Sí | Reporte de salud |
| `constants.md` | ⚪ Opcional | Constantes físicas (específico de este repo) |

---

## Nivel 0 — 00-META/

| Archivo | Obligatorio | Descripción |
|---------|-------------|-------------|
| `ia-contract.md` | ✅ Sí | Ley suprema para IA |
| `ai-directives.md` | ✅ Sí | Directivas técnicas complementarias |
| `nomenclatura-estandar.md` | ✅ Sí | Convenciones de nombrado |
| `notation-cheatsheet.md` | ✅ Sí | Símbolos y notación |
| `bibliografia-general.md` | ✅ Sí | Fuentes académicas |
| `study-guide.md` | ✅ Sí | Guía para estudiantes |
| `prompts-for-students.md` | ✅ Sí | Prompts prediseñados |
| `plantilla-respuestas.md` | ✅ Sí | Modelo para soluciones |
| `audit-file-list.md` | ✅ Sí | Este documento |
| `audit-table-issues.md` | ✅ Sí | Registro de problemas |
| `directory-tree.md` | ✅ Sí | Árbol de directorios ideal |
| `repo-tests.md` | ✅ Sí | Pruebas de integridad |

---

## Nivel 0 — 00-META/tools/

| Archivo | Obligatorio | Descripción |
|---------|-------------|-------------|
| `validate_repo.py` | ✅ Sí | Auditor de estructura |
| `link_knowledge_base.py` | ✅ Sí | Auto-vinculador |
| `check_tables.py` | ✅ Sí | Validador de tablas |
| `requirements.txt` | ✅ Sí | Dependencias Python |
| `README.md` | ⚪ Opcional | Documentación de herramientas |

---

## Nivel 1 — Módulos (XX-Nombre/)

| Archivo | Obligatorio | Descripción |
|---------|-------------|-------------|
| `00-Index.md` | ✅ Sí | Índice del módulo |

---

## Nivel 2 — Subtemas (XX-Nombre-Subtema/)

| Elemento | Obligatorio | Descripción |
|----------|-------------|-------------|
| `manifest.json` | ✅ Sí | Metadatos para IA |
| `_directives.md` | ✅ Sí | Instrucciones específicas |
| `00-Intro.md` | ✅ Sí | Punto de entrada |
| `Resumen-Formulas.md` | ✅ Sí | Cheatsheet |
| `theory/` | ✅ Sí | Carpeta de teoría |
| `methods/` | ✅ Sí | Carpeta de métodos |
| `problems/` | ✅ Sí | Carpeta de ejercicios |
| `solutions/` | ✅ Sí | Carpeta de respuestas |
| `simulation/` | ⚪ Opcional | Archivos Proteus |
| `media/` | ⚪ Opcional | Recursos visuales |
| `Notas/` | ✅ Sí | Zona sandbox |
| `Notas/README.md` | ✅ Sí | Directiva de excepción |

---

## Validación Automática

Ejecutar para verificar archivos obligatorios:

```bash
cd 00-META/tools
python validate_repo.py --check-files
```

---

## Campos Obligatorios en manifest.json

```json
{
  "id": "REQUERIDO",
  "name": "REQUERIDO", 
  "description": "REQUERIDO",
  "topics": "REQUERIDO (array)",
  "status": "REQUERIDO"
}
```

---

## Bloques ::METADATA:: Obligatorios

Todo archivo `.md` de contenido debe incluir:

```markdown
<!--
::METADATA::
type: [theory|method|problem|solution|reference|index]
topic_id: [id-del-tema]
file_id: [nombre-archivo]
status: [draft|review|stable|active]
audience: [student|ai_context|both]
last_updated: YYYY-MM-DD
-->
```
