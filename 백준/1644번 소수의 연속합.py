from typing import List


def get_prime_number(n: int) -> List[int]:
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 1은 소수가 아님

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = [prime for prime, flag in enumerate(is_prime) if flag]
    return primes


n = int(input())
primes = get_prime_number(n)
# print(f"primes: {primes}")

left, right = 0, 0
total = 0
count = 0

while right < len(primes):
    total += primes[right]

    while total > n:
        total -= primes[left]
        left += 1

    if total == n:
        count += 1

    right += 1

print(count)
