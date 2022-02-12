# https://www.acmicpc.net/problem/3052

import sys

x = set()
for _ in range(10):
    num = int(sys.stdin.readline())
    x = x | set([num % 42])
print(len(x))

