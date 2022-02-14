"""
https://www.acmicpc.net/problem/1914

[풀이]
일반적인 하노이의 탑 문제로, 그대로 구현해서 풀면 된다.
또한, N개의 원반을 이동하기 위해서는 (2^n - 1)번이다.
따라서 이동에 필요한 총 횟수를 바로 구하고,
N이 20이하인 경우에만 경로를 출력해주면 된다.

[성능]
메모리 제한: 128MB, 시간 제한: 6s
메모리: 30864KB, 시간: 876ms, 코드 길이: 652B

[성능 기준]
- int 백만개 = 4MB
- 1초 = 1억번 연산 가능
- 참고로, 12! 이상이면 1억 초과함.
"""


def move(start, destination):
    print(f"{start} {destination}")


def hanoi(n, start, destination, via):
    # 원반이 1개일 때 옮기기
    if n == 1:
        move(start, destination)
        return None

    # 원반이 2개 이상일 때 옮기기  (총 3스텝)
    # (1) (n - 1)개를 via로 옮기기
    hanoi(n - 1, start, via, destination)

    # (2) n번째 원반을 destination으로 옮기기
    move(start, destination)

    # (3) (n - 1)개를 destination으로 옮기기
    hanoi(n - 1, via, destination, start)


if __name__ == '__main__':
    N = int(input())
    print(2 ** N - 1)
    if N <= 20:
        hanoi(N, 1, 3, 2)
