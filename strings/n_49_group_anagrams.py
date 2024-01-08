from collections import defaultdict

from utils.time_measurement import time_measurement


class GroupAnagrams:
    @staticmethod
    @time_measurement
    def execute(strs: list[str]) -> list[list[str]]:
        # 1. create default dict
        anagrams = defaultdict(list)

        # 2. iterate strs
        for s in strs:
            # 3. sort string in order
            key = "".join(sorted(s))
            # 4. append the original string to the value of the dictionary
            anagrams[key].append(s)

        # 5. return the list of items
        return [v for v in anagrams.values()]
