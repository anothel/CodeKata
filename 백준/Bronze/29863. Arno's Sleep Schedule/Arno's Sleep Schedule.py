from sys import stdin


def solution(st, at):

    if 20<=st and st<=23:
        print(24-st+at)
    else:
        print(at-st)


if __name__ == "__main__":
    st = int(stdin.readline().strip())
    at = int(stdin.readline().strip())

    solution(st, at)
