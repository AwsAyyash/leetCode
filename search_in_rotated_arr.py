from typing import List


# LeetCode problem link: https://leetcode.com/problems/search-in-rotated-sorted-array/

# It's all about binary search, but now we have to know if we need to eliminate the endpoints or the mid-point (the normal case)

def search(nums: List[int], target: int) -> int:
    beg = 0
    end = len(nums) - 1
    while beg <= end:
        mid = (beg + end) / 2
        mid = int(mid)
        if nums[mid] == target:
            return mid
        elif nums[end] < nums[beg]:  # the opposite way the un-normal case
            if nums[end] < target:
                end = end - 1
            else:
                beg = beg + 1
        else:

            if nums[mid] > target:
                end = mid - 1
            else:
                beg = mid + 1
    return -1


if __name__ == "__main__":
    print(search([4, 5, 6, 7, 0, 1, 2],55))
