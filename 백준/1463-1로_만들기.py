##
# 성공: tabulation
import sys

X = int(sys.stdin.readline())

cache = {}

for x in range(1, X + 1):
    if x == 1:
        cache[x] = 0
        continue

    x2_list = []
    if x % 3 == 0:
        x2_list.append(x // 3)
    if x % 2 == 0:
        x2_list.append(x // 2)
    x2_list.append(x - 1)

    cache[x] = min([cache[x2] for x2 in x2_list]) + 1

print(cache[X])


##
# 실패: 메모리 초과

import sys
sys.setrecursionlimit(10000000)

def func(x, memo):
    if x == 1:
        return 0
    if x in memo:
        return memo[x]
    x2_list = []
    if x % 3 == 0:
        x2_list.append(x // 3)
    elif x % 2 == 0:
        x2_list.append(x // 2)
    x2_list.append(x - 1)
    memo[x] = min([func(x2, memo) for x2 in x2_list]) + 1
    return memo[x]


X = int(sys.stdin.readline())

print(func(X, {}))
