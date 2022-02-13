from functools import reduce

N = 10000


def d(n: int):
    return n + reduce(lambda x, y: int(x) + int(y), str(n), 0)


def get_seq(n: int):
    res = []
    while True:
        n = d(n)
        if n <= N:
            res.append(n)
        else:
            break
    return set(res)


if __name__ == '__main__':
    res = set(range(1, N))
    for i in range(1, N):
        res = res - get_seq(i)
    print(*sorted(res), sep='\n')
