class Item:
    pay_rate = 1
    all = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self):
        self.calculate_total_price = self.price * self.quantity
        return self.calculate_total_price


    def apply_discount(self,):
        self.price = self.price * self.pay_rate
        return self.price

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    print(item1.calculate_total_price())
    print(item2.calculate_total_price())
    Item.pay_rate = 0.8
    item1.apply_discount()
    print(item1.price)
    print(item2.price)

    print(Item.all)