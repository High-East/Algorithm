# https://www.acmicpc.net/problem/2581

def find_prime_number(m: int, n: int):
    prime = set(range(2, n + 1))
    for i in range(2, int((n ** 0.5)) + 1):
        prime -= set(range(i * 2, n + 1, i))
    prime = [num for num in list(prime) if num >= m]
    return prime


if __name__ == '__main__':
    M, N = int(input()), int(input())
    prime = find_prime_number(M, N)
    if prime:
        print(sum(prime))
        print(min(prime))
    else:
        print(-1)
