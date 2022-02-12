# https://www.acmicpc.net/problem/1920
import sys


def binary_search(element, some_list):
    low = 0
    high = len(some_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if element == some_list[mid]:
            return 1
        if element < some_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return 0


sys.stdin.readline()
N = sorted(map(int, sys.stdin.readline().split()))
sys.stdin.readline()
M = map(int, sys.stdin.readline().split())

for m in M:
    print(binary_search(m, N))
