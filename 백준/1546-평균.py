import sys

N = int(sys.stdin.readline())
score_list = list(map(int, sys.stdin.readline().split()))
max_score = max(score_list)
avg_score = sum(map(lambda x: x / max_score * 100, score_list)) / N
print(avg_score)