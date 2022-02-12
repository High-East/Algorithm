# https://www.acmicpc.net/problem/10828
import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.empty():
            return -1
        x, self.stack = self.stack[-1], self.stack[:-1]
        return x

    def size(self):
        return len(self.stack)

    def empty(self):
        return 1 if self.size() == 0 else 0

    def top(self):
        if self.empty():
            return -1
        return self.stack[-1]

    def __repr__(self):
        return str(self.stack)

stack = Stack()

N = int(sys.stdin.readline())
for _ in range(N):
    command = sys.stdin.readline().split()
