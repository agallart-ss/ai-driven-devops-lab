"""
Orders API - lógica de negocio de descuentos.

Regla de negocio (según el equipo de producto):
- 6 a 9 artículos en la orden  -> 10% de descuento
- 10 o más artículos           -> 15% de descuento
- menos de 6 artículos         -> sin descuento
"""


def calculate_total(items, discount_percent=0):
    """Calcula el total de una orden dado un descuento en porcentaje."""
    subtotal = sum(item["price"] * item["quantity"] for item in items)
    discount = subtotal * discount_percent / 100
    total = subtotal - discount
    return round(total, 2)


def apply_bulk_discount(items):
    """Aplica el descuento por volumen según la cantidad total de artículos."""
    total_quantity = sum(item["quantity"] for item in items)

    if total_quantity > 10:
        return calculate_total(items, discount_percent=15)
    elif total_quantity > 5:
        return calculate_total(items, discount_percent=10)
    return calculate_total(items, discount_percent=0)
