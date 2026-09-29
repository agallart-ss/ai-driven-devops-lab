# Semana 5 — Introducción a agentes / Desarrollo de agentes

## Contexto

El equipo quiere dejar de revisar manualmente qué órdenes fallaron y reintentarlas a mano.
Piden un agente simple que lo haga solo, con un límite de reintentos y que sepa cuándo
"rendirse" y avisar a un humano.

## Evidencia disponible

- `agente_esqueleto.py` — el esqueleto incompleto (tiene TODOs).
- `queue-ejemplo.json` — una cola de ejemplo con órdenes en distintos estados, cópiala
  a `app/worker/queue.json` para poder probar tu agente.

## Tu tarea

1. Antes de escribir código, pídele a tu IA que te explique **qué es un agente** en este
   contexto y en qué se diferencia de simplemente llamar a un modelo una vez (revisa
   también el material de "Introducción a agentes" de esta semana).
2. Completa los TODOs de `agente_esqueleto.py` con ayuda de la IA, pero decide tú
   explícitamente:
   - ¿Qué pasa cuando una orden llega a `MAX_RETRIES`? (ORD-1003 en el ejemplo ya está ahí)
   - ¿El agente debe actuar solo, o debe pedir confirmación antes de reintentar?
3. Corre tu agente contra `queue-ejemplo.json` y verifica que el comportamiento sea el
   esperado para cada orden (completed, failed con pocos intentos, failed en el límite,
   pending).
4. Reflexiona: si este agente estuviera corriendo en producción sin supervisión, ¿qué
   podría salir mal? ¿Qué límites de seguridad le pondrías?

## Qué documentar en tu bitácora esta semana

- Qué tan autónomo decidiste hacer al agente y por qué.
- Qué límites de seguridad le pusiste (esto conecta directo con el tema de la Semana 8).
