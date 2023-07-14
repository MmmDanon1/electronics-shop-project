from src.item import Item, InstantiateCSVError
from src.phone import Phone
from src.keyboard import KeyBoard

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
    Item.instantiate_from_csv("items.csv")  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам
    Item.instantiate_from_csv("items.cs")  # создание объектов из данных файла
    assert "Отсутствует файл item.csv"
    Item.instantiate_from_csv("items_test.csv")  # создание объектов из данных файла
    assert "InstantiateCSVError: Файл item.csv поврежден"


def test_string_to_number():
    assert Item.string_to_number('5.5') == 5

def test_str_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'

def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25

def test_number_sim_card():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2
    phone2 = Phone("iPhone 14", 120_000, 5, 2.2)
    assert phone2.number_of_sim == 2

def test_name_subclass():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.name == "iPhone 14"

def test_class_name():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

def test_kb_language():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"

def test_kb_selectid_language():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"













