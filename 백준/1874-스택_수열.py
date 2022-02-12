import sys

n = int(sys.stdin.readline())
stack = []
res = []
num_gen = (i for i in range(1, n + 1))

for _ in range(n):
    target = int(sys.stdin.readline())

    while True:
        if stack and stack[-1] == target:
            stack.pop()
            res.append('-')
            break
        else:
            try:
                stack.append(next(num_gen))
                res.append('+')
            except StopIteration:
                print("NO")
                sys.exit()
print(*res, sep='\n')