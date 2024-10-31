'''
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
'''
from collections import Counter, deque

from test_tool import assert_value


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pending_counter = Counter(t)
        left_idx_cache = deque([])
        pending_count = len(t)
        l, r = -len(s) - 1, -1
        for r_new, c in enumerate(s):
            if c not in t:
                continue
            pending_counter[c] -= 1
            left_idx_cache.append(r_new)
            if pending_counter[c] < 0:
                continue
            pending_count -= 1
            if pending_count:
                continue

            while pending_counter[s[left_idx_cache[0]]] < 0:
                l_new = left_idx_cache.popleft()
                pending_counter[s[l_new]] += 1
            l_new = left_idx_cache.popleft()
            pending_counter[s[l_new]] += 1
            pending_count += 1

            if r - l > r_new - l_new:
                l, r = l_new, r_new

        return s[l:r + 1]

    def minWindow_v1(self, s: str, t: str) -> str:
        pending_chars = Counter(t)
        pending_chars_cnt = len(t)
        possible_idx = deque()
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

    def minWindow_v0(self, s: str, t: str) -> str:
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
