from sys import stdin, stdout


def cal(n: int) -> int:
  nRet: int = 0

  while n > 0:
    nRet += n % 10
    n //= 10

  return nRet


def solve():
  while True:
    n = int(stdin.readline().rstrip())
    if n == 0:
      break
    nRet: int = cal(n)
    while nRet >= 10:
      nRet = cal(nRet)
    stdout.write(str(nRet) + "\n")


def main():
  solve()


if __name__ == "__main__":
    main()
