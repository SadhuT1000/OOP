import pytest

from src.products import Product
from src.category import Category

@pytest.fixture
def first_product():
    return Product(name="Samsung",
                    description="256GB, Серый цвет, 200MP камера",
                   price=180000.0,
                   quantity=5)



@pytest.fixture
def second_product():
    return Product(name="Iphone 15",
                    description="512GB, Gray space",
                   price=210000.0,
                   quantity=8)

@pytest.fixture
def third_product():
    return Product(name="55\ QLED 4K",
                    description="Фоновая подсветка",
                   price=123000.0,
                   quantity=7)

@pytest.fixture
def first_category(first_product,second_product,third_product):
    return Category(name="Смартфоны",
                    description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                    products=[first_product,second_product,third_product])



@pytest.fixture
def second_category(first_product, second_product):
    return Category(name = "Телевизоры",
                    description = "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                    products = [first_product])

def test_category(first_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert first_category.products == [first_product,second_product]

def tests_products(first_product):
    assert first_product.name == "Samsung"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5
