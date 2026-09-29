# Semana 8 — DevSecOps + IA responsable

## Contexto

El equipo quiere finalmente llevar `orders-api` a Kubernetes. Alguien ya preparó un
manifiesto y un Dockerfile "que funcionan en su laptop" y pide luz verde para producción.

## Evidencia disponible

- `manifiesto-inseguro.yaml`
- `Dockerfile-inseguro`

## Tu tarea

1. **Antes de pedirle nada a la IA, sanitiza mentalmente:** este ejercicio contiene
   secretos de ejemplo (falsos) a propósito, para que practiques identificarlos. **Nunca
   pegues credenciales reales en una IA, ni siquiera en un ejercicio como este.**
2. Pídele a tu asistente de IA que revise ambos archivos **desde una perspectiva de
   seguridad** y liste cada problema que encuentre, explicando el riesgo de cada uno
   (no solo "esto está mal", sino *por qué* importa).
3. Compara lo que encontró la IA contra tu propia revisión — ¿se le pasó algo?
   ¿Señaló algo que no era un problema real?
4. Corrige el manifiesto y el Dockerfile aplicando buenas prácticas (secretos fuera del
   YAML, usuario no-root, límites de recursos, sin `privileged: true`).
5. Escribe, con ayuda de la IA, un mini checklist de **"qué revisar antes de desplegar a
   producción"** que el equipo pueda reutilizar en futuros despliegues.

## Qué documentar en tu bitácora esta semana

- Los problemas que encontró la IA vs. los que encontraste tú antes de preguntarle.
- Cómo sanitizaste el contexto que le compartiste (conecta con la sección 14 del programa:
  nunca compartir passwords, API keys, tokens o datos de clientes reales con la IA).
- El checklist final que generaron juntos.

## Cierre del curso

Esta es también la semana de consolidar tu bitácora completa. Antes de la Sesión 16,
completa la sección **"Consolidado — Proyecto Integrador"** de tu bitácora con el
resumen de todo el curso.
