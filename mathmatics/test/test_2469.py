import unittest

from mathmatics.n_2469_convert_the_temperature import ConvertTheTemperature


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        celsius = 36.50
        expected = [309.65000, 97.70000]
        self.assertEqual(
            expected, ConvertTheTemperature.solution(celsius)
        )  # add assertion here

    def test_case_two(self):
        celsius = 122.11
        expected = [395.26000, 251.79800]
        self.assertEqual(expected, ConvertTheTemperature.solution(celsius))


if __name__ == "__main__":
    unittest.main()
