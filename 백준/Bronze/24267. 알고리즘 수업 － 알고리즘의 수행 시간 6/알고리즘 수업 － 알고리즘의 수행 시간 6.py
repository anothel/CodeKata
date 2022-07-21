from sys import stdin, stdout


def solve():
    n: int = int(stdin.readline().rstrip())

    stdout.write("%d\n3\n" % ((n * (n - 1) * (n - 2)) // 6))


if __name__ == "__main__":
    solve()
