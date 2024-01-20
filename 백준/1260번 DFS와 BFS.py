from collections import defaultdict, deque

n, m, v = map(int, input().split())
arr = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)


def dfs(graph, start, visited=[]):
    if start not in visited:
        visited.append(start)
        print(start, end=" ")
        for node in sorted(graph[start]):
            dfs(graph, node, visited)


def bfs(graph, start):
    queue = deque([start])
    visited = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            print(node, end=" ")
            for x in sorted(graph[node]):
                queue.append(x)


dfs(arr, v)
print("")
bfs(arr, v)
