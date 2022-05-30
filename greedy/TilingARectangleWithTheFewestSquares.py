'''
1240. Tiling a Rectangle with the Fewest Squares
https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/
'''
from collections import defaultdict
from typing import List

from test_tool import assert_value


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m:
            return 1
        if n > m:
            m, n = n, m
        spaces = [m] * n

        terminal_hash = 0
        cache = {}

        res = [n * m]

        def dfs(n, m, spaces, cnt):
            if cnt > res[0]:
                return
            # 1. Find the beginning position of the largest space on horizontal direction
            start = 0
            max_space = 0
            for idx, space in enumerate(spaces):
                if space > max_space:
                    max_space = space
                    start = idx

            end = start
            for idx in range(start + 1, n):
                if spaces[idx] != max_space:
                    break
                if idx - start + 1 > max_space:
                    break
                end = idx

            # 2. Backtrack inside the maximum square that fits that position
            for curr_end in range(end + 1, start, -1):
                width = curr_end - start
                # 3. Update the space cache
                for curr_mid in range(start, curr_end):
                    spaces[curr_mid] -= width

                hash_key = self.hash(m, spaces)
                try:
                    if hash_key == terminal_hash:
                        res[0] = min(res[0], cnt + 1)
                        return
                    if hash_key in cache and cache[hash_key] <= cnt + 1:
                        return

                    cache[hash_key] = cnt + 1
                    dfs(n, m, spaces, cnt + 1)
                finally:
                    for curr_mid in range(start, curr_end):
                        spaces[curr_mid] += width

        dfs(n, m, spaces, 0)

        return res[0]

    def hash(self, m, spaces):
        res = 0
        base = m + 1
        for space in spaces:
            res += space * base
            base *= (m + 1)
        return res


assert_value(3, Solution().tilingRectangle, n=2, m=3)
assert_value(5, Solution().tilingRectangle, n=5, m=8)
assert_value(6, Solution().tilingRectangle, n=11, m=13)
