from utils.time_measurement import time_measurement


class ClumsyFactorial:
    @staticmethod
    @time_measurement
    def solution(n: int) -> int:
        operators = ["*", "//", "+", "-"]
        equation = ""
        operator_index = 0
        for i in range(n, 0, -1):
            if operator_index == 0:
                equation += str(i) if equation == "" else operators[3] + str(i)
            elif operator_index == 1:
                equation += operators[0] + str(i)
            elif operator_index == 2:
                equation += operators[1] + str(i)
            elif operator_index == 3:
                equation += operators[2] + str(i)

            if operator_index == 3:
                operator_index = 0
                continue
            operator_index += 1

        return int(eval(equation))
