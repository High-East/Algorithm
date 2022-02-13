# https://www.acmicpc.net/problem/1065

def solve(n: int) -> bool:
    stack = [x for x in str(n)]
    num = int(stack.pop())
    diff = None

    while stack:
        new = int(stack.pop())
        minus = num - new
        num = new
        if diff is None:
            diff = minus
        else:
            if minus == diff:
                continue
            else:
                return False

    return True


if __name__ == '__main__':
    N = int(input())
    res = []
    for n in range(1, N + 1):
        res.append(solve(n))
    print(sum(res))
