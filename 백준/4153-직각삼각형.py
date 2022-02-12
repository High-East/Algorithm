while True:
    x, y, z = map(int, input().split())
    if x == y == z == 0:
        break
    largest = max(x, y, z)
    if largest ** 2 == sum(map(lambda x: x ** 2 if x != largest else 0, [x, y, z])):
        print("right")
    else:
        print('wrong')