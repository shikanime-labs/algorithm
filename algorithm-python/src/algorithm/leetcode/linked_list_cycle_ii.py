from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        acks = set()
        while head is not None:
            if id(head) in acks:
                return head
            acks.add(id(head))
            head = head.next
        return None
