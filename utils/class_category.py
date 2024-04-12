from utils.class_product import Product


class Category:
    """
    Класс категорий продуктов.
    """
    name: str
    description: str
    __products: list
    number_of_unique_products: int  # общее количество уникальных продуктов,
    # не учитывая количество в наличии

    number_of_unique_products = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        :param name: название товара.
        :param description: Описание товара.
        :param products: Список товаров.
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.number_of_unique_products += len(products)

    def add_products(self, new_product) -> None:
        """
        Метод для добавления товара в список товаров
        данной категории.
        :param new_product: Экземпляр класса Product.
        """
        if isinstance(new_product, Category):
            self.__products.append(new_product)

        raise TypeError('Ошибка!')

    @property
    def products(self) -> list:
        """
        Геттер для возврата списка описаний продуктов текущей категории.
        :return: Список с описанием продуктов.
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
        count_quantity = 0

        for product in self.__products:
            count_quantity += product.quantity
        return count_quantity

    def __str__(self) -> str:
        """
        Метод для возвращения строки в заданном формате.
        Пример: "Название категории, количество продуктов: 200 шт.."
        return: str
        """
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}:\n'
                f'-Название категории товаров: {self.name}.\n'
                f'-Описание категории товаров: {self.description}.\n'
                f'-Список товаров: {self.__products}.\n')


#  код для проверки функции __len__
if __name__ == '__main__':
    pt1 = Category('Смартфоны',
                   'Смартфоны, как средство не только коммуникации',
                   [Product("Samsung Galaxy C23 Ultra",
                            "256GB, Серый цвет, 200MP камера",
                            180000.0, 6),
                    Product("Xiaomi Redmi Note 11",
                            "1024GB, Синий",
                            31000.0,
                            14)
                    ])

    print(len(pt1))
