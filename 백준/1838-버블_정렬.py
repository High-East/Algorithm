"""
https://www.acmicpc.net/problem/1838

[풀이]
문제를 그대로 구현하면 안된다. 그럼 제한 시간을 초과한다.
버블 정렬에서 같은 라운드 안에서 아이템이 오른쪽으로는 여러번 움직일 수 있지만,
왼쪽으로는 한 번만 움직일 수 있다는 점을 이용하면 풀 수 있다.
정렬 되기 전(before)과 정렬 된 후(after)를 비교해서,
왼쪽으로 이동한 아이템 중에 가장 많이 이동한 횟수가 정답이 된다.

위에 생각대로 풀면 되긴 하는데, 의문점이 남아있다.
생각해보면 왼쪽으로 이동하는 아이템들의 정렬이 끝난다면,
그 안에 오른쪽으로 이동하는 아이템들의 정렬이 끝났다는 말인데
정말 그런지는 의문이다.

[성능]
메모리 제한: 128MB, 시간 제한: 2s
메모리: 131904KB, 시간: 900ms, 코드 길이: 1065B

[성능 기준]
- int 백만개 = 4MB
- 1초 = 1억번 연산 가능
- 참고로, 12! 이상이면 1억 초과함.
"""

import sys

if __name__ == '__main__':
    N = int(input())
    arr = sys.stdin.readline().rsplit()
    before = {int(item): index for index, item in enumerate(arr)}
    after = sorted(before)

    res = []
    for index, item in enumerate(after):
        num = before[item] - index
        if num >= 0:
            res.append(num)

    print(max(res))
