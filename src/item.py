import csv
import math
import os

class InstantiateCSVError(Exception):
    """
    Класс-исключение
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "InstantiateCSVError: Файл item.csv поврежден"

    def __str__(self):
        return self.message

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
        super().__init__()

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
    def instantiate_from_csv(cls, file_name):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        """
        try:
            cls.all.clear()
            with open(os.path.join(os.path.dirname(__file__), file_name), newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name, price, quantity = row['name'], row['price'], row['quantity']
                    if name or price or quantity == '':
                        raise InstantiateCSVError("Файл item.csv поврежден")
                    cls(name, float(price), int(quantity))
        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(number: str) -> int:
        """
        Статический метод, возвращающий число из числа-строки
        """
        number_float = float(number)
        return math.floor(number_float)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
