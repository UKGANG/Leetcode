'''
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
'''
import collections
from collections import Counter

from test_tool import assert_value


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pending_chars = collections.Counter(t)
        pending_chars_cnt = len(t)
        possible_idx = collections.deque()
        l, r = -len(s) - 1, -1,
        for idx, c in enumerate(s):
            # Skip the other characters.
            if c not in t:
                continue
            pending_chars[c] -= 1
            possible_idx.append(idx)

            if pending_chars[c] < 0:
                continue
            pending_chars_cnt -= 1
            # A candidate chunk
            if not pending_chars_cnt:
                while pending_chars[s[possible_idx[0]]] < 0:
                    pending_chars[s[possible_idx[0]]] += 1
                    possible_idx.popleft()
                if r - l > idx - possible_idx[0]:
                    r, l = idx, possible_idx[0]
                pending_chars[s[possible_idx[0]]] += 1
                possible_idx.popleft()
                pending_chars_cnt += 1

        return s[l: r + 1]

    def _minWindow(self, s: str, t: str) -> str:
        pending_chars = Counter(t)
        pending_chars_cnt = len(t)
        head = 0
        possible_idx = []
        l, r = -len(s) - 1, -1,
        for idx, c in enumerate(s):
            # Skip the other characters.
            if c not in t:
                continue
            pending_chars[c] -= 1
            possible_idx.append(idx)

            if pending_chars[c] < 0:
                continue
            pending_chars_cnt -= 1
            # A candidate chunk
            if not pending_chars_cnt:
                while pending_chars[s[possible_idx[head]]] < 0:
                    pending_chars[s[possible_idx[head]]] += 1
                    head += 1
                if r - l > idx - possible_idx[head]:
                    r, l = idx, possible_idx[head]
                pending_chars[s[possible_idx[head]]] += 1
                head += 1
                pending_chars_cnt += 1

        return s[l: r + 1]


assert_value("BANC", Solution().minWindow, s="ADOBECODEBANC", t="ABC")
assert_value("a", Solution().minWindow, s="a", t="a")
assert_value("", Solution().minWindow, s="a", t="aa")
