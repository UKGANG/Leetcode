"""
336. Palindrome Pairs
https://leetcode.com/problems/palindrome-pairs/
"""
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def check(word):
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = []
        reverse_cache = {word: idx for idx, word in enumerate(words)}
        length_collection = sorted(list(set(len(word) for word in words)))
        if not length_collection[0]:
            del length_collection[0]
            for idx, word in enumerate(words):
                if not word:
                    continue
                if check(word):
                    res.append([idx, reverse_cache['']])
                    res.append([reverse_cache[''], idx])

            del reverse_cache['']

        left_word_cache = collections.defaultdict(list)
        right_word_cache = collections.defaultdict(list)
        for idx, word in enumerate(words):
            if not word:
                continue
            for length in length_collection:
                if length >= len(word):
                    continue

                left_prefix = word[:length]
                left_suffix = word[length:]
                right_prefix = word[:-length]
                right_suffix = word[-length:]

                if check(left_suffix):
                    left_word_cache[left_prefix].append(idx)
                if check(right_prefix):
                    right_word_cache[right_suffix].append(idx)

        for word_1_idx, word in enumerate(words):
            reversed_word = word[::-1]
            if reversed_word in reverse_cache and word_1_idx != reverse_cache[reversed_word]:
                res.append([word_1_idx, reverse_cache[reversed_word]])

            if reversed_word in left_word_cache:
                for word_2_idx in left_word_cache[reversed_word]:
                    res.append([word_2_idx, word_1_idx])

            if reversed_word in right_word_cache:
                for word_2_idx in right_word_cache[reversed_word]:
                    res.append([word_1_idx, word_2_idx])
        return res
