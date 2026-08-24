from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
