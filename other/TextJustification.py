'''
68. Text Justification
https://leetcode.com/problems/text-justification/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        cnt_left = maxWidth
        for word in words:
            if cnt_left < len(word):
                self.format(cnt_left, res, line)
                cnt_left = maxWidth

            cnt_left = cnt_left - len(word) - 1
            line.append(word)

        self.format(cnt_left, res, line, True)

        return res

    def format(self, cnt_left, res, line, last=False):
        space_cnt = cnt_left + len(line)

        if len(line) > 1 and not last:
            space_even = int(space_cnt / (len(line) - 1))
            space_res = space_cnt % (len(line) - 1)
            line_str = line[0]
            for i in range(space_res):
                line_str += ' ' * (space_even + 1) + line[i + 1]
            for i in range(len(line) - 1 - space_res):
                line_str += ' ' * space_even + line[i + 1 + space_res]
        else:
            line_str = ' '.join(line)
            line_str += ' ' * (cnt_left + 1)

        res.append(line_str)
        line.clear()


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
