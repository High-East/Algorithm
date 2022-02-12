# https://www.acmicpc.net/problem/2908

import sys

x, y = map(lambda x: x[::-1], sys.stdin.readline().split())

print(x) if x > y else print(y)