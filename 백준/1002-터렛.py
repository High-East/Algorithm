# https://www.acmicpc.net/problem/1002

import math


def solve(x1, y1, r1, x2, y2, r2):
    if x1 == x2 and y1 == y2 and r1 == r2:
        return -1

    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    R = max(r1, r2)
    r = min(r1, r2)

    if d > R + r or d < R - r:
        return 0
    elif d == R + r or d == R - r:
        return 1
    else:
        return 2


if __name__ == '__main__':
    for _ in range(int(input())):
        print(solve(*map(int, input().split())))
