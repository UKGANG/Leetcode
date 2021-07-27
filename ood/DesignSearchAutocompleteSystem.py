'''
642. Design Search Autocomplete System
https://leetcode.com/problems/design-search-autocomplete-system/
'''
import collections
import uuid
from typing import List

from test_tool import assert_value


class Tier:
    def __init__(self, c: str):
        self._c = c
        self._sentense_ids = []
        self._children = {}

    @property
    def char(self):
        return self._c

    @property
    def sentense_ids(self):
        return self._sentense_ids

    def has_child(self, c: str):
        return c in self._children

    def get_child(self, c: str):
        return self._children[c]

    def add_children(self, c: str):
        self._children[c] = Tier(c)


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self._top_k = 3
        self._terminate_char = '#'
        self._sentence_ids = {}
        self._id_sentences = {}
        self._id_times = collections.defaultdict(lambda: 0)
        self._root = Tier(None)
        self._buffer_tier = self._root
        self._buffer = ''
        for sentence, t in zip(sentences, times):
            self._cache_sentence(sentence.lower(), t)

    def _cache_sentence(self, sentence, t):
        curr_tier = self._root
        if sentence in self._sentence_ids:
            return

        uid = uuid.uuid4()
        self._id_sentences[uid] = sentence
        self._id_times[uid] = t
        for c in sentence:
            curr_tier.sentense_ids.append(uid)
            if not curr_tier.has_child(c):
                curr_tier.add_children(c)
            curr_tier = curr_tier.get_child(c)
        curr_tier.sentense_ids.append(uid)

    def input(self, c: str):
        if self._terminate_char == c:
            self._record_buffer()
            return []
        self._buffer += c
        res = []
        if self._buffer_tier:
            if self._buffer_tier.has_child(c):
                self._buffer_tier = self._buffer_tier.get_child(c)
                sids = [sid for sid in self._buffer_tier.sentense_ids]
                st_mapping = {sid: self._id_times[sid] for sid in sids}
                top_k_ids = sorted(st_mapping.items(), key=lambda item: item[1], reverse=True)[:self._top_k]
                top_k_ids = [sid for sid, t in top_k_ids]
                res = [self._id_sentences[sid] for sid in top_k_ids]

        return res

    def _record_buffer(self):
        if not self._buffer:
            return
        if self._buffer not in self._sentence_ids:
            self._cache_sentence(self._buffer, 1)
        else:
            uid = self._sentence_ids[self._buffer]
            self._id_times[uid] += 1
        self._buffer = ''
        self._buffer_tier = self._root


system = AutocompleteSystem(["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2])
print(system.input('i'))
print(system.input(' '))
print(system.input('a'))
print(system.input('#'))
print(system.input('i'))
print(system.input(' '))
print(system.input('a'))
