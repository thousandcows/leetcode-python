from utils.time_measurement import time_measurement


class MultiplyStrings:
    @staticmethod
    @time_measurement
    def solution(num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
