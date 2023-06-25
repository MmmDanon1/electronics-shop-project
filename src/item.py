import csv
import math
import os

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        """
        отображает информацию об объекте класса в режиме отладки
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        отображает информацию об объекте класса для пользователей
        """
        return self.__name



    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @property
    def name(self):
        """
        Добавим геттер name`
        """
        return self.__name

    @name.setter
    def name(self, crop):
        """
        В сеттере `name` проверяем, что длина наименования товара не больше 10 симвовов.
        """
        if len(crop) > 10:
            self.__name = crop[0:10]
        else:
            self.__name = crop

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        """
        cls.all.clear()
        with open(os.path.join(os.path.dirname(__file__), 'items.csv'), newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name, price, quantity = row['name'], row['price'], row['quantity']
                cls(name, float(price), int(quantity))

    @staticmethod
    def string_to_number(number: str) -> int:
        """
        Статический метод, возвращающий число из числа-строки
        """
        number_float = float(number)
        return math.floor(number_float)










