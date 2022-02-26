'''
Minimizing Permutations
https://leetcode.com/discuss/interview-question/1137426/Facebook-or-Minimizing-Permutations
'''
import collections

from test_tool import assert_value


def minOperations(arr):
    target = ''.join(str(c) for c in sorted(arr))
    curr = ''.join(str(c) for c in arr)
    q = collections.deque([(0, curr)])
    cache = set([curr])
    while q:
        cnt, curr = q.popleft()
        if curr == target:
            return cnt

        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1):
                new_p = f'{curr[:i]}{curr[i:j][::-1]}{curr[j:]}'
                if new_p in cache:
                    continue
                cache.add(new_p)
                q.append([cnt + 1, new_p])

    return -1


assert_value(2, minOperations, arr=(3, 1, 2))
assert_value(1, minOperations, arr=(1, 2, 5, 4, 3))
