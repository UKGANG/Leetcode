'''
1606. Find Servers That Handled Most Number of Requests
https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
'''
import collections
import heapq
from typing import List

from test_tool import assert_value


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        n = len(arrival)
        cache = collections.defaultdict(lambda: [0, 0])
        for i in range(n):
            load[i] += arrival[i]

        for i in range(n):
            idx = i
            while arrival[i] < cache[idx % k][1]:
                idx += 1
                if idx == k + i:
                    idx = None
                    break
            if idx is None:
                continue
            cache[idx % k][0] += 1
            cache[idx % k][1] = load[i]

        server_cnt = []
        for idx, (cnt, _) in cache.items():
            heapq.heappush(server_cnt, (-cnt, idx))

        res = [idx for cnt, idx in server_cnt if cnt == server_cnt[0][0]]
        return res


assert_value([1], Solution().busiestServers,
             k=3,
             arrival=[1, 2, 3, 4, 5],
             load=[5, 2, 3, 3, 3])
assert_value([0], Solution().busiestServers,
             k=3,
             arrival=[1, 2, 3, 4],
             load=[1, 2, 1, 2])
assert_value([0, 1, 2], Solution().busiestServers,
             k=3,
             arrival=[1, 2, 3],
             load=[10, 12, 11])
assert_value([1], Solution().busiestServers,
             k=2,
             arrival=[1, 3, 5, 6, 7, 12],
             load=[3, 4, 6, 5, 5, 6])
assert_value([0], Solution().busiestServers,
             k=7,
             arrival=[1, 3, 4, 5, 6, 11, 12, 13, 15, 19, 20, 21, 23, 25, 31, 32],
             load=[9, 16, 14, 1, 5, 15, 6, 10, 1, 1, 7, 5, 11, 4, 4, 6])
