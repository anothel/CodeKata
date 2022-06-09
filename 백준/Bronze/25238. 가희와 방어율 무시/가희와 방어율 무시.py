from sys import stdin, stdout


def solve():
  am, pe = map(int, stdin.readline().rstrip().split())

  stdout.write("1\n" if am * (100 - pe) * 0.01 < 100 else "0\n")


if __name__ == "__main__":
    solve()
