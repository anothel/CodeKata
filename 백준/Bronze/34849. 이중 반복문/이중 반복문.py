from sys import stdin


def solution(N):
    if N*N <= 100000000:
        print("Accepted")
    else:
        print("Time limit exceeded")


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    solution(N)
