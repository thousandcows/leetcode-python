from utils.time_measurement import time_measurement


class ArrayPartition:
    @staticmethod
    @time_measurement
    def execute(nums: list[int]) -> int:
        return sum(sorted(nums)[::2])
