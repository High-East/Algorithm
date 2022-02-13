"""
https://www.acmicpc.net/problem/1011

[풀이]
각 작동 횟수별 이동할 수 있는 최대 구간을 구해보자.
2번: 2 (1, 1)
3번: 4 (1, 2, 1)
4번: 6 (1, 2, 2, 1)
5번: 9 (1, 2, 3, 2, 1)
6번: 12 (1, 2, 3, 3, 2, 1)
7번: 16 (1, 2, 3, 4, 3, 2, 1)
...
최대 구간이 증가하는 패턴을 찾을 수 있다.
위 패턴을 이용해서 문제를 풀자.
단, 1만큼 움직이는 1번 작동하는 경우는 예외처리를 해준다.

[성능]
메모리 제한: 512MB, 시간 제한: 2s
메모리: 34968KB, 시간: 1132ms, 코드 길이: 400B

[성능 기준]
- int 백만개 = 4MB
- 1초 = 1억번 연산 가능
- 참고로, 12! 이상이면 1억 초과함.
"""


def solve(x, y):
    dist = y - x
    if dist == 1:
        return 1

    arr = [2]
    n, cnt = 2, 0

    while arr[-1] < dist:
        arr.append(arr[-1] + n)
        cnt += 1
        if cnt % 2 == 0:
            n += 1

    return len(arr) + 1


if __name__ == '__main__':
    for _ in range(int(input())):
        print(solve(*map(int, input().split())))
