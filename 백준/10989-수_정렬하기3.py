# https://www.acmicpc.net/problem/10989

import sys
from collections import defaultdict

N = int(sys.stdin.readline())
num_dict = defaultdict(int)

for _ in range(N):
    num_dict[int(sys.stdin.readline())] += 1

for num in sorted(num_dict):
    for _ in range(num_dict[num]):
        print(num)