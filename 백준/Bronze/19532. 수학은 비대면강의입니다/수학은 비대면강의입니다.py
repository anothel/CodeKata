from sys import stdin, stdout


def solution():
    a, b, c, d, e, f = (map(int, stdin.readline().rstrip().split()))

    stdout.write("%d %d" % ((b * f - c * e) / (b * d - a * e),
                            (f * a - c * d) / (a * e - b * d)))


if __name__ == "__main__":
    solution()
