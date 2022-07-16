from sys import stdin, stdout


def solve():
    a: list = [1] * 500000
    n: int = int(stdin.readline().rstrip())
    stdout.write("%d\n" % (n**3))
    stdout.write("3\n")


if __name__ == "__main__":
    solve()
