class SmallestEvenMultiple:
    @staticmethod
    def solution(n: int) -> int:
        return n * 2 if n % 2 != 0 else n
