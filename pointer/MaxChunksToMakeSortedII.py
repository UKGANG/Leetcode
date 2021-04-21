'''
768. Max Chunks To Make Sorted II
https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if not arr:
            return 0

        sorted_arr = arr.copy()
        sorted_arr.sort()
        max_l = [None] * len(arr)
        max_l[0] = arr[0]
        for i in range(1, len(arr)):
            max_l[i] = max(max_l[i - 1], arr[i])

        cnt = 0
        min_r = max_l[-1] + 1
        for i in range(len(arr)):
            if max_l[~i] == sorted_arr[~i]:
                if sorted_arr[~i] > min_r:
                    continue

                cnt += 1
                min_r = arr[~i]

        return cnt


assert_value(1, Solution().maxChunksToSorted, arr=[5, 4, 3, 2, 1])
assert_value(4, Solution().maxChunksToSorted, arr=[2, 1, 3, 4, 4])
assert_value(4, Solution().maxChunksToSorted, arr=[2, 1, 4, 4, 3, 5, 7, 6])
