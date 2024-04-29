from utils.time_measurement import time_measurement


class TestExam:
    @staticmethod
    @time_measurement
    def solution(answers: list[int]) -> list[int]:
        result = [0, 0, 0]
        pattern_one = [1, 2, 3, 4, 5]
        pattern_two = [2, 1, 2, 3, 2, 4, 2, 5]
        pattern_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

        for i, ans in enumerate(answers):
            if pattern_one[(i + 1) % 5 - 1] == ans:
                result[0] += 1
            if pattern_two[(i + 1) % 8 - 1] == ans:
                result[1] += 1
            if pattern_three[(i + 1) % 10 - 1] == ans:
                result[2] += 1
        max_count = max(result)
        return [i + 1 for i in range(3) if result[i] == max_count]
