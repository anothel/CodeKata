from sys import stdin


def solution(N):
    for i in range(1, N+1):
        print(f"{i} ", end='')
        if i % 6 == 0:
            print("Go! ", end='')
        elif i == N:
            print("Go!", end='')


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    solution(N)
