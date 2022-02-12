import sys

N = int(input())

arr = [list(sys.stdin.readline().split()) for _ in range(N)]
arr.sort(key=lambda x: int(x[0]))

for item in arr:
    print(" ".join(item))