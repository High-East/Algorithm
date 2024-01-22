import sys

s, p = map(int, input().split())
dna = sys.stdin.readline().strip()
condition = list(map(int, input().split()))  # A, C, G, T
result = []


def check(source, target):
    for i in range(4):
        if source[i] < target[i]:
            return False
    return True


window_result = {x: dna[:p].count(x) for x in ["A", "C", "G", "T"]}
result.append(check(list(window_result.values()), condition))

for i in range(p, s):
    window_result[dna[i - p]] -= 1
    window_result[dna[i]] += 1
    result.append(check(list(window_result.values()), condition))

print(sum(result))
