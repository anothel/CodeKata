from sys import stdin


def solution(H, I, A, R, C):

    h1 = H * I
    h2 = A * R * C
    print(h1-h2)


if __name__ == "__main__":
    H, I, A, R, C = map(int, stdin.readline().strip().split())
    solution(H, I, A, R, C)
