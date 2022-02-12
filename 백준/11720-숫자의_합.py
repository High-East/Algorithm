# https://www.acmicpc.net/problem/11720

import sys

sys.stdin.readline()
numbers = sys.stdin.readline().rstrip()
res = 0

for num in numbers:
    res += int(num)
print(res)