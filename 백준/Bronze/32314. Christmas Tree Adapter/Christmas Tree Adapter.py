from sys import stdin


def solution(a, w, v):

    if w/v >= a:
        print("1")
    else:
        print("0")


if __name__ == "__main__":
    a = int(stdin.readline().strip())
    w, v = map(int, stdin.readline().strip().split())
    solution(a, w, v)
