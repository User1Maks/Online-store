from function import list_products
from class_product import Product
from class_category import Category


def main():
    list_json = list_products()
    category_list = []

    for category in list_json:
        products_list = []
        for products in category['products']:
            product_append = Product(products['name'],
                                     products['description'],
                                     products['price'],
                                     products['quantity']
                                     )
            products_list.append(product_append)

        product = Category(category['name'],
                           category['description'],
                           products_list

                           )

        category_list.append(product)

    print(f'Общее количество категорий: {Category.number_of_categories}\n'
          f'Общее количество уникальных продуктов: '
          f'{Category.number_of_unique_products}')
    print(category_list)


if __name__ == '__main__':
    main()
