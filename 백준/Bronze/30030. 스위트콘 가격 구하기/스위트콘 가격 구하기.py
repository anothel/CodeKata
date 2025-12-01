from sys import stdin


def solution(B):
    print(round(B/1.1))


if __name__ == "__main__":
    B = int(stdin.readline().strip())
    solution(B)
