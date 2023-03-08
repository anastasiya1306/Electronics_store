import pytest
from main.main import Item


@pytest.mark.parametrize(
    "name, price, quantity, result",
    [("Смартфон", 10000, 20, 200000), ("Ноутбук", 20000, 5, 100000)]
)
def test_calculate_total_price(name, price, quantity, result):
    item = Item(name, price, quantity)
    assert item.calculate_total_price() == result


@pytest.mark.parametrize(
    "name, price, quantity, result",
    [("Смартфон", 10000, 20, 8000.0), ("Ноутбук", 20000, 5, 16000.0)]
)
def test_apply_discount(name, price, quantity, result):
    Item.pay_rate = 0.8
    item = Item(name, price, quantity)
    assert item.price == price
    assert item.apply_discount() == result


def test_name():
    name1 = Item("Суперсмартфон", 20000, 2)
    assert name1.name == "Суперсмартфон"


def test_is_integer():
    assert Item.is_integer(5) is True
    assert Item.is_integer(5.0) is True
    assert Item.is_integer(5.5) is False


def test_name_setter():
    name1 = Item("Суперсмартфон", 20000, 2)
    with pytest.raises(Exception):
        name1.name = "Суперсмартфон"


def test_instantiate_from_csv():
    Item.instantiate_from_csv("test.csv")
    item = Item.all[2]
    assert item.name == "Кабель"
    assert item.price == 10
    assert item.quantity == 5