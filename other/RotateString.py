'''
796. Rotate String
https://leetcode.com/problems/rotate-string/
'''


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        for i in range(n):
            if goal == s[i:] + s[:i]:
                return True

        return False
