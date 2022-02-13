# https://www.acmicpc.net/problem/9020

def get_prime_number(n: int):
    prime_set = set(range(2, n + 1))
    for i in range(2, int((n ** 0.5)) + 1):
        prime_set -= set(range(i * 2, n + 1, i))

    return prime_set


def get_gold_num(n, prime_number):
    prime_list = list(prime_number)
    arr = [(prime, n - prime) for prime in list(prime_list) if (n - prime) in prime_number]
    arr.sort()
    arr.sort(key=lambda x: abs(x[0] - x[1]))

    return arr[0]


if __name__ == '__main__':
    prime_number = get_prime_number(10000)
    for _ in range(int(input())):
        n = int(input())
        print(*get_gold_num(n, prime_number))
