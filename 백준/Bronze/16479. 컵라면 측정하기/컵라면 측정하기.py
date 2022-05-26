from sys import stdin, stdout


def solve():
  k: float = float(stdin.readline().rstrip())
  d1, d2 = map(float, stdin.readline().rstrip().split())
  d1, d2 = min(d1, d2), max(d1, d2)
  stdout.write("%f\n" % (k**2 - ((d2-d1)/2)**2))


if __name__ == "__main__":
    solve()
