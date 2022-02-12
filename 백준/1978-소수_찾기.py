# https://www.acmicpc.net/problem/1978
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
    sys.stdin.readline()
    num_list = set(map(int, sys.stdin.readline().split()))
    print(len(num_list & find_all_prime(max(num_list))))