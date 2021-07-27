'''
819. Most Common Word
https://leetcode.com/problems/most-common-word/
'''
import re
from collections import Counter
from typing import List

from test_tool import assert_value


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[!?\',;.]', ' ', paragraph)
        cnts = Counter(paragraph.lower().split(' '))
        if '' in cnts:
            del cnts['']

        for word in banned:
            if word in cnts:
                del cnts[word]

        return sorted(cnts.items(), key=lambda item: item[1], reverse=True)[0][0]


assert_value('ball', Solution().mostCommonWord,
             paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",
             banned=["hit"])
assert_value('a', Solution().mostCommonWord,
             paragraph="a.",
             banned=[])
assert_value('b', Solution().mostCommonWord,
             paragraph="a, a, a, a, b,b,b,c, c",
             banned=["a"])
