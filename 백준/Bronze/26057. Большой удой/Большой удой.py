from sys import stdin, stdout


def solution():
    l: int = int(stdin.readline().rstrip())
    t: int = int(stdin.readline().rstrip())

    stdout.write("%d\n" % (2 * t - l))


if __name__ == "__main__":
    solution()
