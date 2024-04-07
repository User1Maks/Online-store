class Product:
    """
    Класс продуктов. Имеет два класса наследника: Smartphone и LawnGrass.
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
    def price(self) -> float:
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
            self.__price = self.__price

    @price.deleter
    def price(self) -> None:
        """
        Удаляем цену продукта.
        :return: None
        """
        del self.__price

    def __add__(self, other) -> float:
        """ Метод для определения полной стоимости товаров на складе """
        if isinstance(other, self.__class__):
            return self.__price * self.quantity + other.__price * self.quantity

        raise TypeError(type)

    def __str__(self) -> str:
        """
        Метод для возвращения строки в заданном формате.
        Пример: "Название продукта, 80 руб. Остаток: 15 шт."
        return: str
        """
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity}'

    def __repr__(self):
        return (f'{self.__class__.__name__}:\n'
                f'-Название продута: {self.name}.\n'
                f'-Описание продукта: {self.description}.\n'
                f'-Цена продукта: {self.price}.\n'
                f'-Количество продуктов в наличии: {self.quantity}.\n')


class Smartphone(Product):
    """ Класс 'смартфоны', дочерний от класса продуктов """

    performance: str  # производительность
    model: str  # модель смартфона
    memory: str  # объем встроенной памяти
    color: str  # цвет

    def __init__(self, name, description, price,
                 quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        """ Метод для отладки категории Smartphone"""

        return (f'{self.__class__.__name__}: {self.performance},'
                f'{self.model}, {self.memory}, {self.color}')


class LawnGrass(Product):
    """ Класс 'трава газонная', дочерний от класса продуктов """

    manufacturer_country: str  # страна изготовитель
    germination_period: str  # срок прорастания
    color: str  # цвет

    def __init__(self, name, description, price, quantity,
                 manufacturer_country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        """ Метод для отладки категории LawnGrass"""
        return (f'{self.__class__.__name__}: {self.manufacturer_country},'
                f'{self.germination_period}, {self.color}')
