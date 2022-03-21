'''
827. Making A Large Island
https://leetcode.com/problems/making-a-large-island/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        group_size = {}
        group_ids = []
        for i in range(len(grid)):
            group_ids.append([0] * len(grid[0]))

        n_row = len(grid)
        n_col = len(grid[0])

        def bfs_mark(row, col, group_id):
            if group_ids[row][col]:
                return
            if not grid[row][col]:
                return

            # Mark
            group_ids[row][col] = group_id
            group_size[group_id] = group_size.get(group_id, 0) + 1

            bfs_mark(max(row - 1, 0), col, group_id)
            bfs_mark(row, max(col - 1, 0), group_id)
            bfs_mark(min(row + 1, n_row - 1), col, group_id)
            bfs_mark(row, min(col + 1, n_col - 1), group_id)

        idx = 0
        for i in range(n_row):
            for j in range(n_col):
                # If it is a new island
                if grid[i][j] and not group_ids[i][j]:
                    idx += 1
                    bfs_mark(i, j, idx)

        res = 0
        for i in range(n_row):
            for j in range(n_col):
                group_id = group_ids[i][j]
                if group_id:
                    res = max(res, group_size[group_id])
                else:
                    group_top = group_ids[i + 1][j] if i + 1 < n_row else None
                    group_bottom = group_ids[i - 1][j] if i > 0 else None
                    group_left = group_ids[i][j - 1] if j > 0 else None
                    group_right = group_ids[i][j + 1] if j + 1 < n_col else None

                    group_neighbors = set()
                    group_neighbors.add(group_top)
                    group_neighbors.add(group_bottom)
                    group_neighbors.add(group_left)
                    group_neighbors.add(group_right)

                    neighbor_size = [group_size.get(group_id, 0) for group_id in group_neighbors if group_id]

                    new_size = sum(neighbor_size) + 1
                    res = max(res, new_size)

        return res


assert_value(3, Solution().largestIsland, grid=[[1, 0], [0, 1]])
assert_value(4, Solution().largestIsland, grid=[[1, 1], [1, 0]])
assert_value(4, Solution().largestIsland, grid=[[1, 1], [1, 1]])
assert_value(1, Solution().largestIsland, grid=[[0, 0], [0, 0]])
assert_value(1, Solution().largestIsland, grid=[[0, 0, 0], [0, 0, 0], [0, 0, 0]])
assert_value(18, Solution().largestIsland, grid=[
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0]
])
