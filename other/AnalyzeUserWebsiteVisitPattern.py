'''
1152. Analyze User Website Visit Pattern
https://leetcode.com/problems/analyze-user-website-visit-pattern/
'''
import collections, itertools
from typing import List

from test_tool import assert_value


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visit_log = collections.defaultdict(list)
        data = zip(username, timestamp, website)
        for u, t, w in sorted(data):
            visit_log[u].append(w)

        res = collections.Counter()
        seen = set()
        for usr, logs in visit_log.items():
            if len(logs) < 3:
                continue
            seen.clear()
            pattern = itertools.combinations(logs, 3)
            pattern = set(pattern)
            res.update(collections.Counter(pattern))

        return max(sorted(res), key=res.get)

    def _mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visit_log = collections.defaultdict(list)

        data = zip(username, timestamp, website)
        for u, t, w in sorted(data):
            visit_log[u].append(w)

        res = {}
        res_max = 0
        seen = set()
        for usr, logs in visit_log.items():
            if len(logs) < 3:
                continue
            seen.clear()
            for start in range(len(logs) - 2):
                for end in range(start + 2, len(logs)):
                    for mid in range(start + 1, end):
                        if ((logs[start], logs[mid], logs[end]) in seen):
                            continue
                        seen.add((logs[start], logs[mid], logs[end]))
                        res[(logs[start], logs[mid], logs[end])] = res.get((logs[start], logs[mid], logs[end]), 0)
                        res[(logs[start], logs[mid], logs[end])] += 1
                        res_max = max(res_max, res[(logs[start], logs[mid], logs[end])])

        return list(sorted(k for k, v in res.items() if v == res_max)[0])


assert_value(["home", "about", "career"], Solution().mostVisitedPattern,
             username=["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
             timestamp=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
             website=["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"])
assert_value(["a", "b", "a"], Solution().mostVisitedPattern,
             username=["ua", "ua", "ua", "ub", "ub", "ub"],
             timestamp=[1, 2, 3, 4, 5, 6],
             website=["a", "b", "a", "a", "b", "c"])
assert_value(["oz", "mryxsjc", "wlarkzzqht"], Solution().mostVisitedPattern,
             username=["zkiikgv", "zkiikgv", "zkiikgv", "zkiikgv"],
             timestamp=[436363475, 710406388, 386655081, 797150921],
             website=["wnaaxbfhxp", "mryxsjc", "oz", "wlarkzzqht"])
