class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        shs: dict[str, int] = {}
        ths: dict[str, int] = {}
        for cs, ct in zip(s, t):
            csi = shs.get(cs) or 0
            shs[cs] = csi + 1
            tsi = ths.get(ct) or 0
            ths[ct] = tsi + 1
        return shs == ths
