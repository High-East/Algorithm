# https://www.acmicpc.net/problem/11653

def prime_factorization(n: int) -> list:
    """
    소인수 분해 함수

    :param n:
    :return: 소인수 분해 과정이 담겨 있는 리스트
    """

    i = 2
    res = []

    while i <= n:
        if n % i == 0:
            res.append(i)
            n = n // i
        else:
            i += 1

    if n != 1:
        res.append(n)

    return res


if __name__ == '__main__':
    N = int(input())
    print(*prime_factorization(N), sep='\n')
