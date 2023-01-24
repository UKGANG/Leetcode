"""
423. Reconstruct Original Digits from English
https://leetcode.com/problems/reconstruct-original-digits-from-english/description/
"""
from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        q = [
            [
                ('zero', '0', 'z'),
                ('two', '2', 'w'),
                ('four', '4', 'u'),
                ('six', '6', 'x'),
                ('eight', '8', 'g'),
            ], [
                ('seven', '7', 's'),
                ('three', '3', 't'),
            ], [
                ('five', '5', 'v'),
                ('one', '1', 'o'),
            ], [
                ('nine', '9', 'i'),
            ]
        ]

        res = []
        counter = Counter(s)
        for group in q:
            for word, num, hashcode in group:
                if not counter[hashcode]:
                    continue
                cnt = counter[hashcode]
                res.extend([num] * cnt)
                for c in word:
                    counter[c] -= cnt
        return ''.join(sorted(res))
