import json
from class_category import Category


def list_products():
    """

    :return: словарь продукции, ее описание и количество.
    """
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)







# def class_objects():
#     """
#     Функция для создания объектов классов.
#     :return: объекты классов.
#     """

    # name_category = []
    # description_category = []
    # goods_category = []
    #
    # for x in list_products():
    #     for y in x["products"]:
    #         goods_category.append(y["name"])

    # for dictionary in list_products():
    #     name_category.append(dictionary["name"])
    #     description_category.append(dictionary["description"])

    # number_categories = len(name_category)
    # number_of_unique_products = len(set(goods_category))
    #
    # product = Category(name_category, description_category,
    #                    goods_category, number_categories, number_of_unique_products)
    #
    # print(name_category)
    # print(description_category)
    # print(goods_category)
    # print(number_categories)
    # print(number_of_unique_products)
    # print(product)


# print(class_objects())
