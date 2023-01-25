from sys import stdin, stdout


def solution():
    n, k, a, b = map(int, stdin.readline().rstrip().split())

    stdout.write("%d %d\n" % ((k - 1) * b + (n - 1) * b, (n - 1) * a))


if __name__ == "__main__":
    solution()
