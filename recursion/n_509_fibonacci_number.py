from utils.time_measurement import time_measurement


class FibonacciNumber:
    @staticmethod
    @time_measurement
    def solution(n: int) -> int:
        memoization = [0, 1]
        if n <= 1:
            return memoization[n]

        for i in range(2, n + 1):
            memoization.append(memoization[i - 1] + memoization[i - 2])

        return memoization[n]
