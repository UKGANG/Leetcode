"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack():
            nonlocal cnt_open, cnt_close
            if len(curr) == n << 1:
                res.append(''.join(curr))
                return
            if cnt_open < n:
                curr.append('(')
                cnt_open += 1
                backtrack()
                cnt_open -= 1
                curr.pop()
            if cnt_close < cnt_open:
                curr.append(')')
                cnt_close += 1
                backtrack()
                cnt_close -= 1
                curr.pop()

        res = []
        curr = []
        cnt_open, cnt_close = 0, 0
        backtrack()
        return res
