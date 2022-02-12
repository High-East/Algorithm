import sys
from collections import deque

N = int(sys.stdin.readline())

queue = list()
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    queue.append((s, e, e - s))

queue.sort(key=lambda x: (x[0], x[2]))
queue = deque(queue)

res = 0
s, e, d = 0, 0, 0

while queue:
    c_s, c_e, c_d = queue.popleft()
    if c_s >= e:
        res += 1
        s, e, d = c_s, c_e, c_d
    elif c_e > e:
        pass
    elif c_d < d:
        s, e, d = c_s, c_e, c_d

print(res)