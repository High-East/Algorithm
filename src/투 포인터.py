"""

[1]: https://github.com/TheAlgorithms/Python/blob/3952ba703a5b84a37891a001037c5c366d20941a/maths/two_pointer.py
"""
from typing import List


def two_pointers(arr: List[int], target: int) -> int:
    """
    정렬되지 않은 배열에서, 연속된 부분 수열의 합이 target이 되는 경우의 수를 리턴해라.
    (1) total이 target보다 커질 때까지, end를 이동시킨다.
    (2) total이 target보다 크지 않을 때까지, start를 이동시킨다.
    (3) 크지 않을 뿐더러, 값이 같다면 count를 증가시킨다.
    (4) 위 과정을 반복한다.
    """
    start, end = 0, 0
    total = 0
    count = 0

    while end < len(arr):
        total += arr[end]

        while total > target:
            total -= arr[start]
            start += 1

        if total == target:
            count += 1

        end += 1
    return count


def two_pointers_with_sorted_array(arr: List[int], target: int) -> List[int]:
    """
    정렬된 배열이 주어졌을 때, 합이 target이 되는 두 점을 리턴해라.
    제약 조건 (1): unique solution
    제약 조건 (2): 동일한 index의 값을 사용해서는 안된다
    """
    s = 0
    e = len(arr) - 1

    while s < e:
        if arr[s] + arr[e] == target:
            return [s, e]
        elif arr[s] + arr[e] < target:
            s += 1
        else:
            e += 1

    return []
