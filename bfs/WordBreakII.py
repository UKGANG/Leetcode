'''
140. Word Break II
https://leetcode.com/problems/word-break-ii/
'''
import collections
from collections import defaultdict
from typing import List

from test_tool import assert_value


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        max_word_len = len(max(wordDict, key=len))
        queue = collections.deque([(s, [])])
        res = []
        while queue:
            rest, solution = queue.popleft()
            for i in range(1, min(max_word_len, len(rest)) + 1):
                if rest[:i] not in wordDict:
                    continue
                solution_next = solution.copy()
                solution_next.append(rest[:i])
                if i == len(rest):
                    res.append(' '.join(solution_next))
                else:
                    queue.append((rest[i:], solution_next))

        return res


assert_value(["cats and dog", "cat sand dog"],
             Solution().wordBreak,
             s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"])
assert_value([],
             Solution().wordBreak,
             s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])
