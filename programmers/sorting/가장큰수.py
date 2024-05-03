from utils.time_measurement import time_measurement


class MaxNumber:
    @staticmethod
    @time_measurement
    def solution(numbers: list[int]) -> str:
        numbers = list(map(str, numbers))
        numbers.sort(key=lambda x: x * 3, reverse=True)
        return str(int("".join(numbers)))
