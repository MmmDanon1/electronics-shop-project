import pytest

from src.item import Item
@pytest.fixture
def fixture_calculate_total_price():
    return 200000

@pytest.fixture
def fixture_total_price():
    item1 = Item("Смартфон", 10000, 20)
    return item1

@pytest.fixture
def fixture_discount():
    return 8000.0

@pytest.fixture
def fixture_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    return item1.price

