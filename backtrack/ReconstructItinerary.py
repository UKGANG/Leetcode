'''
332. Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary/
'''
import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def backtrack(depature):
            if len(res) - 1 == len(tickets):
                return True

            for _ in range(len(routes[depature])):
                arrival = routes[depature].popleft()
                res.append(arrival)
                if backtrack(arrival):
                    return res
                routes[depature].append(res.pop())

        routes = collections.defaultdict(list)
        for depature, arrival in tickets:
            routes[depature].append(arrival)

        for depature in routes.keys():
            routes[depature] = collections.deque(sorted(routes[depature]))

        res = ['JFK']
        backtrack('JFK')
        return res
