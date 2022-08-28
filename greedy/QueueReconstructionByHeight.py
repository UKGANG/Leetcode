'''
406. Queue Reconstruction by Height
https://leetcode.com/problems/queue-reconstruction-by-height/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = sorted(people, key=lambda item: (item[0], -item[1]), reverse=True)
        for i in range(len(people)):
            p = res[i]
            if i > p[1]:
                del res[i]
                res.insert(p[1], p)
        return res
