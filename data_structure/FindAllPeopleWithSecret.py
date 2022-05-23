'''
2092. Find All People With Secret
https://leetcode.com/problems/find-all-people-with-secret/
'''
from collections import defaultdict
from typing import List

from test_tool import assert_value


class DisjointedSet:

    def __init__(self):
        self.parent = {}

    def create(self, x):
        self.parent[x] = x

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        if x not in self.parent:
            self.create(x)
        if y not in self.parent:
            self.create(y)
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.parent[root_y] = root_x


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings = sorted(meetings, key=lambda item: item[2])
        grouped_meeting = defaultdict(list)

        for x, y, t in meetings:
            grouped_meeting[t].append([x, y])

        res = set([0, firstPerson])
        for t, pair in sorted(grouped_meeting.items()):
            disjointed_set = DisjointedSet()
            disjointed_set.union(0, firstPerson)
            for x, y in pair:
                disjointed_set.union(x, y)
            group = defaultdict(set)
            for key in disjointed_set.parent.keys():
                group[disjointed_set.find(key)].add(key)

            for p in group.values():
                if p.intersection(res):
                    res.update(p)

        return list(res)


assert_value([0, 1, 2, 3, 5], Solution().findAllPeople,
             n=6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]],
             firstPerson=1)
assert_value([0, 1, 3], Solution().findAllPeople,
             n=4, meetings=[[3, 1, 3], [1, 2, 2], [0, 3, 3]],
             firstPerson=3)
assert_value([0, 1, 2, 3, 4], Solution().findAllPeople,
             n=5, meetings=[[3, 4, 2], [1, 2, 1], [2, 3, 1]],
             firstPerson=1)
assert_value([0, 1, 2, 3], Solution().findAllPeople,
             n=6, meetings=[[0, 2, 1], [1, 3, 1], [4, 5, 1]],
             firstPerson=1)
assert_value([0, 1, 4, 5], Solution().findAllPeople,
             n=1, meetings=[[5, 1, 4], [0, 4, 18]],
             firstPerson=1)
assert_value([0, 1, 3, 4], Solution().findAllPeople,
             n=5, meetings=[[1, 4, 3], [0, 4, 3]],
             firstPerson=3)
assert_value([0, 1, 4, 5, 6, 9, 11], Solution().findAllPeople,
             n=12, meetings=[
        [10, 8, 6], [9, 5, 11], [0, 5, 18], [4, 5, 13], [11, 6, 17], [0, 11, 10], [10, 11, 7], [5, 8, 3], [7, 6, 16],
        [3, 6, 10], [3, 11, 1], [8, 3, 2], [5, 0, 7], [3, 8, 20], [11, 0, 20], [8, 3, 4], [1, 9, 4], [10, 7, 11],
        [8, 10, 18]
    ],
             firstPerson=9)
assert_value([0, 1, 4], Solution().findAllPeople,
             n=6, meetings=[[4, 3, 5], [1, 4, 6], [3, 5, 7]],
             firstPerson=1)
