'''
2272. Substring With Largest Variance
https://leetcode.com/problems/substring-with-largest-variance/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def largestVariance(self, s: str) -> int:
        unique_c = ''.join(set(s))
        res = 0
        for i in range(len(unique_c) - 1):
            for j in range(i + 1, len(unique_c)):
                freq = []
                a, b = unique_c[i], unique_c[j]
                for c in s:
                    if c == a:
                        freq.append(1)
                    elif c == b:
                        freq.append(-1)
                res = max(res, self.max_sum(freq), self.max_sum([-n for n in freq]))
        return res

    def max_sum(self, nums: List[int]):
        max_so_far, max_here = 0, 0
        seen = False
        for n in nums:
            if n < 0:
                seen = True
            max_here += n
            if seen:
                max_so_far = max(max_so_far, max_here)
            else:
                max_so_far = max(max_so_far, max_here - 1)
            if max_here < 0:
                max_here = 0
                seen = False
        return max_so_far

    def _largestVariance(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            max_letter, min_letter = set(), set()
            cache = collections.Counter()
            for j in range(i, len(s)):
                cache[s[j]] += 1

                if s[j] in max_letter:
                    max_letter.remove(s[j])
                if s[j] in min_letter:
                    min_letter.remove(s[j])

                if not max_letter or cache[next(iter(max_letter))] < cache[s[j]]:
                    max_letter = set([s[j]])
                elif cache[next(iter(max_letter))] == cache[s[j]]:
                    max_letter.add(s[j])

                if not min_letter or cache[next(iter(min_letter))] > cache[s[j]]:
                    min_letter = set([s[j]])
                elif cache[next(iter(min_letter))] == cache[s[j]]:
                    min_letter.add(s[j])

                res = max(res, cache[next(iter(max_letter))] - cache[next(iter(min_letter))])
        return res


assert_value(0, Solution().largestVariance, s="ab")
assert_value(1, Solution().largestVariance, s="lripaa")
assert_value(1, Solution().largestVariance, s="lripaa")
assert_value(3, Solution().largestVariance, s="aababbb")
assert_value(0, Solution().largestVariance, s="abcde")
assert_value(18, Solution().largestVariance,
             s="srndawsjtkfjvkgrfqkovajfbvlhqpoxzmtffmlrwwevti"
               "xyksauepdilfyuabdundhlkrbmmeppxslyhnumekdqcsqp"
               "mlcjsyctqebxsbvpapbmlqhrddpdthaboqokljnlbtyaqp"
               "umlzncdjqazugsinxwhcmxvtuiclmjqcsbabuxadnivdvv"
               "rvxygxlrrlummxlnasjrkqbhtuutiakfkwmfbtoxqbzhhv"
               "dlkylxrtcfqgwhcxotklbvfpjmeshlxfzookpharvrgqmw"
               "odlhrwcoxgbkpkvxbdffczbqnjfvxyvijoiguvfjmadjph"
               "aworbwgmwiitphnaavpuywxepfdbygkbjiupvvpkdjfipj"
               "vrdtufofdyvzsecreyylsmxemucryrstlittgqpxaeurnx"
               "ukramvoxfdqqtnwrmnxdxgcxwfsewgqbfoqjc")
assert_value(16, Solution().largestVariance,
             s="xgknvjwxrdigcywnrwtxnidyvilnnqqgudwatezlfeoxse"
               "oebhorlmqsvlwgcsysbiwuzsmhqgemegdlxxjvfpdibgod"
               "cszuedmfwzjozaamrnwonsmotjvqrtqwvqowkmztrvzdfg"
               "sfvzwncwhdqiiewirxbbytqobgwjcbnitqakmxnvdhnrzm"
               "yyimxycfyuyidalctakeyzvsonafrzfsigubineyrtpyow"
               "hsdnhtdymsqcsepmqrqmnthrxoiddlbpzondpqxeqvltyx"
               "xebtwcitbqfniyvrfgtjmwnwygopjyhvhng")
