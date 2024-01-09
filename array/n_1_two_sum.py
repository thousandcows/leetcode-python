from utils.time_measurement import time_measurement


class TwoSome:
    @staticmethod
    @time_measurement
    def execute(nums: list[int], target: int) -> list[int]:
        # create dictionary to save key-value(number-index)
        nums_dict = {}

        # iterate list
        for curr_idx, curr_num in enumerate(nums):
            # find the number to match the target number
            pair_numer = target - curr_num

            # return a list if the number exists in the dictionary and its index is not the same as the current number
            if pair_numer in nums_dict and curr_idx != nums_dict[pair_numer]:
                return [curr_idx, nums_dict[pair_numer]]

            # if the condition is not met, then save current idx and number in the dictionary
            nums_dict[curr_num] = curr_idx
