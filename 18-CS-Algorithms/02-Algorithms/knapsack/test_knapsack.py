import sys
import unittest
from collections import namedtuple
from knapsack import knapsack_solver

Item = namedtuple('Item', ['index', 'size', 'value'])

class Test(unittest.TestCase):
  def setUp_small(self):
    file_contents = open('data/small1.txt', 'r')
    self.small_1_items = []
    
    for line in file_contents.readlines():
      data = line.rstrip().split()
      self.small_1_items.append(Item(int(data[0]), int(data[1]), int(data[2])))

    file_contents.close()

    file_contents = open('data/small2.txt', 'r')
    self.small_2_items = []
    
    for line in file_contents.readlines():
      data = line.rstrip().split()
      self.small_2_items.append(Item(int(data[0]), int(data[1]), int(data[2])))

    file_contents.close()

    file_contents = open('data/small3.txt', 'r')
    self.small_3_items = []
    
    for line in file_contents.readlines():
      data = line.rstrip().split()
      self.small_3_items.append(Item(int(data[0]), int(data[1]), int(data[2])))

    file_contents.close()

  def cleanUp_small(self):
    del self.small_1_items
    del self.small_2_items
    del self.small_3_items

  def setUp_medium(self):
    file_contents = open('data/medium1.txt', 'r')
    self.medium_1_items = []
    
    for line in file_contents.readlines():
      data = line.rstrip().split()
      self.medium_1_items.append(Item(int(data[0]), int(data[1]), int(data[2])))

    file_contents.close()

    file_contents = open('data/medium2.txt', 'r')
    self.medium_2_items = []
    
    for line in file_contents.readlines():
      data = line.rstrip().split()
      self.medium_2_items.append(Item(int(data[0]), int(data[1]), int(data[2])))

    file_contents.close()

    file_contents = open('data/medium3.txt', 'r')
    self.medium_3_items = []
    
    for line in file_contents.readlines():
      data = line.rstrip().split()
      self.medium_3_items.append(Item(int(data[0]), int(data[1]), int(data[2])))

    file_contents.close()

  def cleanUp_medium(self):
    del self.medium_1_items
    del self.medium_2_items
    del self.medium_3_items

  def setUp_large(self):
    file_contents = open('data/large1.txt', 'r')
    self.large_1_items = []
    
    for line in file_contents.readlines():
      data = line.rstrip().split()
      self.large_1_items.append(Item(int(data[0]), int(data[1]), int(data[2])))

    file_contents.close()

  def cleanUp_large(self):
    del self.large_1_items

  def test_with_small_input(self):
    self.setUp_small()
    self.assertEqual(knapsack_solver(self.small_1_items, 100), {'Value': 197, 'Chosen': [1, 7, 8]})
    self.assertEqual(knapsack_solver(self.small_2_items, 100), {'Value': 259, 'Chosen': [1, 9, 10]})
    self.assertEqual(knapsack_solver(self.small_3_items, 100), {'Value': 129, 'Chosen': [4, 5, 7, 9]})
    self.cleanUp_small()

  def test_with_medium_input(self):
    self.setUp_medium()
    self.assertEqual(knapsack_solver(self.medium_1_items, 100), {'Value': 1042, 'Chosen': [44, 49, 60, 77, 80, 83, 94, 104, 107, 117, 127, 134, 157, 160, 170]})
    self.assertEqual(knapsack_solver(self.medium_2_items, 100), {'Value': 969, 'Chosen': [1, 10, 27, 28, 66, 120, 139, 145, 153, 155, 174, 188, 191]})
    self.assertEqual(knapsack_solver(self.medium_3_items, 100), {'Value': 868, 'Chosen': [9, 14, 15, 47, 68, 108, 116, 120, 133, 154, 158, 161, 164, 170, 181, 198]}) 
    self.cleanUp_medium()

  def test_with_large_input(self):
    self.setUp_large()
    self.assertEqual(knapsack_solver(self.large_1_items, 100), {'Value': 2640, 'Chosen': [44, 83, 104, 107, 134, 160, 239, 271, 295, 297, 308, 335, 337, 370, 373, 420, 432, 561, 566, 623, 648, 671, 693, 704, 737, 782, 795, 796, 814, 844, 866, 907, 909, 913, 935, 949, 987, 997]})
    self.cleanUp_large()


if __name__ == '__main__':
  unittest.main()