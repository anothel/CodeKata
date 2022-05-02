from sys import stdin, stdout


def solve():
  for _ in range(int(stdin.readline().rstrip())):
    nTotal: int = 0
    for i in range(1, int(stdin.readline().rstrip()) + 1):
      nTotal += i if i % 2 != 0 else 0
    stdout.write("%d\n" % nTotal)


if __name__ == "__main__":
    solve()
