from sys import stdin, stdout


def solution():
    x: int = int(stdin.readline().rstrip())

    stdout.write("%d\n" % (x * 24))


if __name__ == "__main__":
    solution()
