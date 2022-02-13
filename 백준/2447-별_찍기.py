# https://www.acmicpc.net/problem/2447

def star(n, N, pattern):
    s = []
    cnt = list(range(1, n + 1))
    for i in cnt:
        if i in cnt[n // 3: (n // 3) * 2]:
            s.append(pattern[i % len(pattern) - 1] + " " * len(pattern[0]) + pattern[i % len(pattern) - 1])
        else:
            s.append(pattern[i % len(pattern) - 1] * 3)

    if n == N:
        return s
    else:
        return star(n * 3, N, s)


if __name__ == '__main__':
    print(*star(3, int(input()), ['*']), sep='\n')
