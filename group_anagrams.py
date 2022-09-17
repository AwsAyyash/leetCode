from typing import List

# LeetCode problem link: https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        _dict = {}
        for index, val in enumerate(strs):
            sorted_str = ''.join(sorted(val))

            if sorted_str in _dict:
                _dict[sorted_str].append(index)
            else:
                _dict[sorted_str] = [index]
                print(_dict[sorted_str])

        res = [[] for i in range(len(_dict))]

        for index, val in enumerate(_dict.values()):  # is an array
            for item in val:
                res[index].append(strs[item])  # at max, it will run O(n) times

        return res
