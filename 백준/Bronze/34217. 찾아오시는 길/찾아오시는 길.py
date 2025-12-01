from sys import stdin


def solution(a, b, c, d):

    if a + c == b+d:
        print('Either')
    elif a + c < b+d:
        print('Hanyang Univ.')
    else:
        print('Yongdap')


if __name__ == "__main__":
    a, b = map(int, stdin.readline().strip().split())
    c, d = map(int, stdin.readline().strip().split())
    solution(a, b, c, d)
