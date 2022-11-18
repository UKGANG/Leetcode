'''
127. Word Ladder
https://leetcode.com/problems/word-ladder/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_hash = collections.defaultdict(set)
        hash_word = collections.defaultdict(set)

        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                word_hash_str = word[:i] + '_' + word[i + 1:]
                word_hash[word].add(word_hash_str)
                hash_word[word_hash_str].add(word)

        queue = collections.deque([beginWord])

        seen = set()
        res = 0
        while queue:
            res += 1
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                if word in seen:
                    continue
                seen.add(word)
                if word == endWord:
                    return res
                for hash_str in word_hash[word]:
                    for word_next in hash_word[hash_str]:
                        queue.append(word_next)
        return 0

    def _ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = [beginWord]
        word_hash = collections.defaultdict(set)
        hash_word = collections.defaultdict(list)
        wordList = set(wordList)
        wordList.add(beginWord)

        for word in wordList:
            for i in range(len(word)):
                word_hash[word].add(word[:i] + '_' + word[i + 1:])
        for word, hash_set in word_hash.items():
            for hash_idx in hash_set:
                hash_word[hash_idx].append(word)

        return self.bfs(queue, endWord, word_hash, hash_word)

    def bfs(self, queue, end_word, word_hash, hash_word):
        res = 0
        while queue:
            new_queue = []
            res += 1
            for word in queue:
                if word == end_word:
                    return res

                for hash_idx in word_hash[word]:
                    while hash_word[hash_idx]:
                        word_next = hash_word[hash_idx].pop()
                        if word == word_next:
                            continue
                        new_queue.append(word_next)
                del word_hash[word]
            queue = new_queue
        return 0


assert_value(5, Solution().ladderLength,
             beginWord="hit", endWord="cog",
             wordList=["hot", "dot", "dog", "lot", "log", "cog"])
assert_value(0, Solution().ladderLength,
             beginWord="hit", endWord="cog",
             wordList=["hot", "dot", "dog", "lot", "log"])
assert_value(0, Solution().ladderLength,
             beginWord="talk", endWord="tail",
             wordList=["talk", "tons", "fall", "tail", "gale", "hall", "negs"])
