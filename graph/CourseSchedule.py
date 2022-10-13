'''
207. Course Schedule
https://leetcode.com/problems/course-schedule/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        required_course = collections.defaultdict(set)
        reversed_required_course = collections.defaultdict(set)
        for post, pre in prerequisites:
            required_course[post].add(pre)
            reversed_required_course[pre].add(post)

        available_courses = collections.deque([
            course for course in range(numCourses) if course not in required_course
        ])
        while available_courses:
            size = len(available_courses)
            for _ in range(size):
                pre = available_courses.popleft()
                numCourses -= 1
                for post in reversed_required_course[pre]:
                    required_course[post].remove(pre)
                    if not required_course[post]:
                        available_courses.append(post)

        return not numCourses
