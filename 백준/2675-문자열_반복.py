# https://www.acmicpc.net/problem/2675

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    R, S = sys.stdin.readline().split()
    print("".join([s * int(R) for s in S]))