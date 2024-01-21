class Catalogue:
    def __init__(self, name):
        self.name = name
        self.product = []

    def add_product(self, product):
        self.product.append(product)

    def get_by_letter(self, first_letter):
        return [product for product in self.product if product[0] == first_letter]

    def __repr__(self):
        result = f'Items in the {self.name} catalogue:'
        for product in sorted(self.product):
            result += '\n' + product

        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
