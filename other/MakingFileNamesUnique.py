"""
1487. Making File Names Unique
https://leetcode.com/problems/making-file-names-unique/description/
"""
import collections
from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        counter = collections.Counter()
        seen = set()
        res = []
        for name in names:
            if name not in seen:
                seen.add(name)
                res.append(name)
                continue
            while True:
                counter[name] += 1
                new_name = f'{name}({counter[name]})'
                if new_name not in seen:
                    seen.add(new_name)
                    res.append(new_name)
                    break

        return res
