"""
1197. Minimum Knight Moves
https://leetcode.com/problems/minimum-knight-moves/description/
"""
import collections


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        source_queue = collections.deque([(0, 0)])
        dest_queue = collections.deque([(x, y)])
        res = 0
        from_seen = set([(0, 0)])
        to_seen = set([(x, y)])

        def unidirectional_bfs(queue, from_seen, to_seen):
            nonlocal res
            size = len(queue)
            for _ in range(size):
                from_x, from_y = queue.popleft()
                if (from_x, from_y) in to_seen:
                    return True

                for dx, dy in [
                    (1, 2), (-1, -2), (-1, 2), (1, -2),
                    (2, 1), (-2, -1), (-2, 1), (2, -1),
                ]:
                    to_x, to_y = from_x + dx, from_y + dy
                    if (to_x, to_y) in from_seen:
                        continue
                    from_seen.add((to_x, to_y))
                    queue.append((to_x, to_y))
            res += 1
            return False

        while True:
            if unidirectional_bfs(source_queue, from_seen, to_seen):
                return res
            if unidirectional_bfs(dest_queue, to_seen, from_seen):
                return res

    def _unidirectional_bfs_minKnightMoves(self, x: int, y: int) -> int:
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
