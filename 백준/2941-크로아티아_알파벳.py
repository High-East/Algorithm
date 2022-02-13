# https://www.acmicpc.net/problem/2941


if __name__ == '__main__':
    word = input()
    case = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    for c in case:
        word = word.replace(c, " ")

    print(len(word))
