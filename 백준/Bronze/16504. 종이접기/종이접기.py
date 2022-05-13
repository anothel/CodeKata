from sys import stdin, stdout


def solve():
  nRv: int = 0
  for _ in range(int(stdin.readline().rstrip())):
    nRv += sum(list(map(int, stdin.readline().rstrip().split())))

  stdout.write("%d\n" % nRv)


if __name__ == "__main__":
    solve()
