"""
Worker de ejemplo: procesa órdenes pendientes de un archivo "queue.json".
Deliberadamente simple - no requiere infraestructura real para correr.
"""
import json
import time
import os

QUEUE_FILE = os.path.join(os.path.dirname(__file__), "queue.json")


def process_orders():
    if not os.path.exists(QUEUE_FILE):
        print("No hay cola de órdenes todavía.")
        return

    with open(QUEUE_FILE) as f:
        orders = json.load(f)

    for order in orders:
        print(f"Procesando orden {order.get('id')}...")
        time.sleep(0.2)

    print(f"{len(orders)} órdenes procesadas.")


if __name__ == "__main__":
    process_orders()
