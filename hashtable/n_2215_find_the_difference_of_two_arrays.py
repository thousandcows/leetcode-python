from utils.time_measurement import time_measurement


class FindTheDifferenceOfTwoArrays:
    @staticmethod
    @time_measurement
    def solution(nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return [list(nums1 - nums2), list(nums2 - nums1)]
