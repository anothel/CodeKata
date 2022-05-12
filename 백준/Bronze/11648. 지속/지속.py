from sys import stdin, stdout


def checkDigit(n: int) -> int:
  nCount: int = 0
  while n > 0:
    n //= 10
    nCount += 1
  return nCount


def solve():
  n: int = int(stdin.readline().rstrip())

  nValue: int = n
  nCount: int = 0
  while checkDigit(nValue) > 1:
    nTmpValue:int = 1
    while nValue > 0:
      nTmpValue *= (nValue % 10)
      nValue //= 10
    nValue = nTmpValue
    nCount += 1

  stdout.write("%d\n" % nCount)


if __name__ == "__main__":
    solve()
