'''
839. Similar String Groups
https://leetcode.com/problems/similar-string-groups/
'''
from typing import List

from test_tool import assert_value


class UnionFind:

    def __init__(self):
        self._cache = {}

    def create(self, target: str):
        self._cache[target] = [target, 0]

    def union(self, a: str, b: str):
        root_a, rank_a = self.find(a)
        root_b, rank_b = self.find(b)
        if root_a == root_b:
            return

        if rank_a == rank_b:
            self._cache[root_a][0] = root_b
            self._cache[root_b][1] += 1
            return

        if rank_a > rank_b:
            root_a, root_b = root_b, root_a

        self._cache[root_a][0] = root_b

    def find(self, a: str):
        while self._cache[a][0] != a:
            a = self._cache[a][0]
        return self._cache[a]


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        disjointed_set = UnionFind()
        for s in strs:
            disjointed_set.create(s)

        strs = sorted(strs)
        for i in range(len(strs) - 1):
            for j in range(i, len(strs)):
                s1, s2 = strs[i], strs[j]
                if sum(s1[k] != s2[k] for k in range(len(s1))) not in (0, 2):
                    continue
                disjointed_set.union(s1, s2)

        res = set()
        for s in strs:
            res.add(disjointed_set.find(s)[0])
        return len(res)


assert_value(2, Solution().numSimilarGroups, strs=["tars", "rats", "arts", "star"])
assert_value(1, Solution().numSimilarGroups, strs=["omv", "ovm"])
assert_value(3, Solution().numSimilarGroups, strs=["koqnn", "knnqo", "noqnk", "nqkon"])
assert_value(1, Solution().numSimilarGroups, strs=["jmijc", "imjjc", "jcijm", "cmijj", "mijjc"])
assert_value(2, Solution().numSimilarGroups,
             strs=["ufixvnxsdxalinayfaappbmmj", "nxpxiaauvyjxasbfmfinmdpla", "ujimiyxsaxpavnanfapmlbxdf",
                   "ufimvyxsaxpainanfapdlbxmj", "nxpyajaumxixalbfvpdnmasfi", "nxpxiaauvyjxpsbfmfinmdala",
                   "ufimvyxspxaainanfapdlbxmj", "nxpyaiaumxjxapbfvlanmdsfi", "ufimvyxspxapinanfaadlbxmj",
                   "nxpyaaauvxjxasbfmfinmdpli", "nxpyajaumxixapbfvlanmdsfi", "nxpyaaaumxjxasbfvfinmdpli",
                   "ufixvnbsdxalinayfamppxamj", "ujimvyxsaxpainanfapdlbxmf", "ufixvyxsdxalinanfaappbmmj",
                   "nxpyaaaumxjxapbfvlinmdsfi", "ufixvyxspxalinanfaadpbmmj", "nxpyaaaumxjxasbfvlinmdpfi",
                   "ufixvyxspxapinanfaadlbmmj", "ufixvnbsdxalinayfaappxmmj", "ufiavnbsdxxlinayfamppxamj",
                   "nxpyajaumxixapbfvldnmasfi", "ufiavnbsdxxlinayfamppxajm", "nxpyiaauvxjxasbfmfinmdpla",
                   "ujimiyxsaxpavnanfapdlbxmf"])
