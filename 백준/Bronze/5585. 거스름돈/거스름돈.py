from sys import stdin, stdout


def solution():
    m: int = int(stdin.readline().rstrip())
    curM: int = 1000 - m
    answer: int = 0

    answer += curM // 500
    curM %= 500
    answer += curM // 100
    curM %= 100
    answer += curM // 50
    curM %= 50
    answer += curM // 10
    curM %= 10
    answer += curM // 5
    curM %= 5
    answer += curM // 1
    curM %= 1

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
