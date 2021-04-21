'''
330. Patching Array
https://leetcode.com/problems/patching-array/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        covered = cnt = 0
        for num in nums:
            if num > covered + 1:
                cnt += 1
                covered = covered * 2 + 1
                if covered >= n:
                    return cnt
            covered += num
            if covered >= n:
                return cnt

        while covered < n:
            cnt += 1
            covered = covered * 2 + 1
        return cnt


assert_value(1, Solution().minPatches, nums=[1, 3], n=6)
assert_value(2, Solution().minPatches, nums=[1, 5, 10], n=20)
assert_value(0, Solution().minPatches, nums=[1, 2, 2], n=5)
