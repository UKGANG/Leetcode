'''
About KMP algorithm
http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
'''
from collections import defaultdict, Counter

from test_tool import assert_value


class Solution:
    def kmp(self, text: str, keyword: str) -> int:
        match_dict = []
        for i in range(1, len(keyword) + 1):
            keyword_chunk = keyword[:i]
            cnt = Counter()
            for j in range(1, len(keyword_chunk)):
                cnt[keyword_chunk[:j]] += 1
                cnt[keyword_chunk[-j:]] += 1

            cnt = {k: v for k, v in cnt.items() if v > 1}
            match_len = 0
            if len(cnt) > 0:
                match_len = len(sorted(cnt.items(), key=lambda item: len(item[0]))[0][0])
            match_dict.append(match_len)

        keyword_len = len(keyword)
        text_len = len(text)
        i = 0
        while i < text_len:
            if text_len - i < keyword_len:
                return -1
            text_chunk = text[i:i+keyword_len]

            matched = True
            for j in range(keyword_len):
                if keyword[j] != text_chunk[j]:
                    if j == 0:
                        i += 1
                    else:
                        i += keyword_len - 1 - match_dict[j-1]
                    matched = False
                    break

            if matched:
                return i

        return -1


assert_value(15, Solution().kmp, text="BBC ABCDAB ABCDABCDABDE", keyword="ABCDABD")
assert_value(0, Solution().kmp, text="AABAACAADAABAABA", keyword="AABA")
assert_value(10, Solution().kmp, text="THIS IS A TEST TEXT", keyword="TEST")
