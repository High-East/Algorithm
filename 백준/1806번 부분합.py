import sys

n, s = map(int, input().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

l, r = 0, 0
total = 0
result = int(1e5)

while r < n:
    total += arr[r]
    while total >= s:
        result = min(result, r - l + 1)
        total -= arr[l]
        l += 1
    r += 1

if result == int(1e5):
    print(0)
else:
    print(result)
