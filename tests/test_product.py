import pytest

from src.product import Product


@pytest.fixture
def product_test():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_product(product_test):
    assert product_test.name == "Iphone 15"
    assert product_test.description == "512GB, Gray space"
    assert product_test.price == 210000.0
    assert product_test.quantity == 8
