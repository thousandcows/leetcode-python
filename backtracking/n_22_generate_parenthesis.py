from utils.time_measurement import time_measurement


class GenerateParenthesis:
    @staticmethod
    @time_measurement
    def solution(n: int):
        def is_valid(parenthesis: str):
            stack = []
            for p in parenthesis:
                if p == "(":
                    stack.append(p)
                elif p == ")" and len(stack) == 0:
                    return False
                elif p == ")" and stack[-1] == "(":
                    stack.pop()
            return len(stack) == 0

        def backtrack(parenthesis: str):
            nonlocal limit
            if len(parenthesis) == limit:
                if is_valid(parenthesis):
                    answer.append(parenthesis)
                return

            backtrack(parenthesis + "(")
            backtrack(parenthesis + ")")

        limit = 2 * n
        answer = []
        backtrack("(")
        return answer
