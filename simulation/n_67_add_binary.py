from utils.time_measurement import time_measurement


class AddBinary:
    @staticmethod
    @time_measurement
    def solution(a: str, b: str):
        def change_to_decimal(binary: str):
            decimal = 0
            for i in range(len(binary) - 1, -1, -1):
                decimal += pow(2, i) if binary[len(binary) - 1 - i] == "1" else 0

            return decimal

        return bin(change_to_decimal(a) + change_to_decimal(b))[2:]
