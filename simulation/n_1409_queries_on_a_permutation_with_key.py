from utils.time_measurement import time_measurement


class QueriesOnAPermutationWithKey:
    @staticmethod
    @time_measurement
    def solution(queries: list[int], m: int) -> list[int]:
        p = [i for i in range(1, m + 1)]
        ans = []

        for n in queries:
            index = p.index(n)
            ans.append(index)
            p = [n] + [i for i in p if i != n]
        return ans
