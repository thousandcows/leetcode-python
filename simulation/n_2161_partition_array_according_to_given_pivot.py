from utils.time_measurement import time_measurement


class PartitionArrayAccordingToGivenPivot:
    @staticmethod
    @time_measurement
    def solution(nums: list[int], pivot: int):
        small, equal, greater = [], [], []

        for n in nums:
            if n == pivot:
                equal.append(n)
            elif n < pivot:
                small.append(n)
            else:
                greater.append(n)

        return small + equal + greater
