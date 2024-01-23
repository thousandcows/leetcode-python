from itertools import permutations

from utils.time_measurement import time_measurement


class Permutations:
    @staticmethod
    @time_measurement
    def solution(nums: list) -> list[list[int]]:
        return list(map(list, permutations(nums, len(nums))))

    @staticmethod
    @time_measurement
    def solution_dfs(nums: list) -> list[list[int]]:
        result = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])
                return

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return result
