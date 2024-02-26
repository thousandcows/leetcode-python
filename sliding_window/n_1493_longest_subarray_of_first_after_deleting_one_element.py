from utils.time_measurement import time_measurement


class LongestSubarrayOfFirstAfterDeletingOneElement:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]) -> int:
        zeros = [i for i, v in enumerate(nums) if v == 0]

        if nums.count(0) <= 1:
            return len(nums) - 1

        if len(zeros) == len(nums):
            return 0

        answer, current_sub_length = 0, 0

        for i in range(len(zeros)):
            current_index = zeros[i]
            if i == 0:
                if current_index == 0:
                    current_sub_length = zeros[i + 1] - 1
                else:
                    current_sub_length = zeros[i + 1] - 1
            elif i == len(zeros) - 1:
                if current_index == len(nums) - 1:
                    current_sub_length = zeros[i] - zeros[i - 1] - 1
                else:
                    current_sub_length = len(nums) - zeros[i - 1] - 2
            else:
                current_sub_length = zeros[i + 1] - zeros[i - 1] - 2

            answer = max(answer, current_sub_length)
        return answer