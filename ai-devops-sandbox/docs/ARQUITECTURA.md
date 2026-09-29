# Arquitectura de la app de ejemplo: Orders API

```
        Cliente
           │
           ▼
      ┌─────────┐        ┌──────────┐
      │   API   │──────▶ │  Worker  │
      │ (Flask) │        │ (cola)   │
      └─────────┘        └──────────┘
           │
           ▼
      ┌─────────┐
      │   "DB"  │  (archivo JSON local — simula una base de datos)
      └─────────┘
```

Es una app deliberadamente simple: un servicio de "órdenes" con lógica de descuentos
(`app/api/orders.py`) y un worker que procesa órdenes pendientes (`app/worker/worker.py`).

No necesitas entenderla a fondo — el objetivo de cada lab no es la app en sí, sino el
problema de DevOps/IA que se monta alrededor de ella cada semana (un bug, un pipeline roto,
una configuración de Terraform riesgosa, etc.).

Si trabajas con la Ruta B (problema propio), puedes ignorar esta app por completo.
