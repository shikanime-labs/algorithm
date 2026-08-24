from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        is_balanced, _ = self.traverse(root)
        return is_balanced

    def traverse(self, root: TreeNode | None) -> tuple[bool, int]:
        if not root:
            return True, 0
        is_left_balanced, left = self.traverse(root.left)
        is_right_balanced, right = self.traverse(root.right)
        return (
            is_left_balanced and is_right_balanced and 1 >= abs(left - right),
            max(left, right) + 1,
        )
