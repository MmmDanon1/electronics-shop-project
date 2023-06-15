from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""
def test_calculate_total_price(fixture_calculate_total_price, fixture_total_price):
    assert fixture_calculate_total_price == Item.calculate_total_price(fixture_total_price)

def test_apply_discount(fixture_discount, fixture_apply_discount):
    assert fixture_discount == fixture_apply_discount
