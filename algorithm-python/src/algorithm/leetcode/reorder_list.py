from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        second = self.reverse(self.disconnect(self.middle(head)))
        self.interleave(head, second)

    def disconnect(self, head: ListNode | None):
        if not head:
            return None
        cursor = head.next
        head.next = None
        return cursor

    def middle(self, head: ListNode | None):
        if not head:
            return None
        slow, fast = head, head.next
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head: ListNode | None):
        cursor = head
        prev = None
        while cursor:
            tmp = cursor.next
            cursor.next = prev
            prev = cursor
            cursor = tmp
        return prev

    def interleave(self, a: ListNode | None, b: ListNode | None):
        while a and b:
            tmpa, tmpb = a.next, b.next
            a.next = b
            b.next = tmpa
            a, b = tmpa, tmpb
