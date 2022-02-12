# https://www.acmicpc.net/problem/2742

import sys
N = int(sys.stdin.readline())
print(*range(N, 0, -1), sep='\n')