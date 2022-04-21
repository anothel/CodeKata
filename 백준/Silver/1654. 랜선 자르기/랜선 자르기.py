from sys import stdin, stdout


def solve():
  k, n = map(int, stdin.readline().strip().split())
  wires: list = [int(stdin.readline().strip()) for _ in range(k)]

  nMin: int = 1
  nMax: int = max(wires)
  while nMin <= nMax:
    nMid: int = (nMin + nMax) // 2
    nCnt: int = 0
    for i in wires:
      nCnt += i // nMid

    if nCnt >= n:
      nMin = nMid + 1
    else:
      nMax = nMid - 1

  stdout.write("%d\n" % nMax)


if __name__ == "__main__":
    solve()
