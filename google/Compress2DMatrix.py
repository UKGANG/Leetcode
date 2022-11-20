import collections
import itertools


def compress_2D_array_followup(arr):
    m, n = len(arr), len(arr[0])
    graph = collections.defaultdict(set)
    cnt = {(x, y): 0 for x, y in itertools.product(range(m), range(n))}

    for i in range(m):
        row_sorted = sorted(range(n), key=lambda col: arr[i][col])
        for j in range(n - 1):
            graph[(i, row_sorted[j])].add((i, row_sorted[j + 1]))
            cnt[(i, row_sorted[j + 1])] += 1

    for j in range(n):
        col_sorted = sorted(range(m), key=lambda row: arr[row][j])
        for i in range(m - 1):
            graph[(col_sorted[i], j)].add((col_sorted[i + 1], j))
            cnt[(col_sorted[i + 1], j)] += 1

    queue = collections.deque([
        pos for pos, val in cnt.items() if val == 0
    ])

    rank = 0
    while queue:
        size = len(queue)
        rank += 1
        for _ in range(size):
            x1, y1 = queue.pop()
            arr[x1][y1] = rank
            for x2, y2 in graph[(x1, y1)]:
                cnt[x2, y2] -= 1
                if not cnt[x2, y2]:
                    queue.append((x2, y2))
    return arr


A = [[7, 6], [4, 9]]
res = compress_2D_array_followup(A)
print(res)
