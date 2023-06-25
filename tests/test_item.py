from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""
def test_calculate_total_price(fixture_calculate_total_price, fixture_total_price):
    assert fixture_calculate_total_price == Item.calculate_total_price(fixture_total_price)

def test_apply_discount(fixture_discount, fixture_apply_discount):
    assert fixture_discount == fixture_apply_discount

def test_name():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"

def test_name_setter():
    item1 = Item("Смартфон", 10000, 20)
    item1.name = "1234567891011"
    assert item1.name == "1234567891"

def test_instantiate_from_csv():
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

def test_string_to_number():
    assert Item.string_to_number('5.5') == 5

def test_str_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'





