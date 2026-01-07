from src.order import Order


def test_order_init(product_test):
    quantity = 2
    order = Order(product_test, quantity)

    assert order.product.name == "Iphone 15"
    assert order.quantity == 2
    assert order.total_cost == 420000


def test_order_str(product_test):
    order = Order(product_test, 2)
    assert str(order) == "Заказ: Iphone 15, 2 шт. Итого: 420000.0 руб."
