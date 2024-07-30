import pytest

from src.category import Category
from src.products import Product
from src.tast_iterator import TaskIterator


@pytest.fixture
def first_product():
    return Product(
        name="Samsung",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def third_product():
    return Product(name="55 QLED 4K", description="Фоновая подсветка", price=123000.0, quantity=7)


@pytest.fixture
def fourth_product():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )


@pytest.fixture
def first_category(first_product, second_product, third_product):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[first_product, second_product, third_product],
    )
    #     Product(
    #         name="Samsung",
    #         description="256GB, Серый цвет, 200MP камера",
    #         price=180000.0,
    #         quantity=5,
    #     ),
    #     Product(
    #         name="Iphone 15",
    #         description="512GB, Gray space",
    #         price=210000.0,
    #         quantity=8,
    #     ),
    #     Product(name="55 QLED 4K",
    #             description="Фоновая подсветка",
    #             price=123000.0,
    #             quantity=7)
    # ],


@pytest.fixture
def second_category(first_product, second_product):
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[third_product],
    )


@pytest.fixture
def third_category(fourth_product):
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[fourth_product],
    )


@pytest.fixture
def all_sum1(first_product, second_product):
    return 2580000.0

@pytest.fixture
def all_sum2(first_product, third_product):
    return 1334000.0


@pytest.fixture
def taskiterator(first_category):
    return TaskIterator(first_category)