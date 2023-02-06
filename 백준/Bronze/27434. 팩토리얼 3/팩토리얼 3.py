from sys import stdin, stdout


def fac(n: int) -> int:
    nResult: int = 1
    for i in range(1, n + 1):
        nResult *= i

    return nResult


def solution():
    n: int = int(stdin.readline().rstrip())

    stdout.write("%d\n" % fac(n))


if __name__ == "__main__":
    solution()
