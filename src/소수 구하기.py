# 에라토스테네스의 체
from typing import List


def get_prime_number(n: int) -> List[int]:
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):  # (i*i)보다 작은 숫자는 이미 지워짐
                is_prime[j] = False

    primes = [num for num, flag in enumerate(is_prime) if flag]
    return primes


# 예제 사용
limit = 50
prime_numbers = get_prime(limit)
print(f"Prime numbers up to {limit}: {prime_numbers}")
