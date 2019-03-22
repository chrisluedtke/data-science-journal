from random import randint

class Product(object):
    def __init__(self, name, price = 10, weight = 20, flammability = 0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(10e5, 10e6-1)

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        explosiveness = self.flammability * self.weight
        if explosiveness < 10:
            return  "...fizzle."
        elif explosiveness < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(self, name, price = 10, weight = 10, flammability = 0.5):
        super().__init__(name, price, weight, flammability)
