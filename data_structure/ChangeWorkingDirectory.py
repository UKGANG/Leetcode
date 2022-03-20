'''
Change Working Directory
https://leetcode.com/discuss/interview-question/553454/facebook-phone-change-working-directory
'''
from typing import List

from test_tool import assert_value


class Solution:
    def __init__(self):
        self._splitter = '/'

    def changeWorkingDirectory(self, curr_dir, change_command):
        if change_command.startswith('/'):
            return self.changeWorkingDirectory(change_command, '')

        stack = curr_dir.split('/')
        stack2 = change_command.split('/')

        for op in stack2:
            if '..' == op:
                if stack:
                    stack.pop()
            elif '.' == op:
                continue
            else:
                if op:
                    stack.append(op)

        return '/'.join(stack) if stack else '/'


assert_value("/facebook", Solution().changeWorkingDirectory, curr_dir="/", change_command='/facebook')
assert_value("/facebook/abc/def", Solution().changeWorkingDirectory, curr_dir="/facebook/anin",
             change_command='../abc/def')
assert_value("/", Solution().changeWorkingDirectory, curr_dir="/facebook/instagram", change_command='../../../../.')
