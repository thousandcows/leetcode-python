from utils.time_measurement import time_measurement


class TrappingRainWater:
    @staticmethod
    @time_measurement
    def execute(height: list[int]) -> int:
        # return 0 if height is empty
        if not height:
            return 0

        total = 0  # total volume of water
        left_ptr, right_ptr = (
            0,
            len(height) - 1,
        )  # pointers to move from the start and end edges
        left_max, right_max = (
            height[left_ptr],
            height[right_ptr],
        )  # initialize max values

        # repeat while left_pointer != right pointer
        while left_ptr < right_ptr:
            # set max values
            left_max, right_max = max(height[left_ptr], left_max), max(
                height[right_ptr], right_max
            )

            # core logic
            if left_max <= right_max:
                total += left_max - height[left_ptr]
                left_ptr += 1
            else:
                total += right_max - height[right_ptr]
                right_ptr -= 1

        return total
