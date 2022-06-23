'''
937. Reorder Data in Log Files
https://leetcode.com/problems/reorder-data-in-log-files/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        numeric_list = []
        letter_list = []
        for log in logs:
            idx = log.index(" ")
            if log[idx + 1].isnumeric():
                numeric_list.append(log)
                continue
            letter_list.append((log[idx + 1:], log[:idx]))
        letter_list = sorted(letter_list)
        letter_list = [f'{log_item[1]} {log_item[0]}' for log_item in letter_list]
        letter_list.extend(numeric_list)
        return letter_list


assert_value(
    ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"],
    Solution().reorderLogFiles,
    logs=["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
)
assert_value(
    ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"],
    Solution().reorderLogFiles,
    logs=["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
)
