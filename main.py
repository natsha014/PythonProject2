from src.product import Product
from src.category import Category
from src.utils import read_json, create_objects
from config import PATH_TO_PRODUCTS
from src.product_iterator import ProductIterator

if __name__ == "__main__":  # pragma: no cover
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    # print(product1.name)
    # print(product1.description)
    # print(product1.price)
    # print(product1.quantity)
    #
    # print(product2.name)
    # print(product2.description)
    # print(product2.price)
    # print(product2.quantity)
    #
    # print(product3.name)
    # print(product3.description)
    # print(product3.price)
    # print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    # product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    # category1.add_product(product4)
    # print(category1.products)
    # print(category1.product_count)
    #
    # new_product = Product.new_product(
    #     "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 181000.0,
    #     6, [product1, product2, product3])
    # print(new_product.name)
    # print(new_product.description)
    # print(new_product.price)
    # print(new_product.quantity)
    #
    # new_product.price = 800
    # print(new_product.price)
    #
    # new_product.price = -100
    # print(new_product.price)
    # new_product.price = 0
    # print(new_product.price)

    # print(category1.name == "Смартфоны")
    # print(category1.description)
    # print(len(category1.products))
    # print(category1.category_count)
    # print(category1.product_count)
    #
    # product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    # category2 = Category("Телевизоры",
    #                      "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    #                      [product4])
    #
    # print(category2.name)
    # print(category2.description)
    # print(len(category2.products))
    # print(category2.products)
    #
    # print(Category.category_count)
    # print(Category.product_count)
    #
    # products_j = read_json(PATH_TO_PRODUCTS)
    #
    # all_categories = create_objects(products_j)
    #
    # print(all_categories)
    # print(all_categories[0].name)
    # print(all_categories[0].description)
    # print(all_categories[0].products)
    # print(len(all_categories[0].products))
    # print(all_categories[1].name)
    # print(all_categories[1].description)
    # print(all_categories[1].products)
    # print(len(all_categories[1].products))

    iterator = ProductIterator(category1)
    for product in iterator:
        print(product)
