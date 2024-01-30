from utils.time_measurement import time_measurement


class PowerOfThree:
    @staticmethod
    @time_measurement
    def solution(n: int) -> bool:
        if n <= 0:
            return False
        return 1162261467 % n == 0
