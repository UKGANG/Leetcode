"""
340. Longest Substring with At Most K Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters
"""
import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = collections.Counter()
        res = []
        max_left, max_right = 0, -1
        left = 0
        for right, c in enumerate(s):
            counter[c] += 1
            if counter[c] == 1:
                k -= 1
            while k < 0:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    k += 1
                left += 1
            if right - left > max_right - max_left:
                max_left, max_right = left, right
        return max_right - max_left + 1
