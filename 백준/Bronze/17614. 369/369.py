from sys import stdin, stdout


def getCount3(n: int) -> int:
  nRv: int = 0

  while n > 0:
    tmp = n % 10
    if tmp == 3 or tmp == 6 or tmp == 9:
      nRv += 1
    n //= 10

  return nRv


def solve():
  nRv: int = 0
  for i in range(1, int(stdin.readline().rstrip()) + 1):
    nRv += getCount3(i)
  stdout.write(str(nRv))


def main():
  solve()


if __name__ == "__main__":
    main()
