"""
There are N students who applied to perform on stage,
but there is a interesting regulation that the height difference between highest and shortest students on stages
should be no more than K.
Please output the possible maximum number of students who can make a performance on stage.
Input
Heights : an array of students’ heights ,0<=heights[i]<=10^9, 0<=N=len(heights)<=10^5
K: an integer (0<=K<=10^9)
Output
The maximum number of students
"""
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def maxStudent(self, heights: List[int], k) -> int:
        queue = collections.deque()
        heights.sort()
        res = 0
        for height in \
                heights:
            while queue and height - queue[0] > k:
                queue.popleft()
            queue.append(height)
            res = max(res, len(queue))

        return res


assert_value(3, Solution().maxStudent, heights=[5, 5, 5, 4, 6, 7, 1, 2], k=0)
