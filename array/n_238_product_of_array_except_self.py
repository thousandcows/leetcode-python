from utils.time_measurement import time_measurement


class ProductOfArrayExceptSelf:
    @staticmethod
    @time_measurement
    def execute(nums: list[int]) -> list[int]:
        answer = []

        # multiply the left side
        curr_total = 1
        for i in range(len(nums)):
            answer.append(curr_total)
            curr_total = curr_total * nums[i]

        # multiply the right side
        curr_total = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= curr_total
            curr_total = curr_total * nums[i]

        return answer
