from utils.class_product import Product
import pytest


@pytest.fixture()
def product():
    return Product('Samsung Galaxy C23 Ultra',
                   '512GB, Gray space',
                   210000.0,
                   8
                   )


def test_product_init(product):
    assert product.name == 'Samsung Galaxy C23 Ultra'
    assert product.description == '512GB, Gray space'
    assert product.price == 210000.0
    assert product.quantity_in_stock == 8
