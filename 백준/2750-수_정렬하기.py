"""
https://www.acmicpc.net/problem/2750

[풀이]
버블 정렬로 풀었다.
max(N) = 1000이라서, 버블 정렬로 충분히 풀 수 있다.

[성능]
메모리 제한: 128MB, 시간 제한: 1s
메모리: 30864KB, 시간: 252ms, 코드 길이: 708B

[성능 기준]
- int 백만개 = 4MB
- 1초 = 1억번 연산 가능
- 참고로, 12! 이상이면 1억 초과함.
"""


def bubble_sort(arr):
    for _ in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


if __name__ == '__main__':
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    arr = bubble_sort(arr)
    print(*arr, sep='\n')
