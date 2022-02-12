# https://www.acmicpc.net/problem/10816
# Success

import sys
from collections import Counter

N = int(input())
arr = map(int, sys.stdin.readline().split())
counter = Counter(arr)

input()
answer = []
for num in list(map(int, sys.stdin.readline().split())):
    answer.append(counter.get(num, 0))
print(*answer)
