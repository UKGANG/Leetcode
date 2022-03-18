'''
1868 - Product of Two Run-Length Encoded Arrays
https://leetcode.ca/2021-07-17-1868-Product-of-Two-Run-Length-Encoded-Arrays/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def islandPerimeter(self, encoder1: List[List[int]], encoder2: List[List[int]]) -> List[List[int]]:
        l, r = 0, 0
        len_total = sum(seg[-1] for seg in encoder1)
        idx_1, idx_2 = 0, 0
        res = []
        while r < len_total:
            if encoder1[idx_1][-1] > encoder2[idx_2][-1]:
                idx_1, idx_2 = idx_2, idx_1
            r = encoder1[idx_1][-1]
            res.append([encoder1[idx_1][0] * encoder2[idx_1][0]] * (r - l))
            l = r + 1
            idx_1 += 1
        return res


assert_value([[6, 6]], Solution().islandPerimeter, encoded1=[[1, 3], [2, 3]], encoded2=[[6, 3], [3, 3]])
