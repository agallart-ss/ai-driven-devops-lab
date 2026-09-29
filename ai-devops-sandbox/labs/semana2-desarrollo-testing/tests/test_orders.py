"""
Estos tests verifican la regla de negocio real (ver scenario.md).
Ejecuta: pytest labs/semana2-desarrollo-testing/tests/ -v
(agrega la carpeta app/api al PYTHONPATH, o corre desde ahí)
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "app", "api"))

from orders import apply_bulk_discount


def test_sin_descuento_pocos_articulos():
    items = [{"price": 10, "quantity": 3}]
    assert apply_bulk_discount(items) == 30.0


def test_descuento_10_porciento_rango_medio():
    items = [{"price": 10, "quantity": 6}]
    assert apply_bulk_discount(items) == 54.0


def test_descuento_15_porciento_en_el_limite_de_10():
    """Este es el caso límite: 10 artículos exactos deben tener 15% de descuento."""
    items = [{"price": 10, "quantity": 10}]
    assert apply_bulk_discount(items) == 85.0


def test_descuento_15_porciento_mas_de_10():
    items = [{"price": 10, "quantity": 12}]
    assert apply_bulk_discount(items) == 102.0
