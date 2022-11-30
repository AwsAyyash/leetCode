# LeetCode problem link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

def length_of_longest_substring(self, s: str) -> int:
    if len(s) <= 1:
        return len(s)

    beg = 0

    _set = set()

    max_sub = 0

    for end in range(len(s)):
        while s[end] in _set:
            _set.remove(s[beg])
            beg += 1
        _set.add(s[end])
        max_sub = max(max_sub, end - beg + 1)

    return max_sub
