<!--
::METADATA::
type: reference
topic_id: meta-audit
file_id: audit-table-issues
status: active
audience: ai_context
last_updated: 2026-01-08
-->

# 📝 Registro de Problemas — Auditoría

> Este documento registra problemas detectados durante las auditorías del repositorio.
>
> _Última actualización: 2026-01-08_

---

## Estado General

| Métrica | Valor |
|---------|-------|
| **Problemas abiertos** | 0 |
| **Problemas resueltos** | 3 |
| **Última auditoría** | 2026-01-08 |

---

## 🔴 Problemas Abiertos

_No hay problemas abiertos actualmente._

---

## ✅ Problemas Resueltos

### [RESUELTO] #001 — Archivos faltantes en 00-META

| Campo | Valor |
|-------|-------|
| **Fecha detectado** | 2026-01-08 |
| **Fecha resuelto** | 2026-01-08 |
| **Severidad** | Media |
| **Descripción** | Faltaban archivos de auditoría según plantilla |
| **Archivos afectados** | `ai-directives.md`, `audit-file-list.md`, `audit-table-issues.md`, `directory-tree.md`, `repo-tests.md`, `prompts-for-students.md`, `plantilla-respuestas.md` |
| **Solución** | Creados todos los archivos faltantes |

---

### [RESUELTO] #002 — Script check_tables.py faltante

| Campo | Valor |
|-------|-------|
| **Fecha detectado** | 2026-01-08 |
| **Fecha resuelto** | 2026-01-08 |
| **Severidad** | Baja |
| **Descripción** | No existía el validador de tablas Markdown |
| **Archivos afectados** | `00-META/tools/check_tables.py` |
| **Solución** | Creado script de validación |

---

### [RESUELTO] #003 — Carpetas Notas/ faltantes

| Campo | Valor |
|-------|-------|
| **Fecha detectado** | 2026-01-08 |
| **Fecha resuelto** | 2026-01-08 |
| **Severidad** | Media |
| **Descripción** | Los subtemas no tenían zona sandbox |
| **Archivos afectados** | 11 subtemas |
| **Solución** | Creadas carpetas `Notas/` con `README.md` en cada subtema |

---

## 📊 Historial de Auditorías

| Fecha | Tipo | Problemas encontrados | Problemas resueltos |
|-------|------|----------------------|---------------------|
| 2026-01-08 | Completa | 3 | 3 |

---

## 🔧 Cómo Reportar un Problema

1. Ejecutar `python validate_repo.py` en `00-META/tools/`
2. Documentar el problema en este archivo con formato:

```markdown
### [ABIERTO] #XXX — Título descriptivo

| Campo | Valor |
|-------|-------|
| **Fecha detectado** | YYYY-MM-DD |
| **Severidad** | Alta/Media/Baja |
| **Descripción** | Descripción del problema |
| **Archivos afectados** | Lista de archivos |
| **Solución propuesta** | Acciones a tomar |
```

3. Al resolver, cambiar `[ABIERTO]` por `[RESUELTO]` y añadir fecha de resolución.
