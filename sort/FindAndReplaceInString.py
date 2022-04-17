'''
833. Find And Replace in String
https://leetcode.com/problems/find-and-replace-in-string/
'''
from operator import itemgetter
from typing import List, Optional, Tuple

from test_tool import assert_value


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        n = len(indices)

        indices = [(indices[i], i) for i in range(n)]
        indices = sorted(indices, key=itemgetter(0))

        for i in range(n - 1, -1, -1):
            idx, i = indices[i]
            src, tar = sources[i], targets[i]
            if s[idx:idx + len(src)] != src:
                continue
            s = s[: idx] + tar + s[idx + len(src):]
        return s


assert_value("eeebffff", Solution().findReplaceString, s="abcd", indices=[0, 2], sources=["a", "cd"],
             targets=["eee", "ffff"])
assert_value("eeecd", Solution().findReplaceString, s="abcd", indices=[0, 2], sources=["ab", "ec"],
             targets=["eee", "ffff"])
assert_value("vbfrssozp", Solution().findReplaceString, s="vmokgggqzp", indices=[3, 5, 1], sources=["kg", "ggq", "mo"],
             targets=["s", "so", "bfr"])
