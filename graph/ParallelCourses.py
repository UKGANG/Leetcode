'''
1136. Parallel Courses
https://leetcode.com/problems/parallel-courses/
'''
import collections
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        res = 0
        class_left = n
        prequisites = collections.defaultdict(set)
        reversed_prequisites = collections.defaultdict(set)
        for pre, post in relations:
            prequisites[post].add(pre)
            reversed_prequisites[pre].add(post)

        queue = collections.deque(
            [class_number for class_number in range(1, n + 1) if class_number not in prequisites]
        )

        while queue:
            size = len(queue)
            class_left -= size
            res += 1
            for _ in range(size):
                class_number = queue.popleft()
                for next_class in reversed_prequisites[class_number]:
                    prequisites[next_class].remove(class_number)
                    if prequisites[next_class]:
                        continue
                    queue.append(next_class)
        return res if not class_left else -1
