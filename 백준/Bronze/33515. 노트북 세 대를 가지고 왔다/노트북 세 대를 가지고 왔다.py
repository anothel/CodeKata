from sys import stdin


def solution(T1,T2):
    print(min(T1,T2))


if __name__ == "__main__":
    T1, T2 = map(int,stdin.readline().strip().split())
    solution(T1,T2)
