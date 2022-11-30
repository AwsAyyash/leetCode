from typing import Optional


# LeetCode problem link: https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head.next

        # O(n/2)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None

        # O(n/2)
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # prev is the tail now

        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second

            second.next = tmp1

            first, second = tmp1, tmp2
