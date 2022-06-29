from sys import stdin, stdout


def solution():
    nA: int = 0
    nB: int = 0
    for _ in range(int(stdin.readline().rstrip())):
        a, b = map(int, stdin.readline().rstrip().split())
        if a > b:
            nA += a + b
        elif b > a:
            nB += a + b
        else:
            nA += a
            nB += b
    stdout.write("%d %d\n" % (nA, nB))


if __name__ == "__main__":
    solution()
