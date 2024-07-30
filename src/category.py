from typing import Any

from src.products import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт.\n"

    def add_product(self, product: Product) -> Any:
        self.__products.append(product)
        Category.product_count += 1


    @property
    def get_product_list(self) -> str:
        product_list = ""
        for i in self.__products:
            product_list += f"{str(i)}.\n"
        return product_list


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    #print(category1.products) # Если тут пишу get_product_list то работает норм

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

