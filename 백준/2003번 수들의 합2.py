import sys

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

left, right = 0, 0
count = 0
total = 0

while right < n:
    total += arr[right]

    while total > m:
        total -= arr[left]
        left += 1

    if total == m:
        count += 1

    right += 1

print(count)
