# https://www.acmicpc.net/problem/2108

import sys
from collections import Counter

N = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(N)]
num_list.sort()

print(int(round(sum(num_list) / N, 0)))
print(num_list[int(N // 2)])

num_common = Counter(num_list).most_common(2)
if len(num_common) == 2 and num_common[0][1] == num_common[1][1]:
    print(num_common[1][0])
else:
    print(num_common[0][0])

print(max(num_list) - min(num_list))



