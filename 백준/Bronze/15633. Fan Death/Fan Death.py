from sys import stdin, stdout


def solve():
  n: int = int(stdin.readline().strip())

  nTotal: int = 0
  for i in range(1, n+1):
    if n % i == 0:
      nTotal += i

  stdout.write("%d\n" % (nTotal * 5 - 24))


if __name__ == "__main__":
    solve()
