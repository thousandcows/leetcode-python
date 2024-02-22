import unittest

from two_pointers.n_11_container_with_most_water import ContainerWithMostWater


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        self.assertEqual(expected, ContainerWithMostWater.solution(height))  # add assertion here

    def test_case_two(self):
        height = [1, 1]
        expected = 1
        self.assertEqual(expected, ContainerWithMostWater.solution(height))

    def test_case_three(self):
        height = [4, 3, 2, 1, 4]
        expected = 16
        self.assertEqual(expected, ContainerWithMostWater.solution(height))

if __name__ == '__main__':
    unittest.main()
