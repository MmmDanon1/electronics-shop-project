import pytest

from src.item import Item
@pytest.fixture
def fixture_calculate_total_price():
     item1 = Item("Смартфон", 10000, 20)
     return item1

@pytest.fixture
def fixture_apply_discount():
    pass