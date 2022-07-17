from sys import stdin, stdout


def solve():
    x1, y1, r1 = map(int, stdin.readline().rstrip().split())
    x2, y2, r2 = map(int, stdin.readline().rstrip().split())

    if ((x1 - x2)**2 + (y1 - y2)**2)**0.5 < r1 + r2:
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")


if __name__ == "__main__":
    solve()
