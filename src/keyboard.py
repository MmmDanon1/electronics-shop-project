from src.item import Item

class Mixinlog:
    """
    класс-миксин, который “подмешивается” в цепочку наследования класса `Keyboard', запоминает раскладку клавиатуры
    """
    def __init__(self,language="EN"):
        self.__language = language

    @property
    def language(self):
        """
        обращение к атрибуту
        """
        return self.__language

    def change_lang(self):
        """
        изменить язык клавиатуры
        """
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        return self

class KeyBoard(Item, Mixinlog):
    """
    класс для товара “клавиатура”
    """
    pass









