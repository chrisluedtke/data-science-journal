import unittest
from recipe_batches import recipe_batches

class Test(unittest.TestCase):

  def test_recipe_batches(self):
    self.assertEqual(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }), 0)
    self.assertEqual(recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 }), 1)
    self.assertEqual(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }), 2)
    self.assertEqual(recipe_batches({ 'milk': 2 }, { 'milk': 200}), 100)


if __name__ == '__main__':
  unittest.main()