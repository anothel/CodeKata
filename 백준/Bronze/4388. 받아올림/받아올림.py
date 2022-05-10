from sys import stdin, stdout


def getCountnumber(n: int) -> int:
  nCount: int = 1
  while n > 10:
    nCount += 1
    n %= 10
  return nCount


def solve():
  while True:
    numA, numB = list(map(int, stdin.readline().rstrip().split()))
    if numA == 0 and numB == 0:
      break

    nCount: int = 0
    for _ in range(getCountnumber(max(numA, numB))):
      nextCarry: int = 0
      while max(numA, numB) > 0:
        if (numA % 10 + numB % 10 + nextCarry) >= 10:
          nextCarry = 1
          nCount += 1
        else:
          nextCarry = 0
        numA //= 10
        numB //= 10
    stdout.write("%d\n" % nCount)


if __name__ == "__main__":
    solve()
