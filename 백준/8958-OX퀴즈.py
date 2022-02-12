# https://www.acmicpc.net/problem/8958

import sys

N = int(sys.stdin.readline())


for _ in range(N):
    score, cont = 0, 0
    result_str = sys.stdin.readline().rstrip()
    for result in result_str:
        if result == 'O':
            cont += 1
            score += cont
        else:
            cont = 0
    print(score)


