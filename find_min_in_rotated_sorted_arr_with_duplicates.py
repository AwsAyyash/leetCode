from typing import List


# LeetCode problem link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


def minimum_value(nums: List[int]) -> int:
    beg = 0
    end = len(nums) - 1
    # min_val = nums[0]
    while beg < end:
        mid = (beg + end) / 2
        mid = int(mid)

        #   min_val = min(nums[mid], min_val)
        if nums[end] < nums[mid]:  # the opposite way the un-normal case

            beg = mid + 1


        elif nums[end] > nums[mid]:

            end = mid
        else:

            end -= 1
            while nums[end] == nums[end - 1] and beg < end:
                end -= 1

    return nums[beg]


if __name__ == '__main__':
    print(minimum_value([4, 5, 6, 7, -5, 1, 2]))
