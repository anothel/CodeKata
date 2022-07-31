from sys import stdin, stdout


def solve():
    c, b = map(int, stdin.readline().rstrip().split())
    stdout.write("%f\n" % (c / b))


if __name__ == "__main__":
    solve()
