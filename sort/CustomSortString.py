'''
791. Custom Sort String
https://leetcode.com/problems/custom-sort-string/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_hash = {c:i for i, c in enumerate(order)}
        order_hash_reversed = {i:c for i, c in enumerate(order)}
        s_hash = [order_hash[c] for c in s if c in order_hash]
        s_hash_sorted = sorted(s_hash)
        res = []
        idx = 0
        for c in s:
            if c not in order_hash:
                res.append(c)
                continue
            res.append(order_hash_reversed[s_hash_sorted[idx]])
            idx += 1
        return ''.join(res)
    def customSortString_v0(self, order: str, s: str) -> str:
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
