'''
68. Text Justification
https://leetcode.com/problems/text-justification/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        space_left = maxWidth
        line_words = []
        for word in words:
            if space_left < len(word):
                res.append(self.format(line_words, maxWidth))
                space_left = maxWidth
                line_words.clear()
            line_words.append(word)
            space_left -= (len(word) + 1)
        if line_words:
            res.append(self.format([' '.join(line_words)], maxWidth))
        return res

    def format(self, line_words: List[str], maxWidth: int) -> str:
        if len(line_words) == 1:
            space = ' ' * (maxWidth - len(line_words[0]))
            return line_words[0] + space
        n_space = maxWidth - sum(len(word) for word in line_words)
        n_slot = len(line_words) - 1
        n_orphan = n_space % n_slot
        n_common_space = n_space // n_slot

        orphan_space = ' ' * (n_common_space + 1)
        common_space = ' ' * n_common_space
        res = ''
        for i in range(n_orphan):
            res += line_words[i]
            res += orphan_space
        for i in range(n_orphan, n_slot):
            res += line_words[i]
            res += common_space
        res += line_words[-1]
        return res


assert_value([
    "This    is    an",
    "example  of text",
    "justification.  "
], Solution().fullJustify, words=[
    "This", "is", "an", "example", "of", "text", "justification."
], maxWidth=16)

assert_value([
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
], Solution().fullJustify, words=[
    "What", "must", "be", "acknowledgment", "shall", "be"
], maxWidth=16)

assert_value([
    "Science  is  what we",
    "understand      well",
    "enough to explain to",
    "a  computer.  Art is",
    "everything  else  we",
    "do                  "
], Solution().fullJustify, words=[
    "Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is",
    "everything", "else", "we", "do"
], maxWidth=20)
