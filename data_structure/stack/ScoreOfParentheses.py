"""
856. Score of Parentheses
https://leetcode.com/problems/score-of-parentheses
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        stack.append(0)
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                value = stack.pop();
                total = stack.pop();

                stack.append(total + max(1, value << 1))

        return stack.pop()
