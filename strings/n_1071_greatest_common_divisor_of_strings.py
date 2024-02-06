from utils.time_measurement import time_measurement


class GCD:
    @staticmethod
    @time_measurement
    def solution(str1: str, str2: str) -> str:
        def find_gcd_length_of_strings(longer: int, shorter: int) -> int:
            while shorter:
                longer, shorter = (
                    shorter,
                    longer % shorter,
                )
            return longer

        def get_all_divisor_of_gcd(n: int) -> list[int]:
            divisors_set = set()
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divisors_set.add(i)
                    divisors_set.add(n // i)
            return sorted(list(divisors_set), reverse=True)

        def is_string_concatenable(div: int, candidate: str) -> bool:
            larger_mod, smaller_mod = len(longer_str) // div, len(shorter_str) // div

            if (
                candidate * larger_mod == longer_str
                and candidate * smaller_mod == shorter_str
            ):
                return True
            return False

        longer_str, shorter_str = (
            (str1, str2) if len(str1) >= len(str2) else (str2, str1)
        )

        gcd = find_gcd_length_of_strings(len(longer_str), len(shorter_str))
        divisors = get_all_divisor_of_gcd(gcd)

        for divisor in divisors:
            candidate_str = shorter_str[:divisor]
            if is_string_concatenable(divisor, candidate_str):
                return candidate_str

        return ""
