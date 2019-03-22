import unittest
from acme import Product
from acme_report import generate_products, NAMES


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability_explode(self):
        """Test stealability and explode methods."""
        prod = Product('Test Product', price=10, weight=10, flammability=10)
        self.assertEqual(prod.stealability(), "Very stealable!")
        self.assertEqual(prod.explode(), "...BABOOM!!")

class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports are the tops!"""
    def test_product_len(self):
        """Test generated products list being 30 elements."""
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """Test all names are legal."""
        products = generate_products()
        names = [x.name for x in products]
        self.assertEqual(set(names) - set(NAMES), set())


if __name__ == '__main__':
    unittest.main()
