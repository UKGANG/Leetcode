'''
1152. Analyze User Website Visit Pattern
https://leetcode.com/problems/analyze-user-website-visit-pattern/
'''
import collections
from operator import itemgetter
from typing import List, Optional, Tuple

from test_tool import assert_value


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        timestamp = [(t, idx) for idx, t in enumerate(timestamp)]
        timestamp = sorted(timestamp, key=itemgetter(0))
        visit_log = collections.defaultdict(list)
        for t, idx in timestamp:
            visit_log[username[idx]].append(website[idx])

        res = {}
        res_max = 0
        for usr, logs in visit_log.items():
            if len(logs) < 3:
                continue
            for i in range(2, len(logs)):
                res[(logs[i - 2], logs[i - 1], logs[i])] = res.get((logs[i - 2], logs[i - 1], logs[i]), 0)
                res[(logs[i - 2], logs[i - 1], logs[i])] += 1
                res_max = max(res_max, res[(logs[i - 2], logs[i - 1], logs[i])])

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
