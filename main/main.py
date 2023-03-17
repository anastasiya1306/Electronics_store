import csv


class Item:
    pay_rate = 1
    all = []

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self) -> str:
        """Выводит информацию об экземпляре класса"""
        return f'Item({self.__name}, {self.price}, {self.quantity})'

    def __str__(self) -> str:
        """Выводит информацию пользователям об экземпляре класса"""
        return f'{self.__name}'

    @classmethod
    def instantiate_from_csv(cls, path: str):
        items = []
        """Считывает данные из csv-файла и создает экземпляры класса, инициализируя их данными из файла"""
        with open(path, 'r', encoding="UTF-8") as file:
            file_csv = csv.DictReader(file)
            for row in file_csv:
                items.append(cls(row['name'], int(row['price']), int(row['quantity'])))
        return items

    @staticmethod
    def is_integer(number) -> bool:
        """Проверяет, является ли число целым"""
        return int(number) == float(number)

    @property
    def name(self) -> str:
        """Возвращает название товара"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Проверяет, что при задании названия товара длина его не превышает 10 символов"""
        if len(value) <= 10:
            self.__name = value
        else:
            raise Exception('Длина наименования товара превышает 10 символов')

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        """Возвращает количество SIM-карт"""
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int):
        """Проверяет, чтобы количество физических SIM-карт было целым числом больше нуля"""
        if value > 0:
            self._number_of_sim = value
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __add__(self, other):
        """Сложение экземпляров класса Phone и Item. Сложение идет по количеству товара в магазине."""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError('Запрещено сложение с объектами других классов')

    def __repr__(self) -> str:
        """Выводит информацию об экземпляре класса Phone"""
        return f'Phone({self.name}, {self.price}, {self.quantity}, {self._number_of_sim})'


class MixinLog:
    """Дополнительный функционал по хранению и изменению раскладки клавиатуры"""
    def __init__(self, *args, **kwargs):
        self._language = 'EN'
        super().__init__(*args, **kwargs)

    @property
    def language(self):
        return self._language


    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'


class KeyBoard(MixinLog, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
