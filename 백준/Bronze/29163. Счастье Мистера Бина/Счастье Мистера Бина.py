from sys import stdin


def solution(values):

    s = 0
    h = 0
    for v in values:
        if v % 2 == 0:
            h += 1
        else:
            s += 1

    if h > s:
        print("Happy")
    else:
        print("Sad")


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    values = list(map(int, stdin.readline().strip().split()))
    solution(values)
