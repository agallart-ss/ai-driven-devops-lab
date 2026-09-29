"""
Esqueleto de un agente simple para "Orders API".

Objetivo del agente: revisar la cola de órdenes (app/worker/queue.json) y,
si encuentra órdenes marcadas como "failed", reintentarlas automáticamente
hasta un máximo de 3 intentos, registrando cada acción que toma.

Este archivo está incompleto a propósito (ver los TODO). La idea es que completes
la lógica con ayuda de tu asistente de IA, entendiendo cada decisión de diseño
en vez de pedir el archivo completo de una sola vez.
"""
import json
import os

QUEUE_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "app", "worker", "queue.json")
MAX_RETRIES = 3


def load_queue():
    # TODO: leer el archivo de cola y devolver la lista de órdenes.
    # ¿Qué pasa si el archivo no existe todavía? Decide y documenta por qué.
    pass


def needs_retry(order):
    # TODO: decidir si una orden necesita reintento.
    # Pista: revisa el campo "status" y el campo "attempts" de cada orden.
    pass


def retry_order(order):
    # TODO: incrementar el contador de intentos y registrar la acción.
    # Pregúntale a tu IA: ¿qué debería pasar si se alcanza MAX_RETRIES?
    # ¿el agente debería seguir reintentando para siempre, o escalar a un humano?
    pass


def run_agent():
    orders = load_queue() or []
    for order in orders:
        if needs_retry(order):
            retry_order(order)
    # TODO: decide qué hace el agente con el resultado final:
    # ¿guarda la cola actualizada? ¿imprime un resumen? ¿notifica a alguien?


if __name__ == "__main__":
    run_agent()
