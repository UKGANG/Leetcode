'''
904. Fruit Into Baskets
https://leetcode.com/problems/fruit-into-baskets/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        counter = {}
        i, j = 0, 0
        res = 0
        while i < len(tree) and j < len(tree):
            if len(counter) < 2 or tree[j] in counter:
                res = max(res, j - i + 1)
                counter[tree[j]] = counter[tree[j]] + 1 if tree[j] in counter else 1
                j += 1
            else:
                counter[tree[i]] -= 1
                if counter[tree[i]] == 0:
                    del counter[tree[i]]
                i += 1

        return res


assert_value(3, Solution().totalFruit, tree=[1, 2, 1])
assert_value(3, Solution().totalFruit, tree=[0, 1, 2, 2])
assert_value(4, Solution().totalFruit, tree=[1, 2, 3, 2, 2])
assert_value(5, Solution().totalFruit, tree=[3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4])
