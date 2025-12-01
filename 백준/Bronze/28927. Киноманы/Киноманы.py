from sys import stdin


def solution(H1, I1, A1, H2, I2, A2):

    maxv = 3 * H1 + 20 * I1 + 120 * A1
    melv = 3 * H2 + 20 * I2 + 120 * A2

    if maxv == melv:
        print("Draw")
    elif maxv > melv:
        print("Max")
    else:
        print("Mel")


if __name__ == "__main__":
    H1, I1, A1 = map(int, stdin.readline().strip().split())
    H2, I2, A2 = map(int, stdin.readline().strip().split())
    solution(H1, I1, A1, H2, I2, A2)
