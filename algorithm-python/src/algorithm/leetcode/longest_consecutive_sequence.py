from collections.abc import Iterable
from functools import partial, reduce


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        return self.longestConsecutiveFromSet(set(nums))

    def longestConsecutiveFromSet(self, nums: set[int]) -> int:
        return reduce(
            lambda best, x: max(self.findConsecutiveLength(nums, x), best),
            filter(partial(self.isSequenceHead, nums), nums),
            0,
        )

    def isSequenceHead(self, nums: Iterable[int], x: int) -> bool:
        return x - 1 not in nums

    def findConsecutiveLength(self, nums: Iterable[int], x: int) -> int:
        best = 0
        while x in nums:
            best += 1
            x += 1
        return best
