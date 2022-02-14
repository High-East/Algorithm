# https://www.acmicpc.net/problem/18870
import sys

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    arr_sort = sorted(arr)

    counter = {}
    for n in arr_sort:
        if n not in counter:
            counter[n] = 1

    compression = {}
    keys = list(counter.keys())
    count = 0

    for i in range(len(counter)):
        compression[keys[i]] = count
        count += counter[keys[i]]

    for n in arr:
        print(compression[n], end=' ')
