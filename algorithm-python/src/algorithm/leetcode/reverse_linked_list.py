from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        return self.traverse(head)

    def traverse(
        self, head: ListNode | None, acc: ListNode | None = None
    ) -> ListNode | None:
        if head is None:
            return acc
        return self.traverse(head.next, ListNode(head.val, acc))
