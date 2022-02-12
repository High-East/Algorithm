import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

res = 0

for i, p in enumerate(sorted(P)):
    res += (N - i) * p

print(res)