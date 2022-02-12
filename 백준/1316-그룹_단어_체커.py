"""
https://www.acmicpc.net/problem/1316
3
happy
new
year
"""
import sys


def check_is_group_word(word):
    checker = {}
    previous_word = None
    for w in word:
        if previous_word == w or w not in checker:
            checker[w] = True
            previous_word = w
        else:
            return 0
    return 1


if __name__ == '__main__':

    N = int(sys.stdin.readline())
    result = 0
    for _ in range(N):
        word = sys.stdin.readline().rstrip()
        result += check_is_group_word(word)
    print(result)