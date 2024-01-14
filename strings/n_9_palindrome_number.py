from utils.time_measurement import time_measurement


class PalindromeNumber:
    @staticmethod
    @time_measurement
    def solution(x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]
