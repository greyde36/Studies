class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        kyshat = open(self.__file_name, 'r')
        product = kyshat.read()
        kyshat.close()
        return product

    def add(self, *products):
        for product in products:
            if product.name not in self.get_products():
                ovosh = open(self.__file_name, 'a')
                ovosh.write(product.__str__() + '\n')
                ovosh.close()
            else:
                print(f'Продукт {product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())