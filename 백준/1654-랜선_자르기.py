# https://www.acmicpc.net/problem/1654

import sys
from functools import reduce


def get_lan(lan_list, cut_length):
    return reduce(lambda x, y: x + (y // cut_length), lan_list, 0)


def binary_search(lan_list, N):
    # cut_list = list(range(1, max(lan_list) + 1))
    low = 1
    high = max(lan_list)
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        cnt = get_lan(lan_list, mid)
        if N > cnt:
            high = mid - 1
        else:
            low = mid + 1
            if ans < mid:
                ans = mid
    return ans


if __name__ == '__main__':
    K, N = map(int, sys.stdin.readline().split())
    lan_list = [int(sys.stdin.readline()) for _ in range(K)]
    print(binary_search(lan_list, N))