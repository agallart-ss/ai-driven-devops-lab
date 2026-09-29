# Semana 2 — Desarrollo asistido por IA / Testing y calidad con IA

## Contexto

El equipo de producto reportó que algunos clientes que ordenan **exactamente 10 artículos**
se están quejando: dicen que deberían recibir 15% de descuento (como indica la política),
pero el sistema les está aplicando solo 10%.

**Regla de negocio (confirmada con producto):**
- 6 a 9 artículos → 10% de descuento
- 10 o más artículos → 15% de descuento
- menos de 6 artículos → sin descuento

## Evidencia disponible

- El código de la lógica de descuento: `app/api/orders.py`
- Un set de tests que documentan el comportamiento esperado: `tests/test_orders.py`

## Tu tarea

1. Corre los tests primero, **antes** de mirar el código, para confirmar el síntoma:
   ```bash
   python3 -m pytest labs/semana2-desarrollo-testing/tests/ -v
   ```
2. Usa tu asistente de IA para **investigar la causa**, no para que te dé el fix directo.
   Dale contexto real: pega el código de `orders.py`, el test que falla, y la regla de negocio.
   Pídele que primero te explique qué está pasando antes de proponer una corrección.
3. Valida la hipótesis de la IA tú mismo (no le pidas que "confirme" su propia respuesta).
4. Aplica la corrección y vuelve a correr los tests — los 4 deben pasar.
5. Bonus (recomendado): pídele a la IA que te ayude a pensar en **otro caso límite** que
   los tests actuales no cubran, y agrégalo tú mismo.

## Qué documentar en tu bitácora esta semana

- El contexto exacto que le diste a la IA (¿le diste la regla de negocio completa o solo el error?).
- Si la primera hipótesis de la IA fue correcta o tuviste que corregirla.
- Cómo validaste el fix antes de darlo por bueno.
