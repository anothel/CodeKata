from sys import stdin, stdout
from collections import deque


def solve():
  for _ in range(int(stdin.readline().strip())):
    n, m = map(int, stdin.readline().strip().split())
    nPrintCount: int = 0
    lPrint: deque = deque(map(int, stdin.readline().strip().split()))
    nCurrentIndex: int = m
    while True:
      nCurrentMax: int = max(lPrint)
      nPoped: int = lPrint.popleft()
      nCurrentIndex -= 1
      if nPoped >= nCurrentMax:
        nPrintCount += 1
        if nCurrentIndex < 0:
          break
      else:
        lPrint.append(nPoped)
        if nCurrentIndex < 0:
          nCurrentIndex = len(lPrint) - 1

    stdout.write("%d\n" % nPrintCount)


if __name__ == "__main__":
    solve()
