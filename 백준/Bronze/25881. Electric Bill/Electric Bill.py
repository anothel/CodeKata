from sys import stdin, stdout


def solution():
    d, o = map(float, stdin.readline().rstrip().split())
    n: int = int(stdin.readline().rstrip())

    for _ in range(n):
        a: int = int(stdin.readline().rstrip())
        stdout.write("%d " % (a))
        b: int = 0
        if a > 1000:
            b = a - 1000
            a = 1000
        stdout.write("%d\n" % (d * a + b * o))


if __name__ == "__main__":
    solution()
