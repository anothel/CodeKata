from sys import stdin, stdout


def solve():
  word: list = list(stdin.readline().rstrip())

  for s in word:
    if s.isupper():
      stdout.write("%s" % s.lower())
    else:
      stdout.write("%s" % s.upper())
  stdout.write("\n")


if __name__ == "__main__":
    solve()
