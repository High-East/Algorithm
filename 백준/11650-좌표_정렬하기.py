# https://www.acmicpc.net/problem/11650

import sys

N = int(sys.stdin.readline())
num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
num_list = sorted(num_list, key=lambda x: (x[0], x[1]))
for num in num_list:
    print(*num, sep=' ')

