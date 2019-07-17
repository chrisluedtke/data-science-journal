import unittest
import random
from recursive_sorting import *

class RecursiveSortingTests(unittest.TestCase):
    def test_merge_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        arr2 = []
        arr3 = [2]
        arr4 = [0, 1, 2, 3, 4, 5]
        arr5 = random.sample(range(200), 50)

        self.assertEqual(merge_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
        self.assertEqual(merge_sort(arr2), [])
        self.assertEqual(merge_sort(arr3), [2])
        self.assertEqual(merge_sort(arr4), [0,1,2,3,4,5])
        self.assertEqual(merge_sort(arr5), sorted(arr5))

    # Uncomment this test to test your in-place merge sort implementation
    # def test_in_place_merge_sort(self):
    #     arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    #     arr2 = []
    #     arr3 = [2]
    #     arr4 = [0, 1, 2, 3, 4, 5]
    #     arr5 = random.sample(range(200), 50)

    #     self.assertEqual(merge_sort_in_place(arr1, 0, len(arr1)-1), [0,1,2,3,4,5,6,7,8,9])
    #     self.assertEqual(merge_sort_in_place(arr2, 0, len(arr2)-1), [])
    #     self.assertEqual(merge_sort_in_place(arr3, 0, len(arr3)-1), [2])
    #     self.assertEqual(merge_sort_in_place(arr4, 0, len(arr4)-1), [0,1,2,3,4,5])
    #     self.assertEqual(merge_sort_in_place(arr5, 0, len(arr5)-1), sorted(arr5))


if __name__ == '__main__':
    unittest.main()