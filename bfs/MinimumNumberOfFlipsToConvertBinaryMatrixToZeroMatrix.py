'''
1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        curr_level = [''.join(str(i) for i in sum(mat, []))]
        res = 0
        target = '0' * (m * n)
        visited = set()
        while curr_level:
            next_level = []
            while curr_level:
                curr_board = curr_level.pop()
                if curr_board == target:
                    return res
                for i in range(m * n):
                    move = {i - n, i, i + n}
                    move = {j for j in move if 0 <= j < m * n}
                    if i > 0 and i // n == (i - 1) // n:
                        move.add(i - 1)
                    if i < m * n and i // n == (i + 1) // n:
                        move.add(i + 1)
                    next_board = list(curr_board)
                    for j in move:
                        next_board[j] = '0' if next_board[j] == '1' else '1'
                    next_board = ''.join(next_board)
                    if next_board in visited:
                        continue
                    visited.add(next_board)
                    next_level.append(next_board)

            curr_level = next_level
            res += 1
        return -1


assert_value(3, Solution().minFlips, mat=[
    [0, 0],
    [0, 1]
])
assert_value(0, Solution().minFlips, mat=[
    [0]
])
assert_value(-1, Solution().minFlips, mat=[
    [1, 0, 0],
    [1, 0, 0]
])
assert_value(6, Solution().minFlips, mat=[
    [1, 1, 1],
    [1, 0, 1],
    [0, 0, 0]
])
