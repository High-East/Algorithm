import sys

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

result = []
window_sum = sum(arr[:m])
result.append(window_sum)

for i in range(m, n):
    window_sum = window_sum - arr[i - m] + arr[i]
    result.append(window_sum)

print(max(result))
