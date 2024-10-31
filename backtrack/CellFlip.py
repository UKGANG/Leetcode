'''
You have a grid filled with blue and white cells.
Blue cells are dead if they are not connected to the border by other blue cells.
Can you write an algorithm turning the dead blue cells into white?
'''
from typing import List, Set, Tuple, Union, NoReturn
import itertools


"""
Blue cells: 1
White cells: 0
"""
def is_dead_cell(grid: List[List[int]], x: int, y: int, from_upper_left) -> bool:
    m, n = len(grid), len(grid[0])
    if grid[x][y] == 0:
        return False
    if x == 0 or x == m - 1:
        return False
    if y == 0 or y == n - 1:
        return False
    coordinations = [[-1, 0], [0, -1]]
    if not from_upper_left:
        coordinations = [[1, 0], [0, 1]]
    for dx, dy in coordinations:
        _x, _y = x + dx, y + dy
        if grid[_x][_y] == 1:
            return False
    return True


def activate_cells(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    # 1. For each cells, mark each dead cells as 2
    for x, y in itertools.product(range(m), range(n)):
        if is_dead_cell(grid, x, y, True):
            grid[x][y] = 2

    for x, y in itertools.product(range(m - 1, -1, -1), range(n - 1, -1, -1)):
        if is_dead_cell(grid, x, y, False):
            grid[x][y] = 2

    def backtrack(grid: List[List[int]], x: int, y: int) -> bool:
        if x == 0 or x == m - 1:
            return True
        if y == 0 or y == n - 1:
            return True

        original_color = grid[x][y]
        grid[x][y] = 1
        flipped.add((x, y))
        for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1]):
            _x, _y = x + dx, y + dy
            if (_x, _y) in flipped:
                continue
            if grid[_x][_y] == 1:
                return True
            if backtrack(grid, _x, _y):
                return True

        flipped.remove((x, y))
        grid[x][y] = original_color
        return False

    # 2. Backtrack the flipping road
    flipped = set()
    for x, y in itertools.product(range(m), range(n)):
        if grid[x][y] == 2:
            backtrack(grid, x, y)
    return grid


"""
Optimized version using Union Find
1. Group cells by the union find architecture
2. Mark dead groups
3. Backtrack each cells similar to the previous approach
"""


class UnionFind:
    def __init__(self):
        self._cache = {}
        self._dead_roots = []

    def create(self, x: int, y: int) -> NoReturn:
        self._cache[(x, y)] = (x, y)

    def find(self, x: int, y: int) -> Tuple[int]:
        """
        Retrieve the root of the cluster
        """
        while self._cache[(x, y)] != (x, y):
            x, y = self._cache[(x, y)]
        return x, y

    def union(self, x1: int, y1: int, x2: int, y2: int) -> NoReturn:
        x1_root, y1_root = self.find(x1, y1)
        x2_root, y2_root = self.find(x2, y2)
        if (x1_root, y1_root) != (x2_root, y2_root):
            self._cache[(x1_root, y1_root)] = (x2_root, y2_root)

    def mark_dead_group(self, grid: List[List[int]], x: int, y: int, seen: Set[Tuple[int]]) -> int:
        is_dead = True
        coordinations = [(x, y)]
        if x == 0 or x == m - 1:
            dead = False
        if y == 0 or y == n - 1:
            dead = False
        seen.add((x, y))
        while self._cache[(x, y)] != (x, y):
            x, y = self._cache[(x, y)]
            seen.add((x, y))
            coordinations.append((x, y))
            if x == 0 or x == m - 1:
                dead = False
            if y == 0 or y == n - 1:
                dead = False
        if is_dead:
            dead_root = [x, y, []]
            self._dead_roots.append(dead_root)
            for x, y in coordinations:
                dead_root[-1].append((x, y))
                grid[x][y] = 2

        @property
        def dead_roots(self) -> List[Union[int, List[int]]]:
            return self._dead_roots


def activate_cells_v2(grid: List[List[int]]) -> List[List[int]]:
    disjointed_set = UnionFind()
    # 1. Group cells
    for x, y in itertools.product(range(m), range(n)):
        if grid[x][y] == 1:
            disjointed_set.create(x, y)
    for x, y in itertools.product(range(m), range(n)):
        if grid[x][y] != 1:
            continue
        if x > 0:
            if grid[x - 1][y] == 1:
                disjointed_set.union(x - 1, y, x, y)
        if y > 0:
            if grid[x][y - 1] == 1:
                disjointed_set.union(x, y - 1, x, y)

    # 2. mark dead groups
    seen = set()
    for x, y in itertools.product(range(m), range(n)):
        if (x, y) in seen:
            continue
        if grid[x][y] == 0:
            continue
        disjointed_set.mark_dead_group(grid, x, y, seen)

    # 3. Activate each groups
    def backtrack(grid: List[List[int]], x: int, y: int) -> bool:
        if x == 0 or x == m - 1:
            return True
        if y == 0 or y == n - 1:
            return True

        original_color = grid[x][y]
        grid[x][y] = 1
        flipped.add((x, y))
        for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1]):
            _x, _y = x + dx, y + dy
            if (_x, _y) in flipped:
                continue
            if grid[_x][_y] == 1:
                return True
            if backtrack(grid, _x, _y):
                return True

        flipped.remove((x, y))
        grid[x][y] = original_color
        return False

    # 3.1 Itearate over each groups
    for x, y, nodes in disjointed_set.dead_roots:
        backtrack(grid, x, y)
        for x, y in nodes:
            grid[x][y] == 1
