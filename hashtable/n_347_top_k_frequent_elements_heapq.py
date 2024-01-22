import heapq
from collections import Counter

from utils.time_measurement import time_measurement


class TopKFrequentElementsWithHeapq:
    @staticmethod
    @time_measurement
    def solution(nums: list, k: int) -> list:
        heap_list = []
        for num, count in Counter(nums).items():
            heapq.heappush(heap_list, (-count, num))

        return [heapq.heappop(heap_list)[1] for _ in range(k)]
