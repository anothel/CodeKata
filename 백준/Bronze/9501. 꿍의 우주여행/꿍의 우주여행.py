from sys import stdin, stdout


def solve():
  for _ in range(int(stdin.readline().strip())):
    n, d = map(int, stdin.readline().strip().split())
    nCount: int = 0
    for _ in range(n):
      v, f, c = map(int, stdin.readline().strip().split())
      if d/v * c <= f:
        nCount += 1
    stdout.write("%d\n" % nCount)


if __name__ == "__main__":
    solve()
