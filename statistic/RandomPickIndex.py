'''
398. Random Pick Index
https://leetcode.com/problems/random-pick-index/
'''
import random
from typing import List

from test_tool import assert_value


class Solution:

    # def __init__(self, nums: List[int]):
    #     self.cache = {}
    #     for idx, num in enumerate(nums):
    #         if num not in self.cache:
    #             self.cache[num] = [0, [idx]]
    #         else:
    #             self.cache[num][1].append(idx)
    #
    # def pick(self, target: int) -> int:
    #     idx = self.cache[target][0]
    #     res = self.cache[target][1][idx]
    #     self.cache[target][0] = (idx + 1) % len(self.cache[target][1])
    #     return res

    def __init__(self, nums: List[int]):
        self.cache = {}
        for idx, num in enumerate(nums):
            if num not in self.cache:
                self.cache[num] = [idx]
            else:
                self.cache[num].append(idx)

    def pick(self, target: int) -> int:
        arr = self.cache[target]
        cnt = 0
        for idx in arr:
            rnd = random.randint(0, cnt)
            if rnd == 0:
                res = idx
            cnt += 1

        return res


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3, 3, 3])

assert_value(2, obj.pick, target=3)
assert_value(3, obj.pick, target=3)
assert_value(4, obj.pick, target=3)
