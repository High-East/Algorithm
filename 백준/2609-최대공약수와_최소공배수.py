# https://www.acmicpc.net/problem/2609
import sys


def get_gcd(x, y):
    """
    GCD = Greatest Common Divisor

    Inputs:
        x >= y
    Returns:
        GCD
    Examples:
        x , y = 24, 18
        get_gcd(x, y)
    """
    if x % y == 0:
        return y
    return get_gcd(y, x % y)


def get_lcm(x, y):
    """
    LCM = Least Common Multiple

     Inputs:
        x >= y
    Returns:
        LCM
    Examples:
        x , y = 24, 18
        get_lcm(x, y)
    """
    return int(x * y / get_gcd(x, y))


x, y = map(int, sys.stdin.readline().split())
x, y = (x, y) if x >= y else (y, x)
print(get_gcd(x, y))
print(get_lcm(x, y))
