# https://www.acmicpc.net/problem/1018
import sys
from itertools import cycle


def func(x, y, board):
    bw = cycle('BW')
    cnt = 0
    for dy in range(8):
        for dx in range(8):
            if board[y + dy][x + dx] != next(bw):
                cnt += 1
        next(bw)
    return min(cnt, 64 - cnt)


if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().split())
    board = [sys.stdin.readline().rstrip() for _ in range(M)]
    res = 65
    for y in range(M - 7):
        for x in range(N - 7):
            ret = func(x, y, board)
            if ret == 0:
                print(0)
                sys.exit()
            elif ret < res:
                res = ret
    print(res)
