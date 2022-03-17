'''
953. Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {c: idx for idx, c in enumerate(order)}
        a_num = ord('a')
        words_num = []
        for word in words:
            word_num = []
            for idx, c in enumerate(word):
                word_num.append(chr(dictionary[c] + a_num))
            words_num.append(''.join(word_num))

        words_num_sorted = sorted(words_num)
        for i in range(len(words_num)):
            if words_num[i] != words_num_sorted[i]:
                return False
        return True


assert_value(True, Solution().isAlienSorted, words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz")
assert_value(False, Solution().isAlienSorted, words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz")
assert_value(False, Solution().isAlienSorted, words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz")
assert_value(True, Solution().isAlienSorted, words=["kuvp", "q"], order="ngxlkthsjuoqcpavbfdermiywz")
