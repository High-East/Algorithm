import sys
from functools import reduce
from collections import Counter

num_list = [int(sys.stdin.readline()) for _ in range(3)]
num = reduce(lambda x, y: x * y, num_list)

num_counter = Counter(str(num))

for i in range(10):
    print(num_counter[str(i)])

