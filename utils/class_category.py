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

    list_name = []  # атрибут на уровне класса, содержащий список категорий

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
        Category.list_name.append(self.name)  # при инициализации нового
        # товара добавляем его в список list_name

    def app_products(self, product):
        """
        Метод для добавления товаров в список.
        """
        for new_product in product:
            self.__products.append(new_product)

    @property
    def products(self) -> list:
        """
        Преобразуем список товаров в необходимый формат.
        Пример: "Продукт, 80 руб. Остаток: 15 шт."
        """

        list_pr = []
        for x in self.__products:
            list_pr.append(str(x))
        return list_pr

    def __len__(self) -> int:
        """
        Метод для подсчета количества товара на складе.
        :return: Количество продуктов.
        """
        list_products = Product.list_product  # список продуктов
        # с полным их описанием
        count_quantity = 0
        for products in list_products:
            for quantity in products:
                count_quantity += quantity['quantity']
        return count_quantity

    def __str__(self) -> str:
        """
        Метод для возвращения строки в заданном формате.
        Пример: "Название категории, количество продуктов: 200 шт.."
        return: str
        """
        return f'{self.__class__.__name__},\
                количество продуктов: {Category.__len__} шт.'

    def __repr__(self):
        return (f'{self.__class__.__name__}:\n'
                f'-Название товара: {self.name}.\n'
                f'-Описание товара: {self.description}.\n'
                f'-Список товаров: {self.__products}.\n')
