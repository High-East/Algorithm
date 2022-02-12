# https://www.acmicpc.net/problem/1929
import sys


def find_all_prime(N):
    """
    Args:
        N: natural number more than 2.
    Returns:
        Set of prime numbers.
    Examples:
        find_all_prime(N)
    """
    num_set = set(range(2, N + 1))
    for i in range(2, int((N ** 0.5)) + 1):
        num_set -= set(range(i * 2, N + 1, i))
    return num_set


if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().split())
    prime_set = find_all_prime(N)
    prime_set = prime_set - set(range(M))
    print(*sorted(prime_set), sep='\n')

"""
계속 틀렸었는데, sorted를 추가해서 성공했다.
set은 순서 유지가 안된다는 것을 간과했다...
"""