# https://www.acmicpc.net/problem/1427

from collections import Counter

if __name__ == '__main__':
    c = Counter(input())
    s = ""
    for n in range(9, -1, -1):
        s += str(n) * c[str(n)]

    print(s)
