# Semana 3 — Fundamentos de CI/CD / Pipelines con IA

## Contexto

Alguien del equipo modificó el workflow de GitHub Actions y ahora el pipeline falla en
cada push, pero jura que "no cambió nada importante, solo reordenó unos pasos".

## Tu tarea

1. Reemplaza temporalmente el contenido de `.github/workflows/ci.yml` en tu repo por el de
   `labs/semana3-cicd/pipeline-con-bug.yml` (o simplemente ábrelos lado a lado — no hace
   falta que lo ejecutes en GitHub, puedes analizarlo directamente).
2. Pídele a tu asistente de IA que **explique qué va a pasar antes de que corra**, dado el
   orden de los pasos — no le pidas el fix de inmediato.
3. Si tienes forma de correrlo (push a tu repo o simulándolo local paso a paso), confirma
   el error real y compáralo con la predicción de la IA.
4. Corrige el orden y deja el pipeline funcional (puedes comparar contra
   `.github/workflows/ci.yml`, que es la versión correcta, pero intenta llegar tú primero).
5. Pídele a la IA una sugerencia de **mejora adicional** al pipeline (ej. cachear
   dependencias, agregar un paso de lint) y evalúa si tiene sentido aplicarla.

## Qué documentar en tu bitácora esta semana

- Si la predicción de la IA sobre el error coincidió con lo que realmente pasó.
- Qué mejora adicional propuso y si decidiste aplicarla o no (y por qué).

## Si estás en Ruta B (problema propio)

Si tienes un pipeline real y roto en tu trabajo, úsalo en vez de este — pero sanitiza
cualquier nombre de proyecto, credencial o URL interna antes de compartirlo con la IA.
