'''
331. Verify Preorder Serialization of a Binary Tree
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        if len(nodes) < 3:
            if len(nodes) == 1 and nodes[0] == '#':
                return True
            return False
        if nodes[0] == '#':
            return False

        stack = [0]
        for node in nodes[1:]:
            if not stack:
                return False
            if node == "#":
                stack[-1] += 1
                while stack[-1] == 2:
                    stack.pop()
                    if not stack:
                        break
                    stack[-1] += 1
            else:
                stack.append(0)

        return not stack


assert_value(True, Solution().isValidSerialization, preorder="9,3,4,#,#,1,#,#,2,#,6,#,#")
assert_value(False, Solution().isValidSerialization, preorder="1,#")
assert_value(False, Solution().isValidSerialization, preorder="9,#,#,1")
assert_value(False, Solution().isValidSerialization, preorder="1,#,#,#,#")
assert_value(True, Solution().isValidSerialization, preorder="#")
