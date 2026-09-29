# Semana 4 — Arquitecturas modernas con IA / Servicios de IA en la nube

## Contexto

El equipo necesita un bucket para guardar los reportes de órdenes que genera el worker.
Alguien ya escribió una primera versión de Terraform (`terraform/main.tf`) usando
LocalStack (no se necesita cuenta AWS real) y pide una revisión antes de aplicarla.

## Tu tarea

1. **No corras `terraform apply` todavía.** Primero pídele a tu asistente de IA que te
   explique, línea por línea, qué va a crear este archivo y qué implicaciones tiene —
   especialmente el bloque de `acl` y el de `versioning`.
2. Pregúntale explícitamente: *"¿esta configuración es apropiada para datos de clientes?
   ¿qué cambiarías y por qué?"* — no le pidas el archivo corregido de una vez, primero
   que te explique el razonamiento.
3. Si tienes Docker disponible, levanta LocalStack y prueba `terraform plan` para ver
   qué reporta:
   ```bash
   docker run -d -p 4566:4566 localstack/localstack
   cd labs/semana4-cloud-iac/terraform
   terraform init && terraform plan
   ```
   Si no puedes correr Terraform en tu entorno, analiza el archivo estáticamente —
   es igual de válido para esta práctica.
4. Corrige lo que identifiques como riesgoso y documenta el porqué de cada cambio.
5. **Parte 2 — Servicios de IA en la nube:** además de la revisión de seguridad,
   describe en tu bitácora cómo integrarías un servicio de IA gestionado (por ejemplo,
   una base de datos vectorial o una API de embeddings) si el equipo quisiera agregar
   búsqueda semántica sobre los reportes de órdenes. No hace falta implementarlo,
   solo el razonamiento arquitectónico con ayuda de la IA.

## Qué documentar en tu bitácora esta semana

- Qué riesgos identificó la IA (y si tú los habías notado antes de preguntar).
- Tu decisión final sobre la configuración del bucket y por qué.
- Tu propuesta de integración de un servicio de IA en la nube (Parte 2).

## Si estás en Ruta B (problema propio)

Si tienes IaC real de tu trabajo, pide a la IA la misma revisión (qué cambia, por qué,
impacto, rollback, seguridad) — son las mismas preguntas que en la sección 9 del programa.
