from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        атрибуты класса `Item` и дополнительно атрибут, содержащий количество поддерживаемых сим-карт
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = int(number_of_sim)

    def __repr__(self):
        """
        отображает информацию об объекте класса в режиме отладки
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Добавим геттер number_of_sim`
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, crop):
        """
        В сеттере `number_of_sim` проверяем, что больше или ровно 1ой
        """
        if crop <= 0:
            print("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")
        elif crop > 0:
            self.__number_of_sim = crop
