from sys import stdin, stdout


def solve():
  for _ in range(int(stdin.readline().rstrip())):
    nTotal: int = 0
    for _ in range(int(stdin.readline().rstrip())):
      lStucks: list = list(map(int, stdin.readline().rstrip().split()))
      nTotal += max(lStucks) if max(lStucks) > 0 else 0
    stdout.write("%d\n" % nTotal)


if __name__ == "__main__":
    solve()
