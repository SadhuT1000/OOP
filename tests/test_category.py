import pytest


def test_category(first_category, first_product, third_product, second_product, second_category, third_category):

    assert first_category.name == "Смартфоны"

    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    assert (
        first_category.get_product_list == "Samsung, 180000.0 руб. Остаток: 5 шт..\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт..\n"
        "55 QLED 4K, 123000.0 руб. Остаток: 7 шт..\n"
    )

    assert first_category.product_count == 5

    assert second_category.product_count == 5

    assert first_category.category_count == 3

    assert second_category.category_count == 3

    assert first_category.product_count == 5

    assert second_category.product_count == 5


def test_get_product_list(first_category, second_category):
    with pytest.raises(AttributeError):
        print(first_category.__products)
    assert (
        first_category.get_product_list == "Samsung, 180000.0 руб. Остаток: 5 шт..\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт..\n"
        "55 QLED 4K, 123000.0 руб. Остаток: 7 шт..\n"
    )
