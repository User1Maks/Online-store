class Product:
    """
    Класс продуктов.
    """
    name: str
    description: str
    price: float
    quantity: int

    list_product = []  # список продукта с полным его описанием

    def __init__(self, name: str, description: str, price: float,
                 quantity: int):
        """
        :param name: название продукта.
        :param description: Описание продукта.
        :param price: Цена продукта.
        :param quantity: Количество продуктов в наличии.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.list_product.append(self)

    @classmethod
    def product_creation(cls, new_product: dict):
        """
        Метод, который создает товар и возвращает объект.
        Который можно добавлять в список товаров.
        :return: Новый товар.
        """

        name = new_product['name']
        description = new_product['description']
        price = new_product['price']
        quantity = new_product['quantity']
        for product in Product.list_product:
            if product.name == name and product.description == description:
                product.quantity += quantity
                if product.price < price:
                    product.price = price
                return product
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """
        Декоратор для возращения цены продукта.
        :return: Цена продукта.
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Сеттер для подтверждения корректности введенной цены и ее понижения
        при необходимости.
        :param new_price: Новая цена.
        """
        if new_price <= 0:
            print('Цена введена некорректно')

        if new_price < self.__price:
            user_input = input('Подтвердите цену:\n y - подтвердить'
                               '\n n - отменить').lower().strip()
            if user_input == 'y' or 'yes':
                self.__price = new_price
        else:
            self.__price = new_price

    @price.deleter
    def price(self):
        """
        Удаляем цену продукта.
        :return: None
        """
        del self.__price

    def __repr__(self):
        return (f'Название продута: {self.name}.\n'
                f'Описание продукта: {self.description}.'
                f'Цена продукта: {self.price}.\n'
                f'Количество продуктов в наличии: {self.quantity}.')
