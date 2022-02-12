# https://www.acmicpc.net/problem/2231

import sys


def func(M):
    return M + sum([int(m) for m in str(M)])


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    ans = 0
    for M in range(1, 1000000):
        if func(M) == N:
            ans = M
            break
        if M == N:
            break
    print(ans)