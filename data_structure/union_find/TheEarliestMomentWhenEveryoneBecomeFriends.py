'''
1101. The Earliest Moment When Everyone Become Friends
https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/
'''
from typing import List


class UnionFind:
    def __init__(self):
        self.cache = {}
        self.roots = set()

    def create(self, user_id):
        self.cache[user_id] = user_id
        self.roots.add(user_id)

    def find(self, user_id):
        while user_id != self.cache[user_id]:
            user_id = self.cache[user_id]
        return user_id

    def union(self, user_id_1, user_id_2, ts):
        root_user_id_1 = self.find(user_id_1)
        root_user_id_2 = self.find(user_id_2)

        if root_user_id_1 == root_user_id_2:
            return

        self.cache[root_user_id_2] = user_id_1
        if root_user_id_2 in self.roots:
            self.roots.remove(root_user_id_2)


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()

        union_find_set = UnionFind()
        for i in range(n):
            union_find_set.create(i)

        for ts, user_id_1, user_id_2 in logs:
            union_find_set.union(user_id_1, user_id_2, ts)
            if len(union_find_set.roots) == 1:
                return ts

        return -1
