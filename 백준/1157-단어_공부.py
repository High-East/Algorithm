import sys
from collections import Counter

words = Counter(sys.stdin.readline().lower().rstrip()).most_common(2)
if len(words) == 1 or words[0][1] != words[1][1]:
    word = words[0][0]
else:
    word = '?'
print(word.upper())