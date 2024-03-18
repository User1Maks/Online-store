class Category:
    """
    Класс категорий продуктов.
    """
    name: str
    description: str
    products: list
    number_of_categories: int  # общее количество категорий
    number_of_unique_products: int  # общее количество уникальных продуктов, не учитывая количество в наличии

    number_of_categories = 0
    number_of_unique_products = 0

    def __init__(self, name: str, description: str, products: list):
        """
        :param name: название товара.
        :param description: Описание товара.
        :param products: Список товаров.
        """
        self.name = name
        self.description = description
        self.products = products

        Category.number_of_categories += 1
        Category.number_of_unique_products += len(products)

    def __repr__(self):
        return f'Название товара: {self.name}.\nОписание товара: {self.description}.\nСписок товаров: {self.products}.'
