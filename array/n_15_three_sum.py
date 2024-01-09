from utils.time_measurement import time_measurement


class ThreeSumTwoPointer:
    @staticmethod
    @time_measurement
    def execute(nums: list[int]) -> list[list[int]]:
        # exception handling
        if len(nums) < 3:
            return []

        answer = []
        nums.sort()

        for i in range(len(nums) - 2):
            # skip the duplicated number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # set left and right pointers
            left = i + 1
            right = len(nums) - 1

            # move pointers to find 3sums
            while left < right:
                # declare and assign current list and sum
                curr_list = [nums[i], nums[left], nums[right]]
                curr_sum = sum(curr_list)

                if curr_sum == 0:
                    answer.append(curr_list)  # append list to the answer
                    # skip the numbers on the left and right if nums are to be duplicated
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # let the calculation starts from the new, different numbers
                    left += 1
                    right -= 1

                elif curr_sum > 0:
                    right -= 1
                else:
                    left += 1

        return answer
