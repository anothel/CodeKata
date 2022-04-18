from sys import stdin, stdout


def solve():
  n: int = int(stdin.readline().strip())

  nCount: int = 0
  for b in range(1, 501):
    for a in range(b, 501):
      if a**2 == b**2 + n:
        nCount += 1

  stdout.write("%d\n" % nCount)


if __name__ == "__main__":
    solve()
