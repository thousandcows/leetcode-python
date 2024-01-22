from utils.time_measurement import time_measurement


class LetterCombinationsOfAPhoneNumber:
    @staticmethod
    @time_measurement
    def solution(digits: str) -> list:
        def dfs(string: str = "") -> None:
            if len(string) == len(digits):
                answer.append(string)
                return

            for alpha in phone_dict[digits[len(string)]]:
                dfs(string + alpha)

        # exception handling
        if not digits:
            return []

        # create phone dictionary
        phone_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        # create answer list with dfs
        answer = []
        dfs()
        return answer
