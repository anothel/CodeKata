from sys import stdin, stdout


def solve():
  for _ in range(int(stdin.readline().rstrip())):
    n, m = map(int, stdin.readline().strip().split())
    if n < 12 or m < 4:
      stdout.write("-1\n")
      continue
    stdout.write("%d\n" % (11 * m + 4))


if __name__ == "__main__":
    solve()
