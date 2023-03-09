import pytest
from main.main import Item

def test_calculate_total_price():
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == 200000


def test_apply_discount():
    Item.pay_rate = 0.8
    item1 = Item("Смартфон", 10000, 20)
    assert item1.price == 10000
    assert item1.apply_discount() == 8000.0

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
    Item.instantiate_from_csv("./tests/test.csv")
    item = Item.all[-1]
    assert item.name == "Клавиатура"
    assert item.price == 75
    assert item.quantity == 5