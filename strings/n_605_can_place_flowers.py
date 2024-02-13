from utils.time_measurement import time_measurement


class CanPlaceFlowers:
    @staticmethod
    @time_measurement
    def solution(flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return abs(flowerbed[0] - 1) >= n

        if n == 0:
            return True

        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if n == 0:
                return True

            if flowerbed[i] == 1:
                continue

            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1

        return n == 0
