# Definition for a binary tree node.
from typing import Optional

# LeetCode problem link: https://leetcode.com/problems/maximum-depth-of-binary-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_left = 1 + self.maxDepth(root.left)
        max_right = 1 + self.maxDepth(root.right)

        return max(max_left, max_right)
