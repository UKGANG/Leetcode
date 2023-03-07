"""
1197. Minimum Knight Moves
https://leetcode.com/problems/minimum-knight-moves/description/
"""
import collections


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = collections.deque([(0, 0)])
        res = 0
        seen = set([0, 0])
        while queue:
            size = len(queue)

            for _ in range(size):
                from_x, from_y = queue.popleft()
                if (from_x, from_y) == (x, y):
                    return res

                for dx, dy in [
                    (1, 2), (-1, -2), (-1, 2), (1, -2),
                    (2, 1), (-2, -1), (-2, 1), (2, -1),
                ]:
                    to_x, to_y = from_x + dx, from_y + dy
                    if (to_x, to_y) in seen:
                        continue
                    seen.add((to_x, to_y))
                    queue.append((to_x, to_y))
            res += 1
