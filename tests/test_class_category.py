from utils.class_category import Category
import pytest


@pytest.fixture()
def category():
    return Category('Смартфоны',
                    'Смартфоны, как средство не только коммуникации,'
                    'но и получение дополнительных функций для '
                    'удобства жизни',
                    ['Samsung Galaxy C23 Ultra', 'Iphone 15']
                    )


def test_init(category):
    """Тест для проверки инициализации класса Category"""
    assert category.name == 'Смартфоны'
    assert category.description == (
        'Смартфоны, как средство не только коммуникации,'
        'но и получение дополнительных '
        'функций для удобства жизни')


@pytest.fixture()
def list_products():
    product1 = Category('Смартфоны',
                        'Смартфоны, как средство не только коммуникации,'
                        'но и получение дополнительных функций для '
                        'удобства жизни',
                        ['Samsung Galaxy C23 Ultra', 'Iphone 15']
                        )
    product2 = Category('Телевизоры',
                        'Современный телевизор, который позволяет '
                        'наслаждаться просмотром, станет вашим другом '
                        'и помощником',
                        ['55" QLED 4K']
                        )

    list_name = [product1.name, product2.name]
    return list_name


def test_len(list_products):
    """Тест для проверки подсчета количества товара на складе"""
    assert len(list_products) == 2
