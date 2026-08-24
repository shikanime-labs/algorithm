class Solution:
    def threeSum(self, nums: list[int]) -> set[tuple[int, int, int]]:
        res: set[tuple[int, int, int]] = set()
        for i, target in enumerate(nums):
            # Fastlane skip repeated occurrence
            if i > 0 and target == nums[i - 1]:
                continue
            subnums = nums[:i] + nums[i + 1 :]
            memo: dict[int, int] = {}
            for i, n in enumerate(subnums):
                diff = -target - n
                if diff in memo:
                    res.add(tuple(sorted([target, subnums[memo[diff]], n])))
                memo[n] = i
        return res
