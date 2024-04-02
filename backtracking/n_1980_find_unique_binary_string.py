from utils.time_measurement import time_measurement


class FindUniqueBinaryString:
    @staticmethod
    @time_measurement
    def solution(nums: list[str]):
        def backtrack(curr_num: str):
            nonlocal answer
            if answer is not None:
                return

            if len(curr_num) == len(nums):
                if curr_num not in nums:
                    answer = curr_num
                return

            backtrack(curr_num + "0")
            backtrack(curr_num + "1")

        answer = None
        backtrack("")
        return answer
