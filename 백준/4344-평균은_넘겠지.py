# https://www.acmicpc.net/problem/4344

import sys


def get_ratio(arr):
    N, scores = arr[0], arr[1:]
    avg = sum(scores) / N
    ratio = sum([True for score in scores if score > avg]) / N
    return f"{ratio * 100:0.3f}%"


if __name__ == '__main__':
    C = int(input())
    for _ in range(C):
        arr = [int(item) for item in sys.stdin.readline().split()]
        print(get_ratio(arr))
