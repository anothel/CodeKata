from sys import stdin, stdout


def solve():
  countA: int = 0
  countB: int = 0
  for _ in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())
    if a > b:
      countA += 1
    elif a < b:
      countB += 1

  stdout.write("%d %d" % (countA, countB))


def main():
  solve()


if __name__ == "__main__":
    main()
