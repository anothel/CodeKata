from sys import stdin, stdout


def solution():
    a, b, c = map(int, stdin.readline().rstrip().split())

    stdout.write("%d\n" % (b / a * 3 * c))


if __name__ == "__main__":
    solution()
