from typing import List


# LeetCode problem link: https://leetcode.com/problems/container-with-most-water/

def max_area(height: List[int]) -> int:
    beginning = 0
    last = len(height) - 1

    max_amount = float('-inf')

    while beginning < last:

        x = min(height[last], height[beginning])
        y = last - beginning
        local_max = x * y
        max_amount = max(max_amount, local_max)

        if height[beginning] > height[last]:
            last -= 1
        else:
            beginning += 1
    return max_amount


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
