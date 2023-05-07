"""
311. Sparse Matrix Multiplication
https://leetcode.com/problems/sparse-matrix-multiplication
"""
import collections
import itertools
from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m1, n1 = len(mat1), len(mat1[0])
        m2, n2 = len(mat2), len(mat2[0])

        res = [
            [0] * n2
            for _ in range(m1)
        ]

        mat1_list = collections.defaultdict(list)
        mat2_list = collections.defaultdict(list)

        for x, y in itertools.product(range(m1), range(n1)):
            if mat1[x][y] == 0:
                continue
            mat1_list[x].append((y, mat1[x][y]))
        for x, y in itertools.product(range(m2), range(n2)):
            if mat2[x][y] == 0:
                continue
            mat2_list[x].append((y, mat2[x][y]))

        for x, row in mat1_list.items():
            for k, val1 in row:
                for y, val2 in mat2_list[k]:
                    res[x][y] += val1 * val2

        return res

    def _optimized_multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m1, n1 = len(mat1), len(mat1[0])
        m2, n2 = len(mat2), len(mat2[0])

        res = [
            [0] * n2
            for _ in range(m1)
        ]

        for i in range(m1):
            for k in range(n1):
                if mat1[i][k] == 0:
                    continue
                for j in range(n2):
                    res[i][j] += mat1[i][k] * mat2[k][j]
        return res

    def _naive_multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m1, n1 = len(mat1), len(mat1[0])
        m2, n2 = len(mat2), len(mat2[0])

        res = [
            [0] * n2
            for _ in range(m1)
        ]

        for i in range(m1):
            for j in range(n2):
                for k in range(n1):
                    res[i][j] += mat1[i][k] * mat2[k][j]

        return res
