from sys import stdin, stdout


def solve():
  num: int = 0
  for _ in range(int(stdin.readline().strip())):
    n: int = int(stdin.readline().strip())
    num += (n // 10) ** (n % 10)
  stdout.write("%d\n" % num)


if __name__ == "__main__":
    solve()
