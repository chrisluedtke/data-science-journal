import unittest
import random
from robot_sort import SortingRobot

class Test(unittest.TestCase):

    def setUp(self):
        self.small_list = [5, 4, 3, 2, 1]
        self.medium_list = [11, 13, 7, 17, 9, 20, 1, 21, 2, 4, 22, 16, 15, 10, 23, 19, 8, 3, 5, 14, 6, 0, 24, 12, 18]
        self.large_list = [20, 77, 45, 16, 15, 91, 12, 6, 24, 89, 53, 19, 85, 56, 13, 74, 48, 98, 9, 92, 25, 35, 54, 44, 50, 5, 75, 34, 2, 42, 87, 49, 76, 52, 43, 23, 7, 80, 66, 14, 46, 90, 88, 40, 97, 10, 57, 63, 1, 18, 67, 79, 96, 27, 73, 28, 32, 61, 30, 8, 17, 93, 26, 51, 60, 55, 62, 31, 47, 64, 39, 22, 99, 95, 83, 70, 38, 69, 36, 41, 37, 65, 84, 3, 29, 58, 0, 94, 4, 11, 33, 86, 21, 81, 72, 82, 59, 71, 68, 78]
        self.large_varied_list = [1, -38, -95, 4, 23, -73, -65, -36, 85, 2, 58, -26, -55, 96, 55, -76, 64, 45, 69, 36, 69, 47, 29, -47, 13, 89, -57, -88, -87, 54, 60, 56, -98, -78, 59, 93, -41, -74, 73, -35, -23, -79, -35, 46, -18, -18, 37, -64, 14, -57, -2, 15, -85, 45, -73, -2, 79, -87, -100, 21, -51, 22, 26, -59, 81, 59, -24, 24, -81, 43, 61, 52, 38, -88, -95, 87, -57, -37, -65, -47, -3, 21, -77, 98, 25, 1, -36, 39, 78, 47, -35, -40, -69, -81, 11, -47, 21, 25, -53, -31]
        self.random_list = [random.randint(0, 100) for i in range(0, 100)]

    def test_sorting_small_list(self):
        robot = SortingRobot(self.small_list)
        robot.sort()
        self.assertEqual(robot._list, sorted(self.small_list))

    def test_sorting_medium_list(self):
        robot = SortingRobot(self.medium_list)
        robot.sort()
        self.assertEqual(robot._list, sorted(self.medium_list))

    def test_sorting_large_list(self):
        robot = SortingRobot(self.large_list)
        robot.sort()
        self.assertEqual(robot._list, sorted(self.large_list))

    def test_sorting_large_varied_list(self):
        robot = SortingRobot(self.large_varied_list)
        robot.sort()
        self.assertEqual(robot._list, sorted(self.large_varied_list))

    def test_sorting_random_list(self):
        robot = SortingRobot(self.random_list)
        robot.sort()
        self.assertEqual(robot._list, sorted(self.random_list))

    def test_stretch_times(self):
        robot = SortingRobot(self.small_list)
        robot.sort()
        self.assertLess(robot._time, 110)

        robot = SortingRobot(self.medium_list)
        robot.sort()
        print(robot._time)
        self.assertLess(robot._time, 1948)

        robot = SortingRobot(self.large_list)
        robot.sort()
        print(robot._time)
        self.assertLess(robot._time, 27513)

        robot = SortingRobot(self.large_varied_list)
        robot.sort()
        print(robot._time)
        self.assertLess(robot._time, 28308)


if __name__ == '__main__':
    unittest.main()
