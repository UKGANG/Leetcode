'''
210. Course Schedule II
https://leetcode.com/problems/course-schedule-ii/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        topology_graph = {}
        reversed_topology_graph = {}
        for course, pre in prerequisites:
            topology_graph[pre] = topology_graph.get(pre, set())
            reversed_topology_graph[course] = reversed_topology_graph.get(course, set())

            topology_graph[pre].add(course)
            reversed_topology_graph[course].add(pre)

        no_prerequisite_courses = [course for course in range(numCourses) if course not in reversed_topology_graph]

        res = []
        while no_prerequisite_courses:
            pre = no_prerequisite_courses.pop()
            res.append(pre)

            if pre not in topology_graph:
                continue
            for course in topology_graph[pre]:
                reversed_topology_graph[course].remove(pre)
                if not reversed_topology_graph[course]:
                    no_prerequisite_courses.append(course)

        return res if len(res) == numCourses else []


assert_value([0, 1], Solution().findOrder, numCourses=2, prerequisites=[[1, 0]])
assert_value([0, 2, 1, 3], Solution().findOrder, numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]])
assert_value([0], Solution().findOrder, numCourses=1, prerequisites=[])
assert_value([], Solution().findOrder, numCourses=2, prerequisites=[[0, 1], [1, 0]])
