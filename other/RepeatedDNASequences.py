'''
187. Repeated DNA Sequences
https://leetcode.com/problems/repeated-dna-sequences/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = collections.defaultdict(lambda: 0)
        for i in range(len(s) - 9):
            res[s[i: i + 10]] += 1
        return [k for k, v in res.items() if v > 1]


assert_value(["AAAAACCCCC", "CCCCCAAAAA"], Solution().findRepeatedDnaSequences, s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
assert_value(["AAAAAAAAAA"], Solution().findRepeatedDnaSequences, s="AAAAAAAAAAAAA")
assert_value(["AAAAAAAAAA"], Solution().findRepeatedDnaSequences, s="AAAAAAAAAAA")
