# https://www.acmicpc.net/problem/9012
# Success

import sys


def is_vps(string):
    arr = []
    for s in string:
        if arr:
            if arr[-1] == '(' and s == ')':
                arr.pop()
            else:
                arr.append(s)
        else:
            arr.append(s)
    if arr:
        return 'NO'
    else:
        return 'YES'


N = int(input())

for _ in range(N):
    print(is_vps(sys.stdin.readline().rstrip()))
