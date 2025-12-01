from sys import stdin


def solution(N):
    print('LoveisKoreaUniversity', end='')
    for _ in range(N - 1):
        print(' ', end='')
        print('LoveisKoreaUniversity', end='')


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    solution(N)
