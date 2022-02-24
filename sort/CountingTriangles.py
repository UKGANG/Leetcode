'''
Counting Triangles
https://leetcode.com/discuss/interview-question/922155/facebook-recruiting-portal-counting-triangles
'''
from test_tool import assert_value


def countDistinctTriangles(arr):
    cnt = set([tuple(sorted(t)) for t in arr])
    return len(cnt)


assert_value(2, countDistinctTriangles, arr=[[2, 2, 3], [3, 2, 2], [2, 5, 6]])
assert_value(3, countDistinctTriangles, arr=[[8, 4, 6], [100, 101, 102], [84, 93, 173]])
