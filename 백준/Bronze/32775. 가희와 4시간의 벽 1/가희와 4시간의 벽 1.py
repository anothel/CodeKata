from sys import stdin


def solution(s, f):
    if f < s:
        print('flight')
    else:
        print('high speed rail')


if __name__ == "__main__":
    s = int(stdin.readline().strip())
    f = int(stdin.readline().strip())
    solution(s, f)
