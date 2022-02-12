# https://www.acmicpc.net/problem/10871

import sys

N, X = map(int, sys.stdin.readline().split())
num_list = map(int, sys.stdin.readline().split())

for num in num_list:
    if num < X:
        print(num, end=' ')