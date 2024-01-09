import sys

from utils.time_measurement import time_measurement


class BestTimeToBuyAndSellStock:
    @staticmethod
    @time_measurement
    def execute(prices: list[int]) -> int:
        # set variables
        total = 0
        curr_min = sys.maxsize

        # iterate all indexes
        for price in prices:
            curr_min = min(curr_min, price)
            total = max(total, price - curr_min)

        return total
