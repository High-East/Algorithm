# https://www.acmicpc.net/problem/1181

import sys
from collections import defaultdict

N = int(sys.stdin.readline())

word_list = [sys.stdin.readline().rstrip() for _ in range(N)]
word_dict = defaultdict(set)

for word in word_list:
    word_dict[len(word)].add(word)


for l in sorted(word_dict):
    print(*sorted(word_dict[l]), sep='\n')

