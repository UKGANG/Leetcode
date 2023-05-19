"""
214. Shortest Palindrome
https://leetcode.com/problems/shortest-palindrome
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        s_reversed = s[::-1]
        s_connected = f'{s}#{s_reversed}'
        j = 0
        jump_cache = [0] * len(s_connected)

        for i in range(1, len(s_connected)):
            while j > 0 and s_connected[j] != s_connected[i]:
                j = jump_cache[j - 1]
            if s_connected[j] == s_connected[i]:
                j += 1
            jump_cache[i] = j
        print(jump_cache[-1])
        return s_reversed[:-jump_cache[-1]] + s

    def _bf_shortestPalindrome(self, s: str) -> str:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        candidate_idx = [0]
        for i in range(1, len(s)):
            if s[i] == s[0]:
                candidate_idx.append(i)

        for i in range(len(candidate_idx) - 1, -1, -1):
            if is_palindrome(0, candidate_idx[i]):
                right = candidate_idx[i]
                break
        return s[:right:-1] + s
