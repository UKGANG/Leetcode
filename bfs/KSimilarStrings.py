'''
854. K-Similar Strings
https://leetcode.com/problems/k-similar-strings/
'''
from typing import List, Tuple

from test_tool import assert_value


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        visited = set([s1])
        curr_level = set([s1])
        res = 0
        while curr_level:
            next_level = set()
            for s in curr_level:
                for i in range(len(s) - 1):
                    if s[i] == s2[i]:
                        continue
                    for j in range(i + 1, len(s)):
                        if s[j] == s2[j] or s[j] != s2[i]:
                            continue
                        next_s = f'{s[:i]}{s[j]}{s[i + 1:j]}{s[i]}{s[j + 1:]}'
                        if next_s in visited:
                            continue
                        if next_s == s2:
                            return res + 1
                        visited.add(next_s)
                        next_level.add(next_s)
                    break
            res += 1
            curr_level = next_level

        return -1


assert_value(1, Solution().kSimilarity, s1="ab", s2="ba")
assert_value(2, Solution().kSimilarity, s1="abc", s2="bca")
assert_value(3, Solution().kSimilarity, s1="bccaba", s2="abacbc")
