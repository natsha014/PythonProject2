def test_print_mixin(capsys, product_test):
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"


def test_print_mixin_grass(capsys, product_lawn_grass_1):
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"


def test_print_mixin_smartphone(capsys, product_smartphone_1):
    message = capsys.readouterr()
    assert message.out.strip() == (
        "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, " "180000.0, 5)"
    )
