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
def dict_product():
    return [{'name': 'Samsung Galaxy C23 Ultra',
             'description': '512GB, Gray space',
             'price': 210000.0,
             'quantity': 8
             },
            {'name': 'Samsung Galaxy C30 Ultra',
             'description': '812GB, Red',
             'price': 280000.0,
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


def test_product_creation(dict_product):
    """Тест создания товара и проверка условий разницы цен, наличии такого
    же товара на складе. Проверка описания товара"""
    dict_1 = Product.product_creation(dict_product[0])
    assert dict_1.name == 'Samsung Galaxy C23 Ultra'
    assert dict_1.description == '512GB, Gray space'
    assert dict_1.price == 210000.0
    assert dict_1.quantity == 8

    dict_2 = Product.product_creation(dict_product[1])
    assert dict_2.name == 'Samsung Galaxy C30 Ultra'
    assert dict_2.description == '812GB, Red'
    assert dict_2.price == 280000.0
    assert dict_2.quantity == 10

    dict_3 = Product.product_creation(dict_product[2])
    assert dict_3.name == 'Samsung Galaxy C30 Ultra'
    assert dict_3.description == '812GB, Red'
    assert dict_3.price == 280000.0
    assert dict_3.quantity == 20

    dict_4 = Product.product_creation(dict_product[3])
    assert dict_4.name == 'Samsung Galaxy C23 Ultra'
    assert dict_4.description == '512GB, Gray space'
    assert dict_4.price == 210000.0
    assert dict_4.quantity == 16

