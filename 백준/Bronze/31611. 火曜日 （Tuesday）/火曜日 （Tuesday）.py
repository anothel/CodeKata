from sys import stdin


def solution(x):

    if x % 7 == 2:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    x = (int((stdin.readline().strip())))

    solution(x)
