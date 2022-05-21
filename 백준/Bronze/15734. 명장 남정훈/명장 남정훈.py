from sys import stdin, stdout


def solve():
    l, r, a = map(int, stdin.readline().strip().split())
    stdout.write("%d\n" % (min(l+a, r+a, l+r+a>>1) * 2))


if __name__ == "__main__":
    solve()
