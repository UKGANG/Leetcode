"""
2405. Optimal Partition of String
https://leetcode.com/problems/optimal-partition-of-string/
"""
import collections


class Solution:
    def partitionString(self, s: str) -> int:
        counter = collections.Counter()
        res = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            if counter[s[right]] > 1:
                res += 1
                counter.clear()
                counter[s[right]] += 1

        res += 1
        return res
