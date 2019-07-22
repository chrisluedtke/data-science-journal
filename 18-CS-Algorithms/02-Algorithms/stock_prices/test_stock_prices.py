import unittest
from stock_prices import find_max_profit 

class Test(unittest.TestCase):

  def test_find_max_profit(self):
    self.assertEqual(find_max_profit([10, 7, 5, 8, 11, 9]), 6)
    self.assertEqual(find_max_profit([100, 90, 80, 50, 20, 10]), -10)
    self.assertEqual(find_max_profit([1050, 270, 1540, 3800, 2]), 3530)
    self.assertEqual(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]), 94)
  

if __name__ == '__main__':
  unittest.main()