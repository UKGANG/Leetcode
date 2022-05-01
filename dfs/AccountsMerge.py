'''
721. Accounts Merge
https://leetcode.com/problems/accounts-merge/
'''
import collections
from typing import List

from test_tool import assert_value


class Account:
    def __init__(self, account_list: List[str]):
        self.name = account_list[0]
        self.emails = account_list[1:]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        for account in accounts:
            account = Account(account)
            for email in account.emails:
                graph[email].add(account)

        visited = set()

        def dfs(graph, visited, account, res_usr):
            if account in visited:
                return
            visited.add(account)
            for email in account.emails:
                res_usr.add(email)
                for neighbor_account in graph[email]:
                    dfs(graph, visited, neighbor_account, res_usr)

        res = []
        for account in accounts:
            res_usr = set()
            account = next(iter(graph[account[1]]))
            dfs(graph, visited, account, res_usr)
            if res_usr:
                res.append([account.name, *sorted(res_usr)])

        return res

    def _accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts = [[account[0], set(account[1:])] for account in accounts]
        res = []
        for account in accounts:
            emails = list(account[1])
            for email in emails:
                for merged in res:
                    if email in merged[1]:
                        emails.extend(merged[1])
                        res.remove(merged)

            account[1] = set(emails)
            res.append(account)

        return [[account[0], *sorted(list(account[1]), reverse=False)] for account in res]


assert_value([["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"],
              ["John", "johnnybravo@mail.com"]], Solution().accountsMerge,
             accounts=[["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                       ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                       ["John", "johnnybravo@mail.com"]])
assert_value(
    [["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"], ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
     ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"], ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
     ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"]], Solution().accountsMerge,
    accounts=[["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
              ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
              ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
              ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
              ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]])
assert_value(
    [["David", "David0@m.co", "David1@m.co", "David2@m.co", "David3@m.co", "David4@m.co", "David5@m.co"]],
    Solution().accountsMerge,
    accounts=[["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
              ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
              ["David", "David1@m.co", "David2@m.co"]])
