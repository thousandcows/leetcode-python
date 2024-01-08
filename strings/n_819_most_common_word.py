import re
from collections import Counter

from utils.time_measurement import time_measurement


class MostCommonWord:
    @staticmethod
    @time_measurement
    def execute(paragraph: str, banned: list[str]) -> str:
        paragraph = re.sub("[!?',;.]", " ", paragraph).lower().split()
        words = [w for w in paragraph if w not in banned]

        counted_list = Counter(words)
        return counted_list.most_common(1)[0][0]
