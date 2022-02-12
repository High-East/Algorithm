# https://www.acmicpc.net/problem/10809
import sys
import string

word = sys.stdin.readline().rstrip()

dictionary = {x: -1 for x in string.ascii_lowercase}

for i, w in enumerate(word):
    if dictionary[w] == -1:
        dictionary[w] = i

print(*dictionary.values())