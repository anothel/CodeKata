from sys import stdin, stdout


def solve():
  s: list = list(stdin.readline().rstrip())
  s.reverse()
  for i in range(len(s)):
    stdout.write("%s" % s[i])


if __name__ == "__main__":
    solve()
