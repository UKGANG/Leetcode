'''
239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        for i in range(len(nums)):
            if q and q[0] <= i - k:
                q.popleft()
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

            if i >= k - 1:
                res.append(nums[q[0]])

        return res


assert_value([7, 4], Solution().maxSlidingWindow, nums=[7, 2, 4], k=2)
assert_value([3, 3, 5, 5, 6, 7], Solution().maxSlidingWindow, nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)
assert_value([1], Solution().maxSlidingWindow, nums=[1], k=1)
assert_value([1, -1], Solution().maxSlidingWindow, nums=[1, -1], k=1)
