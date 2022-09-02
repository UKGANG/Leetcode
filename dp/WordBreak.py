'''
139. Word Break
https://leetcode.com/problems/word-break/
'''
import collections
import functools
from typing import List

from test_tool import assert_value


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @functools.lru_cache()
        def backtrack(idx):
            if idx == len(s):
                return True

            for word, length in wordDict:
                if s[idx:idx + length] != word:
                    continue
                if backtrack(idx + length):
                    return True
            return False

        wordDict = [(word, len(word)) for word in wordDict]
        return backtrack(0)

    def _wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = [(word, len(word)) for word in wordDict]

        curr_level = collections.deque([0])
        visited = set([0])
        while curr_level:
            size = len(curr_level)
            for _ in range(size):
                curr = curr_level.popleft()
                for word, length in wordDict:
                    if curr + length in visited:
                        continue
                    if s[curr:curr + length] != word:
                        continue
                    if curr + length == len(s):
                        return True
                    visited.add(curr + length)
                    curr_level.append(curr + length)
        return False

    def __wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = [(word, len(word)) for word in wordDict]

        m, n = len(wordDict), len(s)

        dp = [False] * (n + 1)

        dp[0] = True

        for j in range(1, n + 1):
            for i in range(m):
                if wordDict[i][1] > j:
                    continue
                if dp[j]:
                    continue
                dp[j] = s[j - wordDict[i][1]: j] == wordDict[i][0] and dp[j - wordDict[i][1]]
                if j == len(s) and dp[j]:
                    return True
        return False
