from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        атрибуты класса `Item` и дополнительно атрибут, содержащий количество поддерживаемых сим-карт
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = int(number_of_sim)

    def __repr__(self):
        """
        отображает информацию об объекте класса в режиме отладки
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
