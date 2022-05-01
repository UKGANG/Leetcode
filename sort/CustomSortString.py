'''
791. Custom Sort String
https://leetcode.com/problems/custom-sort-string/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        idx_order = collections.defaultdict(lambda: -1)
        idx_order.update({c: i for i, c in enumerate(order)})
        idx_s = [idx_order[c] for c in s]
        suffix = ''.join(s[idx] for idx, i in enumerate(idx_s) if i == -1)
        idx_s = sorted(i for i in idx_s if i != -1)
        prefix = ''.join(order[i] for i in idx_s)

        return prefix + suffix


assert_value("cbad", Solution().customSortString, order="cba", s="abcd")
assert_value("cbad", Solution().customSortString, order="cbafg", s="abcd")
assert_value("eexvw", Solution().customSortString, order="exv", s="xwvee")
