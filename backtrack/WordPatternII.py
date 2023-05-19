"""
291. Word Pattern II
https://leetcode.com/problems/word-pattern-ii
"""


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(idx_pattern, idx_s):
            if idx_pattern == len(pattern) and idx_s == len(s):
                return True
            if idx_pattern == len(pattern):
                return False
            if idx_s == len(s):
                return False

            pattern_char = pattern[idx_pattern]
            if pattern_char in identified_pattern:
                pattern_str = identified_pattern[pattern_char]
                if pattern_str == s[idx_s: idx_s + len(pattern_str)]:
                    return backtrack(idx_pattern + 1, idx_s + len(pattern_str))
                return False
            for idx_s_end in range(idx_s + 1, len(s) + 1):
                pattern_new = s[idx_s: idx_s_end]
                if pattern_new in existing_pattern_str:
                    continue
                identified_pattern[pattern_char] = pattern_new
                existing_pattern_str.add(pattern_new)
                if backtrack(idx_pattern + 1, idx_s_end):
                    return True
                del identified_pattern[pattern_char]
                existing_pattern_str.remove(pattern_new)
            return False

        existing_pattern_str = set()
        identified_pattern = {}
        return backtrack(0, 0)
