"""
https://www.acmicpc.net/problem/1260
4 5 1
1 2
1 3
1 4
2 4
3 4
"""

import sys
from collections import defaultdict, deque


def dfs(node, visit):
    if node not in visit:
        print(node, end=' ')
        visit[node] = True
        for next_node in sorted(graph[node]):
            dfs(next_node, visit)


def bfs(node, visit):
    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        if node not in visit:
            print(node, end=' ')
            visit[node] = True
            for next_node in sorted(graph[node]):
                queue.append(next_node)


if __name__ == '__main__':
    N, M, V = map(int, sys.stdin.readline().split())

    graph = defaultdict(list)
    for _ in range(M):
        s, e = map(int, sys.stdin.readline().split())
        graph[s].append(e)
        graph[e].append(s)

    dfs(V, {})
    print("")
    bfs(V, {})
