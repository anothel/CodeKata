from sys import stdin, stdout


def solution():
    a, b, c = map(int, stdin.readline().rstrip().split())
    i, j, k = map(int, stdin.readline().rstrip().split())

    m: float = min(a / i, b / j, c / k)
    stdout.write("%f %f %f\n" % (a - i * m, b - j * m, c - k * m))


if __name__ == "__main__":
    solution()
