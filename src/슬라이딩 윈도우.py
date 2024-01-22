from typing import List


def sliding_window(arr: List[int], window_size: int):
    result = []
    window_sum = sum(arr[:window_size])
    result.append(window_sum)

    for i in range(window_size, len(arr)):
        window_sum = window_sum - arr[i - window_size] + arr[i]
        result.append(window_sum)

    return result


# 예제 사용
input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
window_size = 3

result = sliding_window(input_array, window_size)
print(result)
