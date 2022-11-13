'''
909. Snakes and Ladders
https://leetcode.com/problems/snakes-and-ladders/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        target = m * n

        seen = set()

        queue = collections.deque([1])

        cnt = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                pos_curr = queue.popleft()
                # Index check
                if pos_curr > target:
                    continue
                if pos_curr == target:
                    return cnt
                # Check the step at the current position
                if pos_curr in seen:
                    continue
                seen.add(pos_curr)
                row, col = self.get_pos(pos_curr, m, n)
                post_next = board[row][col]
                pos_curr = pos_curr if post_next == -1 else post_next
                if pos_curr == target:
                    return cnt
                for i in range(1, 7):
                    queue.append(pos_curr + i)
            cnt += 1
        return -1

    def get_pos(self, idx, m, n):
        idx -= 1
        row = idx // n
        col = idx % m
        return ~row, (~col if row & 1 else col)


assert_value(1, Solution().snakesAndLadders, board=[
    [-1, -1],
    [-1, 3]
])

assert_value(1, Solution().snakesAndLadders, board=[
    [-1, -1, -1],
    [-1, 9, 8],
    [-1, 8, 9]
])

# assert_value(2, Solution().snakesAndLadders, board=[
#     [-1, 4, -1],
#     [6, 2, 6],
#     [-1, 3, -1]
# ])
