from typing import List


class three_sum:
    def three_sum_func(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []

        for index, num in enumerate(nums):

            if index > 0 and num == nums[index - 1]:
                continue
            beginning = index + 1
            last = len(nums) - 1

            while beginning < last:
                three_sum_var = num + nums[beginning] + nums[last]
                if three_sum_var == 0:
                    res.append([num, nums[beginning], nums[last]])
                    beginning += 1

                    while nums[beginning] == nums[beginning - 1] and beginning < last:
                        beginning += 1

                elif three_sum_var > 0:
                    last -= 1
                else:
                    beginning += 1
        return res

if __name__ == "__main__":
    three_sum_object = three_sum()
    print(three_sum_object.three_sum_func([-1, 0, 1, 2, -1, -4]))
