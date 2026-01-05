<!--
::METADATA::
type: directive
topic_id: ca-02-redes-dos-puertos
file_id: _directives
status: active
audience: ai_context
last_updated: 2026-01-05
-->

# Directivas IA — Redes de Dos Puertos

## Hereda de

- [Contrato IA Global](../../00-META/ia-contract.md)
- [Nomenclatura Estándar](../../00-META/nomenclatura-estandar.md)
- [Notación y Símbolos](../../00-META/notation-cheatsheet.md)

---

## Contexto del Subtema

| Campo | Valor |
|-------|-------|
| **ID** | `ca-02-redes-dos-puertos` |
| **Módulo** | 02-Circuitos-CA |
| **Prerequisitos** | `ca-01-analisis-ca-estado-estacionario` |
| **Nivel base** | ⭐⭐⭐ Avanzado |

---

## Directivas Específicas

### 1. Conceptos Clave a Dominar

- Definición de red de dos puertos
- Parámetros de impedancia (z)
- Parámetros de admitancia (y)
- Parámetros híbridos (h)
- Parámetros de transmisión (ABCD o T)
- Interconexión de redes (serie, paralelo, cascada)

### 2. Convenciones de Notación

| Símbolo | Significado |
|---------|-------------|
| $[z]$ | Matriz de parámetros z |
| $[y]$ | Matriz de parámetros y |
| $[h]$ | Matriz de parámetros h |
| $[T]$ o $[ABCD]$ | Matriz de transmisión |
| $V_1, I_1$ | Variables del puerto 1 |
| $V_2, I_2$ | Variables del puerto 2 |

### 3. Ecuaciones Matriciales

**Parámetros z:**
$$\begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} z_{11} & z_{12} \\ z_{21} & z_{22} \end{bmatrix} \begin{bmatrix} I_1 \\ I_2 \end{bmatrix}$$

**Parámetros y:**
$$\begin{bmatrix} I_1 \\ I_2 \end{bmatrix} = \begin{bmatrix} y_{11} & y_{12} \\ y_{21} & y_{22} \end{bmatrix} \begin{bmatrix} V_1 \\ V_2 \end{bmatrix}$$

### 4. Verificación de Respuestas

- [ ] Verificar condiciones de medición (circuito abierto/cortocircuito)
- [ ] Para red recíproca: $z_{12} = z_{21}$, $y_{12} = y_{21}$
- [ ] Verificar conversión entre parámetros
- [ ] Comprobar determinante de matrices

### 5. Errores Comunes a Detectar

- Confundir condiciones de circuito abierto vs cortocircuito
- Error en convención de corriente $I_2$ (entrante vs saliente)
- Multiplicar matrices en orden incorrecto (cascada)
- Olvidar que $[y] = [z]^{-1}$ solo si existe inversa

---

## Referencias Bibliográficas

Ver [`manifest.json`](manifest.json) para mapeo completo de capítulos.

**Fuentes principales:**
- Sadiku (2013): Capítulo 18
- Nilsson (2015): Capítulo 18

---

## Mapa de Recursos

```
theory/      → Fundamentos teóricos (TH-01 a TH-03)
methods/     → Procedimientos paso a paso (MET-01)
problems/    → Enunciados de ejercicios (PR-01 a PR-03)
solutions/   → Respuestas y soluciones desarrolladas
simulation/  → Archivos Proteus 8.15
```
