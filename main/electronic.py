from main import Item

if __name__ == '__main__':
    # item1 = Item("Смартфон", 10000, 20)
    # item2 = Item("Ноутбук", 20000, 5)
    # print(item1.calculate_total_price())
    # print(item2.calculate_total_price())
    # Item.pay_rate = 0.8
    # item1.apply_discount()
    # print(item1.price)
    # print(item2.price)
    #
    # print(Item.all)
    #
    # item = Item('Телефон', 10000, 5)
    # item.name = 'Смартфон'
    # print(item.name)

    # item.name = 'СуперСмартфон'

    Item.instantiate_from_csv("items.csv")
    print(len(Item.all))
    item1 = Item.all[0]
    print(item1.name)
    print(Item.is_integer(5))
    print(Item.is_integer(5.0))
    print(Item.is_integer(5.5))
