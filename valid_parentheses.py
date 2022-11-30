# LeetCode problem link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    @staticmethod
    def is_valid(s: str) -> bool:

        _dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        _list = []
        for index, val in enumerate(s):

            if val in _dict:
                _list.append(val)
            else:
                if len(_list) == 0:
                    return False
                ch = _list.pop()
                if val != _dict[ch]:
                    return False

        if len(_list) != 0:
            return False
        return True


if __name__ == "__main__":
    print(Solution.is_valid('((()))'))
