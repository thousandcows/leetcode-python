from collections import Counter, defaultdict

from utils.time_measurement import time_measurement


class HowManyNumbersAreSmallerThanTheCurrentNumber:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]) -> list[int]:
        answer = []
        hash_table = dict(Counter(nums))
        sorted_hash_keys = sorted(list(hash_table.keys()))

        memo_dict = defaultdict(int)
        for n in nums:
            if n in memo_dict:
                answer.append(memo_dict[n])
                continue

            cnt = 0
            for idx, key in enumerate(sorted_hash_keys):
                if key < n:
                    cnt += hash_table[key]
            memo_dict[n] += cnt

            answer.append(cnt)
        return answer

    @staticmethod
    @time_measurement
    def pythonic_solution(nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        return [sorted_nums.index(n) for n in nums]
