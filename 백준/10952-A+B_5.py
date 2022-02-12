# https://www.acmicpc.net/problem/10952

import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == B == 0:
        break
    print(A + B)