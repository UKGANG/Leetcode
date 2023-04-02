"""
1647. Minimum Deletions to Make Character Frequencies Unique
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique
"""
import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        counter = collections.Counter(s)
        freq = collections.Counter(counter.values())

        max_freq = max(freq.keys())
        duplicated_cnt = freq[max_freq] - 1
        res = duplicated_cnt
        for i in range(max_freq - 1, 0, -1):
            duplicated_cnt += freq[i]
            duplicated_cnt -= 1
            duplicated_cnt = max(duplicated_cnt, 0)
            res += duplicated_cnt

        return res
