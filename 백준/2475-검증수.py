import sys

numbers = map(int, sys.stdin.readline().split())
print(sum(map(lambda x: x ** 2, numbers)) % 10)