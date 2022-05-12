from sys import stdin, stdout


def solve():
  n, m = map(int, stdin.readline().rstrip().split())
  nRv:int = n
  second: int = n//m
  nRv += second
  while second:
    second //= m
    nRv += second
  stdout.write("%d" % nRv)


if __name__ == "__main__":
    solve()
