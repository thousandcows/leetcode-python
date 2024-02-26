from utils.time_measurement import time_measurement


class LongestSubarrayOfFirstAfterDeletingOneElement:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]) -> int:

        if nums.count(0) <= 1:
            return len(nums) - 1

        zeros = [-1] + [i for i, v in enumerate(nums) if v == 0] + [len(nums)]

        answer = 0

        for i in range(1, len(zeros) - 1):
            current_sub_length = zeros[i + 1] - zeros[i - 1] - 2
            answer = max(answer, current_sub_length)

        return answer