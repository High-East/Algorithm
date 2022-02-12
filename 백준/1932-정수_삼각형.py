# DP: tabulation

import sys

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(len(arr[i]))] for i in range(n - 1)]
dp.append(arr[-1])

for i in range(n - 2, -1, -1):
    for j in range(len(arr[i])):
        dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + arr[i][j]
print(dp[0][0])


