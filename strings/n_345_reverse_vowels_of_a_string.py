from utils.time_measurement import time_measurement


class ReverseVowelsOfAString:
    @staticmethod
    @time_measurement
    def solution(s: str) -> str:
        vowels = "aeiouAEIOU"
        str_list = [char for char in s]

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and str_list[left] not in vowels:
                left += 1

            while left < right and str_list[right] not in vowels:
                right -= 1

            str_list[left], str_list[right] = str_list[right], str_list[left]
            left += 1
            right -= 1

        return "".join(str_list)
