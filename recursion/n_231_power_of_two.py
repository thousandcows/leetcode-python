from utils.time_measurement import time_measurement


class PowerOfTwo:
    @staticmethod
    @time_measurement
    def solution(n: int) -> bool:
        def is_power(num: int):
            if num == 1:
                return True

            if num % 2 != 0 or n == 0:
                return False

            return is_power(num // 2)

        return is_power(n)
