import json
from class_category import Category


def list_products():
    """

    :return: словарь продукции, ее описание и количество.
    """
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)

