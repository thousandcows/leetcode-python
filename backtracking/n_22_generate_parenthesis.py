from utils.time_measurement import time_measurement


class GenerateParenthesis:
    @staticmethod
    @time_measurement
    def solution(n: int):
        def backtrack(parenthesis: str, open_count: int, close_count: int):
            if open_count == n and close_count == 0:
                answer.append(parenthesis)
                return

            if open_count < n:
                backtrack(parenthesis + "(", open_count + 1, close_count + 1)

            if close_count > 0:
                backtrack(parenthesis + ")", open_count, close_count - 1)

        answer = []
        backtrack("(", 1, 1)
        return answer
