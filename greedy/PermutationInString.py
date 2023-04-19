"""
567. Permutation in String
https://leetcode.com/problems/permutation-in-string
"""
import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = collections.Counter()
        s2_freq = collections.Counter()

        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1

        remaining = 26
        for i in range(26):
            if s1_freq[i] == s2_freq[i]:
                remaining -= 1

        for i in range(len(s2) - len(s1)):
            if not remaining:
                break
            idx_left = ord(s2[i]) - ord('a')
            idx_right = ord(s2[i + len(s1)]) - ord('a')

            s2_freq[idx_left] -= 1
            if s1_freq[idx_left] == s2_freq[idx_left]:
                remaining -= 1
            elif s1_freq[idx_left] == s2_freq[idx_left] + 1:
                remaining += 1

            s2_freq[idx_right] += 1
            if s1_freq[idx_right] == s2_freq[idx_right]:
                remaining -= 1
            elif s1_freq[idx_right] == s2_freq[idx_right] - 1:
                remaining += 1

        return not remaining
