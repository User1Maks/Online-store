from utils.class_product import Product
import pytest


@pytest.fixture()
def product():
    return Product('Samsung Galaxy C27 Ultra',
                   '512GB, Gray space',
                   210000.0,
                   8
                   )


def test_product_init(product):
    """Тест инициализации класса Product"""
    assert product.name == 'Samsung Galaxy C27 Ultra'
    assert product.description == '512GB, Gray space'
    assert product.price == 210000.0
    assert product.quantity == 8


def test_price():
    """Тест возращения цены продукта."""
    assert Product.price == Product.price


@pytest.fixture()
def list_product():
    return [{'name': 'Samsung Galaxy C23 Ultra',
             'description': '512GB, Gray space',
             'price': 210000.0,
             'quantity': 8
             },
            {'name': 'Samsung Galaxy C30 Ultra',
             'description': '812GB, Red',
             'price': 380000.0,
             'quantity': 10
             },
            {'name': 'Samsung Galaxy C30 Ultra',
             'description': '812GB, Red',
             'price': 280000.0,
             'quantity': 10
             },
            {'name': 'Samsung Galaxy C23 Ultra',
             'description': '512GB, Gray space',
             'price': 180000.0,
             'quantity': 8
             }
            ]


def test_product_creation(list_product):
    """Тест создания товара и проверка условий разницы цен, наличии такого
    же товара на складе. Проверка описания товара"""
    list_1 = Product.product_creation(list_product[0])
    assert list_1.name == 'Samsung Galaxy C23 Ultra'
    assert list_1.description == '512GB, Gray space'
    assert list_1.price == 210000.0
    assert list_1.quantity == 8

    list_2 = Product.product_creation(list_product[1])
    assert list_2.name == 'Samsung Galaxy C30 Ultra'
    assert list_2.description == '812GB, Red'
    assert list_2.price == 380000.0
    assert list_2.quantity == 10

    dict_3 = Product.product_creation(list_product[2])
    assert dict_3.name == 'Samsung Galaxy C30 Ultra'
    assert dict_3.description == '812GB, Red'
    assert dict_3.price == 380000.0
    assert dict_3.quantity == 20

    list_4 = Product.product_creation(list_product[3])
    assert list_4.name == 'Samsung Galaxy C23 Ultra'
    assert list_4.description == '512GB, Gray space'
    assert list_4.price == 210000.0
    assert list_4.quantity == 16

