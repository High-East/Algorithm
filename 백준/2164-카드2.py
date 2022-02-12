# https://www.acmicpc.net/problem/2164

import sys
from collections import deque

N = int(sys.stdin.readline())
num_list = deque(range(1, N + 1))

while len(num_list) >= 2:
    num_list.popleft()
    num_list.rotate(-1)
print(num_list[0])


