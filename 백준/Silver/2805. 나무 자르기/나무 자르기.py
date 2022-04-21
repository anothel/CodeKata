from sys import stdin, stdout
from collections import deque


def solve():
  n, m = map(int, stdin.readline().strip().split())
  trees: list = list(map(int, stdin.readline().strip().split()))

  nMin: int = 0
  nMax: int = max(trees)

  nCurrentHeight: int = 0

  while nMin < nMax:
    nMid: int = (nMin + nMax) // 2
    nTotal: int = 0
    for i in trees:
      nTotal += i - nMid if i - nMid >= 0 else 0

    if nTotal >= m and nMid > nCurrentHeight:
      nCurrentHeight = nMid
      nMin = nMid
    else:
      nMax = nMid

  stdout.write("%d\n" % nCurrentHeight)


if __name__ == "__main__":
    solve()
