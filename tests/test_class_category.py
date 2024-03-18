from utils.class_category import Category
import pytest


@pytest.fixture()
def category():
    return Category('Смартфоны',
                    'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для '
                    'удобства жизни',
                    ['Смартфоны', 'Телевизоры']
                    )


def test_init(category):
    assert category.name == 'Смартфоны'
    assert category.description == ('Смартфоны, как средство не только коммуникации, но и получение дополнительных '
                                    'функций для удобства жизни')
    assert category.products == ['Смартфоны', 'Телевизоры']

