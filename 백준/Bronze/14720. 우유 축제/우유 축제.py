from sys import stdin, stdout


def solve():
  cusor: int = 0
  nCount: int = 0
  n: int = int(stdin.readline().rstrip())
  for i in list(map(int, stdin.readline().rstrip().split())):
    if i == cusor:
      nCount += 1
      cusor += 1
      if cusor == 3:
        cusor = 0

  stdout.write(str(nCount))


def main():
  solve()


if __name__ == "__main__":
    main()
