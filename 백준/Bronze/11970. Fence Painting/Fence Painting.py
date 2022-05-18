from sys import stdin, stdout


def solve():
  a, b = map(int, stdin.readline().rstrip().split())
  c, d = map(int, stdin.readline().rstrip().split())
  if d <= a or b <= c:
    stdout.write("%d\n" % (b - a + d - c))
  else:
    stdout.write("%d\n" % (max(a, b, c, d) - min(a, b, c, d)))


if __name__ == "__main__":
    solve()
