'''
126. Word Ladder II
https://leetcode.com/problems/word-ladder-ii/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        parents = collections.defaultdict(list)
        curr_level = {beginWord}
        while curr_level:
            next_level = set()
            wordList -= curr_level
            for word in curr_level:
                for i in range(len(word)):
                    for c in range(ord('a'), ord('a')+26):
                        c = chr(c)
                        next_word = f'{word[:i]}{c}{word[i + 1:]}'
                        if next_word in wordList:
                            next_level.add(next_word)
                            parents[next_word].append(word)
            if endWord in next_level:
                break

            curr_level = next_level

        curr_level = [(endWord, [])]
        res = []

        while curr_level:
            prev_level = []
            for word, suffix in curr_level:
                if word == beginWord:
                    suffix.insert(0, word)
                    res.append(suffix)
                    continue
                for parent in parents[word]:
                    prev_suffix = suffix.copy()
                    prev_suffix.insert(0, word)
                    prev_level.append((parent, prev_suffix))
            if res:
                break
            curr_level = prev_level

        return res


assert_value([["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]],
             Solution().findLadders,
             beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"])
assert_value([],
             Solution().findLadders,
             beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"])
assert_value([["red", "ted", "tad", "tax"], ["red", "ted", "tex", "tax"], ["red", "rex", "tex", "tax"]],
             Solution().findLadders,
             beginWord="red", endWord="tax", wordList=["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"])
