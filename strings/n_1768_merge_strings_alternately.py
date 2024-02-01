from utils.time_measurement import time_measurement


class MergeStringsAlternately:
    @staticmethod
    @time_measurement
    def solution(word1: str, word2: str) -> str:
        len_one, len_two = len(word1), len(word2)

        answer = []
        for i in range(max(len_one, len_two)):
            if i < len_one:
                answer.append(word1[i])
            if i < len_two:
                answer.append(word2[i])
        return "".join(answer)
