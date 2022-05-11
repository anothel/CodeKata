from sys import stdin, stdout


def solve():
  n = int(stdin.readline().rstrip())
  nRv: int = 0
  while n > 0:
    nRv += (n % 10) ** 5
    n //= 10
  stdout.write("%d\n" % nRv)


if __name__ == "__main__":
    solve()
