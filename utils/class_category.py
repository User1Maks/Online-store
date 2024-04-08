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

    def __init__(self, name: str, description: str, products: list):
        """
        :param name: название товара.
        :param description: Описание товара.
        :param products: Список товаров.
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.number_of_unique_products += len(products)

    def add_products(self, new_product):
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
        for products in self.__products:
            count_quantity += products.quantity
        return count_quantity

    def __str__(self) -> str:
        """
        Метод для возвращения строки в заданном формате.
        Пример: "Название категории, количество продуктов: 200 шт.."
        return: str
        """
        return f'{self.__class__.__name__},\
                количество продуктов: {len(self)} шт.'

    def __repr__(self):
        return (f'{self.__class__.__name__}:\n'
                f'-Название товара: {self.name}.\n'
                f'-Описание товара: {self.description}.\n'
                f'-Список товаров: {self.__products}.\n')
