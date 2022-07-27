from sys import stdin, stdout


def solve():
    d1, d2, d3 = map(int, stdin.readline().rstrip().split())
    c: float = (d2 + d3 - d1) / 2
    a: float = d2 - c
    b: float = d3 - c

    if a > 0 and b > 0 and c > 0:
        stdout.write("1\n")
        stdout.write("%.1f %.1f %.1f\n" % (a, b, c))
    else:
        stdout.write("-1\n")


if __name__ == "__main__":
    solve()
