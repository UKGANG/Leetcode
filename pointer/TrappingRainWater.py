'''
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def trap_v1(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)
        left[0] = height[0]
        right[-1] = height[-1]
        for idx in range(1, len(height)):
            left[idx] = max(left[idx - 1], height[idx])

        for idx in range(len(height) - 2, -1, -1):
            right[idx] = max(right[idx + 1], height[idx])

        res = 0
        for idx in range(1, len(height) - 1):
            res += (max(0, min(left[idx], right[idx]) - height[idx]))
        return res

    def trap(self, height: List[int]) -> int:
        left_idx = 0
        left_max = height[left_idx]
        right_idx = len(height) - 1
        right_max = height[right_idx]

        res = 0
        while left_idx < right_idx:
            if left_max > right_max:
                right_idx -= 1
                if height[right_idx] > right_max:
                    right_max = height[right_idx]
                else:
                    res += right_max - height[right_idx]
            else:
                left_idx += 1
                if height[left_idx] > left_max:
                    left_max = height[left_idx]
                else:
                    res += left_max - height[left_idx]

        return res


assert_value(6, Solution().trap, height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
assert_value(9, Solution().trap, height=[4, 2, 0, 3, 2, 5])
