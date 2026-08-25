from itertools import dropwhile


class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        while any(height):
            height = list(dropwhile(lambda x: 0 >= x, height))
            height = reversed(height)
            height = list(dropwhile(lambda x: 0 >= x, height))
            water += sum(1 for x in height if x == 0)
            height = [max(x - 1, 0) for x in height]
        return water
