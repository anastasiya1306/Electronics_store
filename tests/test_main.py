import pytest
from main.main import Item, Phone, KeyBoard, MixinLog


@pytest.fixture
def phone():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    return phone


@pytest.fixture
def keyboard():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    return kb


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


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.__str__() == "Смартфон"


def test_number_of_sim(phone):
    assert phone.number_of_sim == 2


def test_number_of_sim_setter(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
    assert phone.number_of_sim == 2


def test_add(phone):
    item1 = Item("Смартфон", 10000, 20)
    with pytest.raises(ValueError):
        phone + 1000
    assert phone + item1 == 25


def test_repr(phone):
    assert phone.__repr__() == 'Phone(iPhone 14, 120000, 5, 2)'


def test_keyboard(keyboard):
    assert keyboard.name == 'Dark Project KD87A'
    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert keyboard.language == 'RU'