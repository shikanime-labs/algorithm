from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None
        tmpr, tmpl = root.right, root.left
        root.right = root.left
        root.left = tmpr
        self.invertTree(tmpr)
        self.invertTree(tmpl)
        return root
