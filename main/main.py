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
