from src.product import Product


def test_product(product_test):
    assert product_test.name == "Iphone 15"
    assert product_test.description == "512GB, Gray space"
    assert product_test.price == 210000.0
    assert product_test.quantity == 8


def test_product_new_product():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 181000.0, 6)
    product.name = "Samsung Galaxy S23 Ultra"
    product.description = "256GB, Серый цвет, 200MP камера"
    product.price = 181000.0
    product.quantity = 6


def test_product_price_setter(capsys, product_test):
    value = 0
    product_test.price = value
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    value = 220000.0
    product_test.price = value
    assert product_test.price == 220000.0
