# https://www.acmicpc.net/problem/7568


if __name__ == '__main__':
    arr = []
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        arr.append((x, y))

    for i in range(n):
        x, y = arr[i]
        count = 0
        for j in range(n):
            if i != j:
                if x < arr[j][0] and y < arr[j][1]:
                    count += 1
        print(count + 1, end=' ')
