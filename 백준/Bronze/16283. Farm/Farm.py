from sys import stdin, stdout


def solve():
  a, b, n, w = map(int, stdin.readline().rstrip().split())

  bGood: bool = False
  nAnswerSheepCount: int = 0
  for nSheep in range(1, n):
    if a * nSheep + (n - nSheep) * b == w and bGood == False:
      nAnswerSheepCount = nSheep
      bGood = True
      continue
    elif a * nSheep + (n - nSheep) * b == w and bGood == True:
      bGood = False
      break

  stdout.write("%d %d\n" % (nAnswerSheepCount, n-nAnswerSheepCount)
               if bGood == True else "-1")


if __name__ == "__main__":
    solve()
