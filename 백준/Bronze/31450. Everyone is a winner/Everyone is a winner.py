from sys import stdin


def solution(m, k):
    if m % k == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    m, k = map(int,(stdin.readline().strip().split()))

    solution(m, k)
