from utils.class_product import Product


class Category:
    """
    Класс категорий продуктов.
    """
    name: str
    description: str
    __products: list
    number_of_categories: int  # общее количество категорий
    number_of_unique_products: int  # общее количество уникальных продуктов,
    # не учитывая количество в наличии

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
        self.__products = products

        Category.number_of_categories += 1
        Category.number_of_unique_products += len(products)

    def app_products(self, product):
        """
        Метод для добавления товаров в список.
        """
        for x in product:
            self.__products.append(x)

    @property
    def products(self):
        """
        Преобразуем список товаров в необходимый формат.
        """
        list_product = Product
        return (f'{list_product.name}, {list_product.price} руб. '
                f'Остаток: {list_product.quantity} шт.')


def __repr__(self):
    return (f'Название товара: {self.name}.\n'
            f'Описание товара: {self.description}.\n'
            f'Список товаров: {self.__products}.')
