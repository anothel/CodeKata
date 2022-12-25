from sys import stdin, stdout


def solution():
    a: int = int(stdin.readline().rstrip())
    b: int = int(stdin.readline().rstrip())
    stdout.write("%d\n" % (a + b))


if __name__ == "__main__":
    solution()
