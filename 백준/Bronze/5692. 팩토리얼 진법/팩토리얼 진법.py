from sys import stdin, stdout


def factorial(n: int) -> int:
  nRv: int = 1
  for i in range(1, n+1):
    nRv *= i
  return nRv


def solve():
  while True:
    lInput: list = list(stdin.readline().rstrip())
    if len(lInput) == 1 and lInput[0] == "0":
      break

    n: int = len(lInput)
    nRv: int = 0
    for s in lInput:
      nRv += int(s) * factorial(n)
      n -= 1

    stdout.write("%d\n" % nRv)


if __name__ == "__main__":
    solve()
