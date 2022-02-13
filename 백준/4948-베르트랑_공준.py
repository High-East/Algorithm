# https://www.acmicpc.net/problem/4948

def find_prime_number(n: int):
    prime_set = set(range(2, n + 1))
    for i in range(2, int((n ** 0.5)) + 1):
        prime_set -= set(range(i * 2, n + 1, i))

    prime_list = [prime for prime in prime_set if prime > n // 2]

    return len(prime_list)


if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            print(find_prime_number(2 * n))
