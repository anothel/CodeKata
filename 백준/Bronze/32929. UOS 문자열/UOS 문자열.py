from sys import stdin


def solution(x):
    if x % 3 == 0:
        print('S')
    elif x % 3 == 1:
        print('U')
    elif x % 3 == 2:
        print('O')


if __name__ == "__main__":
    x = int(stdin.readline().strip())
    solution(x)
