# https://www.acmicpc.net/problem/1966

import sys
from collections import deque


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    num_queue = deque(map(int, sys.stdin.readline().split()))
    idx_queue = deque(range(len(num_queue)))
    target = num_queue[M]
    max_num = max(num_queue)
    cnt = 1
    flag = False
    while not flag:
        if max_num == target:
            while True:
                if idx_queue[0] == M:
                    print(cnt)
                    flag = True
                    break
                else:
                    if num_queue[0] == target:
                        cnt += 1
                        num_queue.popleft()
                        idx_queue.popleft()
                    else:
                        num_queue.rotate(-1)
                        idx_queue.rotate(-1)
        elif max(num_queue) == num_queue[0]:
            num_queue.popleft()
            idx_queue.popleft()
            cnt += 1
            max_num = max(num_queue)
        else:
            num_queue.rotate(-1)
            idx_queue.rotate(-1)