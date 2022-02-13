# https://www.acmicpc.net/problem/5622

import string

UPPER_STR = string.ascii_uppercase
NUM = "".join([x * int(y) for x, y in zip('23456789', '3' * 5 + '434')])
DIAL = {s: int(n) + 1 for s, n in zip(UPPER_STR, NUM)}


def solve(w: str) -> int:
    return DIAL[w]


if __name__ == '__main__':
    word = input()
    res = 0

    for w in word:
        res += solve(w)

    print(res)
