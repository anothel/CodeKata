from sys import stdin, stdout


def solution():
    s: list = stdin.readline().rstrip()
    n: int = int(stdin.readline().rstrip())

    stdout.write("%s\n" % s[n - 1])


if __name__ == "__main__":
    solution()
