from utils.time_measurement import time_measurement


class Subsets:
    @staticmethod
    @time_measurement
    def solution(nums):
        def dfs(start: int, subset: list[int]) -> None:
            result.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])
                dfs(i + 1, subset)
                subset.pop()

        result = []
        dfs(0, [])

        return result
