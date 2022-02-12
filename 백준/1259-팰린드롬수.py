# https://www.acmicpc.net/problem/1259
import sys


def is_palindrome(num):
    for i in range(len(num) // 2):
        if num[i] != num[-1 * (i + 1)]:
            return 'no'
    return 'yes'


while True:
    num = sys.stdin.readline().rstrip()
    if num == '0':
        break
    else:
        print(is_palindrome(num))
