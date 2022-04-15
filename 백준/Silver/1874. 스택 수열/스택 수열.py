from sys import stdin, stdout


def solution():
  lStack: list = list()
  lResult: list = list()
  nCount: int = 0
  isPossible: bool = True
  for _ in range(int(stdin.readline().rstrip())):
    n = int(stdin.readline().rstrip())
    while nCount < n:
      nCount += 1
      lStack.append(nCount)
      lResult.append("+")
    if lStack[-1] == n:
      lStack.pop()
      lResult.append("-")
    else:
      isPossible = False
  stdout.write("\n".join(lResult) if isPossible else "NO")


if __name__ == "__main__":
  solution()
