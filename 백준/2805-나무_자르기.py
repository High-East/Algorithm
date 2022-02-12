# https://www.acmicpc.net/problem/2805
"""
문제 해설
절단기의 설정할 수 있는 높이의 최댓값을 구하는 것이 문제의 목표이다.
절단기의 높이는 0부터 가장 높은 나무의 길이까지의 범위에 속할 것이다.
그 이상은 잘라도 의미가 없기 때문이다.
즉, [0, 가장 높은 나무의 길이]에 대한 절단기의 높이를 탐색하는 문제이다.

탐색 알고리즘을 사용해서 문제를 풀기로 했으니, 어떤 탐색을 사용할지 정해보자.
제약 조건에 따라 가장 효율적인 방법이 달라진다.
현재 문제에서 완전 탐색의 경우 최대 O(M*N)의 시간이 소요되는데, M의 최대값이 20억이기 때문에 불가능하다.
하지만, 이진 탐색의 경우 최대 O(Nlog(M))의 시간이 소요된다.
따라서, 이진 탐색으로 문제를 풀어보자.

절단기의 높이가 가능한 범위 [0, 가장 높은 나무의 길이]에 대해 이진 탐색을 수행하면서,
각 높이에 대해 모든 나무를 자르고 집에 가져갈 수 있는 길이를 더한다(=ans).
ans >= M을 만족하는 경우 중에 가장 작은 값일 때의 절단기의 높이가 정답이 된다.
"""

import sys


def get_tree(tree_list, C):
    return sum([tree - C for tree in tree_list if tree - C > 0])


def binary_search(tree_list, M):
    low = 0
    high = max(tree_list)
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        res = get_tree(tree_list, mid)
        if M == res:
            return mid
        elif M > res:
            high = mid - 1
        else:
            low = mid + 1
            if ans < mid:
                ans = mid
    return ans


N, M = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))
print(binary_search(tree_list, M))
