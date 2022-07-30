from sys import stdin, stdout


def solve():
    n, m = map(int, stdin.readline().rstrip().split())
    stdout.write("YES\n" if (n * m) % 3 == 0 else "NO\n")


if __name__ == "__main__":
    solve()
