from utils.time_measurement import time_measurement


class ReverseVowelsOfAString:
    @staticmethod
    @time_measurement
    def solution(s: str) -> str:
        vowels = "aeiouAEIOU"
        str_list = [char for char in s]
        idx_list = []
        vowel_list = []

        for idx, char in enumerate(s):
            if char in vowels:
                idx_list.append(idx)
                vowel_list.append(char)

        vowel_list = vowel_list[::-1]

        for idx in range(len(idx_list)):
            str_list[idx_list[idx]] = vowel_list[idx]

        return "".join(str_list)
