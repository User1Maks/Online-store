from utils.function import list_products
from utils.class_product import Product
from utils.class_category import Category


def main():
    list_json = list_products()  # список продукта с полным его описанием
    category_list = []

    for category in list_json:
        products_list = []
        for product in category['products']:
            product_append = Product(product['name'],
                                     product['description'],
                                     product['price'],
                                     product['quantity']
                                     )
            products_list.append(product_append)

        new_category = Category(category['name'],
                                category['description'],
                                products_list
                                )

        category_list.append(new_category)

    print(f'Общее количество категорий: {len(category_list)}\n'
          f'Общее количество уникальных продуктов: '
          f'{Category.number_of_unique_products}')
    print(category_list)


if __name__ == '__main__':
    main()
