from sys import stdin, stdout


def solve():
  a, b, c, m = map(int, stdin.readline().rstrip().split())

  nTired: int = 0
  nWork: int = 0
  for _ in range(24):
    if nTired + a <= m:
      nTired += a
      nWork += b
    else:
      nTired -= c
      if nTired < 0:
        nTired = 0

  stdout.write("%d\n" % nWork)


if __name__ == "__main__":
    solve()
