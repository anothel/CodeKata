from sys import stdin


def solution(N):

    sstr = 'WelcomeToSMUPC'
    length = len(sstr)

    print(sstr[(N % length) - 1])


if __name__ == "__main__":
    N = int(stdin.readline().strip())

    solution(N)
