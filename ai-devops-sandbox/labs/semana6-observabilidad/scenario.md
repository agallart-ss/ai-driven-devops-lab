# Semana 6 — Observabilidad moderna / AIOps en práctica

## Contexto

Recibiste una alerta genérica de "latencia elevada" en `orders-api` durante la mañana del
20 de septiembre. No hay más contexto que el log crudo del servicio.

## Evidencia disponible

- `logs/orders-api.log` — log real (simulado) del servicio durante esa mañana.

## Tu tarea

1. **No abras el archivo completo de un jalón.** Dale el log (o un fragmento representativo,
   si es muy largo para el contexto de tu asistente) a la IA y pídele que:
   - Detecte el patrón anómalo.
   - Te diga en qué ventana de tiempo ocurrió.
   - Proponga hipótesis de causa raíz basadas *solo* en lo que ve en el log.
2. Valida tú mismo la hipótesis: cuenta cuántas líneas de error hay, confirma el rango de
   timestamps, y revisa si la latencia y el mensaje de error son consistentes con la
   hipótesis de la IA.
3. Pídele que te ayude a redactar un resumen tipo "postmortem corto" del incidente
   (una sección de la sección 11 y 19 del programa) con: qué pasó, cuándo, impacto
   estimado, y causa probable.
4. Piensa qué **evidencia adicional** (que no está en este log) pedirías en un incidente
   real para confirmar la causa raíz antes de tomar acción.

## Qué documentar en tu bitácora esta semana

- La hipótesis de la IA vs. lo que tú verificaste manualmente en el log.
- Qué evidencia adicional pedirías en un caso real.
