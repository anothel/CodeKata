from sys import stdin


def solution(a, b, x):
    print(a * (x-1)+b)


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    for _ in range(N):
        a, b, x = map(int, stdin.readline().strip().split())
        solution(a, b, x)
