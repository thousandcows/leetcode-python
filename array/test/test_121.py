import unittest

from array.n_121_best_time_to_buy_and_sell_stock import BestTimeToBuyAndSellStock


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        prices = [7, 1, 5, 3, 6, 4]
        max_profit = 5
        self.assertEqual(
            max_profit, BestTimeToBuyAndSellStock.execute(prices)
        )  # add assertion here

    def test_case_two(self):
        prices = [7, 6, 4, 3, 1]
        max_profit = 0
        self.assertEqual(max_profit, BestTimeToBuyAndSellStock.execute(prices))

    def test_case_three(self):
        prices = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        max_profit = 88
        self.assertEqual(max_profit, BestTimeToBuyAndSellStock.execute(prices))

    def test_case_four(self):
        prices = [1]
        max_profit = 0
        self.assertEqual(max_profit, BestTimeToBuyAndSellStock.execute(prices))


if __name__ == "__main__":
    unittest.main()
