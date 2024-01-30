from utils.time_measurement import time_measurement


class PowerOfThree:
    @staticmethod
    @time_measurement
    def solution(n: int) -> bool:
        def is_power(num: int) -> bool:
            if num <= 0 or (num % 3 != 0 and num != 1):
                return False

            if num == 1:
                return True

            return is_power(num // 3)

        return is_power(n)
