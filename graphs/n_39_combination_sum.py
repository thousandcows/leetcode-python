from utils.time_measurement import time_measurement


class CombinationSum:
    @staticmethod
    @time_measurement
    def solution(candidates: list[int], target: int) -> list[list[int]]:
        def dfs(total: int, index: int, path: list[int]):
            if total < 0:
                return

            if total == 0:
                result.append(path)

            for i in range(index, len(candidates)):
                dfs(total - candidates[i], i, path + [candidates[i]])

        result = []

        dfs(target, 0, [])

        return result
