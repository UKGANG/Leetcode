'''
414. Third Maximum Number
https://leetcode.com/problems/third-maximum-number/
'''
import heapq
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        queue = []
        for num in nums:
            if num in queue:
                continue
            heapq.heappush(queue, num)
            if len(queue) == 4:
                heapq.heappop(queue)
        return queue[0] if len(queue) == 3 else queue[-1]
