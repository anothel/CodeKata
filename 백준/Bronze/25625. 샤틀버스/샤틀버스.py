from sys import stdin, stdout


def solution():
    x, y = map(int, stdin.readline().rstrip().split())
    stdout.write("%d\n" % (x + y) if x > y else "%d\n" % (y - x))


if __name__ == "__main__":
    solution()