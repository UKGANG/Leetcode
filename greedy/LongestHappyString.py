"""
1405. Longest Happy String
https://leetcode.com/problems/longest-happy-string/
"""
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        queue = []
        if a:
            heapq.heappush(queue, [-a, 'a'])
        if b:
            heapq.heappush(queue, [-b, 'b'])
        if c:
            heapq.heappush(queue, [-c, 'c'])

        res = []
        while queue:
            pair_1 = heapq.heappop(queue)

            if len(res) > 1 and res[-1] == res[-2] == pair_1[1]:
                if not queue:
                    break
                pair_2 = heapq.heappop(queue)
                res.append(pair_2[1])
                pair_2[0] += 1
                if pair_2[0]:
                    heapq.heappush(queue, pair_2)

            res.append(pair_1[1])
            pair_1[0] += 1
            if pair_1[0]:
                heapq.heappush(queue, pair_1)

        return ''.join(res)
