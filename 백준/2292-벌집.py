import sys

N = int(sys.stdin.readline())
total = 1
cnt = 0

while total < N:
    cnt += 1
    total += 6 * cnt
print(cnt + 1)