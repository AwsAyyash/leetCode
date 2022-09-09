from typing import List


# LeetCode problem link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


def minimum_value(nums: List[int]) -> int:
    beg = 0
    end = len(nums) - 1
    min_val = float('inf')
    while beg <= end:
        mid = (beg + end) / 2
        mid = int(mid)

        min_val = min(nums[mid], min_val)
        if nums[end] < nums[mid]:  # the opposite way the un-normal case

            beg = mid + 1

        else:

            end = mid - 1

    return min_val


if __name__ == '__main__':
    print(minimum_value([4, 5, 6, 7, -5, 1, 2]))
