from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_head = ListNode()
        curr = dummy_head
        while list1 and list2:

            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return dummy_head.next



head1 = ListNode(1, None)

head1.next = ListNode(2, None)
head1.next.next = ListNode(3, None)
head1.next.next.next = ListNode(4, None)

head2 = ListNode(1, None)

head2.next = ListNode(2, None)
head2.next.next = ListNode(5, None)
head2.next.next.next = ListNode(6, None)

sol = Solution()
res = sol.mergeTwoLists(head1, head2)

print(res.next.next.val)
