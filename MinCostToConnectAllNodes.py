'''
Min Cost to Connect All Nodes
https://leetcode.com/discuss/interview-question/356981/amazon-oa-2019-min-cost-to-connect-all-nodes
'''


def compute_min_cost(num_nodes, base_mst, poss_mst):
    sccs = {}
    cache = {}
    for e1, e2 in base_mst:
        if e1 in cache:
            scc = cache[e1]
        elif e2 in cache:
            scc = cache[e2]
        else:
            scc = set()
        cache[e1] = scc
        cache[e2] = scc
        scc.add(e1)
        scc.add(e2)
        scc = sorted(scc)
        sccs[''.join(str(i) for i in scc)] = scc

    res = 0
    for e1, e2, cost in poss_mst:
        if e1 in cache:
            scc = cache[e1]
        elif e2 in cache:
            scc = cache[e2]
        else:
            scc = set()
        if e1 not in cache:
            scc.add(e1)
            cache[e1] = scc
            res += cost
        elif e2 not in cache:
            scc.add(e2)
            cache[e2] = scc
            res += cost
        elif e1 in scc and e2 in scc:
            continue
        else:
            scc1 = cache[e1]
            scc2 = cache[e2]
            del sccs[''.join(str(i) for i in scc2)]
            for e in scc2:
                cache[e] = scc1
                scc1.add(e)

            res += cost
        scc = sorted(scc)
        sccs[''.join(str(i) for i in scc)] = scc

    if len(sccs) == 1:
        return res
    return -1


if __name__ == '__main__':
    n = 6
    edges = [[1, 4], [4, 5], [2, 3]]
    new_edges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
    print(compute_min_cost(n, edges, new_edges))
