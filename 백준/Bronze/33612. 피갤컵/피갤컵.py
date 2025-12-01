from sys import stdin


def solution(N):
    year = 2024
    month = 8

    total_month = month + (N - 1)*7
    new_year = year + (total_month - 1) // 12
    new_month = (total_month - 1) % 12 + 1

    print(f"{new_year} {new_month}", end='')


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    solution(N)
