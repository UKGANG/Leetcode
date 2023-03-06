"""
1328. Break a Palindrome
https://leetcode.com/problems/break-a-palindrome/
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            return ''
        strs = list(palindrome)
        found = False
        for i in range(len(strs) >> 1):
            if strs[i] != 'a':
                strs[i] = 'a'
                found = True
                break

        if found:
            return ''.join(strs)

        strs[-1] = 'b'
        return ''.join(strs)
