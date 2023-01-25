"""
1529. Minimum Suffix Flips
https://leetcode.com/problems/minimum-suffix-flips/
"""


class Solution:
    def minFlips(self, target: str) -> int:
        res = 0
        if target[0] == '1':
            res += 1
        for i in range(1, len(target)):
            if target[i - 1] != target[i]:
                res += 1
        return res

    def _minFlips(self, target: str) -> int:
        res = 0
        for i in range(len(target)):
            if not res & 1 and target[i] == "1":
                res += 1
            elif res & 1 and target[i] == "0":
                res += 1
        return res
