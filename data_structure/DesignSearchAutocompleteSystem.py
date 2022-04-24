'''
642. Design Search Autocomplete System
https://leetcode.com/problems/design-search-autocomplete-system/
'''
import heapq
from typing import List

from test_tool import assert_value


class Trie:
    def __init__(self):
        self.sub_trie = {}
        self.cnt = 0
        self.end = False

    def add(self, word, time):
        trie = self.sub_trie.get(word[0], Trie())
        self.sub_trie[word[0]] = trie
        if len(word) > 1:
            trie.add(word[1:], time)
        else:
            trie.end = True
            trie.cnt += time

    def top_3(self):
        h = []
        if self.end:
            h.append((-self.cnt, ''))
        for prefix, trie in self.sub_trie.items():
            top_3 = trie.top_3()
            for suffix, cnt in top_3:
                heapq.heappush(h, (-cnt, prefix + suffix))
        res = []
        while h:
            cnt, word = heapq.heappop(h)
            res.append((word, -cnt))
            if len(res) == 3:
                return res
        return res


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self._root_trie = Trie()
        for sentence, time in zip(sentences, times):
            self._root_trie.add(sentence, time)

        self._curr_trie = self._root_trie
        self._curr_prefix = ''

    def input(self, c: str) -> List[str]:
        if c == '#':
            self._curr_trie = self._root_trie
            self._curr_trie.add(self._curr_prefix, 1)
            self._curr_prefix = ''
            return None
        self._curr_prefix += c
        if c not in self._curr_trie.sub_trie:
            self._curr_trie.sub_trie[c] = Trie()
        self._curr_trie = self._curr_trie.sub_trie[c]
        return [self._curr_prefix + word for word, cnt in self._curr_trie.top_3()]


# Your AutocompleteSystem object will be instantiated and called as such:
sentences = ["i love you", "island", "iroman", "i love leetcode"]
times = [5, 3, 2, 2]
obj = AutocompleteSystem(sentences, times)
res_1 = obj.input('i')
res_2 = obj.input(' ')
res_3 = obj.input('a')
res_4 = obj.input('#')

res_1 = obj.input('i')
res_2 = obj.input(' ')
res_3 = obj.input('a')
res_4 = obj.input('#')

res_1 = obj.input('i')
res_2 = obj.input(' ')
res_3 = obj.input('a')
res_4 = obj.input('#')
