from sys import stdin, stdout


def solve():
  for _ in range(int(stdin.readline().rstrip())):
    n: int = int(stdin.readline().rstrip())
    stdout.write(str("Pairs for %d: " % n))
    comma: bool = False
    for i in range(1, 13):
      for j in range(i+1, 13):
        if i + j == n:
          stdout.write(str(", " if comma else ""))
          stdout.write(str("%d %d" % (i, j)))
          comma = True
    stdout.write(str("\n"))


def main():
  solve()


if __name__ == "__main__":
    main()
