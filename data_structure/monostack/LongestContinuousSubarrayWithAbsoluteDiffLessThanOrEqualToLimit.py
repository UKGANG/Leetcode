'''
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = collections.deque()
        min_q = collections.deque()

        res = 0
        left = 0
        for right, num in enumerate(nums):
            while max_q and max_q[-1] < num:
                max_q.pop()
            while min_q and min_q[-1] > num:
                min_q.pop()

            min_q.append(num)
            max_q.append(num)

            while max_q[0] - min_q[0] > limit:
                if nums[left] == max_q[0]:
                    max_q.popleft()
                elif nums[left] == min_q[0]:
                    min_q.popleft()
                left += 1

            res = max(res, right - left + 1)

        return res


assert_value(2, Solution().longestSubarray, nums=[8, 2, 4, 7], limit=4)
assert_value(4, Solution().longestSubarray, nums=[10, 1, 2, 4, 7, 2], limit=5)
assert_value(3, Solution().longestSubarray, nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0)
