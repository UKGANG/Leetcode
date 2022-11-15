import itertools
from functools import lru_cache

from test_tool import assert_value


class Solution:
    def generate_string(self, numbers: str, target: int):
        @lru_cache(None)
        def dfs(l, r):
            if l + 1 == r:
                return [(numbers[l], str(numbers[l]))]

            res = []
            for i in range(l + 1, r):

                left_results = dfs(l, i)
                right_results = dfs(i, r)

                for (left_val, left_exp), (right_val, right_exp) in itertools.product(left_results, right_results):
                    res.append((left_val + right_val, f'({left_exp}+{right_exp})'))
                    res.append((left_val - right_val, f'({left_exp}-{right_exp})'))
                    res.append((left_val * right_val, f'({left_exp}*{right_exp})'))
            return res

        combinations = dfs(0, len(numbers))

        for combo in combinations:
            if combo[0] == target:
                return combo[-1]
        return None


assert_value('((-5*7)+(8*11))', Solution().generate_string, numbers=[-5, 7, 8, 11], target=53)
