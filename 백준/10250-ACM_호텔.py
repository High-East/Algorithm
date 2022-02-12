# https://www.acmicpc.net/problem/10250
# Success

def get_room(h, _, n):
    room = n // h
    floor = n % h
    if floor != 0:
        room += 1
    else:
        floor = h
    return str(floor) + str(room).rjust(2, '0')


for _ in range(int(input())):
    print(get_room(*map(int, input().split())))
