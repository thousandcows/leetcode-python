from utils.time_measurement import time_measurement


class AllPathsFromSourceToTarget:
    @staticmethod
    @time_measurement
    def solution(graph: list[list[int]]) -> list[list[int]]:
        def backtrack(curr_node: int, path: list[int]):
            nonlocal n
            if curr_node == n:
                answer.append(path)
                return

            for node in graph[curr_node]:
                backtrack(node, path + [node])

        answer = []
        n = len(graph) - 1
        backtrack(0, [0])
        return answer
