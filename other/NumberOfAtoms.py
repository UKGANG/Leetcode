'''
726. Number of Atoms
https://leetcode.com/problems/number-of-atoms/
'''
import re


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        token_regexp = r'([A-Z]{1}[a-z]*|\(|\)|\d+)'

        stack = []
        curr_cache = {}

        tokens = [token for token in re.split(token_regexp, formula) if token != '']
        idx = 0
        while idx < len(tokens):
            token = tokens[idx]
            if token == '(':
                stack.append(curr_cache)
                curr_cache = {}
            elif token == ')':
                n = 1
                if idx + 1 < len(tokens) and tokens[idx + 1].isdigit():
                    n = int(tokens[idx + 1])
                    idx += 1
                for k, v in curr_cache.items():
                    stack[-1][k] = stack[-1].get(k, 0) + v * n
                curr_cache = stack.pop()
            elif not token.isdigit():
                n = 1
                if idx + 1 < len(tokens) and tokens[idx + 1].isdigit():
                    n = int(tokens[idx + 1])
                    idx += 1
                curr_cache[token] = curr_cache.get(token, 0) + n
            else:
                continue
            idx += 1
        return ''.join(f'{k}{"" if v == 1 else v}' for k, v in sorted(curr_cache.items(), key=itemgetter(0)))
