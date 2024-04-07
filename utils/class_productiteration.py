class ProductIteration:
    """
    Класс для реализации возможности использовать цикл for для прохода по
    всем товарам данной категории.
    """
    category: dict  # категория товара со списком товаров

    def __init__(self, category):
        self.category = category

    def __iter__(self):
        """
        Метод итераций, для начала отсчета цикла.
        :return: Длина списка продуктов внутри категории.
        """
        self.iter_index = len(self.category)
        return self

    def __next__(self):
        """
        Запускает цикл, пока не выполнится условие.
        :return: Экземпляр класса "продукт" из списка "продуктов".
        """

        if self.iter_index == 0:
            raise StopIteration
        self.iter_index -= 1
        return self.category['products'][self.iter_index]

