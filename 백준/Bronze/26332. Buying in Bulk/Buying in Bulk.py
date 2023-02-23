from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    nTotal: int = 0
    for _ in range(n):
        c, p = map(int, stdin.readline().rstrip().split())
        if c < 2:
            nTotal = p
        else:
            nTotal = c * p
            nTotal -= (c - 1) * 2
        stdout.write("%d %d\n" % (c, p))
        stdout.write("%d\n" % nTotal)


if __name__ == "__main__":
    solution()
