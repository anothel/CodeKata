from sys import stdin, stdout


def solve():
  n, x, k = map(int, stdin.readline().rstrip().split())

  nBallLocation: int = x
  for _ in range(k):
    a, b = map(int, stdin.readline().rstrip().split())
    if a == nBallLocation:
      nBallLocation = b
    elif b == nBallLocation:
      nBallLocation = a
  stdout.write("%d\n" % nBallLocation)


if __name__ == "__main__":
    solve()
