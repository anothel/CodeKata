from sys import stdin, stdout


def solve():
  l: int = int(stdin.readline().strip())
  s: list = list(stdin.readline().strip())

  nTotal: int = 0
  for i in range(len(s)):
    nTotal += ((ord(s[i]) - 96) * (31 ** i))

  stdout.write("%d\n" % (nTotal % 1234567891))


if __name__ == "__main__":
    solve()
