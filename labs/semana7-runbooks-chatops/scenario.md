# Semana 7 — Runbooks inteligentes / ChatOps con IA

## Contexto

Después del incidente de la Semana 6 (pico de errores 500 por "connection pool exhausted"),
el equipo se dio cuenta de que no existe un runbook para este tipo de incidente — cada vez
que pasa, alguien tiene que resolverlo desde cero.

## Tu tarea — Parte 1: Runbook inteligente

1. Usa tu bitácora de la Semana 6 (causa probable, evidencia, qué hiciste) como contexto.
2. Pídele a tu IA que te ayude a redactar un **runbook** para este tipo de incidente,
   con esta estructura mínima:
   - Síntomas (cómo se detecta)
   - Diagnóstico rápido (qué comandos/consultas correr primero)
   - Mitigación inmediata (qué hacer para aliviar el síntoma, aunque no sea el fix final)
   - Causa raíz probable y cómo confirmarla
   - Solución definitiva
   - Cuándo escalar a un humano en vez de seguir el runbook
3. Guarda el runbook en `labs/semana7-runbooks-chatops/runbook-connection-pool.md`.

## Tu tarea — Parte 2: ChatOps (conceptual)

No necesitas implementar un bot real. Diseña, con ayuda de la IA, cómo se vería este
runbook si estuviera integrado en un canal de Slack/Teams tipo ChatOps:
- ¿Qué comando escribiría un ingeniero en el chat para activarlo? (ej. `/runbook connection-pool`)
- ¿Qué pasos podría ejecutar el bot automáticamente vs. cuáles requieren aprobación humana?
- ¿Dónde pondrías el límite de autonomía del bot, y por qué? (conecta con lo que decidiste
  para el agente de la Semana 5)

## Qué documentar en tu bitácora esta semana

- El runbook generado (o un resumen si es largo).
- Dónde decidiste poner el límite de autonomía del ChatOps bot y por qué.

## Si estás en Ruta B (problema propio)

Usa un incidente real (sanitizado) de tu trabajo en vez del de la Semana 6.
