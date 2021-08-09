'''
71. Simplify Path
https://leetcode.com/problems/simplify-path/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def __init__(self):
        self._splitter = '/'

    def simplifyPath(self, path: str) -> str:
        q = path.split(self._splitter)

        res = []
        for item in q:
            if '' == item:
                continue
            if '.' == item:
                continue
            if '..' == item:
                if len(res) > 0:
                    res.pop()
            else:
                res.append(item)

        return '/' + '/'.join(res)


assert_value("/home", Solution().simplifyPath, path="/home/")
assert_value("/", Solution().simplifyPath, path="/../")
assert_value("/home/foo", Solution().simplifyPath, path="/home//foo/")
assert_value("/c", Solution().simplifyPath, path="/a/./b/../../c/")
