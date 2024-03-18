class Product:
    """
    Класс продуктов.
    """
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name: str, description: str, price: float, quantity_in_stock: int):
        """
        :param name: название продукта.
        :param description: описание продукта.
        :param price: цена продукта.
        :param quantity_in_stock: количество продуктов в наличии.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def __repr__(self):
        return f'Название продута: {self.name}.\nОписание продукта: {self.description}.'\
                f'Цена продукта: {self.price}.\nКоличество продуктов в наличии: {self.quantity_in_stock}.'

