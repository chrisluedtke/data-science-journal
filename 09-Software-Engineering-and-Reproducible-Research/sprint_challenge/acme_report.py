from typing import List
from random import choice, triangular
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
NAMES = [x + ' ' + y for x in ADJECTIVES for y in NOUNS]


def generate_products(n=30) -> List[Product]:
    products = []
    for x in range(n):
        p = Product(
            name = choice(NAMES),
            price = int(triangular(5, 100, 10)),
            weight = int(triangular(5, 100, 20)),
            flammability = triangular(0, 2.5, 0.5),
        )
        products.append(p)

    return products


def inventory_report(products:List[Product]):
    names = [x.name for x in products]
    prices = [x.price for x in products]
    weights = [x.weight for x in products]
    flammabilities = [x.flammability for x in products]

    def avg(ls:List):
        return sum(ls) / len(ls)

    s = (f"Unique product names: {len(set(names))}\n"
         f"Average price: {avg(prices)}\n"
         f"Average weight: {avg(weights)}\n"
         f"Average flammability: {avg(flammabilities)}")

    print(s)
    return s


if __name__ == '__main__':
    inventory_report(generate_products())
