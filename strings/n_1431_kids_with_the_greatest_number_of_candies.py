from utils.time_measurement import time_measurement


class KidsWithTheGreatestNumberOfCandies:
    @staticmethod
    @time_measurement
    def solution(candies: list[int], extra_candies: int) -> list[bool]:
        # Find the maximum number of candies among all children
        max_candies = max(candies)
        # Determine if each child can have the greatest number of candies
        return [candy + extra_candies >= max_candies for candy in candies]
