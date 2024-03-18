from project_90_100.product import Product


class Drink(Product):
    DEFAULT_QUANTITY = 10

    def __init__(self, name):
        super().__init__(name, self.DEFAULT_QUANTITY)