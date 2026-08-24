from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        top: list[list[int]] = [[] for _ in range(len(nums))]
        for ck, cc in count.items():
            top[cc - 1].append(ck)
        res: list[int] = []
        for i in reversed(range(len(top))):
            for tk in top[i]:
                res.append(tk)
                if len(res) == k:
                    return res
        return []
