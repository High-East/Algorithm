import sys

value, index = 0, 0
for i in range(1, 10):
    num = int(sys.stdin.readline())
    if num > value:
        value = num
        index = i

print(value)
print(index)