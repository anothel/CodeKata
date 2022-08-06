from sys import stdin, stdout


def solution():
    _ = int(stdin.readline().rstrip())
    sen: str = stdin.readline().rstrip()
    stdout.write("%s\n" % sen[-5:])


if __name__ == "__main__":
    solution()
