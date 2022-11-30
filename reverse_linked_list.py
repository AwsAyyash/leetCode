# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None

    curr = head
    while bool(curr):
        old_next = curr.next
        curr.next = prev
        prev = curr
        curr = old_next
    head = prev

    return head


head = ListNode(1, None)

head.next = ListNode(2, None)
head.next.next = ListNode(3, None)
head.next.next.next = ListNode(4, None)

res = reverse_list(head)
if res.next:
    print(res.next.val)
else:
    print(res.val)
