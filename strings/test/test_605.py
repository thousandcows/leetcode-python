import unittest

from strings.n_605_can_place_flowers import CanPlaceFlowers


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 1
        expected = True
        self.assertEqual(
            expected, CanPlaceFlowers.solution(flowerbed, n)
        )  # add assertion here

    def test_case_two(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 2
        expected = False
        self.assertEqual(expected, CanPlaceFlowers.solution(flowerbed, n))

    def test_case_three(self):
        flowerbed = [0] * 20
        n = 10
        expected = True
        self.assertEqual(expected, CanPlaceFlowers.solution(flowerbed, n))

    def test_case_four(self):
        flowerbed = [0] * 3
        n = 2
        expected = True
        self.assertEqual(expected, CanPlaceFlowers.solution(flowerbed, n))

    def test_case_five(self):
        flowerbed = [1]
        n = 1
        expected = False
        self.assertEqual(expected, CanPlaceFlowers.solution(flowerbed, n))


if __name__ == "__main__":
    unittest.main()
