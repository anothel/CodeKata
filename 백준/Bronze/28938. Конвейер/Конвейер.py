from sys import stdin


def solution(values):

    result = 0
    for v in values:
        result += v

    if result == 0:
        print("Stay")
    elif result > 0:
        print("Right")
    else:
        print("Left")


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    values = list(map(int, stdin.readline().strip().split()))
    solution(values)
