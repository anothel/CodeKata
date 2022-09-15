from sys import stdin, stdout


def getMyNum(n: int, i: int) -> int:
    return n * i + i


def solution():
    n: int = int(stdin.readline().rstrip())

    answer: int = 0
    for i in range(1, n):
        answer += getMyNum(n, i)

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
