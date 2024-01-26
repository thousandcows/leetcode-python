from utils.time_measurement import time_measurement


class FibonacciNumber:
    @staticmethod
    @time_measurement
    def solution(n: int) -> int:
        if n <= 1:
            return n

        return FibonacciNumber.solution(n - 1) + FibonacciNumber.solution(n - 2)
