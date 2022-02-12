"""
https://www.acmicpc.net/problem/2606
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""

import sys
from collections import defaultdict


def dfs(node, visit):
    if node not in visit:
        visit[node] = True
        for next_node in sorted(graph[node]):
            dfs(next_node, visit)


if __name__ == '__main__':
    sys.stdin.readline()
    M = int(sys.stdin.readline())

    graph = defaultdict(list)

    for _ in range(M):
        s, e = map(int, sys.stdin.readline().split())
        graph[s].append(e)
        graph[e].append(s)

    visit = {}
    dfs(1, visit)
    print(len(visit) - 1)
