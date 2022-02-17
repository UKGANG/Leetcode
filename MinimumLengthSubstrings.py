'''
Minimum Length Substrings
https://leetcode.com/problems/minimum-window-substring/
'''
import collections
from typing import List

from test_tool import assert_value


def min_length_substring(s, t):
    cnt = collections.Counter(t)
    n = len(t)
    indices = []
    res = len(s)
    found = False
    head = 0
    for idx, c in enumerate(s):
        if c not in t:
            continue
        cnt[c] -= 1
        indices.append(idx)

        # Skip duplications in the middle
        if cnt[c] < 0:
            continue

        n -= 1
        # Detect an ending char
        if n == 0:
            # Jump to the starting point with no duplications in the middle
            while cnt[s[indices[head]]] < 0:
                cnt[s[indices[head]]] += 1
                head += 1
            res = min(res, indices[-1] - indices[head] + 1)
            cnt[s[indices[head]]] += 1
            head += 1
            n += 1
            found = True

    if not found:
        return -1
    return res


assert_value(5, min_length_substring, s="dcbefebce", t="fd")
assert_value(4, min_length_substring, s="ADOBECODEBANC", t="ABC")
assert_value(1, min_length_substring, s="a", t="a")
assert_value(-1, min_length_substring, s="a", t="aa")
assert_value(4, min_length_substring, s="acbbaca", t="aba")
